# how-to-use-ai

A Korean guide to prompting, workflows, and checking AI output.

[한국어](README.md) · [Cheatsheet (KO)](CHEATSHEET.md) · [Evidence report (KO)](research/evidence-report.md)

> The main content of this repository is in **Korean**. This page summarizes it in English.

It draws on official documentation from Anthropic, OpenAI, Google and Microsoft, published research, and practitioners such as Andrej Karpathy and Simon Willison. Sources are listed at the end of each page; figures confirmed only through secondary sources, and disputed studies, are flagged in the evidence report. Most study results reflect the models tested at the time and may not carry over at the same size to current models. Research date: 2026-11-09.

---

## The 30-second version

> **The unit of good AI use is not a clever sentence. It is a good specification plus good verification.**

### 1. Instruct with six elements

| Role | Context | Instruction | Format | Constraints | Examples |
|---|---|---|---|---|---|
| perspective & tone | why, for whom, in what situation | what to do, what "done" means | structure & length | must-follow rules | 3–5 diverse samples |

Spend your effort on context, instruction, and format. Controlled studies (Wharton Prompting Science Report 4; Zheng et al., EMNLP 2024) found that expert personas do **not** reliably improve factual accuracy.

### 2. Diagnose failures with three categories

| Misunderstanding (오해) | Omission (누락) | Fabrication / hallucination (지어냄) |
|---|---|---|
| The model read the request differently | Requirements or mid-document content were dropped | The model invented facts, numbers, or citations |
| Give goal, audience and done-criteria; let it ask ≤3 questions; if a chat derails, consolidate and **start a fresh chat** (multi-turn underspecification costs ~39%, Laban et al. 2025) | Number requirements and ask for a **coverage table**; put long documents first and the question last; split large jobs | **Allow "I don't know"**; ground in supplied documents; quote first, then answer; retract unsupported claims; **open every citation yourself** |

Plus **sycophancy**: in a 2023 study of ten models, asking "Are you sure?" made models change their answer 46% of the time, and accuracy fell by about 17 percentage points on average (FlipFlop). Ask for an independent re-solve in a fresh chat instead.

### 3. Work in a loop

```
Specify → Plan → Execute → Verify → Learn
```

---

## What's inside

| Folder | Contents |
|---|---|
| [`docs/`](docs/) | 10 guides: mindset, the six elements, few-shot examples, the three failure modes, models & reasoning, workflows & context engineering, AI coding (vibe coding → agentic engineering), verification & evals, security & privacy, myths vs. evidence |
| [`templates/`](templates/) | 8 copy-paste Korean prompt templates (universal prompt, clarify-first, coverage check, grounded answer, honest critique, meta-prompt, coding task, AGENTS.md) |
| [`examples/`](examples/) | 7 before/after walkthroughs (email, long-document summary, research with sources, data analysis, coding agent, learning with AI, designing your own agent) |
| [`resources/`](resources/) | A curated resource list (official guides, Karpathy's talks/posts/repos, university resources, GitHub repos with star counts as of 2026-11-09) |
| [`research/`](research/) | The full evidence report (288 sources, with a verification-status table) |

---

## Myths vs. evidence (highlights)

| Popular tip | Verdict | Evidence |
|---|---|---|
| "I'll tip you $1,000" / threats | No reliable effect | Wharton Prompting Science Report 3 (2025) |
| Being polite (or rude) | No reliable aggregate effect | Wharton Report 1 (2025) |
| "You are a world-class expert" | No accuracy gain; sometimes worse | Wharton Report 4 (2025); Zheng et al. (2024) |
| "Think step by step" on reasoning models | Negligible gain, 20–80% slower | Wharton Report 2 (2025); OpenAI; Microsoft |
| ALL-CAPS / "NEVER!!!" emphasis | Can cause over-triggering in recent models | Anthropic prompting best practices |
| Specifying output format is cosmetic | Wrong: removing it hurt accuracy (GPT-4o era) | Wharton Report 1 (2025) |
| "Are you sure?" as a check | Destabilizes answers (2023 models) | FlipFlop (2023) |

---

## Key sources

- **Labs:** [Anthropic prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) · [Anthropic context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) · [OpenAI prompt engineering](https://developers.openai.com/api/docs/guides/prompt-engineering) · [Google prompt design strategies](https://aistudio.google.com/docs/prompting-strategies) · [Claude Code best practices](https://code.claude.com/docs/en/best-practices) · [Codex best practices](https://learn.chatgpt.com/guides/best-practices)
- **Karpathy:** [How I use LLMs](https://www.youtube.com/watch?v=EWvNQjAaOHw) · [Deep Dive into LLMs](https://www.youtube.com/watch?v=7xTGNNLPyMI) · [Sequoia Ascent 2026 summary](https://karpathy.bearblog.dev/sequoia-ascent-2026/)
- **Research:** [Wharton Prompting Science Reports](https://arxiv.org/abs/2503.04818) · [Jagged Technological Frontier](https://www.oneusefulthing.org/p/centaurs-and-cyborgs-on-the-jagged) · [Lost in the Middle](https://arxiv.org/abs/2307.03172) · [Why Language Models Hallucinate](https://arxiv.org/abs/2509.04664) · [The Prompt Report](https://arxiv.org/abs/2406.06608)

---

## Contributing

Corrections and broken-link reports are welcome via [issues](https://github.com/ji-hun-git/how-to-use-ai/issues).

## License

[MIT](LICENSE). Rights to quoted or summarized external material remain with their original authors.
