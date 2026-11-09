# 06. Workflows: from a single prompt to a way of working

> Few tasks end with one good prompt. Real work has **multiple steps**, and a person needs to check each one.
> This document covers (1) **context engineering**, deciding what the AI gets to see; (2) **five patterns** for breaking work down; (3) a **basic loop** that works for any task; and (4) **playbooks** for specific tasks.

---

## 1. Context engineering

### From prompt engineering to context engineering

The term spread widely in June 2025, after Shopify CEO Tobi Lütke and Andrej Karpathy promoted it in quick succession. Karpathy described it as **the delicate art of filling the context window with just the right information for the next step**.

- **Prompt engineering:** how to **write** the instructions
- **Context engineering:** what the AI **gets to see** each time (instructions, materials, conversation history, memory files, tool results: all of it)

In a September 2025 post, Anthropic compared the context window to a **limited attention budget**. As context piles up, **context rot** sets in: the model can no longer accurately recall earlier information. So the goal is **the smallest amount of high-signal information that gives the best chance of the desired outcome**.

### Six principles for everyday use

| Principle | In a regular chat | In a coding agent |
|---|---|---|
| **New topic, fresh start** | New chat | `/clear` or a new session |
| **Only the materials you need, when you need them** | Attach only relevant documents. Don't add everything | Don't paste whole files; let the agent read them when it needs to |
| **Put long-lived information in files** | Instructions in the Projects feature, custom GPT settings | `AGENTS.md` / `CLAUDE.md` (keep it short!) |
| **Hand off long tasks with notes** | "Summarize what we've decided so far" → paste into a new chat | Record in a progress file (progress.md), compaction |
| **Turn procedures into reusable units** | Saved prompt templates | Skills |
| **Enforce must-follow rules with settings, not text** | Use only company-approved tools | Hooks, permission deny rules, CI |

