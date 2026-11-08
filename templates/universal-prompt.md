# Universal prompt template

> A template built on the six elements, **Role · Context · Instruction · Format · Constraints · Examples**, plus **verification**.
> You don't have to fill in every slot. Delete the ones you don't need. For a short question, the three-line version is enough.
> Why each element matters is explained in [docs/02-prompt-anatomy.md](../docs/02-prompt-anatomy.md).

---

## 1. Three-line version (everyday use)

```text
[Goal] Please ___ so that ___.
[Context] The reader is ___, and my situation is ___. Reference material: ___
[Format] Use a ___ format, about ___ long. Mark anything you're not sure about as "needs checking."
```

**Example**

```text
[Goal] Write an email telling my manager that the project schedule will slip by one week.
[Context] My manager likes to hear the bottom line first. The delay is because we're waiting for approval from an external API provider. As an alternative, we have a reduced-scope option.
[Format] Five sentences or fewer, polite but without filler. Add a subject line too.
```

---

## 2. Full version (for important work)

If your material is long, put **the material at the top and the question at the bottom**. Anthropic reports that doing this can improve response quality by up to 30%.

```xml
<role>
(Optional) You are a ___ specializing in ___.
Note: use this to set tone and perspective. It does not raise accuracy. (See docs/10.)
</role>

<context>
- Purpose (why I'm doing this):
- Audience / where it will be used:
- Current situation and background:
- Already decided / already tried:
</context>

<documents>
<document index="1" source="file name or URL">
(Paste the material here)
</document>
</documents>

<task>
1.
2.
3.
Done when: ___.
</task>

<format>
- Structure: (e.g., one table + a three-line summary / section headings + bullets)
- Length:
- Tone:
</format>

<constraints>
- Must follow:
- Write "do this" instead of "don't do that": (e.g., "no jargon" → "use words a middle schooler would understand")
- Grounding rule: don't guess about anything that isn't in <documents>; mark it "not in the documents."
</constraints>

<examples>
<example>
Input: ...
Output: ...
</example>
<example>
Input: ...
Output: ...
</example>
</examples>

<before_answering>
If any part of the request is ambiguous, ask me up to 3 of the most important questions before you answer.
If nothing is ambiguous, go ahead.
</before_answering>

<self_check>
Before giving your answer, check it item by item against <task> and <constraints> to make sure nothing is missing.
If there are items you couldn't verify, list them separately at the end of your answer.
</self_check>
```

---

## 3. Tips for each slot

| Slot | When you need it | Common mistake |
|---|---|---|
| `role` | When tone, perspective, or domain vocabulary matters | Believing that "world's best expert" makes the answer more accurate |
| `context` | **Almost always** | Assuming the AI knows background that exists only in your head |
| `documents` | When factual accuracy matters | Asking for "the latest information" without providing any material |
| `task` | Always | Mixing several jobs into one request and not writing done criteria |
| `format` | When you'll paste the result somewhere else | Not specifying a format, then asking for rewrites later |
| `constraints` | When there are rules that must be followed | Overusing ALL CAPS or "NEVER!!!" (current models over-follow them) |
| `examples` | When the style or format you want is hard to describe in words | Giving only one example (the model copies it) |
| `before_answering` | When the request is big or ambiguous | Making it ask questions even for simple jobs |
| `self_check` | When there are five or more requirements | Using "Are you sure?" as verification (it actually flips correct answers) |

---

## 4. What to remove when using reasoning (thinking) models

- Delete "think step by step." Reasoning models think on their own, and the phrase has almost no effect.
- Instead of dictating each step, state **the goal and the done criteria** clearly.
- Try without examples first, and add them only if the output doesn't match the format you want.
- If you want deeper thinking, use the app's or API's **reasoning effort (effort/thinking) setting** rather than wording.
