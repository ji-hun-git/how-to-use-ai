# Changelog

This repository is updated as AI tools and official guides change. The evidence behind each update is in the reports in the [research/](research/) folder.

---

## 2026-11-09 · Installable edition

Made the guide usable inside AI tools, not just readable, after comparing it with the most popular repositories in this space ([COMPARISON.md](COMPARISON.md)).

### Added
- **10 Agent Skills** ([skills/](skills/README.md)): clarify-first, coverage-check, grounded-answer, verify-claims, honest-critique, fresh-eyes-review, fresh-start-handoff, prompt-improver, task-spec, learning-tutor; each with inline evidence
- **Claude Code plugin and marketplace** (`.claude-plugin/`), installable with one command; also installable with `npx skills add`
- **Drop-in rules** ([drop-in/](drop-in/README.md)): an 18-rule AGENTS.md / CLAUDE.md, a Cursor rule, and short/long custom instructions for chat apps
- **Prompt library** ([prompts/](prompts/README.md)): 30 prompts by task, tagged by failure mode
- **Prompt clinic** ([examples/08](examples/08-prompt-clinic.md)): 12 common prompts diagnosed and fixed
- **Guide 11** ([docs/11](docs/11-skills-and-agent-rules.md)): where instructions should live (prompt, rules file, skill, hook)
- **Runnable eval** ([evals/](evals/README.md)): promptfoo comparison of a naive vs a grounded prompt
- **Comparison page** ([COMPARISON.md](COMPARISON.md)), **llms.txt**, Mermaid diagrams, and a CI workflow that validates skills, manifests and links

### Changed
- README first screen: one-line installs, before/after evidence, and a failure-mode map

---

## 2026-11-09 · English-only edition

Translated the whole repo to English and removed program-specific and personal references.

---

## 2026-11-09 · 2026 update

Re-researched and incorporated the official guides, research, tool changes, and South Korean laws and guidelines published in 2026 (especially May–November). Evidence: [2026 update report](research/2026-update-report.md)

### Added
- **Measurements on the newest models** ([04](docs/04-failure-modes.md#-2026-update-how-current-models-fare)): hallucination rates for 2026 models (Vectara, AI Index 2026, AA-Omniscience), a 2026 study on fabricated references, 2,266 court incidents, the *Science* 2026 sycophancy study, sycophancy collapse in long conversations (SPINE), research on 1M-token context, and the limit of 5–6 simultaneous constraints
- **Snapshot of major models** ([05](docs/05-models-and-reasoning.md#-snapshot-major-models-as-of-november-2026)): Anthropic, OpenAI, and Google models as of November 2026, plus new features such as memory, skills, and scheduled runs
- **AI coding tool changes** ([07](docs/07-ai-coding.md#7--tool-changes-in-2026)): `/goal`, Stop hooks, `/code-review`, auto mode as the default, Gemini CLI → Antigravity CLI, and the shift from "reading every line" to "verifying with evidence"
- **Managing memory** ([06](docs/06-workflows.md#-managing-memory-anthropic-2026-11)): Anthropic's principles for agent memory, separating the generator from the evaluator
- **Local laws and guidelines (example: South Korea)** ([09](docs/09-security-privacy.md#5-local-laws-and-guidelines-example-south-korea-2026)): the AI Basic Act (in force since 2026-01-22), the PIPC user guide (2026-05), the revised guidelines for writing privacy policies, public-sector AI guides and ethics standards, and materials from KICE and KCUE
- **2026 myths vs. evidence** ([10](docs/10-myths-vs-evidence.md#11--new-evidence-from-2026)): METR's 2026 follow-up results, Wharton Report 5, the *Science* sycophancy study
- **Learning research** ([Example 6](examples/06-learning-with-ai.md)): Anthropic's 2026 learning experiment, a randomized trial of a university AI tutor
- **Resources** ([awesome](resources/awesome.md)): Karpathy's 2026 activity (joining Anthropic, agentic engineering, HackerTube), repositories that took off in 2026 (checked directly), 2026 research and independent evaluations

### Corrections
- Date "agentic engineering" was proposed: based on press coverage (2026-02) → **based on the original post, 2026-02-04**
- Date of the MOIS/NIA *Public-Sector AI Adoption and Use Guide*: 2026-07 → **2026-06-10**
- OpenAI's "trimmed-down prompts score 10–15% higher": source changed from "the latest guide" to **an internal evaluation in the GPT-5.6 guide (2026-07), a directional figure**
- "Remove verification instructions" and "remove emphatic phrasing": wording that implied all three companies agreed → corrected to **advice that differs by model and company**
- METR "19% slower": now reflects METR's 2026-02 statement that this result does not represent current tools

### Marked as historical data
Figures measured on older 2023–2025 models (FlipFlop 46%, fabricated citations 55%/18%, FActScore 58%, Stanford legal tools 17–34%, etc.) are kept as illustrations of the underlying principles, but they now note when they were measured and appear alongside 2026 measurements.

---

## 2026-11-09 · First release

- 10 guides, 8 templates, 7 examples, a curated resource list, and the evidence report (288 sources)
