---
name: verify-claims
description: Fact-checks a draft, answer, report or AI-generated text before it is used or published. Use when the user asks to check, verify or fact-check something; before finalizing anything with facts, numbers, quotes or citations; or for high-stakes content (legal, medical, financial, public). Splits text into atomic claims, checks each independently against sources, and reports what holds up.
license: MIT
---

# Verify claims

Asking a model "are you sure?" is not verification; it makes models flip correct answers. Check claims one by one, independently, against evidence outside the draft.

## Steps

1. **Split into atomic claims.** List every checkable statement in the text, one fact per line, numbered (names, dates, numbers, quotes, causal claims, citations).
2. **Plan a check for each.** Write a verification question per claim ("Was X founded in 2019?").
3. **Answer the questions independently.** Answer each verification question without relying on the draft's wording. Use the provided sources, files, a search tool, or code (for arithmetic). Open every cited link or file; check that it exists *and* says what the draft claims.
4. **Report a verdict table:**

   | # | Claim | Verdict (✅ supported / ❌ contradicted / ❓ unverified) | Evidence |
   |---|---|---|---|

5. **Fix the draft.** Propose corrected wording for ❌ items and either remove ❓ items or mark them as unverified.

## Scale the effort to the stakes

- Low (brainstorms, drafts): check the claims that look most specific (numbers, names, dates).
- Medium (work documents): check every number and every citation.
- High (legal, medical, financial, published): check every claim, read laterally (confirm with independent sources), recompute every number, and never accept the same model's agreement as proof.

## Evidence

- Chain-of-Verification: plan questions, answer them independently, revise: Dhuliawala et al., 2023 — https://arxiv.org/abs/2309.11495
- Atomic-fact checking for long text: FActScore, 2023 — https://arxiv.org/abs/2305.14251
- "Are you sure?" made models flip answers 46% of the time (2023 study): FlipFlop — https://arxiv.org/abs/2311.08596
- Even real citations often don't support the claim: Walters & Wilder, 2023 — https://www.nature.com/articles/s41598-023-41032-5
- More in the guide: https://github.com/ji-hun-git/how-to-use-ai/blob/main/docs/08-verification-and-evals.md
