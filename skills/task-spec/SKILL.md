---
name: task-spec
description: Writes a clear task specification before delegating work to a coding agent or starting a non-trivial change. Use when the user describes a feature, bug, refactor or automation loosely; before long-running or unattended agent work; or when the user asks for a spec, plan, ticket, goal or "done when" criteria. Produces Goal / Context / Constraints / Done when, with a verifiable check.
license: MIT
---

# Task spec

Most disappointing agent sessions trace back to missing information, no way for the agent to check its own work, or rules nothing enforces. A short spec fixes the first two.

## Steps

1. **Gather facts, but don't stall.** If you can read the code, docs or data, read the relevant parts first so the spec refers to real files and behavior (don't change anything yet). If you can't access them, or the user only wants the instructions written, write the spec now from what you were told: put unknowns in angle brackets (`<file?>`, `<current p95 latency?>`) and list the questions or measurements needed to fill them.
2. **Write the spec:**

   ```markdown
   ## Goal
   What changes and why, in one or two sentences.

   ## Context
   - Relevant files: ...
   - Current behavior / symptom (exact error, reproduction steps): ...
   - Existing pattern to follow: ...

   ## Constraints
   - Out of scope / don't touch: ...
   - No new dependencies without asking.

   ## Done when
   - [ ] A check that can be run and returns pass/fail (test, build, script, screenshot comparison)
   - [ ] ...
   - [ ] Report: what changed, the commands run and their output, remaining risks
   ```

3. **Make "done" verifiable.** Every item under *Done when* should be checkable by running something, not by opinion. For bugs, the first item is a failing test that reproduces the bug (red), which must pass afterwards (green).
4. **Size the process to the task.** A small bug needs a paragraph; a large feature may need a plan the user approves before any code is written.
5. **Move non-negotiable rules out of prose.** If a rule must never be broken (don't read `.env`, don't touch `migrations/`), recommend enforcing it with permission rules, hooks or CI rather than the spec alone.

## Evidence

- Goal / Context / Constraints / Done when: OpenAI Codex best practices — https://learn.chatgpt.com/guides/best-practices
- Four causes of disappointing sessions; give the agent a check it can run; deterministic vs non-deterministic controls: Claude Code best practices — https://code.claude.com/docs/en/best-practices
- Goals should state outcome, constraints and verification: OpenAI Codex long-running work — https://learn.chatgpt.com/docs/long-running-work
- Red/green TDD with agents: Simon Willison — https://simonwillison.net/guides/agentic-engineering-patterns/red-green-tdd/
- More in the guide: https://github.com/ji-hun-git/how-to-use-ai/blob/main/docs/07-ai-coding.md
