# Skill template (with decision rules)

> Copy the block below into `<skill-name>/SKILL.md`, fill it in, and delete the comments. The folder name must match `name`.
> Why each part is there: [docs/12. Writing decision rules](../docs/12-writing-decision-rules.md). Format rules: [Agent Skills specification](https://agentskills.io/specification).

```markdown
---
name: your-skill-name
description: <What it does, in the third person.> Use when <the situations and words that should trigger it>. <Optional: when NOT to use it.>
---

# <Skill title>

<One or two sentences: the job this skill does and why it matters.>

## Before you start
<!-- What to check in the input before doing anything: required fields, files, IDs. -->
- Check that <required input> is present. If not, see Exceptions.

## Rules (apply in order)
<!-- Each rule: When <observable condition>, do <specific action>. Unless <exception>, in which case <alternative>. (Source) -->
1. When <condition>, <action>. Unless <exception>, in which case <alternative>. (Source: <policy> / experience, provisional)
2. When <condition>, <action>.
3. ...

## Exceptions
<!-- Cover all three. -->
- Missing information: <what to ask for or report; never guess>.
- Ambiguous case: <list the candidate options and the reason; mark "needs confirmation">.
- Irreversible or high-impact action: <prepare only; mark "needs approval"; never send/pay/delete/commit on your own>.

## Output
<!-- Structure, what goes first, done criteria, and one or two example lines. -->
- First line: <the decision or key fact>.
- Then: <table / bullets / sections>.
- Done when: <what must be true>.
- Example: "<one realistic example line>"

## Never
- <Things that must never happen, whatever the input.>
- Don't state facts, numbers or policies that aren't in the input or the rules above.
```

## Test before you trust it

Run these four inputs and confirm each behaves as expected. Change one rule at a time and rerun.

| Input | Expected |
|---|---|
| Typical case | Output format and done criteria are met |
| Missing information | It asks or reports the gap instead of guessing |
| Case that triggers your key rule | The rule visibly changes the result |
| Unrelated request | The skill doesn't activate |

## Checklist

- [ ] Remove tone/format lines: does at least one result-changing rule remain?
- [ ] Each rule starts with an observable "When…" condition.
- [ ] All three exception types are covered.
- [ ] The description says what it does and when, and doesn't overlap other skills.
- [ ] Policy rules cite a source; guessed thresholds are marked provisional.
