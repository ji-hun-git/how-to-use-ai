#!/usr/bin/env python3
"""With-vs-without evaluation of the skills in skills/.

For every case in cases.yaml and every model, the model answers twice:
  without: a plain assistant system prompt
  with:    the same prompt plus the skill's SKILL.md
A grader model then checks each criterion as pass/fail. The grader sees the conversation,
the answer and the criteria, but not which condition produced the answer.

This measures what a skill's instructions do once loaded. It does not test whether an agent
picks the skill on its own (triggering); see the README for trigger tests.

Examples
  python evals/skills/run.py --dry-run
  python evals/skills/run.py --models openai:gpt-6.1-terra openai:gpt-6-luna --judge openai:gpt-6.1-sol --runs 3
  python evals/skills/run.py --models anthropic:claude-sonnet-5-5 --judge anthropic:claude-opus-5-5
  python evals/skills/run.py --models claude-cli:sonnet --judge claude-cli:opus --runs 2

Providers
  openai:<model>      needs OPENAI_API_KEY       (pip install openai)
  anthropic:<model>   needs ANTHROPIC_API_KEY    (pip install anthropic)
  claude-cli:<alias>  needs a logged-in Claude Code CLI (`claude` then /login); uses your plan's usage
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import datetime as dt
import json
import re
import subprocess
import sys
import tempfile
import threading
from pathlib import Path

import yaml

EVALS = Path(__file__).resolve().parent.parent
ROOT = EVALS.parent
BASE_SYSTEM = (
    "You are a helpful assistant in a text chat. In this conversation you cannot run tools, "
    "browse, or read files; answer in text."
)
LOCK = threading.Lock()
CLEAN_CWD = tempfile.mkdtemp(prefix="skill-evals-")  # empty folder for CLI runs


# ------------------------------------------------------------------ loading
def load_cases(only: list[str] | None) -> list[dict]:
    data = yaml.safe_load((EVALS / "skills" / "cases.yaml").read_text(encoding="utf-8"))
    cases = data["cases"]
    if only:
        cases = [c for c in cases if c["id"] in only or c["skill"] in only]
    for c in cases:
        skill_file = ROOT / "skills" / c["skill"] / "SKILL.md"
        if not skill_file.exists():
            sys.exit(f"case {c['id']}: missing {skill_file}")
        msgs = [dict(m) for m in c["messages"]]
        if c.get("document"):
            doc = (EVALS / c["document"]).read_text(encoding="utf-8")
            msgs[0]["content"] = f"<document>\n{doc}\n</document>\n\n{msgs[0]['content']}"
        c["_messages"] = msgs
        c["_skill_text"] = skill_file.read_text(encoding="utf-8")
    return cases


def system_prompt(case: dict, condition: str) -> str:
    if condition == "without":
        return BASE_SYSTEM
    return (
        f"{BASE_SYSTEM}\n\nThe following skill is loaded. Follow its instructions when they apply.\n\n"
        f"<skill>\n{case['_skill_text']}\n</skill>"
    )


def flatten(messages: list[dict]) -> str:
    """Render a multi-turn conversation as one prompt (used by the CLI provider)."""
    if len(messages) == 1:
        return messages[0]["content"]
    lines = ["Conversation so far:"]
    for m in messages[:-1]:
        lines.append(f"{m['role'].capitalize()}: {m['content']}")
    lines.append("")
    lines.append(f"The user now says: {messages[-1]['content']}")
    lines.append("Reply to the user's latest message.")
    return "\n".join(lines)


# ---------------------------------------------------------------- providers
def call_model(provider: str, system: str, messages: list[dict], max_tokens: int = 2000) -> str:
    kind, _, model = provider.partition(":")
    if kind == "openai":
        from openai import OpenAI

        client = OpenAI()
        resp = client.responses.create(model=model, instructions=system, input=messages,
                                       max_output_tokens=max_tokens * 4)
        return resp.output_text
    if kind == "anthropic":
        import anthropic

        client = anthropic.Anthropic()
        resp = client.messages.create(model=model, system=system, messages=messages, max_tokens=max_tokens * 4)
        return "".join(b.text for b in resp.content if getattr(b, "type", "") == "text")
    if kind == "claude-cli":
        # Isolate the run: no tools, no user/plugin settings or hooks, no MCP servers,
        # and an empty working directory, so only our system prompt shapes the answer.
        # The prompt goes through stdin: long prompts (e.g. grading a long answer) exceed
        # the Windows command-line length limit.
        cmd = ["claude", "-p", "--model", model, "--tools", "", "--no-session-persistence",
               "--setting-sources", "project", "--strict-mcp-config",
               "--system-prompt", system]
        out = subprocess.run(cmd, input=flatten(messages), capture_output=True, text=True,
                             encoding="utf-8", timeout=600, cwd=CLEAN_CWD)
        if out.returncode != 0 or "Not logged in" in out.stdout:
            raise RuntimeError(f"claude CLI failed: {out.stdout.strip()[:200]} {out.stderr.strip()[:200]}")
        return out.stdout
    raise ValueError(f"unknown provider '{provider}'")


# ------------------------------------------------------------------ grading
JUDGE_SYSTEM = (
    "You grade an AI assistant's answer against a list of yes/no criteria. "
    "Judge only what the answer actually says. Be strict: if a criterion is only partly met, answer false. "
    "Return only JSON: {\"results\": [{\"criterion\": <number>, \"pass\": true|false, \"reason\": \"<short>\"}]}"
)


def grade(judge: str, case: dict, answer: str) -> list[dict]:
    convo = "\n\n".join(f"[{m['role']}]\n{m['content']}" for m in case["_messages"])
    crit = "\n".join(f"{i + 1}. {c}" for i, c in enumerate(case["criteria"]))
    prompt = (
        f"<conversation>\n{convo}\n</conversation>\n\n<answer>\n{answer}\n</answer>\n\n"
        f"<criteria>\n{crit}\n</criteria>\n\nGrade every criterion."
    )
    raw = call_model(judge, JUDGE_SYSTEM, [{"role": "user", "content": prompt}], max_tokens=1500)
    m = re.search(r"\{.*\}", raw, re.S)
    if not m:
        raise RuntimeError(f"judge returned no JSON: {raw[:200]}")
    results = json.loads(m.group(0))["results"]
    by_num = {int(r["criterion"]): r for r in results}
    return [
        {"criterion": i + 1, "pass": bool(by_num.get(i + 1, {}).get("pass", False)),
         "reason": by_num.get(i + 1, {}).get("reason", "missing")}
        for i in range(len(case["criteria"]))
    ]


# ------------------------------------------------------------------ running
def job_key(case_id: str, model: str, condition: str, run: int) -> str:
    return f"{case_id}|{model}|{condition}|{run}"


def run_one(case: dict, model: str, condition: str, run: int, judge: str) -> dict:
    answer = call_model(model, system_prompt(case, condition), case["_messages"])
    grades = grade(judge, case, answer)
    return {
        "key": job_key(case["id"], model, condition, run),
        "case": case["id"], "skill": case["skill"], "kind": case["kind"],
        "model": model, "condition": condition, "run": run, "judge": judge,
        "passed": all(g["pass"] for g in grades), "grades": grades, "answer": answer,
    }


def summarize(rows: list[dict], cases: list[dict], out: Path, models: list[str], judge: str, runs: int) -> None:
    def rate(subset):
        n = len(subset)
        p = sum(r["passed"] for r in subset)
        return p, n

    lines = [
        f"# Skill evaluation results ({out.name})",
        "",
        f"- Models under test: {', '.join(f'`{m}`' for m in models)}",
        f"- Grader: `{judge}` (blind to condition)",
        f"- Base system prompt (both conditions): \"{BASE_SYSTEM}\"",
        f"- Cases: {len(cases)} ({sum(c['kind'] == 'trigger' for c in cases)} trigger, "
        f"{sum(c['kind'] == 'control' for c in cases)} control), runs per case and condition: {runs}",
        "- A run passes only if every criterion passes. **without** = plain assistant; **with** = SKILL.md loaded.",
        "- Trigger cases test whether the skill improves the result; control cases test that it doesn't break correct default behavior.",
        "",
        "## Overall",
        "",
        "| Model | Case type | Without | With |",
        "|---|---|---|---|",
    ]
    for m in models:
        for kind in ("trigger", "control"):
            wo = rate([r for r in rows if r["model"] == m and r["kind"] == kind and r["condition"] == "without"])
            wi = rate([r for r in rows if r["model"] == m and r["kind"] == kind and r["condition"] == "with"])
            lines.append(f"| `{m}` | {kind} | {wo[0]}/{wo[1]} | {wi[0]}/{wi[1]} |")
    lines += ["", "## By skill (trigger and control cases combined)", "",
              "| Skill | " + " | ".join(f"`{m}` without → with" for m in models) + " |",
              "|---|" + "---|" * len(models)]
    for skill in sorted({c["skill"] for c in cases}):
        cells = []
        for m in models:
            wo = rate([r for r in rows if r["model"] == m and r["skill"] == skill and r["condition"] == "without"])
            wi = rate([r for r in rows if r["model"] == m and r["skill"] == skill and r["condition"] == "with"])
            cells.append(f"{wo[0]}/{wo[1]} → {wi[0]}/{wi[1]}")
        lines.append(f"| {skill} | " + " | ".join(cells) + " |")
    lines += ["", "## By case", "", "| Case | Kind | " + " | ".join(f"`{m}` without → with" for m in models) + " |",
              "|---|---|" + "---|" * len(models)]
    for c in cases:
        cells = []
        for m in models:
            wo = rate([r for r in rows if r["model"] == m and r["case"] == c["id"] and r["condition"] == "without"])
            wi = rate([r for r in rows if r["model"] == m and r["case"] == c["id"] and r["condition"] == "with"])
            cells.append(f"{wo[0]}/{wo[1]} → {wi[0]}/{wi[1]}")
        lines.append(f"| {c['id']} | {c['kind']} | " + " | ".join(cells) + " |")
    lines += [
        "", "## Limitations", "",
        "- Small sample: a few runs per case. Treat differences of one or two runs as noise.",
        "- The skill is placed in the system prompt, as an agent would after activating it; whether an agent selects the skill on its own is not tested here.",
        "- A model grades the answers. Criteria are binary and specific, but spot-check `raw.jsonl` against your own judgment.",
        "- Cases are synthetic and short; real tasks are longer and messier.",
        "",
        "Raw answers and per-criterion grades: [raw.jsonl](raw.jsonl). Cases: [cases.yaml](../../skills/cases.yaml).",
    ]
    (out / "summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--models", nargs="+", default=["openai:gpt-6.1-terra"])
    ap.add_argument("--judge", default="openai:gpt-6.1-sol")
    ap.add_argument("--runs", type=int, default=3)
    ap.add_argument("--cases", nargs="*", help="case ids or skill names to include")
    ap.add_argument("--out", default=None, help="output folder (default: evals/results/<today>)")
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--dry-run", action="store_true", help="validate cases and show the plan; no model calls")
    ap.add_argument("--base-prompt", default=None, help="override the base system prompt used in both conditions")
    args = ap.parse_args()
    if args.base_prompt:
        global BASE_SYSTEM
        BASE_SYSTEM = args.base_prompt

    cases = load_cases(args.cases)
    jobs = [(c, m, cond, r) for c in cases for m in args.models for cond in ("without", "with")
            for r in range(1, args.runs + 1)]
    print(f"{len(cases)} cases x {len(args.models)} model(s) x 2 conditions x {args.runs} run(s) "
          f"= {len(jobs)} answers + {len(jobs)} grading calls")
    if args.dry_run:
        c = cases[0]
        print(f"\nExample (case {c['id']}, condition 'with'):\n--- system ---\n{system_prompt(c, 'with')[:600]}...\n"
              f"--- messages ---\n{json.dumps(c['_messages'], ensure_ascii=False)[:600]}\n--- criteria ---")
        for i, cr in enumerate(c["criteria"], 1):
            print(f"{i}. {cr}")
        return 0

    out = Path(args.out) if args.out else EVALS / "results" / dt.date.today().isoformat()
    out.mkdir(parents=True, exist_ok=True)
    raw_path = out / "raw.jsonl"
    done = {}
    if raw_path.exists():
        for line in raw_path.read_text(encoding="utf-8").splitlines():
            row = json.loads(line)
            done[row["key"]] = row
    todo = [j for j in jobs if job_key(j[0]["id"], j[1], j[2], j[3]) not in done]
    print(f"{len(done)} already done, {len(todo)} to run -> {out}")

    failures = 0
    with cf.ThreadPoolExecutor(max_workers=args.workers) as pool:
        futs = {pool.submit(run_one, *j, args.judge): j for j in todo}
        for i, fut in enumerate(cf.as_completed(futs), 1):
            c, m, cond, r = futs[fut]
            try:
                row = fut.result()
            except Exception as e:  # keep going; failed jobs can be resumed
                failures += 1
                print(f"[{i}/{len(todo)}] FAILED {c['id']} {m} {cond} run{r}: {e}")
                continue
            with LOCK:
                with raw_path.open("a", encoding="utf-8") as f:
                    f.write(json.dumps(row, ensure_ascii=False) + "\n")
                done[row["key"]] = row
            print(f"[{i}/{len(todo)}] {'PASS' if row['passed'] else 'fail'} {c['id']} {m} {cond} run{r}")

    rows = [done[k] for k in (job_key(j[0]["id"], j[1], j[2], j[3]) for j in jobs) if k in done]
    summarize(rows, cases, out, args.models, args.judge, args.runs)
    print(f"\nWrote {out / 'summary.md'} ({len(rows)}/{len(jobs)} runs complete, {failures} failed)")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
