# 02. The six elements of a prompt: Role · Context · Instruction · Format · Constraints · Examples

> A good prompt is defined not by its length but by **how little the AI has to guess**.
> The six elements are a checklist for reducing that guesswork. You don't need all six every time, but **if an element is missing, it should be missing on purpose.**

---

## At a glance

| Element | Question | Impact | What goes wrong without it |
|---|---|---|---|
| **Context** | Why, for whom, in what situation? | ★★★ | Misunderstanding, fabrication |
| **Instruction** | What exactly should it do, and when is it done? | ★★★ | Misunderstanding, omission |
| **Format** | What shape should the output take? | ★★★ | Rework, omission |
| **Examples** | What does a good output look like? | ★★☆ | Style mismatch |
| **Constraints** | What must it follow or avoid? | ★★☆ | Incidents, rule violations |
| **Role** | What perspective and tone? | ★☆☆ | Tone mismatch (little to do with accuracy) |

> ⚠️ Many courses put "assign a role" first, but the research shows that role is **the element with the least effect on accuracy**. Keep the order "Role · Context · Instruction · Format · Constraints · Examples" because it's easy to remember, but **spend your time on Context, Instruction, and Format**. (Evidence in Section 1 below.)

### How this maps to other frameworks

The six elements in this repo combine the components that several organizations propose. The names differ, but the content is nearly the same.

| This repo | OpenAI recommended order | Microsoft | MIT Sloan |
|---|---|---|---|
| Role | Identity | — | Part of Context (role/persona) |
| Context | Context | Primary content, Supporting content | Context |
| Instruction | Instructions | Instructions | Task, Specificity |
| Format | (included in Instructions) | Cue (plus Instructions) | Examples & constraints |
| Constraints | (included in Instructions) | (included in Instructions) | Examples & constraints |
| Examples | Examples | Examples | Examples & constraints |

---

## 1. Role

**What:** Sets the position and perspective the AI answers from. "You are an HR manager with 10 years of experience." "You are an elementary school teacher."

**What the research says**
- A 2025 report from the Wharton Generative AI Labs (Prompting Science Report 4) found that expert personas such as "Answer like a physics expert" **did not reliably improve factual accuracy**. In some conditions accuracy actually dropped, and low-knowledge personas such as "a toddler" clearly hurt performance.
- A study that tested 162 roles on 2,410 questions (Zheng et al., EMNLP Findings 2024) also found that assigning a role did not improve accuracy, and **automatically picking the best role was no better than picking one at random.**

**So when should you use it?**
- To set **tone, perspective, and vocabulary level**: "like a senior colleague explaining things to a new hire," "as a reviewer looking for risks from the legal team's perspective"
- To get an **opposing view**: "as a reviewer who wants to reject this proposal" → [Preventing sycophancy](../templates/honest-critique.md)

| ❌ No effect | ✅ Effective |
|---|---|
| You are the world's greatest marketing genius. | You are a B2B SaaS marketer. Your readers are small-business owners who aren't technical, so explain things in terms of cost and time savings instead of jargon. |

> The second example works better not because of the "marketer" role but because it spells out **the audience and how to explain (context and instruction)**.

---

## 2. Context: the most important element

**What:** Information that exists only in your head: purpose, audience, situation, background material, what you've already tried, success criteria.

**Why it matters most:** The AI knows nothing about your situation. Without context it gives **the most average answer** or **fills the gaps with guesses** (fabrication).

### 2-1. Tell it the purpose (the why), and the AI generalizes on its own

An example from Anthropic's official guide:

| ❌ Rule only | ✅ Rule plus reason |
|---|---|
| Never use ellipses (…). | Your response will be read aloud by a text-to-speech (TTS) engine. TTS can't pronounce ellipses, so don't use them. |

Given the reason, the AI avoids not only ellipses but **other symbols TTS struggles with (emoji, tables, and so on) on its own.** Given only the rule, it follows exactly that rule.

### 2-2. Provide the material directly, and generic answers disappear

Adapted from an example in Google's official guide:

| ❌ Without material | ✅ With material |
|---|---|
| My router's light is slowly blinking yellow. What should I do? | (Paste the troubleshooting section of the router manual.) Answer using only this manual. My router's light is slowly blinking yellow. |
| → Generic steps that apply to any router | → Steps that match this LED state on this product |

### 2-3. Context checklist

