# Agent test plan template

> Fill this in **before** you run your agent, rerun it after every change, and keep it next to the agent's instructions or skill.
> Why each part is there: [docs/13. Verifying agent runs](../docs/13-verifying-agent-runs.md).

---

## 1. Required steps

List every step a correct run must include, so you can tick them off against the run log.

| # | Step | Evidence in the run log |
|---|---|---|
| 1 | Read the input with `<tool>` | Tool returned non-empty data |
| 2 | Apply rule `<n>` | Decision visible in output |
| 3 | Compute `<x>` with code | Code and result shown |
| 4 | Ask for approval before `<send/save/pay>` | Approval prompt appeared |

## 2. Test cases (write before running)

```markdown
### Case A — typical
Input: <exact request or test file>
Must include: <labels, numbers from tool results, sources, sections>
Must not include: <unverified sources, sample values from the instructions, numbers not in the data, actions without approval>

### Case B — missing or ambiguous
Input: <same as A but with a required field removed, or an input that fits no rule cleanly>
Must include: <a request for the missing item, or a "needs confirmation" flag with the options>
Must not include: <any guessed value for the missing item>

### Case C — key rule
Input: <a case a plain summary/search gets wrong, ideally one that failed before>
Must include: <the result your rule should produce>
Must not include: <the wrong result you saw before>
```

**Plant a unique value** (a distinctive name, ID or date) in each test input and check it appears in the output. That catches leftover example text.

**Run each case twice.** Key decisions and required items should match across runs.

## 3. Results

| Date | Change made | Case A | Case B | Case C | Same result on rerun? | Notes |
|---|---|---|---|---|---|---|
| | (baseline) | | | | | |
| | | | | | | |

## 4. Change log

```markdown
### <date> — <short title>
Observed: <input used, what went wrong or what limitation appeared>
Diagnosis: <which step/setting caused it, and why you think so>
Change and result: <what you changed; what happened when you reran the same cases>
```

## 5. Measuring the benefit

| | Current way | With the agent (including review time) |
|---|---|---|
| Time for the same inputs | | |
| Items processed | | |
| Errors or omissions found | | |
| Rubric score (rubric written in advance; scored by someone else if possible) | | |
