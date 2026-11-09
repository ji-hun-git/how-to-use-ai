# 01. Mindset: how to approach AI

> Before any prompting technique, decide **what kind of collaborator you take AI to be**.
> Once that view is settled, most of what makes a good prompt follows naturally.

---

## 1. AI is a "capable new hire with zero context"

Two AI labs (Anthropic and OpenAI) and Andrej Karpathy use the same kind of analogy.

| Source | Analogy | Meaning |
|---|---|---|
| Anthropic | A brilliant new employee with no context at all | It **doesn't know** your situation, goals, or standards **unless you tell it** |
| OpenAI (reasoning model guide) | A seasoned senior coworker | Give it a goal and it **works out the method** itself. You don't need to spell out every step |
| Andrej Karpathy | A capable but error-prone intern | Its output **must be reviewed** |

Put the three together and you get:

> **Give the goal and context in detail, leave the method to the AI, and check the result.**

---

## 2. AI's abilities are uneven (the jagged frontier)

An experiment by Harvard Business School and BCG with 758 consultants (Dell'Acqua et al., 2023) showed that the boundary of AI capability is **not a smooth line but a jagged, sawtooth edge**.

- On **tasks AI is good at**, the group using AI completed 12.2% more tasks, 25.1% faster, at roughly 40% higher quality.
- On **tasks outside AI's capabilities**, the group using AI was **19 percentage points less likely** to get the right answer, because they trusted AI's plausible wrong answers.
- The researchers called this **"falling asleep at the wheel."**

AI can do well on work that looks hard and still get work that looks easy wrong. So **don't judge by a gut feeling that "it'll surely get this right."** Use it yourself and learn how far AI can be trusted in your own work.

> 🆕 This study was formally published in *Organization Science* in March 2026. And in 2026 the frontier is still jagged. According to the Stanford AI Index 2026, AI reached gold-medal level at the International Mathematical Olympiad, yet even the top model **read analog clocks correctly only 50.1%** of the time.

The researchers described two kinds of people who use AI well.

- **Centaurs:** divide the work and hand AI only the parts it's good at.
- **Cyborgs:** work back and forth with AI continuously across the whole task.

Both got good results. What they had in common: **they knew where to trust AI and where to doubt it.**

---

## 3. Responsibility stays with people

- In the US, lawyers submitted case law fabricated by ChatGPT to a court and were sanctioned $5,000 (Mata v. Avianca, 2023). The court took issue not with using AI but with **failing to check**.
- MIT Sloan's AI guide calls checking citations and sources **non-negotiable**.
- In a survey of 319 knowledge workers by Carnegie Mellon and Microsoft (CHI 2025), **the more people trusted AI, the less critical thinking they did**, while those more confident in their own abilities tended to do more.

> The moment you send out AI output under your name, it is **your output**.

---

## 4. You can outsource thinking, but not understanding

Karpathy summed it up in a 2026 post: you can outsource your thinking, but **you can't outsource your understanding.**

- In an experiment by Wharton (University of Pennsylvania) researchers with about 1,000 high school students in Türkiye (Bastani et al., *PNAS*, 2025), students who studied with an AI that handed them answers improved their practice scores substantially but scored **17% lower on the exam taken without AI.** A tutor-style AI that gave only hints, by contrast, did not lower exam scores.
- 🆕 2026 research points the same way. In Anthropic's randomized experiment (2026-01, 52 junior developers), the group that learned a new library with AI scored 50% on a comprehension quiz, 17 percentage points below the group that coded by hand (67%). However, those who **asked conceptual questions or asked for explanations after receiving code** scored higher.
- In other words, the question is not whether you use AI but **how** you use it. → [Example 6: Learning with AI](../examples/06-learning-with-ai.md)

**In practice:** for important work, **think it through or write a draft yourself first**, then show it to the AI. Reverse the order and the AI's answer becomes the frame for your own thinking.

---

## 5. Adjust autonomy like a slider

In his 2025 YC talk, Karpathy said to build AI tools **more like Iron Man suits than Iron Man robots**. Rather than full automation, the human keeps control while the AI amplifies their abilities. He called this the **autonomy slider**.

| Level | AI's role | Human's role | Example |
|---|---|---|---|
| 1 | Answers questions | Makes every judgment | Explaining concepts, ideas |
| 2 | Drafts | Edits and uses the draft | Emails, report drafts |
| 3 | Performs tasks | Approves each step | Coding agent (approve plan → implement) |
| 4 | Handles multiple tasks on its own | Reviews only the results | Repetitive tasks with good test coverage |

**Start at a low level, and move up one level each time you gain a way to check the results (tests, checklists, comparison against the source).**

---

## 6. When to skip AI or use it with care

| Situation | Reason |
|---|---|
| Work where **you have no way to verify** the result and a mistake would be costly | It may lie outside the jagged frontier |
| **Core skills you are currently learning** | You end up outsourcing understanding |
| Putting **confidential or personal data** into tools your company hasn't approved | [09. Security and privacy](09-security-privacy.md) |
| Short tasks that are faster to do yourself | Explaining takes longer |

> 💡 "Using AI always makes you faster" isn't true either. In a 2025 experiment by the nonprofit research organization METR, experienced developers **felt** AI made them 20% faster, but they were actually 19% **slower**. In February 2026, METR said this result no longer represents current tools; a follow-up experiment suggested a possible speedup, but METR itself called that "very weak evidence." The lesson stands: **perceived speed and actual speed can differ.**

---

## Key takeaways

1. Give goals and context in detail, leave the method to the AI, and check the result.
2. AI's abilities are jagged. Don't trust your gut; learn the boundary in your own work.
3. Responsibility for the result stays with people.
4. For important work, think first, then bring in AI.
5. Raise autonomy only as far as your means of verification allow.

---

### Sources

- Anthropic, Prompting best practices — https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- OpenAI, Reasoning best practices — https://developers.openai.com/api/docs/guides/reasoning-best-practices
- Karpathy, Sequoia Ascent 2026 summary (2026-04-30) — https://karpathy.bearblog.dev/sequoia-ascent-2026/
- Karpathy, "Software Is Changing (Again)" YC AI Startup School (2025-06-18) — https://www.youtube.com/watch?v=LCEmiRjPEtQ (talk summary: https://ikyle.me/blog/2025/andrej-karpathy-software-is-changing-again)
- Dell'Acqua et al., "Navigating the Jagged Technological Frontier" (HBS Working Paper, 2023) — commentary by coauthor Ethan Mollick: https://www.oneusefulthing.org/p/centaurs-and-cyborgs-on-the-jagged
- Mata v. Avianca sanctions decision (2023-06-22) — https://law.justia.com/cases/federal/district-courts/new-york/nysdce/1:2022cv01461/575368/54
- MIT Sloan Teaching & Learning Technologies, "Addressing AI Hallucinations and Bias" — https://mitsloanedtech.mit.edu/ai/basics/addressing-ai-hallucinations-and-bias/
- Lee et al., "The Impact of Generative AI on Critical Thinking" (CHI 2025) — https://advait.org/files/lee_2025_ai_critical_thinking_survey.pdf
- Bastani et al., "Generative AI without guardrails can harm learning" (*PNAS*, 2025) — https://knowledge.wharton.upenn.edu/article/without-guardrails-generative-ai-can-harm-education/
- METR, early-2025 study of AI and experienced developers (2025-07-10) — https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/

**2026 update (checked 2026-11-09)**
- Dell'Acqua et al., formally published in *Organization Science* (2026-03) — https://pubsonline.informs.org/doi/10.1287/orsc.2025.21838
- Stanford HAI, AI Index 2026 — https://hai.stanford.edu/ai-index/2026-ai-index-report
- Anthropic, "How AI assistance impacts the formation of coding skills" (2026-01-29) — https://www.anthropic.com/research/AI-assistance-coding-skills / paper (preprint): https://arxiv.org/abs/2601.20245
- METR, follow-up results on the productivity experiment (2026-02-24) — https://metr.org/blog/2026-02-24-uplift-update/
