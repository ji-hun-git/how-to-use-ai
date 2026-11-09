#!/usr/bin/env python3
"""Generate the repository's figures, each in a light and a dark version, plus the social preview.

  assets/fig-results-{light,dark}.svg        Figure 1: skill off vs. on (from evals/results/*/raw.jsonl)
  assets/fig-eval-method-{light,dark}.svg    Figure 2: how each evaluation case is run and graded
  assets/fig-verdicts-{light,dark}.svg       Figure 3: verdicts for the methods in docs/14 (from its tables)
  assets/fig-failure-modes-{light,dark}.svg  Figure 4: where each failure mode enters a task
  assets/social-preview.png                  1280x640 image for the repository's social preview

Data figures read their numbers from the repository, so they can't drift from the data.
Every figure has an opaque background in its theme's colors, so it stays readable even when
GitHub shows the other theme's version. Output is deterministic.

Requires matplotlib.   Run:  python scripts/make_assets.py
"""
from __future__ import annotations

import io
import json
import math
import re
from collections import defaultdict
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402
from matplotlib.patches import FancyArrowPatch, Patch, Rectangle  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets"
RESULTS = ROOT / "evals" / "results"
METHODS_DOC = ROOT / "docs" / "14-methods-and-papers.md"
SUITES = [("First suite", "2026-11-09-round2"), ("Harder suite", "2026-11-09-round4-hard-suite")]
MODELS = [("Sonnet", "claude-cli:sonnet"), ("Haiku", "claude-cli:haiku")]
LABELS = {  # case id -> short label for Figure 1b; * = skill revised after this run (see the change log)
    "tutor-homework": "learning-tutor: homework request",
    "tutor-debug-attempt": "learning-tutor: student's buggy code",
    "clarify-vague-offsite": "clarify-first: vague request",
    "improve-weak-prompt": "prompt-improver: weak prompt",
    "spec-vague-coding-task": "task-spec: vague coding task",
    "coverage-ticket-export": "coverage-check: 9,000-word export",
    "spec-destructive-job": "task-spec: destructive job",
    "critique-expert-pushback": "honest-critique: expert pushback",
    "handoff-reversals": "fresh-start-handoff: reversed edits*",
    "improve-support-bot-prompt": "prompt-improver: support-bot prompt*",
}
# GitHub Primer colors, so figures sit naturally on github.com in either theme.
THEMES = {
    "light": dict(bg="#ffffff", panel="#f6f8fa", border="#d0d7de", text="#1f2328", muted="#59636e", grid="#d8dee4",
                  without="#8c959f", with_="#0550ae", down="#bc4c00",
                  blue="#0969da", orange="#bc4c00", red="#cf222e", purple="#8250df", green="#1a7f37", gray="#8c959f"),
    "dark": dict(bg="#0d1117", panel="#161b22", border="#3d444d", text="#e6edf3", muted="#9198a1", grid="#30363d",
                 without="#8b949e", with_="#4493f8", down="#f0883e",
                 blue="#4493f8", orange="#f0883e", red="#f85149", purple="#ab7df8", green="#3fb950", gray="#8b949e"),
}
FONT = ["Arial", "Helvetica", "DejaVu Sans"]
MONO = ["Consolas", "DejaVu Sans Mono", "monospace"]


def base_style(t: dict) -> None:
    plt.rcParams.update({"font.family": FONT, "font.size": 10.5, "svg.fonttype": "path",
                         "svg.hashsalt": "how-to-use-ai", "text.color": t["text"]})


def save(fig, name: str, theme: str) -> None:
    t = THEMES[theme]
    buf = io.StringIO()
    fig.savefig(buf, format="svg", bbox_inches="tight", pad_inches=0.3, facecolor=t["bg"],
                metadata={"Date": None})
    (OUT / f"{name}-{theme}.svg").write_text(buf.getvalue(), encoding="utf-8", newline="\n")
    plt.close(fig)
    print(f"wrote assets/{name}-{theme}.svg")


def axis_style(ax, t):
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color(t["muted"])
    ax.tick_params(colors=t["muted"], labelcolor=t["text"], length=3)
    ax.tick_params(axis="y", length=0)
    ax.grid(axis="x", color=t["grid"], linewidth=0.6)
    ax.set_axisbelow(True)
    ax.set_facecolor(t["bg"])


