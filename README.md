# how-to-use-ai

**How to actually use AI well: an evidence-based guide to prompting, workflows, and verification**

[One-page cheatsheet](CHEATSHEET.md) · [Evidence report](research/evidence-report.md)

![updated](https://img.shields.io/badge/updated-2026--11-blue) ![license](https://img.shields.io/badge/license-MIT-green)

> Instead of viral "prompt hacks," this guide checks and distills what the **official guides from Anthropic · OpenAI · Google · Microsoft**, **research from MIT · Harvard · Wharton · Stanford**, and practitioners like **Andrej Karpathy** actually say.
> Every claim has a source, and anything we could not verify is marked as unverified.

---

## 🆕 2026 update (2026-11-09)

This update reflects the latest research, official guides, tool changes, and laws (example: South Korea) from 2026. Here are the highlights. → [Full changelog](CHANGELOG.md) · [2026 update report](research/2026-update-report.md)

| What changed | Summary |
|---|---|
| **Hallucination is down, not gone** | The newest models are better at saying "I don't know," but even models released in 2026 mixed fabricated entries into 35% of their reference responses, and court filings containing AI-fabricated case law have grown to 2,266 → [04](docs/04-failure-modes.md#-2026-update-how-current-models-fare) |
| **Sycophancy grows in long conversations** | Under persistent pushback on a false claim, even the newest models caved in 20–97% of cases within 25 turns. People trust sycophantic answers more (*Science* 2026) → make important judgments in a **fresh chat** |
| **1M tokens: retrieval solved, synthesis not** | Finding a single sentence in long material is now near-perfect, but reasoning that ties multiple pieces of information together still degrades → including only the material you need is still good advice |
| **AI coding: from "reading every line" to "verifying with evidence"** | `/goal`, Stop hooks, and independent review agents have become standard tools. The key question is "What did you verify it with?" → [07](docs/07-ai-coding.md#-what-changed-in-2026-from-reading-every-line-to-verifying-with-evidence) |
| **South Korea: the AI Basic Act is in force** | Took effect 2026-01-22. Notice and labeling duties fall on AI providers. The PIPC published a guide for general users in 2026-05 (including opting out of training use) → [09](docs/09-security-privacy.md#5-local-laws-and-guidelines-example-south-korea-2026) |

---

## The 30-second version

> **The unit of good AI use is not a "good sentence." It is "good instructions + good verification."**

### 1. How to instruct: the six elements

| Role | Context ★ | Instruction ★ | Format ★ | Constraints | Examples |
|---|---|---|---|---|---|
| From what perspective, in what tone | Why, for whom, in what situation | What to do, and when it counts as done | Structure and length of the output | Rules that must be followed | 3–5 samples of a good result |

★ According to the research, the place to spend your time is **Context · Instruction · Format**. Role prompts like "the world's best expert" do not improve accuracy. → [02. The six elements of a prompt](docs/02-prompt-anatomy.md)

### 2. How to diagnose: the three failure modes

| Misunderstanding | Omission | Fabrication (hallucination) |
|---|---|---|
| It understood the request differently | It left out something it should have done | It made up something that doesn't exist |
| Give context and done criteria, let it ask questions first, and if the chat gets tangled, summarize and **start a fresh chat** | Number your requirements, put material on top and the question at the bottom, use a **coverage table** | **Give it the right to say "I don't know,"** ground answers only in the material, quote first, **check sources yourself** |

There is also a bonus failure: **sycophancy** (going along with whatever you say). Asking "Are you really sure?" flipped even correct answers 46% of the time (a 2023 study), and even the newest 2026 models cave under prolonged pushback. → [04. Misunderstanding · Omission · Fabrication](docs/04-failure-modes.md)

### 3. How to work: the basic loop

```
Specify → Plan → Execute → Verify → Learn
```

Write the goal and done criteria first, get the plan approved before big jobs, give the AI a way to check its own work, verify **with outside evidence**, and fold recurring mistakes back into your templates. → [06. Workflows](docs/06-workflows.md)

---

## Use it now: copy-and-paste templates

| Situation | Template |
|---|---|
| Any task | [Universal prompt template](templates/universal-prompt.md) (3-line version / full version) |
| When the AI keeps misunderstanding what you mean | [Preventing misunderstanding: clarify first](templates/clarify-first.md) |
| When requirements or document content get dropped | [Preventing omission: coverage check](templates/coverage-check.md) |
| When facts, numbers, or sources matter | [Preventing fabrication (hallucination): grounded answer](templates/grounded-answer.md) |
| When you need honest feedback | [Preventing sycophancy: honest critique](templates/honest-critique.md) |
| When you want to improve the prompt itself | [Meta-prompt](templates/meta-prompt.md) |
| When handing work to a coding agent | [Coding task instructions](templates/coding-task.md) · [AGENTS.md template](templates/AGENTS.template.md) |

---

## Table of contents

### 📘 Guides (docs)

| # | Guide | Key question |
|---|---|---|
| 01 | [Mindset](docs/01-mindset.md) | How should you think of AI? When should you not use it? |
| 02 | [The six elements of a prompt](docs/02-prompt-anatomy.md) | How do you write Role · Context · Instruction · Format · Constraints · Examples? |
| 03 | [Instructing with examples](docs/03-examples-few-shot.md) | How many examples, and how do you choose them? |
| 04 | [Misunderstanding · Omission · Fabrication](docs/04-failure-modes.md) | Why does AI get things wrong, how do you prevent it, and how do you catch it? |
| 05 | [Models and reasoning](docs/05-models-and-reasoning.md) | Which models and tools should you use? How do you handle reasoning models differently? |
| 06 | [Workflows](docs/06-workflows.md) | Context engineering, five patterns, playbooks by task |
| 07 | [AI coding](docs/07-ai-coding.md) | From vibe coding to agentic engineering |
| 08 | [Verification and evaluation](docs/08-verification-and-evals.md) | How do you verify a single answer, and how do you evaluate a prompt? |
| 09 | [Security and privacy](docs/09-security-privacy.md) | What should you never put in? What about prompt injection? |
| 10 | [Myths vs. evidence](docs/10-myths-vs-evidence.md) | Do "I'll tip you," "act like an expert," and "think step by step" really work? |

### 🧪 Examples: how a bad prompt becomes a good one

| # | Example | What you learn |
|---|---|---|
| 1 | [Work email: adding one element at a time](examples/01-email-step-by-step.md) | How the six elements change the result |
| 2 | [Summarizing a long document](examples/02-document-summary.md) | Preventing omission and fabrication at the same time |
| 3 | [Research](examples/03-research-with-sources.md) | Filtering out fake sources |
| 4 | [Data analysis](examples/04-data-analysis.md) | Calculations in code, assumptions out in the open |
| 5 | [Fixing a bug with a coding agent](examples/05-coding-agent.md) | Explore → plan → test → implement → verify |
| 6 | [Learning with AI](examples/06-learning-with-ai.md) | How to gain understanding, not just answers |
| 7 | [Designing your own agent](examples/07-build-your-own-agent.md) | Task analysis → instructions → evaluation set → security |

### 📚 Resources

- [Curated resource list (Awesome List)](resources/awesome.md): official guides, **Karpathy**'s videos, posts, and repos, materials from **MIT · Harvard · Wharton · Stanford**, and popular GitHub repositories (star counts and status checked)

### 🔬 Evidence (research)

- [Evidence report](research/evidence-report.md): the research report behind every recommendation in this repo. 288 sources, with a table of verification status for each claim
- 🆕 [2026 update report](research/2026-update-report.md): what changed in 2026 (especially May–November), corrections, and measurements on the newest models

---

## Learning paths

| Time | For | Order |
|---|---|---|
| **30 minutes** | Beginners | [Cheatsheet](CHEATSHEET.md) → [02. The six elements](docs/02-prompt-anatomy.md) → [Example 1](examples/01-email-step-by-step.md) → [Universal template](templates/universal-prompt.md) |
| **2 hours** | People who want to use AI seriously at work | All of the above + [01. Mindset](docs/01-mindset.md) → [04. Misunderstanding · Omission · Fabrication](docs/04-failure-modes.md) → [08. Verification](docs/08-verification-and-evals.md) → [10. Myths vs. evidence](docs/10-myths-vs-evidence.md) → Examples 2–4 |
| **1 day** | Developers and people building agents | All of the above + [05](docs/05-models-and-reasoning.md) → [06](docs/06-workflows.md) → [07](docs/07-ai-coding.md) → [09](docs/09-security-privacy.md) → Examples 5 and 7 → [Karpathy "How I use LLMs"](https://www.youtube.com/watch?v=EWvNQjAaOHw) |

---

## What makes this repo different

1. **Evidence-based.** Every recommendation has a source. Lab guides were checked directly on 2026-11-09, and papers were checked for bibliographic details and abstracts.
2. **It filters out myths.** Tricks that controlled studies, such as Wharton's repeated experiments, found to be ineffective (tips, threats, expert roles, "think step by step" for reasoning models) are collected separately. → [10](docs/10-myths-vs-evidence.md)
3. **Up to date.** Outdated habits that 2026 lab guides now say to drop (ALL-CAPS emphasis, excessive verification instructions, prefilling, and so on) are flagged.
4. **Honest.** Figures confirmed only through secondary sources, things we could not verify, and disputed studies are labeled as such. → [Evidence report §8](research/evidence-report.md#8-what-is-verified-and-what-is-not)
5. **Ready to use.** Every concept comes with copy-paste prompts and before/after examples.

> ⚠️ **About the terms:** "Role · Context · Instruction · Format · Constraints · Examples" combines elements common to guides from several organizations, and "Misunderstanding · Omission · Fabrication" is this repo's own teaching taxonomy. The causes of and remedies for each failure mode are all linked to research evidence.

### Myths vs. evidence (highlights)

| Popular tip | Verdict | Evidence |
|---|---|---|
| "I'll tip you" / threats | No effect | Wharton Report 3 (2025) |
| Being polite (or bossy) | No overall difference | Wharton Report 1 (2025) |
| "You are the world's best expert" | No accuracy gain, sometimes worse | Wharton Report 4 (2025), Zheng et al. (2024) |
| "Think step by step" on reasoning models | Almost no effect, only more time | Wharton Report 2 (2025), OpenAI, Microsoft |
| ALL CAPS, "NEVER!!!", "IMPORTANT" emphasis | Newest models overreact | Anthropic, OpenAI |
| Specifying output format is trivial | **Wrong: format instructions affect performance** | Wharton Report 1 (2025) |
| "Are you really sure?" as a check | Flips correct answers | FlipFlop (2023), SPINE (2026) |

Full table and details: [10. Myths vs. evidence](docs/10-myths-vs-evidence.md)

---

## Key sources

| Category | Representative sources |
|---|---|
| Official lab guides | [Anthropic](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) · [OpenAI](https://developers.openai.com/api/docs/guides/prompt-engineering) · [Google](https://aistudio.google.com/docs/prompting-strategies) · [Microsoft](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/prompt-engineering) · [Claude Code](https://code.claude.com/docs/en/best-practices) · [Codex](https://learn.chatgpt.com/guides/best-practices) |
| Andrej Karpathy | [How I use LLMs](https://www.youtube.com/watch?v=EWvNQjAaOHw) · [Deep Dive into LLMs](https://www.youtube.com/watch?v=7xTGNNLPyMI) · [Sequoia Ascent 2026](https://karpathy.bearblog.dev/sequoia-ascent-2026/) · [nanochat](https://github.com/karpathy/nanochat) · [llm-council](https://github.com/karpathy/llm-council) |
| Universities and research | [MIT Sloan](https://mitsloanedtech.mit.edu/ai/basics/effective-prompts/) · [Wharton Prompting Science Reports](https://arxiv.org/abs/2503.04818) · [Harvard/BCG Jagged Frontier](https://www.oneusefulthing.org/p/centaurs-and-cyborgs-on-the-jagged) · [Stanford legal AI hallucinations](https://hai.stanford.edu/news/ai-trial-legal-models-hallucinate-1-out-6-or-more-benchmarking-queries) · [The Prompt Report](https://arxiv.org/abs/2406.06608) |
| Research on failures | [Lost in the Middle](https://arxiv.org/abs/2307.03172) · [Why LMs Hallucinate](https://arxiv.org/abs/2509.04664) · [LLMs Get Lost in Multi-Turn](https://arxiv.org/abs/2505.06120) · [Sycophancy](https://arxiv.org/abs/2310.13548) · [Chain-of-Verification](https://arxiv.org/abs/2309.11495) |
| GitHub | [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide) · [anthropics/prompt-eng-interactive-tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) · [openai/openai-cookbook](https://github.com/openai/openai-cookbook) · [github/spec-kit](https://github.com/github/spec-kit) · [agents.md](https://agents.md/) |

Full list: [resources/awesome.md](resources/awesome.md) · All 288 sources: [research/evidence-report.md](research/evidence-report.md#references)

---

## Repository structure

```
how-to-use-ai/
├── README.md                 ← the document you are reading
├── CHEATSHEET.md             ← one-page summary
├── CHANGELOG.md              ← change history
├── docs/                     ← 10 guides
├── templates/                ← 8 copy-paste prompt templates
├── examples/                 ← 7 before/after examples
├── resources/                ← curated resource list
└── research/                 ← evidence report + 2026 update report
```

---

## Update policy

AI tools and official guides change every few months. This repo states its **research date (currently 2026-11-09)**, records changes in the [CHANGELOG](CHANGELOG.md), and flags or fixes advice that has gone stale as model generations change. Fast-changing information such as model names is described in general terms (standard models / reasoning models) wherever possible.

Found an error or broken link? Open an issue: https://github.com/ji-hun-git/how-to-use-ai/issues

## License

[MIT](LICENSE). Rights to external material quoted or summarized in each document remain with the original authors.
