#!/usr/bin/env python3
"""Generate the README images in assets/ (light and dark variants).

  banner-{light,dark}.svg        header banner
  eval-results-{light,dark}.svg  with-vs-without results chart (numbers below, from evals/results/README.md)
  social-preview.svg             1280x640 image for the repository's social preview (render to PNG to upload)

Run:  python scripts/make_assets.py
Update RESULTS when new eval results are published.
"""
from __future__ import annotations

from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets"

SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, 'Liberation Mono', monospace"

THEMES = {
    "light": {
        "bg": "#ffffff", "panel": "#f6f8fa", "border": "#d0d7de", "text": "#1f2328", "muted": "#59636e",
        "track": "#eaeef2", "without": "#afb8c1",
        "accents": ["#0969da", "#bc4c00", "#cf222e", "#8250df"], "brand": "#0969da", "good": "#1a7f37",
    },
    "dark": {
        "bg": "#0d1117", "panel": "#161b22", "border": "#30363d", "text": "#e6edf3", "muted": "#9198a1",
        "track": "#21262d", "without": "#57606a",
        "accents": ["#4493f8", "#db6d28", "#f85149", "#ab7df8"], "brand": "#4493f8", "good": "#3fb950",
    },
}

FAILURES = [  # failure mode, the skill that fixes it first
    ("Misunderstanding", "clarify-first"),
    ("Omission", "coverage-check"),
    ("Fabrication", "grounded-answer"),
    ("Sycophancy", "honest-critique"),
]

# Trigger cases, passing runs without -> with the skill (evals/results/README.md, 2026-11-09).
RESULTS = [
    ("First suite · 20 short cases", "Claude Sonnet", (42, 48), (47, 48)),
    ("First suite · 20 short cases", "Claude Haiku", (41, 48), (48, 48)),
    ("Harder suite · 16 long or tricky cases", "Claude Sonnet", (39, 42), (41, 42)),
    ("Harder suite · 16 long or tricky cases", "Claude Haiku", (36, 42), (39, 42)),
]
TUTORING = ((0, 12), (12, 12))
CONTROLS = ((36, 36), (36, 36))


def t(x, y, s, size, fill, family=SANS, weight=400, anchor="start", spacing=None, opacity=None):
    extra = f' letter-spacing="{spacing}"' if spacing is not None else ""
    extra += f' fill-opacity="{opacity}"' if opacity is not None else ""
    return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" '
            f'fill="{fill}" text-anchor="{anchor}"{extra}>{escape(s)}</text>')


def failure_cards(c, x0, y0, w, h, gap, title_size=23, skill_size=15):
    parts = []
    for i, (name, skills) in enumerate(FAILURES):
        x = x0 + (i % 2) * (w + gap)
        y = y0 + (i // 2) * (h + gap)
        accent = c["accents"][i]
        parts += [
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{c["panel"]}" stroke="{c["border"]}"/>',
            f'<rect x="{x}" y="{y + 18}" width="5" height="{h - 36}" rx="2.5" fill="{accent}"/>',
            t(x + 26, y + 40, f"0{i + 1}", 14, accent, MONO, 700, spacing=1),
            t(x + 26, y + 40 + title_size + 8, name, title_size, c["text"], SANS, 650),
            t(x + 26, y + h - 22, f"→ {skills}", skill_size, c["muted"], MONO),
        ]
    return parts


def banner(theme: str) -> str:
    c = THEMES[theme]
    W, H = 1280, 400
    p = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
        f'aria-label="how-to-use-ai: an evidence-based guide, tested Agent Skills and rules that stop AI from '
        f'misunderstanding, omitting, fabricating and flattering">',
        f'<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="24" fill="{c["bg"]}" stroke="{c["border"]}"/>',
        t(64, 104, "EVIDENCE-BASED · TESTED · 2026", 15, c["brand"], SANS, 700, spacing=2.5),
        t(62, 168, "how-to-use-ai", 60, c["text"], MONO, 700, spacing=-1),
        t(64, 222, "Stop AI from misunderstanding you,", 25, c["text"], SANS, 500),
        t(64, 256, "skipping things, making things up", 25, c["text"], SANS, 500),
        t(64, 290, "and just agreeing with you.", 25, c["text"], SANS, 500),
        t(64, 342, "Guide · 10 Agent Skills · Drop-in rules · 460+ sources", 19, c["muted"], SANS, 500),
    ]
    p += failure_cards(c, 676, 64, 262, 124, 16)
    p.append("</svg>")
    return "\n".join(p) + "\n"


