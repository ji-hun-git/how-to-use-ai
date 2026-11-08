# 12. Writing decision rules: what makes a skill (or prompt) actually useful

> A skill that only sets a role, a tone and a layout produces output that *looks* right and is the same no matter what comes in. The value of a skill is in its **decision rules**: instructions that make the result change when the input changes. This guide shows how to find those rules in your own head, write them so an agent can follow them, and prove they work.

---

## 1. Format is not judgment

Compare two versions of an expense-review skill given the same input: *"Dinner with client, $480, receipt attached, 6 attendees listed."*

| | Format-only skill | Skill with decision rules |
|---|---|---|
| **Instructions** | "You are a finance reviewer. Be concise and professional. Output: verdict, reason, next step." | Same, plus: "When a meal exceeds $60 per attendee, flag it for manager approval. Unless an approved event code is on the report, in which case approve and note the code." |
| **Result** | "Approved. Business meal with receipt. No action needed." | "Flag for approval: $80 per attendee exceeds the $60 limit. No event code found." |

Both outputs are well formatted. Only the second one does the job. One rule, with a condition the agent can check in the input, changed the result.

This is the difference between an agent and a template: **a template fills in the same blanks every time; an agent should decide differently when the facts are different.** If removing your skill's tone and format instructions leaves nothing behind, the skill has no judgment in it yet.

---

## 2. Why rules are hard to write down

People who are good at a task often decide by recognizing the situation rather than consulting a checklist, so they may not be aware of the criteria they use. Asked "how do you decide?", most people answer with values ("I look for quality"). Asked "what did you do the last time X happened?", they answer with a rule ("I didn't use it; I moved it to a separate list").

So there are two sources of rules:

- **Written rules** that already exist in a policy, handbook, contract or style guide. Copy them precisely and note the source.
- **Unwritten rules** you apply from experience. These need to be pulled out with concrete questions, then written as conditions and actions.

## 3. Pulling rules out of your head

Answer these about a task you do often. Concrete stories beat general principles; answer with the last real case you remember.

| Probe | What it uncovers |
|---|---|
| **The last time this went wrong:** what happened, and what should have been done instead? | A missing rule, and your best test case |
| **The beginner's mistake:** what does someone new to this task get wrong most often? | Rules experts apply without noticing |
| **The fork:** when do you handle a case differently from the usual way? What tips you off? | The core decision rule: "normally A, but when X, B" |
| **The stop sign:** when do you pause, ask someone, or refuse to continue? | Exceptions and escalation points |
| **The gaps:** what do you do when information is missing, contradictory, or there's no time? | The three most common exception paths |
| **Done:** what must be true for the work to count as finished? | Output requirements and done criteria |
| **Never:** what must never happen, whatever the input? | Hard limits (and candidates for hard controls, see [docs/11](11-skills-and-agent-rules.md)) |

Start with "the fork" or "the beginner's mistake". Either one usually yields a rule that changes results. You don't have to write polished sentences: describe a case out loud to an AI and ask it to interview you one question at a time and turn your answers into rules (the [clarify-first](../skills/clarify-first/SKILL.md) and [prompt-improver](../skills/prompt-improver/SKILL.md) skills do this). Then check that the rules it wrote match what you meant.

---

## 4. The shape of a rule

Write each rule as **condition → action → exception**:

> **When** [something the agent can observe in the input: a keyword, a number, a field, a state],
> **do** [a specific action: a classification, a tool call, what goes where in the output].
> **Unless** [an observable exception], **in which case** [the alternative].
> *(Source: [policy name] / experience, provisional.)*

Each part prevents a specific failure:

| Missing part | What goes wrong |
|---|---|
| **Condition** | The agent can't tell when the rule applies, so it applies it everywhere or nowhere. "Prioritize important requests" has no condition; "when the request mentions a legal deadline or a regulator" does |
| **Specific action** | "Handle appropriately" instructs nothing. Say what the label becomes, which tool to call, or what line goes first |
| **Exception** | The rule fires where it shouldn't. One "unless" clause often fixes most false positives |
| **Source** | No one can tell a company policy from a guess. Mark experience-based thresholds as provisional and tune them with tests |

