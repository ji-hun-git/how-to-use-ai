---
name: clarify-first
description: Prevents misunderstanding before work starts. Use when a request is ambiguous, underspecified, large, or multi-step (for example "build a dashboard", "write the report", "refactor this module"), or when the user's goal, audience, scope or definition of done is unclear. Asks at most three targeted questions with defaults, then restates the goal and done criteria. Skip it when the request is already clear.
license: MIT
---

# Clarify first

Models rarely notice ambiguity on their own, and they tend to lock in early assumptions. A few targeted questions before starting are cheaper than redoing the work.

## Steps

1. **Decide whether to ask.** Ask only if a wrong guess would change the result in a way that matters (goal, audience, scope, format, constraints, data source). If the request is clear, skip to step 3.
2. **Ask at most three questions**, the ones with the biggest impact on the result. For each, give a default:
   > 1. Who will read this? *(Default: non-technical managers.)*
   > 2. ...
   > If you don't answer, I'll go with the defaults.
3. **Restate the task** in two or three lines before doing it:
   - Goal: what the result is for
   - Deliverable: what you will produce, in what format
   - Done when: how the user will judge it finished
   - Not doing: anything you are deliberately leaving out
4. **Surface assumptions.** If you proceed on defaults, list the assumptions at the top of your answer and mark with ⚠️ any that would change the result significantly if wrong.

## If the conversation has drifted

When requirements have piled up over many turns and the output keeps missing, stop patching. Consolidate every requirement and decision so far into one prompt and suggest the user start a fresh chat with it.

## Don't

- Don't ask about things you can find out yourself by reading the files, docs or data you have access to.
- Don't ask more than three questions, and don't ask when the answer wouldn't change what you do.

## Evidence

- Selective clarification (asking only on the most uncertain cases) doubled the gain compared with asking at random: Zhang & Choi, 2023 — https://arxiv.org/abs/2311.09469
- Models are poor at noticing ambiguity unaided: CLAMBER, 2024 — https://arxiv.org/abs/2405.12063
- Spreading requirements over several turns cut performance by 39% on average; consolidating and restarting helps: Laban et al., ICLR 2026 — https://arxiv.org/abs/2505.06120
- More in the guide: https://github.com/ji-hun-git/how-to-use-ai/blob/main/docs/04-failure-modes.md#1-misunderstanding