> 💡 In 2026, context windows have grown to 1 million tokens and automatic compaction exists, so running **out** of context is rare. Still, the shared recommendation is that **keeping context narrow gives better answers at lower cost**. A 2026 study found that top models located a single sentence within 1 million tokens 100% of the time, but on **tasks that require reasoning across multiple pieces of information**, performance dropped as length increased. → [04 🆕 table](04-failure-modes.md#-2026-update-how-current-models-fare)

### 🆕 Managing memory (Anthropic, 2026-11)

As **memory features** in AI services and agents have become common, Anthropic set out design principles for agent memory in November 2026. They apply just as well to everyday users.

| Principle | What it means for users |
|---|---|
| **Keep always-loaded context small** | The longer instruction files and memory get, the less reliably instructions are followed → keep project instructions, `AGENTS.md`, and memory short |
| **Store only what the environment can't tell you** | Don't store things that can be found again in the code or documents |
| **Say what the memory is for, not how to do it** | "Remember this project's decisions and the reasons behind them" |
| **A short index file** | Split long memory into files by topic, with a short list at the top |

In the same post, using a wiki (organized knowledge documents) together with search produced higher accuracy than search alone (61% vs 53%). This points in the same direction as Karpathy's [llm-wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) pattern.

---

## 2. Five patterns for breaking work down

Anthropic's "Building effective agents" (2024-12) presents five basic patterns for structuring AI work. It was written for developers, but you can use the patterns **as-is in a chat window**. The most important principle: **start with the simplest approach, and add complexity only when it is shown to help**.

| Pattern | What it is | How to do it in a chat | Where a person checks |
|---|---|---|---|
| **Prompt chaining** | Split the work into sequential steps and handle each one | ① Outline → check → ② draft → ③ critique against a rubric → ④ revise | Review the result at each step before moving on |
| **Routing** | Send each kind of task to a different tool or model | Simple questions to a fast model, hard analysis to a reasoning model, research to deep research | I choose the mode |
| **Parallelization** | ⓐ Independent parts at the same time ⓑ the same task several times | ⓐ A separate chat for each chapter of a report ⓑ the same question 2–3 times / to several models | Merging, checking where they differ |
| **Orchestrator-workers** | A lead splits the work, workers do it, the lead combines it | Deep research features, subagents in coding agents | Verifying the final result |
| **Evaluator-optimizer** | One generates, another evaluates, and they repeat | Write in chat A, evaluate against a rubric in a new chat B | I write the rubric |

> 📌 Anthropic's 2026 documentation says current models handle most multi-step reasoning **internally**. Chaining is still useful **when you want to see intermediate results yourself**. The most common chain is **draft → review against criteria → revise**.

> 📌 Multi-agent setups are expensive. In Anthropic's research-system case, the multi-agent system used about **15 times** as many tokens as a regular chat. It pays off for large research tasks that split into independent parts, but fits poorly with work that needs shared context (most coding).

---

## 3. A basic loop for any task

The 2026 official guides (Anthropic, OpenAI) and practitioners (Karpathy, Simon Willison) end up converging on the same loop.

```
① Specify   Write the goal, context, constraints, and done criteria. If you're stuck, have the AI interview you
      ↓
② Plan      For multi-step work, get a plan and approve it before execution
      ↓
③ Execute   Give the AI criteria it can check on its own (tests, checklists, source text)
      ↓
④ Verify    Check the result against evidence. If possible, have a new chat or another person/model look at it
      ↓
⑤ Learn     For recurring mistakes, add a line to a template, memory file, or checklist
```

| Step | What happens if you skip it |
|---|---|
| ① Specify | **Misunderstanding**. The AI fills the gaps with guesses |
| ② Plan | You discover the overall direction was wrong only after everything is built |
| ③ Check criteria | The AI says "Done," but there are actually **omissions** |
| ④ Verify | **Fabrications** go out the door as-is |
| ⑤ Learn | The same mistake repeats every time |

---

## 4. Playbooks by task

### 4-1. Writing (reports, proposals, blog posts)

```
1. [Me]   Write the core argument in 3 lines myself first (don't outsource the thinking)
2. [AI]   Give it the audience and purpose, get an outline → I edit it
3. [AI]   Draft section by section from the outline (for long pieces, one section at a time)
4. [AI*]  Critique against a rubric in a new chat (*separate from the chat that wrote it)
5. [AI]   Revise based on the critique
6. [Me]   Check facts, numbers, and quotes; polish it into my own voice
```

### 4-2. Research

```
1. Define the question and the source criteria (primary sources first, time period, region)
2. Gather material with search or deep research
3. Require a source for every claim; mark anything unverified as [unverified]
4. Open the original source to check key claims yourself (lateral reading)
5. Check for one-sidedness with "Find only the counter-evidence"
```
→ [Example 3](../examples/03-research-with-sources.md)

### 4-3. Data analysis

```
1. Start by checking the data (missing values, duplicates, units) → I decide how to handle them
2. I write the metric definitions
3. Do calculations by running code, and show the code
4. Recalculate 1–2 numbers myself
5. In the interpretation, separate "what the data shows" from "speculation"
```
→ [Example 4](../examples/04-data-analysis.md)

### 4-4. Long-document summaries and meeting notes

```
1. Document at the top, question at the bottom
2. Have it extract the relevant sentences verbatim first
3. Summarize based only on those quotes; delete unsupported claims
4. Keep a separate "Not confirmed in the document" section
```
→ [Example 2](../examples/02-document-summary.md)

---

## 5. Meta-prompting and reuse

### Have the AI write the prompt

- **Get interviewed:** "Ask me about any missing information, one question at a time, and complete the prompt."
- **Get improvements:** "Predict the misunderstandings, omissions, and fabrications this prompt could cause, and fix it."
- **Minimal edits:** When revising a prompt you already use, OpenAI recommends asking the model what **minimal edits** would elicit the behavior you want.

→ Template: [templates/meta-prompt.md](../templates/meta-prompt.md)

### Save prompts that work

A prompt that worked once is worth using again. Many services offer ways to save them.

| Feature | What it is |
|---|---|
| Projects | Bundle instructions and materials, then chat inside that space |
| Custom GPTs / Gems | Your own chatbot with built-in instructions (Google is migrating Gems to skills) |
| Skills | A folder that bundles instructions + scripts + materials. The AI loads it when needed |
| Project memory files | `AGENTS.md` / `CLAUDE.md`, which a coding agent reads every time |

> **Re-test** saved prompts whenever the model changes.

---

## 6. Long tasks: work that spans multiple sessions

A large task that takes more than a day can't be finished in one conversation. Anthropic's long-running agent case (2025-11) works like this:

1. **First session:** Create a full task list (checklist) and a progress file.
2. **Every later session:** Read the progress file → handle **only one item** → verify it → leave a record.
3. Use **version control (git)** so you can roll back at any time.

You can do the same in chat. When a conversation gets long, ask "Summarize what we've decided so far, what's left, and what to watch out for," then paste the result into a new chat.

🆕 Anthropic's March 2026 post (harness design for long-running apps) adds two more points.
- **Separate the generator from the evaluator.** Agents show a clear tendency to **lean favorable** when evaluating their own work. In chat, evaluate in a different chat from the one that did the writing.
- **Turn subjective quality into explicit criteria.** Instead of "good design," give a list of evaluation criteria. The post also recommends re-checking this setup when the model changes.

---

### Sources

- Karpathy, "context engineering" post (2025-06-25) — https://x.com/karpathy/status/1937902205765607626
- Tobi Lütke, "context engineering" post (2025-06) — https://twitter.com/tobi/status/1935533422589399127
- Simon Willison, "Context engineering" (2025-06-27) — https://simonwillison.net/2025/Jun/27/context-engineering/
- Anthropic, Effective context engineering for AI agents (2025-09-29) — https://www.anthropic.com/research/effective-context-engineering-for-ai-agents
- Anthropic, Building effective agents (2024-12-19) — https://www.anthropic.com/research/building-effective-agents
- Anthropic, How we built our multi-agent research system (2025-06-13) — https://www.anthropic.com/research/multi-agent-research-system
- Anthropic, Effective harnesses for long-running agents (2025-11-26) — https://www.anthropic.com/research/effective-harnesses-for-long-running-agents
- Anthropic, Equipping agents for the real world with Agent Skills — https://www.anthropic.com/research/equipping-agents-for-the-real-world-with-agent-skills
- Anthropic, Prompting best practices (chaining, subagents) — https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- Claude Code, Best practices — https://code.claude.com/docs/en/best-practices
- OpenAI Cookbook, GPT-5 prompting guide (meta-prompting; archived document) — https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_prompting_guide
- Chroma, Context Rot (2025) — https://research.trychroma.com/context-rot

**2026 update (checked 2026-11-09)**
- Anthropic, The components of agent memory (2026-11-06) — https://www.anthropic.com/research/components-of-agent-memory
- Anthropic, Harness design for long-running application development (2026-03-24) — https://www.anthropic.com/research/harness-design-long-running-apps
- Chow, Retrieval and multi-step reasoning in 1-million-token contexts (2026-05, preprint) — https://arxiv.org/abs/2605.02173
- Ethan Mollick, "An Opinionated Guide to Which AI to Use" (2026-07-23) — https://www.oneusefulthing.org/p/an-opinionated-guide-to-which-ai-b22
- Model Context Protocol, specification changelog (revised 2026-07-28) — https://modelcontextprotocol.io/specification/latest/changelog