Use numbers where your judgment really uses numbers (3 times, 10%, 48 hours), but don't invent precision. If you're unsure of a threshold, mark it provisional and adjust it after testing.

### Examples from different kinds of work

| Task | Rule |
|---|---|
| **Code review** | When a change touches authentication, payments or data deletion, list it under "Needs human review" at the top, whatever its size. Unless the change only edits comments or tests, in which case review it normally. |
| **Literature screening** | When a study's sample is under 30 or it has no control group, put it in "Low-evidence" and don't count it toward conclusions. Unless it's the only study on the question, in which case include it and say so explicitly. |
| **Meeting scheduling** | When a requested time falls outside 9:00–18:00 in any attendee's time zone, propose the two nearest in-hours slots instead of booking. Unless the organizer wrote "after-hours OK", in which case book it. |
| **Refund requests** | When the order is older than 30 days, explain the policy and offer store credit; don't promise a refund. Unless the item is reported defective, in which case route to a human with the order details. |
| **Weekly metrics note** | When a metric moves more than 15% week over week, add one line on the likely cause; otherwise report the number only. Unless the metric is less than four weeks old, in which case always add a note (provisional thresholds). |

### Words that instruct nothing

| Vague | Ask yourself | Testable version |
|---|---|---|
| "appropriately", "as needed" | What exactly would I look at? | "when the amount exceeds $X" |
| "carefully", "thoroughly" | What does careful mean here? | "check every figure against the source table" |
| "important", "urgent" | What makes something urgent? | "mentions a deadline within 48 hours or a customer outage" |
| "reliable sources" | Which ones, in what order? | "official statistics and peer-reviewed papers first; news only if it cites a primary source" |
| "handle exceptions" | Which ones, and then what? | "if the order number is missing, ask for it; don't guess" |

---

## 5. Exceptions and where a human must decide

Most fabrications and costly mistakes happen where a skill says nothing about exceptions. Cover three cases explicitly:

| Case | Rule to write | Example |
|---|---|---|
| **Missing information** (a field is empty, a lookup returns nothing, an attachment is absent) | Name what to ask for or what to report; never fill the gap with a guess | "If no order number is given, ask for it. If the lookup is empty, say 'not found' and why." |
| **Ambiguous case** (fits two rules, or none) | Don't decide alone: state the candidates and the reason, and mark it for review | "If a request could be a refund or an exchange, list both options and mark 'needs confirmation'." |
| **Irreversible or high-impact action** (sending, publishing, paying, deleting, committing to money or terms) | The agent prepares; a person approves | "Draft the reply; never promise compensation; mark 'needs approval' when an amount is involved." |

Where your tool supports it, back the third case with a hard control: an approval step before sending, or permission rules that block the action outright. Written rules are followed most of the time, not every time ([docs/11](11-skills-and-agent-rules.md)). In some places this is also a legal question; South Korea's AI Basic Act, for example, treats systems where a human makes the final decision differently from fully automated ones ([docs/09](09-security-privacy.md#5-local-laws-and-guidelines-example-south-korea-2026)).

---

## 6. Where rules go in a SKILL.md

The `description` decides **whether** the skill is used; the body decides **what** it does. A layout that works:

```markdown
---
name: expense-report-review
description: Reviews employee expense reports against the travel and meals policy and flags items that need approval. Use when the user shares an expense report, receipt list or reimbursement request, or asks whether an expense is allowed.
---

# Expense report review

## Before you start
- Check that each line has a date, amount, category and receipt. List any that don't.

## Rules (apply in order)
1. When a meal exceeds $60 per attendee, flag it for manager approval. Unless an approved event code is present, in which case approve and note the code. (Source: Travel & Meals Policy §4)
2. When the same vendor appears 3+ times in one month for similar amounts, flag "possible split charge". Unless the vendor is on the recurring-subscriptions list. (Provisional: experience)
3. When a receipt is missing for an item over $25, mark it "receipt required"; don't approve it.

## Exceptions
- Missing amount or date: ask for it; don't estimate.
- Item fits no category: list it under "Needs a human decision" with the two closest categories.
- Never approve anything over $1,000; mark "needs finance approval".

## Output
- First line: Approve / Approve with flags / Return for fixes.
- Then a table: line | amount | flag | rule number.
- Example first line: "Approve with flags: 2 items need manager approval (rule 1)."

## Never
- Don't invent policy that isn't written above.
- Don't change amounts or categories in the report.
```

