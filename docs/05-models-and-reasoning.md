# 05. Choosing models and working with reasoning (thinking) models

> Just as important as the prompt is **which model and which tools** you use to ask.
> And as reasoning models went mainstream in 2025–2026, many old prompting tricks became **unnecessary or even harmful.**

---

## 1. Karpathy's everyday principles

Here are the habits Andrej Karpathy recommended in his "How I use LLMs" (2025) talk and in later posts.

| Principle | Why |
|---|---|
| **Check which model you're actually using** | Even within the same service, the model differs by free/paid tier and by mode, and so does performance, by a lot |
| **Choose models by comparison, not marketing** | Judge by leaderboards and direct comparison. Asking several models the same question is another option |
| **New topic, new chat** | The context window is working memory. Unrelated content piles up, gets in the way, and slows things down |
| **Supply the material yourself** | Don't rely on the model's memory; paste in the documents (context engineering) |
| **Use reasoning models for hard problems** | Math, code, complex analysis. A fast model is enough for easy questions |
| **Search for facts, code for calculations** | Search tools for current information, code execution for numbers |
| **Verify what matters** | Models make mistakes a person wouldn't |

---

## 🆕 Snapshot: major models as of November 2026

> Models change every few months. The table below reflects each company's official documentation as of **2026-11-09**. The rest of this repo is written so that it doesn't depend on specific model names.

| Company | Major models | Notes |
|---|---|---|
| Anthropic | **Claude Fable 5.1** (most capable generally available model, 2026-09-01), **Opus 5.5** (2026-09-22, recommended as the first choice for most tasks), Sonnet 5.5 (2026-09-28), Haiku 5.5 (2026-10-07) | All have a 1M-token context. Fable 5.x and Opus 5.5 have adaptive thinking always on |
| OpenAI | **GPT-6 Astra** (recommended flagship, 2026-09-03), GPT-6.1 Sol, GPT-6.1 Terra (2026-10-26), GPT-6 Luna | All have a context of about 1.05M tokens |
| Google | **Gemini 4 Argon** (flagship reasoning model, launched in the Gemini app on 2026-10-13), Gemini 3.8 Flash, Gemini 3.6 Flash | Requests to Gemini 2.5 Flash and Pro switch automatically to newer models starting 2026-12-01 |

**Features that became important for everyday users in 2026**
- **Memory and personalization:** Claude (memory overhaul, 2026-07 to 2026-08), Gemini (personalization across 40-some connected apps, 2026-10), Codex (memory on by default, 2026-10), and others have strengthened features that remember your conversations and work. They're convenient, but check periodically what has been saved. → [09. Security](09-security-privacy.md)
- **Skills:** The open standard that Anthropic started (Agent Skills) has spread to many tools. Google announced that Gems in the Gemini app will be replaced by, and migrated to, skills (2026-09).
- **Scheduled runs and always-on agents:** Many services now offer agents that run tasks at set times or keep working even when your computer is off. Schedule only tasks that already run reliably when you do them by hand.
- **Connecting external apps:** Connections to dozens of apps, such as email, drive, and calendar, are now standard. Keep [the lethal trifecta](09-security-privacy.md#3-the-lethal-trifecta-and-the-rule-of-two) in mind.

---

## 2. Choosing tools by task

| Task | Recommended setting | Why |
|---|---|---|
| Ideas, drafts, translation, polishing tone | Fast model | There's no single right answer, and you can check the result right away |
| Latest news, statistics, product information | **Turn on search** | A model's training data has a cutoff date |
| Calculations, table analysis, charts | **Turn on code execution** | Language models are weak at mental arithmetic |
| Math, logic, complex coding, strategic analysis | **Reasoning model / high reasoning effort** | It checks multiple steps on its own |
| Research reports that pull together many sources | Deep research feature + **source verification** | Convenient, but it doesn't screen for source quality → [Example 3](../examples/03-research-with-sources.md) |
| Q&A over your own documents | File attachments / projects feature | Limits the grounding to your material |
| Codebase work | Coding agent | It can read files and run tests → [07. AI coding](07-ai-coding.md) |

---

## 3. Treat reasoning models like a "senior colleague"

OpenAI compares the two kinds of models like this:

- **Standard models:** a **junior coworker** who needs precise, step-by-step instructions
- **Reasoning models:** a **seasoned senior coworker** who works out the method once given a goal

So you need to write for reasoning models differently.

| Old habit (for standard models) | For reasoning models |
|---|---|
| "Think step by step" | **Drop it.** They already think on their own |
| Dictating the solution as steps 1–10 | Make only **the goal and success criteria** clear. Anthropic explains that general instructions ("think thoroughly") often work better than hand-written steps |
| Adding lots of examples | Try **without examples first** (OpenAI) |
| "Write your thought process in `<thinking>` tags" | Don't. Recent Claude models may refuse, and OpenAI and Microsoft state that forcing out internal reasoning is not supported |
| "Think harder," "think hard" | Use the app's or API's **reasoning effort (effort) setting** instead of phrases. Claude Code's docs list such phrases among "things you no longer need to do" (though `ultrathink` still works, for a single turn) |
| Tuning temperature | Most reasoning models don't support it or ignore it. Google ignores custom values on the latest Gemini models (3.6+, 4) and plans to return errors in the future; OpenAI says to omit it on the GPT-6 family unless reasoning effort is `none`. Some recent Claude models **reject** non-default temperature, top_p, and top_k values **with an error** |

### What the research has confirmed

The Wharton Generative AI Labs' Prompting Science Report 2 (2025) measured the effect of "think step by step" instructions.

- **Standard models:** average performance went up (by as much as 13.5 percentage points), but they sometimes **got easy questions wrong** that they had answered correctly before.
- **Reasoning models:** the effect ranged from +3.1 to −3.3 percentage points, **almost nothing**, while the time to answer grew by 20–80%.
- Conversely, the report warned that telling standard models to "just give the answer" is likely to hurt performance.

> **Bottom line:** Give standard (instant-answer) models room to think, and don't tell reasoning models how to think.

---

## 4. Working with reasoning effort

Many services let you choose a "reasoning effort" (for example, low / medium / high, or turning on a Thinking mode).

- **Start with the default**, and raise it one step at a time if the results fall short.
- **Before** raising the effort, check: Did you write success criteria? Did you provide the material? Do you have a way to verify the result? OpenAI recommends checking for missing success criteria or verification loops before raising the effort.
- If it deliberates too long (overthinking), tell it "Pick one approach and see it through," or lower the effort (Anthropic).

---

## 5. As of 2026: old habits to drop

The common direction across the three companies' latest guides is **not "add new tricks" but "strip out old ones."** But what to strip out **varies by model**, so check the guide for the model you use.

| Habit to drop | Why |
|---|---|
| ALL-CAPS emphasis, "CRITICAL: You MUST" | Anthropic says to soften such phrasing, and OpenAI says to reserve absolute language for **rules that truly have no exceptions**. Recent models over-follow emphasis |
| "Don't be lazy," "Finish everything" | Anthropic: recent models already have a strong tendency to finish the job. Such phrases invite overreach |
| Habitual verification instructions | **Depends on the model.** Anthropic says to remove old verification instructions for Opus 5 but still recommends self-checking as such. OpenAI notes that GPT-6 Astra tends to overuse tests and advises against writing tests for small, reversible changes |
| Repeating "be concise" | Recent models are already trending toward concision, and output can end up too short (conversely, GPT-6 Astra tends to over-format, so OpenAI says to specify the writing style you want) |
| Long, verbose system prompts | In OpenAI's GPT-5.6 guide (2026-07), a prompt with the fluff removed scored about 10–15% higher on an internal coding-agent eval (OpenAI itself calls it a "directional" figure, and the GPT-6 guide doesn't repeat it) |

