---
name: fresh-eyes-review
description: Reviews finished work as an independent reviewer who did not produce it. Use after drafting a document, plan, analysis or code change and before declaring it done; when the user asks for a final check, a second opinion or a review against a spec; or when the same session wrote the work and is about to grade it. Checks the result against the original requirements and evidence only, not against the conversation that produced it.
license: MIT
---

# Fresh-eyes review

Agents grading their own work skew positive, and a reviewer that watched the work being made inherits its blind spots. Separate the maker from the checker.

## Steps

1. **Start clean.** If you can, run this review in a new session or a subagent that has not seen the drafting conversation. If you can't, explicitly set aside the conversation and work only from the inputs below.
2. **Gather only:**
   - the original request or spec (requirements, done criteria),
   - the final artifact (document, diff, data output),
   - the evidence (sources, test output, data).
3. **Check requirement by requirement.** For each requirement or done criterion: met / partly met / not met, with the specific evidence (line, section, test output).
4. **Check correctness, not style.** Look for factual errors, unsupported claims, broken logic, failing or missing checks, security issues and scope creep. Skip style preferences unless the spec asks for them.
5. **Report only what matters.** List issues that would make the work wrong, unsafe or incomplete, each with a fix. If nothing significant is wrong, say "No significant issues" rather than inventing minor ones.
6. **Hand back** the findings; let the original author (or the user) decide on fixes.

## Evidence

- Agents reliably skew positive when grading their own work; separate generator and evaluator: Anthropic, Harness design for long-running apps (2026) — https://www.anthropic.com/research/harness-design-long-running-apps
- A fresh reviewer helps more than delegating the same task; review against the spec, report only correctness gaps: Claude Code best practices — https://code.claude.com/docs/en/best-practices
- Answer verification questions independently so the draft can't bias them: Chain-of-Verification — https://arxiv.org/abs/2309.11495
- More in the guide: https://github.com/ji-hun-git/how-to-use-ai/blob/main/docs/08-verification-and-evals.md
