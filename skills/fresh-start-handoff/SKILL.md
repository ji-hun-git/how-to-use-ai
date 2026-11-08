---
name: fresh-start-handoff
description: Writes a complete handoff so work can continue in a fresh chat or session. Use when a conversation has become long, the assistant keeps repeating the same mistake, requirements were added piecemeal over many turns, the user says the chat is "going in circles", the topic changes, or the user asks for a summary to continue elsewhere. Consolidates goals, decisions, constraints, progress and open questions into one paste-ready prompt.
license: MIT
---

# Fresh-start handoff

Long, patched-up conversations degrade: models lock in early assumptions, errors compound over later turns, and they give in more to pushback as conversations grow. Restarting with one consolidated prompt is the evidence-backed fix.

## When to suggest it

- The same correction has been made twice and the problem persists.
- Requirements arrived in pieces across many turns.
- The topic has changed, or the context is full of material that no longer matters.
- The conversation has turned into a back-and-forth argument about whether an answer is right.

## Steps

1. **Collect** everything that should survive, from the whole conversation (not just the last few turns).
2. **Write the handoff** as a single prompt in a code block:

   ```markdown
   ## Goal
   ## Context (audience, background, source material to re-attach)
   ## Requirements (numbered, final versions only)
   ## Decisions made (and why)
   ## Constraints and preferences
   ## Progress so far (what is done, with file names/links)
   ## Known pitfalls (approaches that failed and why)
   ## Open questions
   ## Next step
   ```

3. **Resolve, don't copy, history.** Where a requirement changed over the conversation, keep only the final version. Don't carry over discarded drafts or the argument itself.
4. **Flag gaps.** List anything you're unsure was decided, so the user can confirm before pasting.
5. **Tell the user** to open a new chat or run `/clear`, paste the handoff, and re-attach the listed source files.

## Evidence

- Requirements spread across turns cut performance by 39% on average; consolidating and restarting is the recommended fix: Laban et al., ICLR 2026 — https://arxiv.org/abs/2505.06120
- Hallucination errors compound in later turns (preprint): HalluHard, 2026 — https://arxiv.org/abs/2602.01031
- Sycophantic collapse rises from 0–57% within 5 turns to 20–97% within 25 turns (preprint): SPINE, 2026 — https://arxiv.org/abs/2609.09090
- After two failed corrections, clear and start over with a better prompt: Claude Code best practices — https://code.claude.com/docs/en/best-practices
- More in the guide: https://github.com/ji-hun-git/how-to-use-ai/blob/main/docs/06-workflows.md
