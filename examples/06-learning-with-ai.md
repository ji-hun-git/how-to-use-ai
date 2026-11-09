# Example 6. Learning with AI: grow your thinking instead of collecting answers

> You can outsource your thinking to AI, but you can't outsource your **understanding**. (Paraphrasing Karpathy)

---

## What the research shows

- **AI that simply hands out answers hurt performance.** In an experiment by University of Pennsylvania researchers with about 1,000 high school students in Türkiye (Bastani et al., *PNAS*, 2025), students who used unrestricted GPT-4 raised their practice-problem scores by 48%, but **scored 17% lower on an exam taken without AI.**
- **A tutor-style AI that gives only hints was different.** A version designed to give hints instead of answers raised practice scores by 127% and did not lower exam scores.
  (The 48% and 127% figures come from press coverage of the 2024 working paper; what the *PNAS* abstract confirms is the 17% drop in exam scores.)
- In a preliminary study from the MIT Media Lab ("Your Brain on ChatGPT," 2025, a preprint not yet peer-reviewed, 54 participants), the group that wrote essays with an LLM showed the lowest brain engagement and had trouble remembering their own writing. It's a small study that has drawn rebuttals, so don't treat its conclusions as settled, but the direction is worth noting.

- 🆕 **Anthropic randomized experiment (2026-01, preprint):** When 52 junior developers learned a new Python library, the group using AI scored 50% on a comprehension quiz, versus 67% for the group that coded by hand (a 17-percentage-point gap). The gap was especially large for **debugging** comprehension, and the time saved was about 2 minutes, which was not statistically significant. By contrast, people who **asked conceptual questions, or asked for explanations after receiving code**, scored high, at 65–86%.
- 🆕 **University randomized experiment (2026-10, working paper, 2,379 undergraduates):** Giving students access to an AI tutor integrated into the course **lowered** final grades by 0.37 standard deviations and sharply reduced engagement with the learning site. Losses were larger among first-generation college students. Being called a "tutor" doesn't make a tool safe; **how it was designed to be used, and how you use it,** determine the outcome.
- Harvard's CS50 turned this lesson into policy. Its own AI tutor (the "CS50 Duck") is designed not to give answers directly but to guide students toward them, and commercial AI that writes answers for you may not be used for assignments.

**Bottom line:** When you study, use AI as a **tutor**, not an **answer key**.

Sources: [Knowledge at Wharton (Bastani et al.)](https://knowledge.wharton.upenn.edu/article/without-guardrails-generative-ai-can-harm-education/) · [PNAS bibliographic record](https://econpapers.repec.org/RePEc:nas:journl:v:122:y:2025:p:e2422633122) · [MIT "Your Brain on ChatGPT"](https://arxiv.org/abs/2506.08872) · [Rebuttal](https://arxiv.org/abs/2601.00856) · [CS50 academic honesty policy](https://cs50.harvard.edu/x/honesty/) · [Karpathy, Sequoia Ascent 2026](https://karpathy.bearblog.dev/sequoia-ascent-2026/) · [Anthropic learning experiment (2026)](https://www.anthropic.com/research/AI-assistance-coding-skills) · [University AI tutor experiment, EdWorkingPaper 26-1598 (2026)](https://edworkingpapers.com/ai26-1598)

---

## Tutor-mode prompt

```text
You are my tutor for ___. My level is ___.
Rules:
- Don't give me the answer or finished code right away.
- When I get stuck, give me hints one step at a time (small hints first, then bigger ones).
- When I give an answer, don't tell me right away whether it's right; first ask me why I think so.
- Show me the full solution only when I say "show solution."
Today's topic: ___
```

## Concept check: explain it back (the Feynman technique)

```text
I'm going to try explaining the concept of ___. Listen, then point out
(1) what's wrong, (2) what's missing, and (3) what I glossed over.
Skip the praise, and if there's nothing to fix, say so.

My explanation: ...
```

## Exam prep: ask it to write questions

```text
Write 5 questions on ___ that target the points I'm most likely to get confused about.
Give me one question at a time, then grade my answer and explain it after I respond.
```

## Learning to code: keep it separate from vibe coding

```text
I'm learning Python. Don't fix this code for me. Instead,
(1) tell me only where the problem is, and (2) tell me which concept I should look up.
I'll show it to you again after I fix it.
```

> "Vibe coding," a term coined by Karpathy, means handing code over to AI while barely reading it. It's fine for weekend toy projects, but **if you're still learning**, stop the AI from fixing things for you, as above.

---

## Self-check

- [ ] I can explain what I learned today in 3 sentences without AI
- [ ] I checked at least one of the AI's explanations against a textbook or official documentation
- [ ] There's evidence I tried on my own before looking at the answer (notes, wrong answers)