### When you switch models, retune your prompts

The same prompt can produce different results when the model version changes. Whenever you switch models, **recheck important prompts with the same test inputs**. OpenAI recommends starting from a prompt that works and **removing one chunk at a time**, rerunning the same eval after each change. → [08. Verification and evaluation](08-verification-and-evals.md)

---

## 6. Ask several models the same question

Karpathy's open-source [llm-council](https://github.com/karpathy/llm-council) has several models each answer, review one another's answers, and then has a chair model compile the final answer. To do the same by hand:

1. Ask the same question in 2–3 services.
2. Mark where the answers differ. → Those are **the spots that most need checking**.
3. Show one model the other models' answers and have it analyze the differences.

---

### Sources

- Karpathy, "How I use LLMs" (2025-02-27) — https://www.youtube.com/watch?v=EWvNQjAaOHw
- Karpathy, "Deep Dive into LLMs like ChatGPT" (2025-02-05) — https://www.youtube.com/watch?v=7xTGNNLPyMI
- Karpathy, llm-council — https://github.com/karpathy/llm-council
- OpenAI, Prompt engineering guide (reasoning model = senior coworker analogy) — https://developers.openai.com/api/docs/guides/prompt-engineering
- OpenAI, Reasoning best practices (written for the o-series; some content reflects earlier generations) — https://developers.openai.com/api/docs/guides/reasoning-best-practices
- OpenAI, prompt guidance for the latest models — https://developers.openai.com/api/docs/guides/prompt-guidance
- OpenAI, GPT-5.6 prompt guidance (removing fluff, effort criteria) — https://developers.openai.com/api/docs/guides/prompt-guidance-gpt-5p6
- Anthropic, Prompting best practices (general instructions > step-by-step instructions, effort, over-verification) — https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- Claude Code, Best practices ("things you no longer need to do") — https://code.claude.com/docs/en/best-practices
- Google, Prompt design strategies (thinking models, temperature) — https://aistudio.google.com/docs/prompting-strategies
- Microsoft, Prompt engineering techniques (banner advising against these techniques for reasoning models) — https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/prompt-engineering
- Meincke et al., Prompting Science Report 2 "The Decreasing Value of Chain of Thought in Prompting" (Wharton, 2025, preprint) — https://arxiv.org/abs/2506.07142

**2026 update (checked 2026-11-09)**
- Anthropic, Models overview — https://platform.claude.com/docs/en/about-claude/models/overview
- Anthropic, API release notes — https://platform.claude.com/docs/en/release-notes/overview
- Claude app release notes (memory, Cowork, skills) — https://support.claude.com/en/articles/12138966-release-notes
- OpenAI, Models — https://developers.openai.com/api/docs/models
- OpenAI, Using the latest model (GPT-6) — https://developers.openai.com/api/docs/guides/latest-model
- OpenAI, API changelog — https://developers.openai.com/api/docs/changelog
- OpenAI, Deprecations — https://developers.openai.com/api/docs/deprecations
- Google, Gemini models — https://aistudio.google.com/docs/models
- Google, Gemini app release notes — https://gemini.google/release-notes/
- Agent Skills open standard — https://agentskills.io