# ------------------------------------------------------------------ Figure 1: results
def load(run_dir: str) -> list[dict]:
    path = RESULTS / run_dir / "raw.jsonl"
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def wilson(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    """95% Wilson score interval for k successes out of n."""
    p = k / n
    centre = (p + z * z / (2 * n)) / (1 + z * z / n)
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    return max(0.0, centre - half), min(1.0, centre + half)


def collect_results():
    overall, cases = [], []
    for suite, run_dir in SUITES:
        rows = [r for r in load(run_dir) if r["kind"] == "trigger"]
        for name, model in MODELS:
            cnt = {}
            for cond in ("without", "with"):
                sub = [r for r in rows if r["model"] == model and r["condition"] == cond]
                cnt[cond] = (sum(r["passed"] for r in sub), len(sub))
            overall.append((f"{name}, {suite.lower()}", cnt["without"], cnt["with"]))
        per = defaultdict(lambda: {"without": [0, 0], "with": [0, 0]})
        for r in rows:
            per[r["case"]][r["condition"]][0] += r["passed"]
            per[r["case"]][r["condition"]][1] += 1
        for case, c in per.items():
            if c["without"][0] != c["with"][0]:
                cases.append((LABELS.get(case, case), tuple(c["without"]), tuple(c["with"])))
    cases.sort(key=lambda x: (x[2][0] - x[1][0], x[2][0]), reverse=True)
    return overall, cases


def fig_results(theme: str, overall, cases):
    t = THEMES[theme]
    base_style(t)
    fig, (a, b) = plt.subplots(2, 1, figsize=(8.0, 8.2),
                               gridspec_kw={"height_ratios": [len(overall) * 1.55, len(cases)], "hspace": 0.5})
    fig.patch.set_facecolor(t["bg"])
    axis_style(a, t)
    for i, (label, wo, wi) in enumerate(overall):
        y = len(overall) - 1 - i
        for (k, n), dy, color, face in ((wo, 0.14, t["without"], t["bg"]), (wi, -0.14, t["with_"], t["with_"])):
            lo, hi = wilson(k, n)
            a.plot([lo * 100, hi * 100], [y + dy, y + dy], color=color, linewidth=1.2, solid_capstyle="butt")
            a.plot(k / n * 100, y + dy, "o", markersize=6.5, markerfacecolor=face, markeredgecolor=color,
                   markeredgewidth=1.4)
    a.set_yticks(range(len(overall)))
    a.set_yticklabels([f"{o[0]}\n{o[1][0]}/{o[1][1]} → {o[2][0]}/{o[2][1]}" for o in reversed(overall)],
                      linespacing=1.5)
    a.set_xlim(55, 101)
    a.set_xticks(range(55, 101, 5))
    a.set_ylim(-0.6, len(overall) - 0.4)
    a.set_xlabel("Runs that passed every check (%), with 95% CI", color=t["text"])
    a.set_title("(a) All trigger cases", loc="left", fontsize=11.5, fontweight="bold", color=t["text"], pad=10)

    axis_style(b, t)
    for i, (label, wo, wi) in enumerate(cases):
        y = len(cases) - 1 - i
        color = t["with_"] if wi[0] >= wo[0] else t["down"]
        b.annotate("", xy=(wi[0], y), xytext=(wo[0], y),
                   arrowprops=dict(arrowstyle="-|>", color=color, linewidth=1.3, shrinkA=4, shrinkB=4,
                                   mutation_scale=10))
        b.plot(wo[0], y, "o", markersize=6.5, markerfacecolor=t["bg"], markeredgecolor=t["without"],
               markeredgewidth=1.4)
        b.plot(wi[0], y, "o", markersize=6.5, markerfacecolor=color, markeredgecolor=color)
    b.set_yticks(range(len(cases)))
    b.set_yticklabels([c[0] for c in reversed(cases)])
    b.set_xlim(-0.3, 6.3)
    b.set_xticks(range(7))
    b.set_ylim(-0.6, len(cases) - 0.4)
    b.set_xlabel("Runs passed, of 6 (two models, 3 runs each)", color=t["text"])
    b.set_title("(b) Cases where the skill changed the outcome", loc="left", fontsize=11.5, fontweight="bold",
                color=t["text"], pad=10)
    handles = [Line2D([], [], marker="o", linestyle="", markersize=6.5, markerfacecolor=t["bg"],
                      markeredgecolor=t["without"], markeredgewidth=1.4, label="Without skill"),
               Line2D([], [], marker="o", linestyle="", markersize=6.5, color=t["with_"], label="With skill"),
               Line2D([], [], marker="o", linestyle="", markersize=6.5, color=t["down"], label="With skill, worse")]
    fig.legend(handles=handles, loc="lower center", ncol=3, frameon=False, bbox_to_anchor=(0.5, -0.02),
               labelcolor=t["text"])
    fig.align_ylabels([a, b])
    return fig


# ------------------------------------------------------------------ Figure 3: verdicts in docs/14
VERDICTS = ["Use", "Situational", "Mostly built in now", "Skip"]


def collect_verdicts():
    text = METHODS_DOC.read_text(encoding="utf-8")
    groups = []
    for sec in re.split(r"\n## ", text):
        title = sec.split("\n", 1)[0].strip()
        m = re.match(r"(\d+)\. (.+)", title)
        if not m or not any(l.startswith("| Method |") for l in sec.split("\n")):
            continue
        counts = dict.fromkeys(VERDICTS, 0)
        for line in sec.split("\n"):
            if not line.startswith("| ") or line.startswith("| Method |"):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            verdict = cells[2] if len(cells) >= 4 else ""
            for v in VERDICTS:
                if verdict.startswith(v.split()[0]):
                    counts[v] += 1
                    break
            else:
                raise ValueError(f"unrecognized verdict in docs/14: {verdict!r}")
        groups.append((m.group(2), counts))
    return groups


def fig_verdicts(theme: str, groups):
    t = THEMES[theme]
    base_style(t)
    colors = {"Use": t["green"], "Situational": t["blue"], "Mostly built in now": t["gray"], "Skip": t["orange"]}
    fig, ax = plt.subplots(figsize=(8.0, 5.4))
    fig.patch.set_facecolor(t["bg"])
    axis_style(ax, t)
    for i, (name, counts) in enumerate(groups):
        y = len(groups) - 1 - i
        left = 0
        for v in VERDICTS:
            n = counts[v]
            if n:
                ax.barh(y, n, left=left, height=0.62, color=colors[v], edgecolor=t["bg"], linewidth=1.2)
                ax.text(left + n / 2, y, str(n), ha="center", va="center", fontsize=9.5, color=t["bg"],
                        fontweight="bold")
            left += n
        ax.text(left + 0.25, y, str(left), va="center", fontsize=9.5, color=t["muted"])
    ax.set_yticks(range(len(groups)))
    ax.set_yticklabels([g[0] for g in reversed(groups)])
    total = sum(sum(c.values()) for _, c in groups)
    ax.set_xlim(0, max(sum(c.values()) for _, c in groups) + 1.5)
    ax.set_xlabel(f"Number of methods ({total} in total)", color=t["text"])
    totals = {v: sum(c[v] for _, c in groups) for v in VERDICTS}
    handles = [Patch(color=colors[v], label=f"{v} ({totals[v]})") for v in VERDICTS]
    ax.legend(handles=handles, loc="lower center", bbox_to_anchor=(0.42, 1.0), ncol=4, frameon=False,
              labelcolor=t["text"], handlelength=1.2, columnspacing=1.4)
    return fig


# ------------------------------------------------------------------ diagrams
def box(ax, t, x, y, w, h, title, body, accent=None, mono_lines=()):
    ax.add_patch(Rectangle((x, y), w, h, facecolor=t["panel"], edgecolor=t["border"], linewidth=1.0))
    if accent:
        ax.add_patch(Rectangle((x, y + h - 0.9), w, 0.9, facecolor=accent, edgecolor="none"))
    ax.text(x + 1.4, y + h - 3.0, title, fontsize=11, fontweight="bold", color=t["text"], va="top")
    ax.text(x + 1.4, y + h - 7.2, body, fontsize=9.6, color=t["muted"], va="top", linespacing=1.45)
    if mono_lines:
        ax.text(x + 1.4, y + 2.2, "\n".join(mono_lines), fontsize=9.2, color=t["text"], va="bottom",
                family=MONO, linespacing=1.5)


def arrow(ax, t, start, end):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=11, color=t["muted"],
                                 linewidth=1.2, shrinkA=0, shrinkB=0))


