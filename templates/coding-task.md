# Coding agent task template

> A template for handing work to coding agents such as Claude Code, Codex, Gemini CLI, and Cursor.
> The four-part structure of **Goal, Context, Constraints, Done when** is the format recommended by OpenAI's Codex guide, while "plan first" and "give it a way to verify" are central to Anthropic's Claude Code guide.
> For details, see [docs/07-ai-coding.md](../docs/07-ai-coding.md).

---

## Basic template

```markdown
## Goal
What to change and why, in one or two sentences.

## Context
- Relevant files/folders: @src/auth/login.ts, @tests/auth/
- Current symptom (if it's a bug): steps to reproduce, exact error message
- Existing pattern to follow: same approach as @src/auth/signup.ts

## Constraints
- Do not touch: public API signatures, DB schema
- Do not add new libraries (ask first if you need one)
- Follow the existing code style and error-handling approach

## Done when
- [ ] `npm test -- auth` passes
- [ ] Following the reproduction steps no longer produces the error
- [ ] You report a summary of the changes and any remaining risks
```

---

## Bad → good

| ❌ Vague instruction | ✅ Specific instruction |
|---|---|
| Fix the login bug | Logging in after a session expires returns a 500 error. Check the token refresh logic in `src/auth/`, write a failing test that reproduces this bug first, then fix it. |
| Add tests | Add tests for `parseDate` in `utils/date.ts` covering leap years, empty strings, and time zone boundary cases. Don't use mocks. |
| Build a dashboard | Build a sales dashboard. Don't stop at the basics: make it a polished version with filters, period-over-period comparison, and empty-state screens. |

---

## Big tasks: get a plan first

```text
Don't modify any code yet.
1) Read the relevant code and summarize the current structure.
2) Propose a step-by-step plan for the change. (Include the files to modify, risks, and how to test.)
3) Implement it only after I approve.
```

> Most coding agents have a **Plan mode**. In Plan mode the agent only reads; it doesn't make changes.

## Bug fixes: test first (Red → Green)

```text
1) First write a test that reproduces this bug, and confirm that it fails. (Red)
2) Then make the minimal change needed for the test to pass. (Green)
3) Don't modify the test code.
```

## When two fixes haven't worked

If you've asked for the same problem to be fixed twice and it still isn't working, don't keep the conversation going. **Reset the conversation (/clear) or open a new session**, then start again with a better first prompt that reflects what you've learned so far. This is what Claude Code's official guide recommends.
