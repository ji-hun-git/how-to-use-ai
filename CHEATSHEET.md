# AI Cheatsheet (one-page summary)

> Print it and keep it next to your monitor. For details, start with the [README](README.md).

---

## ✍️ Instruct: the six elements

| | Question | One-line tip |
|---|---|---|
| **Role** | From what perspective, in what tone? | Doesn't improve accuracy. Use it for tone and reader level |
| **Context** ★ | Why? For whom? In what situation? | **Most important.** State the purpose and the reason, and the AI can adapt on its own |
| **Instruction** ★ | What? When is it done? | Write done criteria. If you want more than the default, say so explicitly |
| **Format** ★ | What should the output look like? | Set the structure and length. Say "do this" instead of "don't do that" |
| **Constraints** | What rules must be followed? | The fewer, the better they're followed. Instead of ALL CAPS or "NEVER!!!", add a one-line reason |
| **Examples** | What does a good result look like? | 3–5, varied, wrapped in tags. With reasoning models, try without examples first |

**Placement:** long material at the **top**, the question at the **very bottom** · separate material and instructions with `<tags>`

**All-purpose line:** `If you're not sure about something, mark it "needs verification," and if anything is ambiguous, ask me up to 3 questions first.`

---

## 🚨 Diagnose failures: Misunderstanding · Omission · Fabrication

| Symptom | Diagnosis | Fix |
|---|---|---|
| A plausible answer that goes in the wrong direction | **Misunderstanding** | Add goal, audience, and done criteria / "Restate my request" / if the chat gets tangled, **summarize and start a fresh chat** |
| Requirements dropped, middle content missing | **Omission** | Number the requirements + coverage table / quote the relevant passages first / split the work |
| Facts, numbers, or sources that don't exist | **Fabrication (hallucination)** | "If you don't know, say so" / use only the provided material / delete anything it can't quote / **open the sources yourself** |
| Agrees with whatever you say, flips when you push back | **Sycophancy** | Don't say it's your work / don't ask in the form "I believe X" / ask for weaknesses first / **no "Really?"** → have it re-solve in a fresh chat (sycophancy grows as conversations get longer) |

---

## 🔁 The working loop

```
Specify → Plan → Execute → Verify → Learn
(goal, context, constraints, done criteria)  (approve the plan for big jobs)  (with a way to check)  (with outside evidence)  (recurring mistakes go into templates)
```

---

## ✅ Verification ladder

| Risk | Minimum verification |
|---|---|
| Low (ideas, drafts) | Skim + "Which parts are you unsure about?" |
| Medium (internal documents, code review) | + coverage table + check against quotes + second opinion in a fresh chat |
| High (legal, medical, financial, public release, deployment) | + **open every source** + recalculate the numbers + run the tests + cross-check against other sources |

---

## 🧠 Habits to drop in 2026

- ❌ "Think step by step" (reasoning models) → use the reasoning effort setting
- ❌ "I'll tip you," "Something terrible happens if you don't" → no effect
- ❌ "You're the world's best expert" → no effect on accuracy
- ❌ Overusing ALL CAPS and "NEVER!!!" → the newest models overreact
- ❌ "Are you really sure?" → flips correct answers
- ❌ Doing everything in one chat → start a fresh chat when the topic changes

---

## 🔒 Safety

- Never put in passwords, keys, personal data, or confidential information (use only company-approved tools)
- **The lethal trifecta:** private data + untrusted input + sending data out → remove one of the three
- A **human approves** sending, deleting, paying, and deploying
- Don't ship code or documents if you can't answer "What did you verify it with?"

---

## 🆕 Things to remember in 2026

- Even the newest models **still fabricate references** (35% even for models released in 2026) → keep opening sources yourself
- 1M-token context: **retrieval works, but synthesis is weak** → include only the material you need
- Once more than **5–6 constraints** must be followed at the same time, compliance collapses sharply → break the work into steps
- Give coding agents a **done condition** with `/goal` and tests
- Memory and connected external apps are convenient, but periodically check **what is stored and what is connected**
- Check your **training opt-out** setting (South Korea's PIPC guide recommends this, for example)

---

> You can outsource your thinking, but **not your understanding.** For important work, think it through yourself first, then bring in the AI.