def fig_eval_method(theme: str):
    t = THEMES[theme]
    base_style(t)
    fig, ax = plt.subplots(figsize=(10.0, 3.6))
    fig.patch.set_facecolor(t["bg"])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 36)
    ax.axis("off")
    box(ax, t, 0.5, 6, 19, 24, "Test case", "The request, any\ndocuments, and\npass/fail criteria\n\n36 cases: 30 trigger,\n6 control")
    box(ax, t, 26, 19.5, 20, 13.5, "Without skill", "Base system prompt", accent=t["gray"])
    box(ax, t, 26, 2.5, 20, 13.5, "With skill", "Base system prompt\nplus the SKILL.md", accent=t["blue"])
    box(ax, t, 53, 6, 19, 24, "Model under test", "Claude Sonnet and\nClaude Haiku\n\n3 runs per case and\ncondition")
    box(ax, t, 79, 6, 20.5, 24, "Grading", "Claude Opus, blind to\nthe condition, plus\ncode checks for counts\nand exact IDs\n\nA run passes only if\nevery criterion passes")
    arrow(ax, t, (19.5, 20), (26, 26))
    arrow(ax, t, (19.5, 16), (26, 9.5))
    arrow(ax, t, (46, 26), (53, 20))
    arrow(ax, t, (46, 9.5), (53, 16))
    arrow(ax, t, (72, 18), (79, 18))
    return fig