def results_chart(theme: str) -> str:
    c = THEMES[theme]
    W, H = 1280, 724
    bx, bw = 380, 600  # bar start and width of 100%
    p = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
        f'aria-label="Passing runs on trigger cases without and with the skills: first suite Sonnet 42/48 to 47/48, '
        f'Haiku 41/48 to 48/48; harder suite Sonnet 39/42 to 41/42, Haiku 36/42 to 39/42. Tutoring 0/12 to 12/12. '
        f'Control cases 36/36 either way.">',
        f'<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="24" fill="{c["bg"]}" stroke="{c["border"]}"/>',
        t(64, 72, "Same task, skill off vs. on", 30, c["text"], SANS, 700),
        t(64, 108, "Share of runs that passed every check · trigger cases · blind-graded · 2026-11-09", 19, c["muted"]),
        f'<rect x="{W - 380}" y="56" width="18" height="18" rx="3" fill="{c["without"]}"/>',
        t(W - 354, 72, "Without skill", 18, c["muted"], SANS, 500),
        f'<rect x="{W - 214}" y="56" width="18" height="18" rx="3" fill="{c["brand"]}"/>',
        t(W - 188, 72, "With skill", 18, c["muted"], SANS, 500),
    ]
    top, step = 150, 100
    # gridlines
    for frac, label in ((0, "0%"), (0.5, "50%"), (1, "100%")):
        x = bx + bw * frac
        p.append(f'<line x1="{x}" y1="{top - 14}" x2="{x}" y2="{top + step * 4 - 18}" stroke="{c["border"]}" '
                 f'stroke-dasharray="4 6"/>')
        p.append(t(x, top + step * 4 + 2, label, 15, c["muted"], SANS, 500, anchor="middle"))
    for i, (suite, model, wo, wi) in enumerate(RESULTS):
        y = top + i * step
        p.append(t(64, y + 20, model, 21, c["text"], SANS, 650))
        p.append(t(64, y + 48, suite, 16, c["muted"]))
        for j, ((num, den), fill) in enumerate(((wo, c["without"]), (wi, c["brand"]))):
            by = y + j * 32
            width = bw * num / den
            p.append(f'<rect x="{bx}" y="{by}" width="{bw}" height="24" rx="6" fill="{c["track"]}"/>')
            p.append(f'<rect x="{bx}" y="{by}" width="{width:.1f}" height="24" rx="6" fill="{fill}"/>')
            pct = round(100 * num / den)
            p.append(t(bx + bw + 18, by + 19, f"{num}/{den} · {pct}%", 19,
                       c["text"] if j else c["muted"], MONO, 700 if j else 500))
    # callout cards
    cy, ch = top + step * 4 + 30, 134
    cards = [
        ("Tutoring (learning-tutor)", f"{TUTORING[0][0]}/{TUTORING[0][1]} → {TUTORING[1][0]}/{TUTORING[1][1]}",
         "runs that gave hints instead of handing over the answer", c["good"]),
        ("Control cases", f"{CONTROLS[0][0]}/{CONTROLS[0][1]} → {CONTROLS[1][0]}/{CONTROLS[1][1]}",
         "no regressions: a skill never broke a correct default", c["brand"]),
    ]
    for k, (title, big, sub, accent) in enumerate(cards):
        x = 64 + k * 584
        p += [
            f'<rect x="{x}" y="{cy}" width="568" height="{ch}" rx="14" fill="{c["panel"]}" stroke="{c["border"]}"/>',
            f'<rect x="{x}" y="{cy + 18}" width="5" height="{ch - 36}" rx="2.5" fill="{accent}"/>',
            t(x + 26, cy + 38, title, 18, c["muted"], SANS, 600),
            t(x + 26, cy + 84, big, 38, accent, MONO, 700),
            t(x + 26, cy + 114, sub, 17, c["muted"]),
        ]
    p.append("</svg>")
    return "\n".join(p) + "\n"


def social_preview() -> str:
    c = THEMES["light"]
    W, H = 1280, 640
    p = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">',
        f'<rect width="{W}" height="{H}" fill="{c["bg"]}"/>',
        f'<rect x="0" y="0" width="{W}" height="10" fill="{c["brand"]}"/>',
        t(80, 120, "EVIDENCE-BASED · TESTED · 2026", 20, c["brand"], SANS, 700, spacing=3),
        t(76, 210, "how-to-use-ai", 88, c["text"], MONO, 700, spacing=-2),
        t(80, 280, "Stop AI from misunderstanding you, skipping things,", 32, c["text"], SANS, 500),
        t(80, 324, "making things up and just agreeing with you.", 32, c["text"], SANS, 500),
    ]
    # four cards in one row
    w, h, gap = 266, 130, 16
    for i, (name, skills) in enumerate(FAILURES):
        x, y = 80 + i * (w + gap), 380
        accent = c["accents"][i]
        p += [
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{c["panel"]}" stroke="{c["border"]}"/>',
            f'<rect x="{x}" y="{y + 20}" width="5" height="{h - 40}" rx="2.5" fill="{accent}"/>',
            t(x + 24, y + 42, f"0{i + 1}", 15, accent, MONO, 700, spacing=1),
            t(x + 24, y + 76, name, 24, c["text"], SANS, 650),
            t(x + 24, y + h - 22, f"→ {skills}", 15, c["muted"], MONO),
        ]
    p.append(t(80, 584, "Guide · 10 tested Agent Skills · Drop-in rules · github.com/ji-hun-git/how-to-use-ai",
               20, c["muted"], SANS, 500))
    p.append("</svg>")
    return "\n".join(p) + "\n"


def main() -> None:
    OUT.mkdir(exist_ok=True)
    files = {"social-preview.svg": social_preview()}
    for theme in THEMES:
        files[f"banner-{theme}.svg"] = banner(theme)
        files[f"eval-results-{theme}.svg"] = results_chart(theme)
    for name, svg in files.items():
        (OUT / name).write_text(svg, encoding="utf-8", newline="\n")
        print("wrote", (OUT / name).relative_to(OUT.parent).as_posix())


if __name__ == "__main__":
    main()
