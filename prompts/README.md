# Prompt library: 30 evidence-based prompts by task

> Copy, fill in the `{{blanks}}`, and paste. Every prompt is built from the six elements (role, context, instruction, format, constraints, examples) and tagged with the failure modes it guards against:
> 🎯 misunderstanding · 📋 omission · 🔍 fabrication (hallucination) · 🪞 sycophancy
>
> Why these patterns work: [docs/02 (six elements)](../docs/02-prompt-anatomy.md) · [docs/04 (failure modes)](../docs/04-failure-modes.md). Longer, annotated versions: [templates/](../templates/).

**Contents:** [Writing](#writing) · [Summarizing](#summarizing) · [Research](#research) · [Analysis & decisions](#analysis--decisions) · [Coding](#coding) · [Learning](#learning) · [Thinking partner](#thinking-partner) · [Building agents](#building-agents)

---

## Writing

### 1. Email that gets a decision 🎯🪞
```text
Write an email to {{recipient and their role}} about {{topic}}.
Context: {{what happened, why it matters, what options exist}}. They prefer the conclusion first.
Format: subject line + at most 5 sentences: conclusion, reason, options, the decision I need from them and by when, closing.
Constraints: state facts plainly, apologize at most once, don't blame anyone.
```

### 2. Rewrite for a different audience 🎯
```text
Rewrite the text below for {{audience}}, who {{what they know / don't know}}.
Goal: after reading, they should be able to {{action or decision}}.
Keep every fact and number unchanged. Replace jargon with plain words; if a technical term is unavoidable, define it in one clause.
Length: about {{n}} words.
<text>{{paste}}</text>
```

### 3. Draft in my voice 🎯
```text
Below are 3 samples of my writing. Note sentence length, tone and recurring phrases, then write {{piece}} about {{topic}} in the same style.
Copy the style, not the content or exact sentences.
<example>{{sample 1}}</example>
<example>{{sample 2}}</example>
<example>{{sample 3}}</example>
```

### 4. Outline first, then sections 📋
```text
I need a {{document type}} on {{topic}} for {{audience}}, about {{length}}.
Step 1: give me only an outline with section headings and one line on what each covers. Wait for my approval.
Step 2: when I say "next", write one section at a time.
```

---

## Summarizing

### 5. Decision-ready summary of a long document 📋🔍
```text
<document>{{paste long document}}</document>

This summary is for {{reader}}, who has 2 minutes and needs to know what was decided.
1. First, quote word for word every sentence about decisions, owners, deadlines and open issues, numbered, from start to end of the document (including the middle).
2. Then, using only those quotes, write:
   - One-line conclusion
   - Decisions table: decision | owner | deadline | quote #
   - Open issues (max 5)
   - Not stated in the document (e.g., missing owners or deadlines)
If an owner or deadline isn't in the document, write "TBD". Don't infer it.
```

### 6. Meeting notes → action items 📋🔍
```text
<transcript>{{paste}}</transcript>
Extract every action item as: action | owner | due date | quote from the transcript.
Only include items someone actually committed to. If owner or date is missing, write "not stated".
End with: "Possibly missed:" listing anything ambiguous.
```

### 7. Compare two documents 📋🔍
```text
<document index="1" source="{{name}}">{{...}}</document>
<document index="2" source="{{name}}">{{...}}</document>
Compare the two on: {{criteria}}.
Output a table: criterion | document 1 (with quote) | document 2 (with quote) | difference.
If a document doesn't address a criterion, write "not addressed". Don't fill gaps from general knowledge.
```

---

## Research

### 8. Research with verifiable sources 🔍
```text
Research {{question}} (use web search). Prefer primary sources: papers, official reports, government data, official docs.
Output a table: claim | source (title, publisher, date) | URL | primary or secondary | confidence.
Only include sources you actually opened. If you couldn't verify a number, mark it [unverified]. If you found nothing, say so.
End with: where sources disagree, and what evidence would settle it.
```

### 9. Find the evidence against 🪞🔍
```text
Here is my current conclusion: {{conclusion}}.
Search for the strongest evidence and arguments AGAINST it. For each: the claim, the source (URL), and how strong it is.
Then tell me whether my conclusion survives, needs qualifying, or should be dropped.
```

### 10. Fact-check a draft 🔍
```text
Fact-check the text below.
1. List every checkable claim, one per line (names, dates, numbers, quotes, citations).
2. Check each one independently against sources you open now; don't rely on the text's own wording.
3. Table: claim | ✅ supported / ❌ contradicted / ❓ unverified | evidence (URL or quote).
4. Suggest corrected wording for ❌ and ❓ items.
<text>{{paste}}</text>
```

### 11. Explain a paper honestly 🔍🎯
```text
<paper>{{paste paper or abstract + methods}}</paper>
Explain this paper for {{audience}}: question, method, sample, main result (with numbers), limitations stated by the authors, and whether it's peer-reviewed.
Separate what the paper shows from what it doesn't show. Quote the sentence behind each key number.
```

---

## Analysis & decisions

### 12. Data analysis with code 🔍📋🎯
```text
The attached {{file}} contains {{what}}. (Units: {{units}}.)
0. Check the data first: rows/columns, missing values, duplicates, outliers, unit problems. Propose fixes and wait for my OK.
1. Compute {{metric}} defined as {{exact definition}}.
2. Do every calculation by running code, and show the code.
3. Output: data check, results table, 3 notable points with supporting numbers.
If the data can't explain why something happened, say "can't tell from the data".
```

### 13. Decision matrix 🎯🪞
```text
I'm choosing between {{options}} for {{goal}}. Constraints: {{budget, time, must-haves}}.
1. Propose 5–7 criteria with weights and explain each weight; let me adjust.
2. Score each option 1–5 per criterion with a one-line justification.
3. Show the weighted totals, then tell me which result is most sensitive to the weights.
Don't favor the option I seem to prefer.
```

### 14. Pre-mortem 🪞
```text
Imagine it's {{date}} and {{project/plan}} has failed badly.
Write the 7 most likely reasons it failed, ranked by likelihood × impact. For each: the early warning sign and one thing we can do now to prevent it.
<plan>{{paste}}</plan>
```

### 15. Spreadsheet formula 🎯🔍
```text
In {{Excel / Google Sheets}}, columns: {{A = ..., B = ...}}. I want {{result}} in column {{X}}.
Give the formula, explain each part in one line, and give 2 test rows with the expected output so I can check it.
If my request is ambiguous (e.g., how to treat blanks), state your assumption.
```

---

## Coding

### 16. Bug fix spec for an agent 🎯🔍
```text
Bug: {{symptom}}. Reproduce: {{steps}}. Error: {{exact message}}.
Look at {{files/dirs}}. Don't change code yet: first explain the likely cause with file and line references.
Then: write a failing test that reproduces the bug, run it and show it fails; make the minimal fix; run the related tests and show the output.
Don't edit the test to make it pass. Report remaining risks.
```

### 17. Feature with done criteria 🎯📋
```text
Goal: {{feature}} so that {{user benefit}}.
Context: {{relevant files, existing patterns to follow}}.
Constraints: {{don't touch X; no new dependencies without asking}}.
Done when: {{runnable checks: tests pass, command output, screenshot matches}}.
Plan first and wait for my approval before writing code.
```

### 18. Code review that matters 🪞
```text
Review this diff for correctness, security and maintainability, in that order.
List only issues that would cause a bug, a security problem, or real maintenance pain, each with file:line, why it matters, and a fix.
Skip style nitpicks. If there are no significant issues, say so.
<diff>{{paste}}</diff>
```

### 19. Explain unfamiliar code 🔍
```text
Explain what {{file/function}} does for someone new to this codebase: purpose, inputs/outputs, key steps, side effects, and how it's called.
Only describe code you've actually read; if something depends on code you haven't opened, say so and open it first.
```

### 20. Write tests for edge cases 📋
```text
Write tests for {{function}} in {{file}}. Cover: normal cases, boundaries, empty/invalid input, and {{domain-specific edge cases}}.
First list the cases you'll test as a numbered list, then write the tests, then run them and show the output.
Don't mock {{X}}.
```

---

## Learning

### 21. Tutor mode 🎯
```text
Be my tutor for {{topic}}. My level: {{level}}.
Don't give me answers or finished code directly. When I'm stuck, give one small hint at a time.
When I answer, ask me why before telling me if I'm right. Show the full solution only if I type "show solution".
```

### 22. Check my understanding 🪞
```text
I'll explain {{concept}} in my own words. Point out (1) what's wrong, (2) what's missing, (3) what's vague.
No praise; if there are no gaps, just say "no gaps".
My explanation: {{...}}
```

### 23. Quiz me on my weak spots 🎯
```text
Write 5 questions on {{topic}} that target common misconceptions. Ask one at a time; after each of my answers, grade it and explain briefly.
```

---

## Thinking partner

### 24. Stress-test my plan (third-person framing) 🪞
```text
Another team submitted the plan below. As a skeptical {{reviewer type}}, give its 3 biggest weaknesses with evidence and a fix for each, then the strongest argument that it will fail.
<plan>{{paste}}</plan>
```

### 25. Brainstorm, then filter 🎯
```text
Goal: {{goal}}. Constraints: {{constraints}}.
1. Generate 20 varied ideas, one line each (include some unconventional ones).
2. Define 4 criteria for a good idea here.
3. Score the ideas and return the top 5 with the reason each made the cut.
```

### 26. Steelman both sides 🪞
```text
Give the strongest case for and the strongest case against {{position}}, as an expert on each side would argue it. Then list the facts that would change which side is right.
```

### 27. Untangle a long chat 🎯📋
```text
Consolidate everything I've asked for and every decision we've made in this conversation into one complete prompt I can paste into a new chat. Don't leave anything out; list open questions at the end.
```

---

## Building agents

### 28. Agent system prompt 🎯🔍📋
```text
Write a system prompt for an agent that {{job}} for {{users}}.
Include: role and goal; context and the policies it must follow (only from the documents I provide); step-by-step task; output format (JSON schema below); constraints (what it must never decide on its own and when to hand off to a human); 2–3 varied examples.
Add: "If the policy doesn't cover a case, say so and escalate; don't invent policy."
<policies>{{paste}}</policies>
<schema>{{paste}}</schema>
```

### 29. Build an evaluation set 📋
```text
For the agent/prompt below, write 20 test cases as a table: input | expected behavior | which failure it checks (misunderstanding / omission / fabrication / sycophancy / safety).
Include easy cases, ambiguous cases, out-of-scope requests, and adversarial inputs (e.g., text that tries to override instructions).
<prompt>{{paste}}</prompt>
```

### 30. Improve a prompt 🎯📋🔍🪞
```text
Improve the prompt below.
1. Predict the 3 most likely bad outputs it would produce and why (misunderstanding, omission, fabrication, sycophancy).
2. Rewrite it to prevent them: add missing context and done criteria, keep only essential constraints with reasons, remove ALL-CAPS emphasis and filler.
3. Show a table of what changed and why, and 3 test inputs to compare old vs new.
<prompt>{{paste}}</prompt>
```
