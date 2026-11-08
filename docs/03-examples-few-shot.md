# 03. Teaching with examples (few-shot)

> Showing **a single example** is often more precise than ten lines of explanation.
> Examples are one of the most reliable ways to align format, tone, structure, and judgment criteria. (Anthropic, Google, and OpenAI all agree.)

---

## 1. Examples show the bar a good answer must clear

The point of giving examples is not to have the AI copy their content but to **show what "good enough" looks like**.

So when you pick examples, ask yourself:

> Looking only at these examples, could someone new to the task infer **what counts as a passing answer**?

---

## 2. Rules from the official guides

| Rule | Source |
|---|---|
| **3–5** examples is about right | Anthropic, Google prompt engineering whitepaper |
| Choose **varied** examples (including edge cases) | Anthropic, OpenAI |
| Wrap them in `<example>` tags to separate them from the instructions | Anthropic |
| Use **exactly the same format** in every example (tags, line breaks, delimiters) | Google |
| Too many examples cause **overfitting** (answers that fit only the examples) | Google |
| For classification, start with about 6 and **mix up the order of the classes** | Google whitepaper |
| Examples and instructions **must not contradict each other** | OpenAI |
| For reasoning models, try **without examples first** and add them only if needed | OpenAI |
| Delete examples that don't help | OpenAI (latest model guide) |

---

## 3. Types of examples

### 3-1. Input → output pairs (the basic form)

```xml
<examples>
<example>
Input: Shipping is way too slow. It's been a week and it still hasn't arrived.
Output: {"category": "shipping", "sentiment": "negative", "urgency": "high"}
</example>
<example>
Input: The packaging was really careful. Loved it!
Output: {"category": "packaging", "sentiment": "positive", "urgency": "low"}
</example>
<example>
Input: Can I exchange this for a different size?
Output: {"category": "exchange", "sentiment": "neutral", "urgency": "medium"}
</example>
</examples>

Now classify the review below in the same format.
Input: {{review}}
```

> The three examples all differ in sentiment (negative/positive/neutral) and urgency (high/low/medium). Choosing them to be this **varied** keeps the AI from learning an odd pattern like "just answer negative every time."

### 3-2. Contrasting good and bad examples

Useful when the judgment criteria are subtle.

```xml
<good_example>
Title: Q3 revenue up 12%, driven by new customers
→ Why it's good: the title contains both the number and the cause
</good_example>
<bad_example>
Title: Q3 results report
→ Why it's bad: you learn nothing until you read the whole thing
</bad_example>
```

> Adding **a one-line explanation of why each is good or bad** helps the AI learn the principle rather than the surface. Anthropic also recommends noting "why this response is correct" alongside examples.

### 3-3. Examples that show the reasoning

For tasks that require reasoning, show examples in the order **problem → approach → answer**. Anthropic explains that the model's own thinking then comes to resemble the examples.

### 3-4. Your own writing as examples (matching a style)

```text
Below are 3 pieces I wrote. Analyze their sentence length, tone, and recurring expressions, and write in the same style.
Don't borrow their content or topics.
<example>...</example>
<example>...</example>
<example>...</example>
```

---

## 4. Common failures and fixes

| Failure | Cause | Fix |
|---|---|---|
| **Copies example sentences verbatim** | Only 1 example, or no instructions | Add more examples and write "Follow only the pattern; use fresh wording" |
| Every answer gets **the same label** | Example labels are skewed toward one side | Balance the labels and shuffle their order |
| Resembles only the last example | Tendency to be pulled toward the most recent example | Test with the order rearranged |
| **Handles cases not in the examples oddly** | Not enough edge-case examples | Add examples of ambiguous cases, empty input, and exceptions |
| Instructions and examples **conflict** | Long examples, but the instruction says "keep it short" | Revise the examples to match the instructions |
| Reasoning model performance **actually drops** | The examples interfere with the model's own reasoning | Try without examples and compare |

> 📌 The way results get pulled by the label distribution or order of examples has been studied for a long time (Zhao et al., "Calibrate Before Use," 2021). The effect is weaker in recent models, but it's still worth checking for **classification tasks**.

> 📌 In a preprint by Microsoft researchers (2024), giving few-shot examples to a reasoning model (o1) **actually lowered its performance.** That's why "no examples first" is the default for reasoning models.

---

## 5. No examples? Have the AI create them

```text
Create 5 examples for this task: 2 easy cases, 2 ambiguous cases, and 1 exception.
For each example, give the correct answer and the reason.
```

**Review and fix** the AI-generated examples before putting them in your prompt. Fixing them also sharpens your own criteria. Anthropic also describes having Claude evaluate examples or generate new ones.

---

## 6. Checklist

- [ ] There are at least 2 examples, and they differ enough from each other
- [ ] At least one edge case (an ambiguous case) is included
- [ ] All examples use exactly the same format
- [ ] The examples don't contradict the instructions
- [ ] I spelled out what to take from the examples and what to ignore
- [ ] For a reasoning model, I also tried without examples

---

### Sources

- Anthropic, Prompting best practices (3–5 examples, diversity, tags) — https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- Anthropic, Effective context engineering (representative examples over lists of rules) — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- OpenAI, Prompt engineering guide — https://developers.openai.com/api/docs/guides/prompt-engineering
- OpenAI, Reasoning best practices (zero-shot first for reasoning models) — https://developers.openai.com/api/docs/guides/reasoning-best-practices
- OpenAI Cookbook, GPT-4.1 Prompting Guide (models repeating example phrasing; archived document) — https://developers.openai.com/cookbook/examples/gpt4-1_prompting_guide
- Google, Prompt design strategies (format consistency, overfitting) — https://aistudio.google.com/docs/prompting-strategies
- Google/Kaggle, Prompt Engineering whitepaper (Lee Boonstra) — https://www.kaggle.com/whitepaper-prompt-engineering
- Microsoft, Prompt engineering techniques (before/after few-shot comparison) — https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/prompt-engineering
- Nori et al., "From Medprompt to o1" (Microsoft Research, 2024, preprint) — https://arxiv.org/abs/2411.03590
- Zhao et al., "Calibrate Before Use: Improving Few-Shot Performance of Language Models" (ICML 2021) — https://arxiv.org/abs/2102.09690
- Schulhoff et al., "The Prompt Report" (2024–2025) — https://arxiv.org/abs/2406.06608