- [ ] **Purpose:** What will you do with this output?
- [ ] **Audience:** Who will read it? What do they already know, and what don't they know?
- [ ] **Situation:** Deadlines, budget, politics, decisions already made
- [ ] **Material:** Internal documents or recent information the AI can't know
- [ ] **History:** What you've already tried that didn't work

> **The colleague test (recommended by Anthropic):** If a colleague with no background would be confused by this prompt as written, the AI will be too.

### 2-4. Context: "as much as needed," not "as much as possible"

More context isn't always better. Anthropic compares the AI's attention to a **limited budget** and calls the tendency to lose track of earlier information as input grows **context rot**. The goal is to provide **the information that affects the result, in the smallest possible amount**. → [06. Workflows and context engineering](06-workflows.md)

---

## 3. Instruction

**What:** What to do, in what order, and when it's done.

### 3-1. State the level you want

Recent models increasingly do **exactly what you ask and no more**. If you want more than that, say so. An example from Anthropic's official guide:

| ❌ | ✅ |
|---|---|
| Build an analytics dashboard. | Build an analytics dashboard. Include as many relevant features and interactions as possible, and go beyond the basics to a fully featured implementation. |

### 3-2. Number the steps when order or completeness matters

```text
1. Classify the 200 attached customer reviews as positive/negative/neutral
2. Extract the top 5 recurring complaint themes from the negative reviews
3. Quote 1 representative review for each theme
```

### 3-3. Write done criteria ("Done when")

"Make it good" never ends. Write down **what has to be true for it to be done**.

```text
Done when: a non-technical executive can read it in under a minute and decide, "Let's go with Option A."
```

### 3-4. For reasoning models, give goals rather than procedures

Both OpenAI and Anthropic advise that, for recent reasoning (thinking) models, it's better to give **clear goals and success criteria** than to dictate each step. → [05. Models and reasoning](05-models-and-reasoning.md)

---

## 4. Format

**What:** The shape of the output: structure (tables, bullets, sections), length, tone, file format (JSON, Markdown, CSV).

**What the research says:** In Wharton's Prompting Science Report 1 (2025), **removing** the output-format instruction cut accuracy by 8.6 percentage points on GPT-4o and 12.1 points on GPT-4o-mini. Format instructions aren't decoration; they're a **performance factor**.

### 4-1. Be specific

