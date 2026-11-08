---
name: grounded-answer
description: Prevents fabrication (hallucination) when answering from documents or facts. Use when answering questions about provided files, PDFs, transcripts, contracts or data; when summarizing sources; when the user asks for citations, statistics, quotes, references or "facts"; or whenever accuracy matters more than fluency. Quotes evidence first, cites every claim, marks unknowns, and removes unsupported claims.
license: MIT
---

# Grounded answer

Models hallucinate partly because training and evaluation reward confident guessing over "I don't know". Counter that explicitly: ground every claim in evidence and make abstaining acceptable.

## Steps

1. **Collect evidence first.** From the provided material (or from sources you actually retrieved with a search tool), extract the passages that bear on the question. Quote them word for word, numbered, with their location:
   > [1] "…" (report.pdf, p. 12)
2. **Answer only from the evidence.** Attach a citation like [1] to every factual claim. If you add general knowledge, label it *[general knowledge]*.
3. **Say what's missing.** If the material doesn't answer part of the question, write "Not in the provided material" for that part. Don't fill gaps with plausible guesses.
4. **Retract what you can't support.** Re-read your draft; for each claim, check that a quoted passage supports it. Delete any claim without support and note *[removed: unsupported]*.
5. **Flag confidence.** Where it helps, tag claims as *[from source]*, *[from memory, unverified]* or *[inference]*.

## Citations and references

- Only cite sources you actually opened in this session. Never construct a URL, DOI, case name, page number or quote from memory.
- If you can't verify that a source exists and says what you claim, say so instead of citing it.

## Numbers

- Compute totals, percentages and statistics by running code, and show the code.

## Evidence

- Why models guess instead of abstaining: Kalai et al. (OpenAI), 2025 — https://arxiv.org/abs/2509.04664
- Allow "I don't know", extract quotes first, cite or retract: Anthropic, Reduce hallucinations — https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations
- 2026-released models still fabricated references in 35% of responses (preprint): Topaz et al., 2026 — https://arxiv.org/abs/2609.14988
- AI-fabricated citations in court filings: 2,266 cases as of 2026-11-05 — https://www.damiencharlotin.com/hallucinations/
- More in the guide: https://github.com/ji-hun-git/how-to-use-ai/blob/main/docs/04-failure-modes.md#3-fabrication-hallucination
