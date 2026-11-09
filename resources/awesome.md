# Curated resources (awesome list)

> Official lab guides, Andrej Karpathy, universities and research institutions, and popular GitHub repositories: **only resources we checked directly**.
> GitHub star counts and status were checked with the GitHub API on **2026-11-09**. Star counts show popularity, not quality.

**Legend:** 🟢 Actively maintained, 🟡 Complete or rarely updated, 🔴 Archived or deprecated, ⚠️ Read with caution

---

## 1. Official lab guides (read these first)

| Organization | Resource | One-line summary |
|---|---|---|
| Anthropic | [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) | Be clear, give reasons, use 3–5 examples, put long material at the top. Includes a list of "habits to drop" for the newest models |
| Anthropic | [Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview) | Before refining prompts, start with success criteria and tests |
| Anthropic | [Reduce hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations) | The right to say "I don't know," quote first, retract what can't be quoted |
| Anthropic | [Effective context engineering for AI agents](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents) (2025-09) | Context is a limited attention budget. Use the smallest set of high-signal information |
| Anthropic | [Building effective agents](https://www.anthropic.com/research/building-effective-agents) (2024-12) | Five workflow patterns. Start with the simplest |
| Anthropic | [Claude Code best practices](https://code.claude.com/docs/en/best-practices) | Four causes of failure, asking vs. enforcing, "things you no longer need to do" |
| Anthropic | [Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents) (2026-01) | Start with 20–50 tasks drawn from real failures and grade the outcomes |
| OpenAI | [Prompt engineering guide](https://developers.openai.com/api/docs/guides/prompt-engineering) | Reasoning model = senior colleague, standard model = junior colleague |
| OpenAI | [Prompt guidance (latest models)](https://developers.openai.com/api/docs/guides/latest-model), [GPT-5.6 guide](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-5.6#prompting-best-practices) | Goals and success criteria, trimmed-down prompts, emphatic language only for true invariants |
| OpenAI | [Reasoning best practices](https://developers.openai.com/api/docs/guides/reasoning-best-practices) | Reasoning models don't need CoT instructions; try without examples first (based on the o-series) |
| OpenAI | [Codex best practices](https://learn.chatgpt.com/guides/best-practices) | Goal, context, constraints, done-criteria template, list of common mistakes |
| Google | [Prompt design strategies](https://aistudio.google.com/docs/prompting-strategies) | Examples in a consistent format, put material directly in the prompt, handling thinking models |
| Google | [Prompt Engineering whitepaper (Lee Boonstra, Kaggle)](https://www.kaggle.com/whitepaper-prompt-engineering) | Comprehensive overview of techniques. Some of its sampling-parameter advice is outdated for the newest models |
| Microsoft | [Prompt engineering techniques](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/prompt-engineering) | Techniques for standard models. Carries a banner advising against them for reasoning models |

> [!WARNING]
> OpenAI's [GPT-4.1](https://developers.openai.com/cookbook/examples/gpt4-1_prompting_guide) and [GPT-5](https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_prompting_guide) prompting guides are archived documents. The principles still hold, but the details reflect earlier model generations.

---

## 2. Andrej Karpathy

OpenAI co-founder and former Director of AI at Tesla. He popularized "vibe coding," "context engineering," and "agentic engineering," and is known for educational materials that teach LLMs by **building them from scratch**. He announced that he **joined Anthropic on May 19, 2026** to work on pretraining research (he said he would return to education when the time is right).

### Videos (in the order we most recommend for general users)

| Video | Date | What you'll learn |
|---|---|---|
| [How I use LLMs](https://www.youtube.com/watch?v=EWvNQjAaOHw) | 2025-02-27 | **Essential for general users.** Choosing a model, fresh chats, search and code tools, thinking models |
| [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI) | 2025-02-05 | How LLMs are built and why they hallucinate (3 hours 30 minutes) |
| [Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g) | 2023-11-22 | One-hour introduction |
| [Software Is Changing (Again)](https://www.youtube.com/watch?v=LCEmiRjPEtQ) (YC) | 2025-06-18 | Software 3.0, partial autonomy, the Iron Man suit |
| [Dwarkesh Podcast interview](https://www.youtube.com/watch?v=lXUZvyajciY) | 2025-10-17 | The limits of agents and "the decade of agents" |
| [Neural Networks: Zero to Hero](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ) | — | Build everything from neural networks to GPT yourself (for developers) |

### Writing

| Post | Date | Key points |
|---|---|---|
| [HackerTube](https://karpathy.bearblog.dev/hacker-tube/) | 2026-10-31 | Built a video site based on Hacker News comments with Claude Code in about 2 hours. The human handled only keys, servers, and the domain; the agent did the rest |
| [Post on the AI perception gap ("sharp funnel")](https://x.com/karpathy/status/2109361546505966046) | 2026-10-11 | Why people experience AI so differently: problem size, domain (verifiability), and tool tier |
| [Agentic engineering post](https://x.com/karpathy/status/2019137879310836075) | 2026-02-04 | A look back at one year of vibe coding. Proposes calling supervised, professional agent-driven development "agentic engineering" |
| [Sequoia Ascent 2026 summary](https://karpathy.bearblog.dev/sequoia-ascent-2026/) | 2026-04-30 | **His most recent practical advice.** Delegate to agents in large chunks, but specification, verification, and understanding stay with the human. "LLMs automate what is verifiable" |
| [2025 LLM Year in Review](https://karpathy.bearblog.dev/year-in-review-2025/) | 2025-12-19 | Jagged intelligence, a review of the year |
| [Vibe coding MenuGen](https://karpathy.bearblog.dev/vibe-coding-menugen/) | 2025-04-27 | Vibe coding in practice. The hard parts were deployment, authentication, and payments |
| [Vibe coding post](https://x.com/karpathy/status/1886192184808149383) | 2025-02-02 | Origin of the term |
| [Context engineering post](https://x.com/karpathy/status/1937902205765607626) | 2025-06-25 | Popularized the term |
| [llm-wiki (gist)](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) | 2026-04 | A pattern in which AI continuously maintains a Markdown knowledge base |

### Repositories

| Repository | ⭐ | Status | Notes |
|---|---|---|---|
| [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | 99,571 | 🟢 | The human edits only `program.md` (the instructions) and the agent runs the experiments. A real-world example of context engineering |
| [karpathy/nanochat](https://github.com/karpathy/nanochat) | 60,370 | 🟢 | "The best ChatGPT that $100 can buy." Successor to nanoGPT |
| [karpathy/llm-council](https://github.com/karpathy/llm-council) | 26,338 | 🟡 | Several models answer and rate each other → a chair model synthesizes the result |
| [karpathy/nn-zero-to-hero](https://github.com/karpathy/nn-zero-to-hero) | 25,383 | 🟡 | Course code (complete) |
| [karpathy/micrograd](https://github.com/karpathy/micrograd) | 18,764 | 🟡 | Backpropagation in 100 lines |
| [karpathy/minbpe](https://github.com/karpathy/minbpe) | 11,021 | 🟡 | Understanding tokenization (why LLMs struggle to count letters) |
| [karpathy/nanoGPT](https://github.com/karpathy/nanoGPT) | 64,550 | 🔴 | README says it is "old and deprecated" → use nanochat |
| [karpathy/llm.c](https://github.com/karpathy/llm.c) | 31,408 | 🟡 | No updates since mid-2025 |
| [karpathy/LLM101n](https://github.com/karpathy/LLM101n) | 37,479 | 🔴 | Archived. **The course does not exist yet** (stated in the README) |

---

## 3. Universities and research institutions

| Institution | Resource | Key points |
|---|---|---|
| **MIT** Sloan | [Effective Prompts for AI: The Essentials](https://mitsloanedtech.mit.edu/ai/basics/effective-prompts/) | Task, context, specificity, examples and constraints; a fresh chat for a new topic; "define the problem before writing the prompt" |
| **MIT** Sloan | [Addressing AI Hallucinations and Bias](https://mitsloanedtech.mit.edu/ai/basics/addressing-ai-hallucinations-and-bias/) | Checking citations is non-negotiable |
| **MIT** | [6.S191 Introduction to Deep Learning](https://introtodeeplearning.com/) | Free introductory deep learning course (slides, labs, videos) |
| **MIT** Media Lab | [Your Brain on ChatGPT](https://arxiv.org/abs/2506.08872) (preprint), [Rebuttal](https://arxiv.org/abs/2601.00856) | Essays written with LLMs showed lower recall and sense of ownership. A disputed early signal |
| **MIT** NANDA | [The GenAI Divide 2025](https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf) (preliminary report) | Corporate AI failures stem from missing context and learning. Shadow AI |
| **Wharton** GAIL | Prompting Science Reports [1](https://arxiv.org/abs/2503.04818), [2](https://arxiv.org/abs/2506.07142), [3](https://arxiv.org/abs/2508.00614), [4](https://gail.wharton.upenn.edu/research-and-insights/playing-pretend-expert-personas/) | **The truth about prompting tricks.** Tips, threats, politeness, and expert roles have no effect; CoT benefits are shrinking; format instructions do help |
| **Wharton** | [Bastani et al., PNAS 2025](https://knowledge.wharton.upenn.edu/article/without-guardrails-generative-ai-can-harm-education/) | AI that hands out answers hurts learning; a tutor-style AI that gives hints does not |
| **Wharton** | [Ethan Mollick, One Useful Thing](https://www.oneusefulthing.org/) | The most consistent blog on practical AI use for practitioners |
| **Harvard** / BCG | [Navigating the Jagged Technological Frontier](https://www.oneusefulthing.org/p/centaurs-and-cyborgs-on-the-jagged) | The jagged frontier, centaurs vs. cyborgs, falling asleep at the wheel |
| **Harvard** / P&G | [The Cybernetic Teammate](https://www.nber.org/papers/w33641) | An individual with AI ≈ a team without AI |
| **Harvard** CS50 | [CS50 AI policy](https://cs50.harvard.edu/x/honesty/), [Taming the Duck (2026)](https://news.harvard.edu/gazette/story/2026/09/taming-the-duck-for-starters/) | An AI tutor that guides instead of giving answers. "Prompting alone is not enough to enforce behavior" |
| **Stanford** | [Legal AI hallucination study](https://hai.stanford.edu/news/ai-trial-legal-models-hallucinate-1-out-6-or-more-benchmarking-queries) | Even specialized legal tools hallucinated 17–34% of the time (2024 tools; historical data) |
| **Stanford** HAI | [AI Index 2026: 12 takeaways](https://hai.stanford.edu/news/inside-the-ai-index-12-takeaways-from-the-2026-report) | Capabilities remain jagged |
| **Stanford** NLP | [DSPy](https://arxiv.org/abs/2310.03714), [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy) ⭐38,971 | "Programming, not prompting." Automatic prompt optimization |
| **Stanford** | [CS336 Language Modeling from Scratch](https://cs336.stanford.edu/) | LLMs from scratch (for developers) |
| **Stanford** HAI | [AI Index 2026, Responsible AI chapter](https://hai.stanford.edu/ai-index/2026-ai-index-report/responsible-ai) | Hallucination rates of 22–94% across 26 models; accuracy drops sharply when a claim is framed as "I believe" |
| **Stanford** | [Cheng et al., *Science* 2026](https://www.science.org/doi/10.1126/science.aec8352) | People trust and prefer sycophantic AI more |
| **Wharton** GAIL | [Prompting Science Report 5 (2026-04)](https://gail.wharton.upenn.edu/research-and-insights/hidden-prompt-injections/) | How hidden prompt injections affect AI grading |
| METR | [2026 productivity follow-up](https://metr.org/blog/2026-02-24-uplift-update/), [2026 self-reported usage survey](https://metr.org/blog/2026-05-11-ai-usage-survey/) | The 2025 "19% slower" result no longer represents the present. The new results rest on weak evidence |
| Independent evaluations | [Vectara hallucination leaderboard](https://github.com/vectara/hallucination-leaderboard), [Artificial Analysis AA-Omniscience](https://artificialanalysis.ai/evaluations/omniscience) | Live measurements that keep updating hallucination rates for the newest models |
| UMD et al. | [The Prompt Report](https://arxiv.org/abs/2406.06608) | A taxonomy of 58 text prompting techniques. The most comprehensive survey |
| CMU, Microsoft Research | [Lee et al., CHI 2025](https://advait.org/files/lee_2025_ai_critical_thinking_survey.pdf) | Higher trust in AI goes with less critical thinking (319 participants) |

---

## 4. GitHub repositories

### Getting started: learning to prompt

| Repository | ⭐ | Status | Notes |
|---|---|---|---|
| [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide) | 79,910 | 🟢 | The best-known reference for prompting techniques |
| [anthropics/prompt-eng-interactive-tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) | 39,148 | 🟢 | Anthropic's official hands-on tutorial (clarity, roles, XML, examples, avoiding hallucinations) |
| [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | 123,134 | 🟢 | A 21-lesson introductory generative AI curriculum |
| [f/prompts.chat](https://github.com/f/prompts.chat) (formerly awesome-chatgpt-prompts) | 176,491 | 🟢 | A collection of prompt ideas. Not for learning techniques |
| [NirDiamant/Prompt_Engineering](https://github.com/NirDiamant/Prompt_Engineering) | 7,927 | 🟢 | Notebook tutorials by technique |
| [Learn Prompting](https://learnprompting.org/) | — | 🟢 | Web course (the GitHub repository has stalled since 2025) |

### In practice: working and coding with AI

| Repository | ⭐ | Status | Notes |
|---|---|---|---|
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | 154,976 | 🟢 | Claude Code |
| [openai/codex](https://github.com/openai/codex) | 133,757 | 🟢 | OpenAI Codex CLI |
| [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | 108,781 | 🟢 | Gemini CLI (individual users moved to [Antigravity CLI](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/) starting 2026-06-18; still distributed for enterprise and API-key users) |
| [anthropics/skills](https://github.com/anthropics/skills) | 189,325 | 🟢 | Official agent skill examples |
| [agentsmd/agents.md](https://github.com/agentsmd/agents.md) | 25,395 | 🟢 | The AGENTS.md standard ([agents.md](https://agents.md/)) |
| [github/spec-kit](https://github.com/github/spec-kit) | 148,629 | 🟢 | Spec-driven development toolkit |
| [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | 74,272 | 🟢 | Lightweight spec-driven development |
| [obra/superpowers](https://github.com/obra/superpowers) | 314,454 | 🟢 | A skill collection that enforces a brainstorm → plan → TDD → review flow (⚠️ unusually high star count) |
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | 57,529 | 🟢 | Index of Claude Code community resources |
| [coleam00/context-engineering-intro](https://github.com/coleam00/context-engineering-intro) | 13,901 | 🟢 | Context engineering templates |
| [jasontang-ai/Context-Engineering](https://github.com/jasontang-ai/Context-Engineering) (formerly davidkimai) | 9,279 | 🟢 | Context engineering handbook |

### Repositories that took off in 2026 (checked directly, 2026-11-09)

In 2026, collections of agent **skills** and **harness engineering** resources exploded. Many are unverified personal setups even when they have huge star counts, so choose based on what each one actually is, as described below.

| Repository | ⭐ | Created | Notes |
|---|---|---|---|
| [agentskills/agentskills](https://github.com/agentskills/agentskills) | 27,068 | 2025-12 | Specification and docs for the Agent Skills open standard ([agentskills.io](https://agentskills.io)) |
| [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | 230,850 | 2026-01 | A single `CLAUDE.md` based on common coding-agent mistakes that Karpathy pointed out. ⚠️ **Not made by Karpathy himself** |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 114,055 | 2026-02 | A collection of practical engineering skills (Addy Osmani) |
| [mattpocock/skills](https://github.com/mattpocock/skills) | 318,346 | 2026-02 | A public version of the skills in his personal `.agents` folder |
| [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | 23,659 | 2026-03 | Introductory harness engineering tutorial |
| [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | 77,763 | 2026-03 | An AI engineering learning path |
| [ai-evals-course/evals-skills](https://github.com/ai-evals-course/evals-skills) | 1,720 | 2026-06 | Skills for building product-specific evals with a coding agent (tied to Hamel Husain's course) |

> [!WARNING]
> Repositories that **copy one person's entire setup**, such as [garrytan/gstack](https://github.com/garrytan/gstack) (⭐140,753) and [affaan-m/ECC](https://github.com/affaan-m/ECC) (⭐299,550), also became very popular. They are useful for reference, but skills and plugins are code too, so review the contents and take only what you need. → [09. Security](../docs/09-security-privacy.md)

### Builders: building AI apps and agents

| Repository | ⭐ | Status | Notes |
|---|---|---|---|
| [openai/openai-cookbook](https://github.com/openai/openai-cookbook) | 77,003 | 🟢 | OpenAI's official recipes |
| [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) (formerly anthropic-cookbook) | 54,429 | 🟢 | Anthropic's official recipes |
| [google-gemini/cookbook](https://github.com/google-gemini/cookbook) | 17,915 | 🟢 | Google's official recipes |
| [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | 79,192 | 🟢 | Introductory course on agents |
| [huggingface/agents-course](https://github.com/huggingface/agents-course) | 34,599 | 🟢 | Hugging Face's agents course |
| [humanlayer/12-factor-agents](https://github.com/humanlayer/12-factor-agents) | 27,044 | 🟡 | Design principles for production agents (no updates since 2025-09; the principles still hold) |
| [NirDiamant/RAG_Techniques](https://github.com/NirDiamant/RAG_Techniques) | 30,272 | 🟢 | A collection of RAG techniques |
| [NirDiamant/GenAI_Agents](https://github.com/NirDiamant/GenAI_Agents) | 24,875 | 🟢 | Agent implementation tutorials |
| [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | 26,958 | 🟢 | Prompt evaluation and red-teaming tool |
| [microsoft/mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners) | 17,625 | 🟢 | Introduction to MCP |

### Fundamentals: how LLMs work

| Repository | ⭐ | Status | Notes |
|---|---|---|---|
| [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) | 108,015 | 🟢 | Code for a book that implements an LLM from scratch |
| [mlabonne/llm-course](https://github.com/mlabonne/llm-course) | 84,950 | 🟡 | An LLM learning roadmap |
| [karpathy/nanochat](https://github.com/karpathy/nanochat) | 60,370 | 🟢 | The full pipeline for a small ChatGPT |

### Read with caution

| Repository | Why |
|---|---|
| [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) ⭐144,559 | A collection of **leaked** system prompts from various AI tools. Useful for learning structure, but the provenance is unclear and there may be copyright issues |
| [anthropics/courses](https://github.com/anthropics/courses) | 🔴 Archived |
| [brexhq/prompt-engineering](https://github.com/brexhq/prompt-engineering) | 🟡 No updates since 2023 (GPT-4-era content) |
| [microsoft/promptbase](https://github.com/microsoft/promptbase) | 🟡 No updates since 2024 |

---

## 5. Practitioners (worth reading regularly)

| Person | Resources | Why |
|---|---|---|
| Simon Willison | [Blog](https://simonwillison.net/tags/prompt-engineering/), [Agentic Engineering Patterns](https://simonwillison.net/guides/agentic-engineering-patterns/), [The lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/), [Vibe coding and agentic engineering are converging (2026-05)](https://simonwillison.net/2026/May/6/vibe-coding-and-agentic-engineering/), [Prompt injection case collection](https://simonwillison.net/tags/prompt-injection/) | The most accurate and consistent record of real-world LLM use and security |
| Hamel Husain & Shreya Shankar | [LLM Evals FAQ](https://hamel.dev/blog/posts/evals-faq/), [Critique of automated eval tools (2026-09)](https://hamel.dev/blog/posts/claude-auto-evals/) | The practical standard for evals. "Look at your data yourself first" |
| Ethan Mollick | [One Useful Thing](https://www.oneusefulthing.org/), [Which AI to use: summer 2026 guide](https://www.oneusefulthing.org/p/an-opinionated-guide-to-which-ai-b22) | Wharton professor. AI use from the perspective of everyday office work |
| Anthropic Engineering | [Components of agent memory (2026-11)](https://www.anthropic.com/research/components-of-agent-memory), [Harness design for long-running apps (2026-03)](https://www.anthropic.com/research/harness-design-long-running-apps) | Keep memory small; separate the side that generates from the side that evaluates |
| Birgitta Böckeler | [Understanding Spec-Driven Development](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html) | A sober assessment of spec-driven development |

---

> [!NOTE]
> For local laws and guidelines on AI and privacy (example: South Korea's AI Basic Act, the PIPC guide for users of generative AI services, and the public-sector AI adoption guide), see [09. Security and privacy §5](../docs/09-security-privacy.md#5-local-laws-and-guidelines-example-south-korea-2026).

> The full source list and the verification level of each resource are in the references of [research/evidence-report.md](../research/evidence-report.md) (base research) and [research/2026-update-report.md](../research/2026-update-report.md) (2026 update).
