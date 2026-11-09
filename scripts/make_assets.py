#!/usr/bin/env python3
"""Generate the README figure and the social preview from the published eval data.

  assets/fig-results-light.svg, assets/fig-results-dark.svg   Figure 1, one file per GitHub theme
  assets/social-preview.png                                   1280x640 image for the repository's social preview

Every number is read from evals/results/*/raw.jsonl, so the figure can't drift from the data.
Requires matplotlib.   Run:  python scripts/make_assets.py
"""
from __future__ import annotations

import json
import math
from collections import defaultdict
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets"
RESULTS = ROOT / "evals" / "results"
SUITES = [("First suite", "2026-11-09-round2"), ("Harder suite", "2026-11-09-round4-hard-suite")]
MODELS = [("Sonnet", "claude-cli:sonnet"), ("Haiku", "claude-cli:haiku")]
LABELS = {  # case id -> short label for panel (b); * = skill revised after this run (see the change log)
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
THEMES = {
    "light": dict(text="#1f2328", muted="#59636e", grid="#d8dee4", without="#8c959f", with_="#0550ae", down="#bc4c00"),
    "dark": dict(text="#e6edf3", muted="#9198a1", grid="#30363d", without="#8b949e", with_="#4493f8", down="#f0883e"),
}


def load(run_dir: str) -> list[dict]:
    path = RESULTS / run_dir / "raw.jsonl"
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def wilson(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    """95% Wilson score interval for k successes out of n."""
    p = k / n
    centre = (p + z * z / (2 * n)) / (1 + z * z / n)
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    return max(0.0, centre - half), min(1.0, centre + half)


def collect():
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


def style(ax, t):
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color(t["muted"])
    ax.tick_params(colors=t["muted"], labelcolor=t["text"], length=3)
    ax.tick_params(axis="y", length=0)
    ax.grid(axis="x", color=t["grid"], linewidth=0.6)
    ax.set_axisbelow(True)


def figure(theme: str, overall, cases):
    t = THEMES[theme]
    plt.rcParams.update({"font.family": ["Arial", "Helvetica", "DejaVu Sans"], "font.size": 10.5,
                         "svg.fonttype": "path", "text.color": t["text"]})
    fig, (a, b) = plt.subplots(2, 1, figsize=(8.0, 8.2),
                               gridspec_kw={"height_ratios": [len(overall) * 1.55, len(cases)], "hspace": 0.5})

    # (a) all trigger cases, with 95% Wilson intervals
    style(a, t)
    for i, (label, wo, wi) in enumerate(overall):
        y = len(overall) - 1 - i
        for (k, n), dy, color, face in ((wo, 0.14, t["without"], "none"), (wi, -0.14, t["with_"], t["with_"])):
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

    # (b) cases where the skill changed the outcome
    style(b, t)
    for i, (label, wo, wi) in enumerate(cases):
        y = len(cases) - 1 - i
        color = t["with_"] if wi[0] >= wo[0] else t["down"]
        b.annotate("", xy=(wi[0], y), xytext=(wo[0], y),
                   arrowprops=dict(arrowstyle="-|>", color=color, linewidth=1.3, shrinkA=4, shrinkB=4,
                                   mutation_scale=10))
        b.plot(wo[0], y, "o", markersize=6.5, markerfacecolor="none", markeredgecolor=t["without"], markeredgewidth=1.4)
        b.plot(wi[0], y, "o", markersize=6.5, markerfacecolor=color, markeredgecolor=color)
    b.set_yticks(range(len(cases)))
    b.set_yticklabels([c[0] for c in reversed(cases)])
    b.set_xlim(-0.3, 6.3)
    b.set_xticks(range(7))
    b.set_ylim(-0.6, len(cases) - 0.4)
    b.set_xlabel("Runs passed, of 6 (two models, 3 runs each)", color=t["text"])
    b.set_title("(b) Cases where the skill changed the outcome", loc="left", fontsize=11.5, fontweight="bold",
                color=t["text"], pad=10)

    handles = [Line2D([], [], marker="o", linestyle="", markersize=6.5, markerfacecolor="none",
                      markeredgecolor=t["without"], markeredgewidth=1.4, label="Without skill"),
               Line2D([], [], marker="o", linestyle="", markersize=6.5, color=t["with_"], label="With skill"),
               Line2D([], [], marker="o", linestyle="", markersize=6.5, color=t["down"], label="With skill, worse")]
    fig.legend(handles=handles, loc="lower center", ncol=3, frameon=False, bbox_to_anchor=(0.5, -0.02),
               labelcolor=t["text"])
    fig.align_ylabels([a, b])
    return fig


def social_preview(overall) -> None:
    plt.rcParams.update({"font.family": ["Arial", "Helvetica", "DejaVu Sans"]})
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
    fig.savefig(OUT / "social-preview.png", dpi=100, facecolor="#ffffff")
    plt.close(fig)


def main() -> None:
    OUT.mkdir(exist_ok=True)
    overall, cases = collect()
    for theme in THEMES:
        fig = figure(theme, overall, cases)
        path = OUT / f"fig-results-{theme}.svg"
        fig.savefig(path, format="svg", bbox_inches="tight", pad_inches=0.3, transparent=True,
                    metadata={"Date": None})
        plt.close(fig)
        print("wrote", path.relative_to(ROOT).as_posix())
    social_preview(overall)
    print("wrote assets/social-preview.png")
    for label, wo, wi in overall + cases:
        print(f"  {label}: {wo[0]}/{wo[1]} -> {wi[0]}/{wi[1]}")


if __name__ == "__main__":
    main()