| ❌ | ✅ |
|---|---|
| Summarize it briefly. | 3-line summary + table (item / status / risk level) + 3 next-step bullets |
| Keep it short. | Under 200 characters |
| Make it look nice. | Use section headings (##), and keep paragraphs to 3 sentences or fewer |

### 4-2. "Do this" instead of "don't do that"

Both Anthropic and Google recommend **positive instructions over negative ones**.

| ❌ | ✅ |
|---|---|
| Don't use Markdown. | Write in plain text, as flowing paragraphs. |
| Don't make it too long. | Write 5 sentences or fewer. |
| Don't use jargon. | Use words a middle-school student would understand. |

### 4-3. For output a program will read, use structured outputs

If code needs to read the result directly, specify a schema with the API's **Structured Outputs feature** rather than asking for "JSON, please" in the prompt. OpenAI says this feature guarantees schema adherence.

### 4-4. The shape of the prompt shapes the answer

A prompt full of Markdown tends to get an answer full of Markdown. Write your prompt in a style similar to the output you want.

---

## 5. Constraints

**What:** Rules and boundaries that must be respected: grounding rules, prohibitions, scope, policies.

### 5-1. The fewer the constraints, the better they're followed

The more instructions you give, **the lower the chance that all of them are followed.** Several studies (ManyIFEval 2025, IFScale 2025) found that performance declined steadily as the number of instructions grew; in an experiment with 500 instructions, even the best model followed only 68%. 🆕 In a 2026 experiment with 15 models, the rate of following every constraint dropped sharply once the number of simultaneous constraints **exceeded 5–6** (Vasileva, 2026, preprint). **Keep only the truly important constraints, around five of them, and if you need more, split the task into steps.**

### 5-2. Drop ALL CAPS and "NEVER!!!" emphasis (as of 2026)

Emphasis such as `IMPORTANT`, `MUST`, and `NEVER` used to help, but current guides say to tone it down. Anthropic says to **soften** phrasing like "CRITICAL: You MUST," and OpenAI says to reserve absolute language for **rules that truly have no exceptions**. Recent models over-follow emphasis, ignoring other instructions or behaving rigidly.

| ❌ | ✅ |
|---|---|
| NEVER!!! use the customer's name!!! | Write "Dear customer" instead of the customer's name, because this reply may also be shared with other customers. |

> Use `always`/`never` only for **rules that truly have no exceptions**.

### 5-3. A constraint worth including: the grounding rule

```text
If something isn't in the material I provided, don't guess. Write "Not in the material."
```

This one line is the cheapest way to reduce fabrication (hallucination). → [04. Misunderstanding · Omission · Fabrication](04-failure-modes.md)

---

## 6. Examples

**What:** Samples of the output you want. A way to **show** style, format, and judgment criteria that are hard to describe in words.

Here's the short version. Details are in [03. Teaching with examples](03-examples-few-shot.md).

- **3–5 examples**, **varied**, wrapped in `<example>` tags (Anthropic, Google)
- Give only 1 example and the AI copies it
- For reasoning models, try **without examples first** and add them when needed (OpenAI)

---

## 7. Layout and separation: what goes where

### 7-1. Divide the prompt with delimiters

When context, material, and instructions are mixed in one paragraph, the AI may **mistake sentences in the material for instructions**. Separate them with XML tags or Markdown headings. Anthropic, OpenAI, Google and Microsoft all give the same advice. Use **only one style** within a single prompt.

```xml
<context>...</context>
<document>...</document>
<task>...</task>
<format>...</format>
```

### 7-2. Long material on top, question at the bottom

With long material (dozens of pages or more), put the material **first** and the question and instructions **at the very end**. Anthropic reports that this improved response quality by **up to 30%**. When including multiple documents, label each one with its source.

```xml
<documents>
  <document index="1"><source>2026_business_plan.pdf</source><content>...</content></document>
  <document index="2"><source>competitor_analysis.xlsx</source><content>...</content></document>
</documents>

Compare the two documents above and ...  ← question goes at the end
```

---

## 8. Final checklist

Take 10 seconds before you hit send.

- [ ] **Context:** I stated the purpose and the audience
- [ ] **Instruction:** What to do and when it's done are clear
- [ ] **Format:** I set the structure and length
- [ ] **Constraints:** I kept only the truly important rules and included a grounding rule
- [ ] **Examples:** If style matters, I included 3–5
- [ ] **Role:** I included one only where tone or perspective matters
- [ ] **Separation:** I separated material and instructions with tags and put long material on top
- [ ] **Colleague test:** A colleague without context could understand it

→ Ready-to-use template: [templates/universal-prompt.md](../templates/universal-prompt.md)
→ An example that improves step by step: [examples/01-email-step-by-step.md](../examples/01-email-step-by-step.md)

---

### Sources

- Anthropic, Prompting best practices — https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- Anthropic, Prompt engineering overview — https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview
- Anthropic, Effective context engineering for AI agents (2025-09-29) — https://www.anthropic.com/research/effective-context-engineering-for-ai-agents
- OpenAI, Prompt engineering guide — https://developers.openai.com/api/docs/guides/prompt-engineering
- OpenAI, Structured outputs — https://developers.openai.com/api/docs/guides/structured-outputs
- Google, Prompt design strategies — https://aistudio.google.com/docs/prompting-strategies
- Microsoft, Prompt engineering techniques — https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/prompt-engineering
- MIT Sloan Teaching & Learning Technologies, Effective Prompts for AI: The Essentials — https://mitsloanedtech.mit.edu/ai/basics/effective-prompts/
- Meincke et al., Prompting Science Report 1 "Prompt Engineering is Complicated and Contingent" (Wharton, 2025, preprint) — https://arxiv.org/abs/2503.04818
- Basil et al., Prompting Science Report 4 "Playing Pretend: Expert Personas Don't Improve Factual Accuracy" (Wharton, 2025, preprint) — https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5879722
- Zheng et al., "When 'A Helpful Assistant' Is Not Really Helpful: Personas in System Prompts Do Not Improve Performances of Large Language Models" (EMNLP Findings 2024) — https://arxiv.org/abs/2311.10054
- ManyIFEval / StyleMBPP: performance decline as the number of instructions grows (2025) — https://arxiv.org/abs/2509.21051
- IFScale: following up to 500 simultaneous instructions (2025) — https://arxiv.org/abs/2507.11538
- Vasileva, phase transition in following simultaneous constraints (2026-08, preprint) — https://arxiv.org/abs/2608.12426
