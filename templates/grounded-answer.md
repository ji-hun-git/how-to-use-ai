# Snippets to prevent fabrication (Grounded Answer)

> **Fabrication (hallucination)**: plausibly inventing facts, numbers, quotes, papers, court cases, or code functions that don't exist.
> Causes and evidence are covered in [docs/04-failure-modes.md](../docs/04-failure-modes.md#3-fabrication-hallucination).

One root cause of fabrication is that training and evaluation reward **guessing** more than saying "I don't know" (OpenAI, 2025). So you need to explicitly give the model **permission to say it doesn't know**, and make it **ground its answers in sources**.

---

## A. Give it permission to say "I don't know"

```text
If you're not sure about something or have no basis for it, don't guess. Write "I don't know" or "needs checking."
"I don't know" is much better than a wrong answer.
```

## B. Ground answers only in the provided material

```xml
<documents> ... </documents>

Answer using only what is in <documents>.
If you need something that isn't in the material, mark it "not in the documents." When you supplement with general knowledge, label it [general knowledge].
```

## C. Quotes first, then the answer

```text
1) Copy the source sentences relevant to the question word for word into <quotes>. (Number them.)
2) In <answer>, end each claim with the number of the quote that supports it, like [1], [2].
3) Delete any claim that isn't supported by a quote.
```

This is the method recommended in Anthropic's official documentation. The key is making the model **retract on its own** any claim it can't find support for.

## D. Require sources, then check them yourself

```text
Attach a source (URL or bibliographic details) to every factual claim.
If you can't actually verify a source, write "source unverified" next to that claim.
```

> ⚠️ The sources the AI provides may themselves be fabricated. In one 2023 study, 55% of the references cited by GPT-3.5 and 18% of those cited by GPT-4 did not actually exist. **Open the links yourself.** Asking with search turned on is much safer.

## E. Chain-of-Verification

```text
Step 1: List the claims in the answer above that need fact-checking.
Step 2: Write a verification question for each claim.
Step 3: Answer each verification question independently, without looking at the original answer.
Step 4: Find where the results differ and correct the original answer.
```

> The most reliable approach is to run this four-step verification in **a new chat or with a different model**.

## F. Use code for numbers and calculations

```text
Don't do calculations in your head. Run code (Python) to do them, and show me the code you used.
```

## G. Ask the same question several times (self-consistency)

Ask important questions again 2–3 times in new chats. If the answer is different each time, that part is likely something the AI **doesn't know**.
