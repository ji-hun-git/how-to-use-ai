# How this repo compares

> A fair look at the most popular repositories for learning and improving how people work with AI, as of **2026-11-09**. Star counts come from the GitHub API on that date. The ratings are our own assessment from reading each repository; they describe fit for purpose, not overall quality. Many of these projects are excellent, and several are listed in our [resources](resources/awesome.md).

**Legend:** ● strong, ◐ partial, ○ not a focus

| Repository | ⭐ | What you get | Evidence & sources | Up to date (2026) | Failure modes covered | Copy-paste prompts | Installable skills / rules | Runnable evals | Course structure | Non-coders |
|---|---|---|---|---|---|---|---|---|---|---|
| **how-to-use-ai** (this repo) | new | Guide + 10 skills + drop-in rules + prompt library + 73-method catalog graded for 2026 + eval demo | ● 460+ cited sources, verification status per claim | ● | ● misunderstanding, omission, fabrication, sycophancy | ● 30 prompts + 10 templates | ● 10 skills, Claude Code plugin, AGENTS.md / CLAUDE.md / Cursor / chat versions | ● with-vs-without skill evals with published results and raw answers | ◐ learning paths | ● |
| [mattpocock/skills](https://github.com/mattpocock/skills) | 318,372 | Engineering skills from one developer's setup | ◐ | ● | ● (for coding) | ◐ | ● | ○ | ○ | ◐ |
| [obra/superpowers](https://github.com/obra/superpowers) | 314,491 | Skills that enforce a brainstorm → plan → TDD → review workflow | ○ | ● | ◐ | ○ | ● | ◐ | ○ | ○ |
| [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | 230,864 | One CLAUDE.md based on Karpathy's observations of coding-agent mistakes (not made by Karpathy) | ◐ | ◐ | ● (for coding) | ● | ● | ○ | ○ | ○ |
| [anthropics/skills](https://github.com/anthropics/skills) | 189,417 | Official example skills and the skill format | ○ | ● | ○ | ○ | ● | ● | ○ | ◐ |
| [f/prompts.chat](https://github.com/f/prompts.chat) | 176,525 | Large community prompt collection | ○ | ● | ○ | ● | ◐ | ○ | ◐ | ● |
| [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | 123,143 | 21-lesson course on building generative AI apps | ◐ | ● | ◐ | ◐ | ○ | ● | ● | ○ |
| [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide) | 79,913 | Reference of prompting techniques and papers | ◐ | ◐ (last push 2026-03) | ◐ | ◐ | ○ | ◐ notebooks | ◐ | ◐ |
| [anthropics/prompt-eng-interactive-tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) | 39,151 | Interactive 9-chapter prompting tutorial | ◐ | ○ (uses older models) | ◐ | ◐ | ○ | ● | ● | ◐ |

## What this repo does differently

1. **Evidence first.** Every recommendation links to a source, old statistics are labeled as historical, and two research reports list what is verified and what isn't. No other repo in this table does this.
2. **Built around failure modes, not tricks.** The guide, the skills, the rules file and the prompt library all target the same four documented failure modes, including sycophancy, which coding-focused repos rarely address.
3. **Myth-busting.** It shows which popular tips don't hold up in controlled studies (tips and threats, expert personas, "think step by step" for reasoning models, ALL-CAPS emphasis).
4. **For everyone, not just developers.** Chat-app custom instructions, writing, research, analysis and learning examples sit alongside coding-agent skills.
5. **Read it or install it.** The same evidence is available as documentation, as skills, and as one drop-in rules file.

## When another repo is the better choice

- **You want a full engineering workflow for coding agents:** [obra/superpowers](https://github.com/obra/superpowers) or [mattpocock/skills](https://github.com/mattpocock/skills).
- **You want to build AI applications step by step:** [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners).
- **You want an exhaustive catalog of prompting techniques and papers:** [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide).
- **You want hands-on exercises in a notebook:** [anthropics/prompt-eng-interactive-tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial).
- **You want thousands of prompt ideas:** [f/prompts.chat](https://github.com/f/prompts.chat).
- **You want to learn the official skill format from its source:** [anthropics/skills](https://github.com/anthropics/skills).

## What we're still missing (honest gaps)

- **Broader measurements.** [Skill evals](evals/results/README.md) are published for two Claude models; other vendors' models, longer real-world tasks and skill *selection* (triggering) aren't tested yet.
- **Interactive exercises.** There are no notebooks or graded exercises.
- **Visual assets.** Diagrams are Mermaid only; there's no illustrated course.
