# Snippets to prevent sycophancy (Honest Critique)

> **Sycophancy**: going along with the user's opinion, or reversing even a correct answer when the user pushes back.
> Evidence is covered in [docs/04-failure-modes.md](../docs/04-failure-modes.md#4-bonus-sycophancy).

Research found that when asked "Are you sure?", models changed their answer 46% of the time, and accuracy actually dropped by 17% (FlipFlop, 2023). **Asking again is not verification.**

---

## A. Don't say it's yours (third-party framing)

```text
Below is a proposal submitted by another team. From the point of view of an investment reviewer, find its 3 weakest points.
```

> If you ask "I wrote this, what do you think?", you're likely to get praise first.

## B. Assign it the opposing side

```text
You are on the side opposing this argument. Give the 3 strongest counterarguments, with supporting evidence.
Then assess which of those counterarguments is actually fatal.
```

## C. Set the evaluation criteria first

```text
First, create 5 criteria for evaluating a good ___.
Then score my draft 1–5 on each criterion, and give concrete improvements for any item scored 3 or lower.
```

## D. Ask for evidence instead of asking again

```text
❌ "Are you sure?"
✅ "List the facts that support that conclusion, and mark which of them are unverified."
✅ "If this answer were wrong, what would be the most likely reason?"
```

## E. Get feedback without the praise

```text
Skip the praise and pleasantries; list only the problems and how to fix them.
If there are no problems, it's fine to just write "No problems."
```

> The last sentence matters. If you tell it that it **must** find problems, it may invent problems that aren't there.