def fig_failure_modes(theme: str):
    t = THEMES[theme]
    base_style(t)
    fig, ax = plt.subplots(figsize=(10.0, 3.9))
    fig.patch.set_facecolor(t["bg"])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 39)
    ax.axis("off")
    stages = [
        ("1. The request", "Misunderstanding", t["blue"],
         "Gaps in the request get\nfilled with assumptions,\nwhich then stick", ["clarify-first", "task-spec", "fresh-start-handoff"]),
        ("2. Working on the input", "Omission", t["orange"],
         "Requirements and long\ninputs are only partly\nused", ["coverage-check"]),
        ("3. The answer", "Fabrication", t["red"],
         "A confident guess is\nrewarded over \"I don't\nknow\"", ["grounded-answer", "verify-claims"]),
        ("4. Review and pushback", "Sycophancy", t["purple"],
         "Agreement is rewarded\nover checking", ["honest-critique", "fresh-eyes-review"]),
    ]
    w, gap = 22.4, 3.2
    for i, (stage, mode, color, cause, skills) in enumerate(stages):
        x = 0.5 + i * (w + gap)
        ax.add_patch(Rectangle((x, 1), w, 36.5, facecolor=t["panel"], edgecolor=t["border"], linewidth=1.0))
        ax.add_patch(Rectangle((x, 36.6), w, 0.9, facecolor=color, edgecolor="none"))
        ax.text(x + 1.4, 34.2, stage, fontsize=9.6, color=t["muted"], va="top")
        ax.text(x + 1.4, 30.2, mode, fontsize=12.5, fontweight="bold", color=color, va="top")
        ax.text(x + 1.4, 25.4, cause, fontsize=9.6, color=t["text"], va="top", linespacing=1.45)
        ax.plot([x + 1.4, x + w - 1.4], [12.6, 12.6], color=t["border"], linewidth=0.8)
        ax.text(x + 1.4, 11.2, "Skills", fontsize=9, color=t["muted"], va="top")
        ax.text(x + 1.4, 7.6, "\n".join(skills), fontsize=9.2, color=t["text"], va="top", family=MONO,
                linespacing=1.5)
        if i < len(stages) - 1:
            arrow(ax, t, (x + w + 0.3, 20), (x + w + gap - 0.3, 20))
    return fig


# ------------------------------------------------------------------ social preview
def social_preview(overall) -> None:
    plt.rcParams.update({"font.family": FONT})
    fig = plt.figure(figsize=(12.8, 6.4), dpi=100)
    fig.patch.set_facecolor("#ffffff")
    ink, muted, accent = "#1f2328", "#59636e", "#0550ae"
    wo = sum(o[1][0] for o in overall), sum(o[1][1] for o in overall)
    wi = sum(o[2][0] for o in overall), sum(o[2][1] for o in overall)
    fig.text(0.07, 0.80, "how-to-use-ai", fontsize=54, fontweight="bold", color=ink, family="monospace")
    for i, line in enumerate(["Evidence-based guide and tested Agent Skills that make AI",
                              "assistants ask before guessing, cover every requirement,",
                              "cite what they claim, and hold their ground when they're right."]):
        fig.text(0.07, 0.62 - i * 0.075, line, fontsize=24, color=ink)
    fig.add_artist(Line2D([0.07, 0.93], [0.30, 0.30], color="#d0d7de", linewidth=1.2))
    fig.text(0.07, 0.19, f"Skills on vs. off, blind-graded:  {wo[0]}/{wo[1]} → {wi[0]}/{wi[1]} passing runs",
             fontsize=20, color=accent, fontweight="bold")
    fig.text(0.07, 0.09, "github.com/ji-hun-git/how-to-use-ai", fontsize=18, color=muted)
    fig.savefig(OUT / "social-preview.png", dpi=100, facecolor="#ffffff", metadata={"Software": None})
    plt.close(fig)
    print("wrote assets/social-preview.png")


def main() -> None:
    OUT.mkdir(exist_ok=True)
    overall, cases = collect_results()
    groups = collect_verdicts()
    for theme in THEMES:
        save(fig_results(theme, overall, cases), "fig-results", theme)
        save(fig_eval_method(theme), "fig-eval-method", theme)
        save(fig_verdicts(theme, groups), "fig-verdicts", theme)
        save(fig_failure_modes(theme), "fig-failure-modes", theme)
    social_preview(overall)
    for label, wo, wi in overall + cases:
        print(f"  {label}: {wo[0]}/{wo[1]} -> {wi[0]}/{wi[1]}")
    for name, counts in groups:
        print(f"  {name}: {counts}")


if __name__ == "__main__":
    main()