Notes:
- **Name and description:** the name should say when it's used; the description says what it does and when, in the third person, with words users actually type. If the description is vague, the skill won't be picked when it's needed.
- **Number the rules** and say whether order matters.
- **One or two example output lines** stabilize the format more than a paragraph of formatting instructions.
- Keep the body focused on one job. Ready-made template: [templates/skill-template.md](../templates/skill-template.md).

---

## 7. Improve the skill you have; don't fork it

When a test goes wrong, it's tempting to create `report-skill-v2` or `report-skill-final`. Usually you should edit the existing skill instead:

- **The agent can't choose between near-duplicates.** It picks skills by name and description; two similar descriptions make the choice arbitrary, and results vary from run to run.
- **Fixes scatter.** A rule change has to be made in every copy, and copies drift apart.
- **Knowledge doesn't accumulate.** Ten edits to one skill give you ten rules; ten forks give you ten overlapping drafts.

Create a separate skill only if it has a clearly different trigger (you can write a description that doesn't overlap) and different rules, not just a different target. If you can't say which one you'd edit next month, merge them. Keep skills in version control so every rule change is visible.

---

## 8. Prove the rule works

A skill isn't finished when it's saved; it's finished when you've seen its rules change a result. Run at least these inputs, before and after the change:

| Input | Example (expense skill) | What it tests | If it fails, fix… |
|---|---|---|---|
| **Typical** | A normal report with receipts, under all limits | Output format and done criteria | The Output section |
| **Missing / edge** | A line with no amount | That it asks or reports instead of guessing | The Exceptions section |
| **Rule trigger** | $480 dinner for 6, no event code | That *your rule* fires and visibly changes the result | The rule's condition or action |
| **Should not trigger** | A request unrelated to expenses | That the skill stays out of the way | The description |

The rule-trigger input matters most: take a case the format-only version got wrong (often your "last time this went wrong" story) and confirm the new rule fixes it.

**Change one rule at a time** and rerun the same inputs. If you change three rules and the result changes, you won't know which rule did it. When a result surprises you, write one sentence: "If I had handled this myself, I would have…", turn it into a condition → action → exception rule, and add it. For larger skills, keep the inputs as a small eval set and rerun it after every change ([docs/08](08-verification-and-evals.md), [evals/](../evals/README.md)). Verifying whole agent runs, including silent failures and change logs: [docs/13](13-verifying-agent-runs.md).

---

## 9. Checklist

- [ ] Without the tone and format lines, at least one rule that changes the result remains.
- [ ] Every rule has an observable condition ("when…"), a specific action, and an exception where needed.
- [ ] You've seen each key rule change a test result.
- [ ] Missing information, ambiguous cases and irreversible actions each have an explicit path.
- [ ] The name and description say what the skill does and when; they don't overlap your other skills.
- [ ] Someone new could read the rules and reach the same decisions you would.
- [ ] Policy-based rules cite their source; experience-based thresholds are marked provisional.

---

### Sources
- Anthropic, Agent Skills best practices (concise bodies, third-person descriptions, examples, evaluation) — https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
- Agent Skills specification — https://agentskills.io/specification
- Agent Skills, optimizing descriptions — https://agentskills.io/skill-creation/optimizing-descriptions
- Claude Code best practices (rules followed most of the time vs. hard controls; checks the agent can run) — https://code.claude.com/docs/en/best-practices
- Anthropic, Demystifying evals for AI agents (start from real failures; grade outcomes) — https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- Hamel Husain & Shreya Shankar, LLM Evals FAQ (error analysis first; binary checks) — https://hamel.dev/blog/posts/evals-faq/
- Anthropic, Prompting best practices (explain the reason behind a rule; use examples) — https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
