---
name: coverage-check
description: Prevents omissions when a task has many requirements or long inputs/outputs. Use when the user gives a list of requirements or constraints, asks to process a long document, transcript or dataset, asks for a long report or translation, or asks to confirm nothing was missed. Numbers the requirements, works section by section, and ends with a coverage table.
license: MIT
---

# Coverage check

The more requirements a task has, the less likely all of them are met, and the longer the input, the less reliably all of it is used. Make coverage explicit instead of hoping for it.

## Steps

1. **Number the requirements.** Rewrite the user's requirements as R1, R2, R3 … (keep their wording). If there are more than about five hard constraints, propose splitting the work into stages.
2. **Long input:** before answering, extract the passages relevant to each requirement (quote them word for word, with location). Go through the whole input, start to end, including the middle.
3. **Long output:** produce an outline first, then write one section at a time. Don't compress the end of a long output into "…and so on".
4. **Finish with a coverage table:**

   | Req | Status (✅ done / ⚠️ partial / ❌ not done) | Where | Note |
   |---|---|---|---|

5. **Report gaps honestly.** List anything skipped, shortened or uncertain, and anything you added that wasn't asked for.

## Don't

- Don't mark a requirement ✅ unless the output actually satisfies it.
- Don't silently drop a requirement because it conflicts with another; flag the conflict and ask which wins.

## Evidence

- Success at meeting every instruction falls as instructions are added; earlier instructions are favored: IFScale, 2025 — https://arxiv.org/abs/2507.11538
- Reliable compliance breaks down beyond about 5–6 simultaneous constraints (preprint): Vasileva, 2026 — https://arxiv.org/abs/2608.12426
- Information in the middle of long inputs is used worst: Liu et al., "Lost in the Middle" — https://arxiv.org/abs/2307.03172
- Splitting long outputs into planned sections fixes truncation: LongWriter, 2024 — https://arxiv.org/abs/2408.07055
- More in the guide: https://github.com/ji-hun-git/how-to-use-ai/blob/main/docs/04-failure-modes.md#2-omission
