# Snippets to prevent misunderstanding (Clarify First)

> **Misunderstanding**: the AI interprets your request differently and builds a plausible answer on that interpretation.
> Causes and evidence are covered in [docs/04-failure-modes.md](../docs/04-failure-modes.md#1-misunderstanding).

AI often doesn't notice on its own that a request is ambiguous, and it tends to stick with assumptions it made early on. That's why checking its understanding **before you get the answer** is the cheapest fix.

---

## A. Get questions first

```text
Before you start, ask me up to 3 questions about information I haven't given you that would most affect the result.
For each question, also state a default: "If you don't answer, I'll assume ___."
```

> With defaults included, when you're busy you can move on with one line: "Go with the defaults."

## B. Have it restate its understanding

```text
Before answering, restate my request in your own words in 2–3 sentences.
- Goal:
- Deliverable:
- What you won't do:
Start only after I say "Correct."
```

## C. Make it surface its assumptions

```text
At the very top of your answer, list the assumptions you made as bullets.
Mark with ⚠️ any assumption that would change the result significantly if it were wrong.
```

## D. When the conversation gets tangled: consolidate, then start a new chat

Adding requirements bit by bit over many turns causes a large drop in performance. In one study (Laban et al., 2025; published at ICLR 2026), performance fell by an average of 39% when the same request was split across multiple turns.

```text
Consolidate every requirement and decision I've given so far into a single prompt, leaving nothing out.
(Make it something I can paste straight into a new chat.)
```

→ Paste the consolidated prompt into a **new chat** and start over.

## E. The colleague test (self-check before sending)

> If you sent this prompt as-is to **a colleague with no background knowledge**, could they produce the result you want without asking any follow-up questions?

This is a check Anthropic recommends. If the answer is "no," you're missing context.
