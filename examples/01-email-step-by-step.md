# Example 1. Work email: adding one element at a time

> This example shows how the result changes as you add **Context → Format → Constraints → Examples** to the same request, one at a time.
> The "Expected result" notes below are not verbatim model outputs; they describe what typically comes out at each stage.

---

## v0. One-line request

```text
Write an email about a schedule delay.
```

**Expected result:** A harmless but useless template that opens with something like "Hello, I'm writing regarding the project schedule…". Who it's for, why, and how long the delay is all come out as `[ ]` blanks.

**Problem:** The AI doesn't know your situation. → **Misunderstanding** and **fabrication** (inventing a reason for the delay) happen together.

---

## v1. + Context (to whom, why, what)

```text
Write an email to my manager about a schedule delay.
- Project: customer portal redesign; original deadline 11/20 → 11/27, a one-week delay
- Reason: the payment provider still hasn't approved our API access (not a problem on our side)
- Alternative: we could launch on 11/20 without the payment feature
- My manager likes to hear the bottom line first
```

**Expected result:** The content is now accurate, but the greeting and apology may run long, and the bottom line may not show up until the third paragraph.

---

## v2. + Format (structure, length)

```text
(v1 content) +
Format:
- One-line subject
- Body of 5 sentences or fewer: ① bottom line ② reason ③ alternative ④ what I need from you (a decision) ⑤ closing
```

**Expected result:** The bottom line comes in the first sentence, and the email takes 20 seconds to read.

---

## v3. + Constraints (rules to follow)

```text
(v2 content) +
Constraints:
- Don't make it sound like we're blaming the payment provider; state the facts calmly
- Apologize only once
- Make the options clear so my manager can pick Option A or Option B today
```

**Expected result:** The tone steadies, and it becomes clear **what the recipient needs to decide**.

---

## v4. + Examples (your voice)

```text
(v3 content) +
Below is an email I'd typically write. Match its tone and length. (Don't use its content.)
<example>
Bottom line first: I think we should push the deployment to tomorrow morning.
QA found one payment error; we'll fix it tonight and re-verify.
Could you confirm whether we can go ahead with a 10 a.m. deployment?
</example>
```

**Expected result:** An email that "sounds like you wrote it."

> 💡 If you give **only one** example, the model sometimes copies even its sentence structure. Tell it what to imitate, as in "match the tone only, not the content," or give 2–3 examples.

---

## Summary

| Stage | Element added | Problem it prevented |
|---|---|---|
| v1 | Context | Misunderstanding, fabrication (no invented reasons or dates) |
| v2 | Format | Back-and-forth asking for rewrites |
| v3 | Constraints | Tone mishaps, leaving out the decision you need |
| v4 | Examples | That "written by AI" feel |

> This is a two-minute investment. In return, you save ten minutes of fixing the email.
