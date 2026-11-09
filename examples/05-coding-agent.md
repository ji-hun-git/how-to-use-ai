# Example 5. Fixing a bug with a coding agent: explore → plan → test → implement → verify

> Coding agents like Claude Code and Codex read files, run commands, and modify code.
> Because they're powerful, **when they head in the wrong direction, they get somewhere wrong fast.** The key is to break the work into short steps and, at each step, give **the agent a way to check its own work**.

**Situation:** In an online store's shopping cart, applying a discount coupon twice makes the total negative.

---

## Step 1. Explore (no code changes)

```text
Don't modify any code yet.
Find where the cart total calculation and the coupon logic live, and summarize the flow.
Also tell me whether there are related test files.
```

> If your tool has a Plan mode, run this in Plan mode.

## Step 2. Plan (a human approves)

```text
Make a plan to fix the duplicate-coupon bug.
- Hypotheses for the cause (up to 2), with the code locations that support each one
- List of files to modify
- Risk of affecting other features
- How you'll verify the fix
```

👀 **Your job:** Check that the cause hypotheses are plausible and that the scope of the changes isn't too broad. Setting the direction at this stage is far cheaper than rolling back later.

## Step 3. Failing test first (Red)

```text
Go ahead with the plan. First write a test that reproduces this bug,
then run it and show me that it actually fails. Don't write the fix yet.
```

> A test is **a standard the agent can check itself against**. Claude Code's official guide names giving the agent ways to check its own work, such as tests, screenshots, and expected outputs, as one of the most effective things you can do.

## Step 4. Implement (Green)

```text
Now make the minimal change needed for the test to pass.
- Don't modify the test code
- Rerun all related tests and confirm that no existing tests broke
```

## Step 5. Verify and report

```text
Summarize the changes.
- What you changed and why
- Tests you ran and their results
- What you couldn't verify, and remaining risks
```

👀 **Your job:** You should be able to say **how you confirmed** that this change is correct. Look at the test results and the execution evidence, and for core parts where a mistake is costly, like money calculations, read the diff yourself. "Opening a PR with AI code you haven't checked" is one of the anti-patterns Simon Willison highlights. (By 2026, even Willison no longer reads every line, but in its place he emphasizes **verifying with evidence** → [07. AI coding](../docs/07-ai-coding.md#what-changed-in-2026-from-reading-every-line-to-verifying-with-evidence))

> With 2026 tools: you can set a `/goal` of "all cart tests pass + the negative-total reproduction test passes," or get an independent review from a fresh subagent with `/code-review` before you finish.

## Step 6. Commit

```text
Suggest a commit message in the Conventional Commits format, then commit.
```

---

## When you're stuck

| Symptom | What to do |
|---|---|
| Still failing after asking for the same fix twice | Reset the conversation (/clear) and start over with a new prompt that includes what you've learned so far |
| It made the tests pass by changing the tests | State "do not modify test code," and if possible block it with permission settings or hooks |
| It modifies unrelated files | Add to the constraints: "Scope of changes: only within `src/cart/`" |
| The conversation got long and it forgets instructions | A sign of context rot. Summarize and start a new session |

---

## Put recurring mistakes in AGENTS.md / CLAUDE.md

When the agent makes the same mistake twice, add a line to the project memory file.

```markdown
## Common mistakes
- For money calculations, use the `Money` class instead of float (because of rounding errors)
```

→ Template: [templates/AGENTS.template.md](../templates/AGENTS.template.md)
