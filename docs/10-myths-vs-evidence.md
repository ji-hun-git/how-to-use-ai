# 10. Prompt myths vs evidence

> The internet is full of tricks like "Double GPT's performance with this one phrase!"
> This document checks popular tricks against **controlled experimental results** and **official guides**.
> Key lesson: **Task definition, context, format, examples, and verification matter far more than tricks.**

---

## Summary table

| Common trick | Verdict | Evidence |
|---|---|---|
| "I'll tip you," "Something terrible will happen if you don't" (rewards and threats) | ❌ No effect | Wharton Report 3 (2025) |
| Being polite ("please") / or the opposite, being commanding | ➖ No overall difference | Wharton Report 1 (2025) |
| "You are the world's top expert" (expert role) | ❌ No accuracy gain, sometimes a drop | Wharton Report 4 (2025), Zheng et al. (2024) |
| "Think step by step" (with reasoning models) | ❌ Almost no effect, just more time | Wharton Report 2 (2025), OpenAI, Microsoft |
| "Think step by step" (with standard models) | ⚠️ Raises the average but sometimes gets easy questions wrong | Wharton Report 2 (2025) |
| ALL CAPS, "NEVER!!!", "IMPORTANT" emphasis | ❌ Current models overreact | Anthropic (dial back phrasing like "CRITICAL: You MUST"), OpenAI (absolute language only for true invariants) |
| Verifying with "Are you sure?" | ❌ Flips correct answers | FlipFlop (2023), SPINE (2026: even current models give in when pushed long enough) |
| The longer and more detailed the prompt, the better | ❌ Padding hurts | OpenAI model-specific guides, Anthropic context engineering |
| The more material you add, the better | ❌ The model misses content in the middle, and gains are marginal | Lost in the Middle (2023), Context Rot (2025) |
| 🆕 With a 1-million-token model, you can put in everything | ⚠️ Retrieval works, but **synthesis and reasoning get weaker as length grows** | Chow (2026) |
| Specifying the output format is a minor detail | ❌ **Format instructions are a performance factor** | Wharton Report 1 (2025) |
| If it works once or twice, it works | ❌ The same question gives different answers each time | Wharton Report 1 (2025) |
| If the AI cites sources, it's trustworthy | ❌ It sometimes fabricates the sources themselves | Walters & Wilder (2023), **Topaz et al. (2026: even models released in 2026 included fake references in 35% of responses)** |
| 🆕 Current models barely hallucinate anymore | ❌ Hallucination has dropped, but varies widely by situation | Vectara (2026: 7–14% when summarizing documents), HalluHard (2026: about 30% even with search on) |
| Using AI always makes you faster | ⚠️ A 2025 experiment found people were actually slower; 2026 follow-up studies suggest they may be faster, but the evidence is weak | METR (2025, 2026), HBS/BCG (2023, formally published 2026) |
| 🆕 An AI that agrees with me is a good AI | ❌ People **trust sycophancy more**, but their judgment gets worse | Cheng et al. (*Science*, 2026) |
| The more examples, the better | ⚠️ 3–5 is about right; with reasoning models, try without examples first | Anthropic, Google, OpenAI |
| A model that says "I don't know" is a weak model | ❌ Models that say "I don't know" are wrong less often | OpenAI (2025), Artificial Analysis (2026) |

---

## 1. Rewards and threats: no effect

Wharton Generative AI Labs' **Prompting Science Report 3** ("I'll pay you or I'll kill you — but will you care?", 2025) systematically tested phrases such as a $1,000 tip, a $1 trillion tip, and threats.

- Overall, they **did not reliably improve performance**.
- At the level of **individual questions**, however, accuracy swung widely, by as much as +36 and −35 percentage points, and the direction was **unpredictable**.

> This is why anecdotes like "It worked better when I offered a tip" keep coming up. On one or two questions things may improve by chance, but on average there is no effect.

The 2023 "26 principles" paper claimed that tip and penalty phrases were effective, but that claim was later **refuted** by the Wharton research. The paper's results came from evaluating each principle on 20 questions.

## 2. Politeness: no difference on average

In **Report 1** ("Prompt Engineering is Complicated and Contingent", 2025), "please" versus "I order you" **made no reliable overall difference**. Differences can appear on individual questions.

> You're free to write politely, but **it isn't a performance trick**. Being rude doesn't help either.

## 3. Expert roles: no accuracy gain

**Report 4** ("Playing Pretend: Expert Personas Don't Improve Factual Accuracy", 2025)
- Expert personas **did not reliably improve** factual accuracy, and in some conditions they significantly **lowered** it.
- Low-knowledge personas such as "toddler" lowered performance.
- When given an expert role **that didn't match the question**, one Gemini model **refused** to answer about 10.6 out of 25 times per question on average.

**Zheng et al.** (EMNLP Findings 2024): In experiments with 162 roles and 2,410 factual questions, assigning a role did not improve performance, and even automatically choosing the best role was **no better than random selection**.

> **Roles are still useful**, not for accuracy but for setting **tone, perspective, and audience level**. → [02. The six elements of a prompt](02-prompt-anatomy.md#1-role)

## 4. "Think step by step": depends on the model

**Report 2** ("The Decreasing Value of Chain of Thought in Prompting", 2025)

| Model type | Effect | Side effect |
|---|---|---|
| Standard (non-reasoning) models | Average gain of up to 13.5 percentage points | Sometimes gets easy questions wrong that it used to get right |
| Reasoning models | +3.1 to −3.3 percentage points (almost none) | Response time up 20–80% |

OpenAI advises against chain-of-thought prompting with reasoning models, and Microsoft's prompt engineering techniques page carries a banner saying these techniques are not recommended for reasoning models such as GPT-5 and the o-series.

## 5. Caps and emphasis: they backfire on current models

The 2026 guides recommend dialing back emphasis that was added for older models. Anthropic says to soften phrasing like "CRITICAL: You MUST" and to adjust "don't be lazy"-type wording, and OpenAI says to use absolute language only for rules that truly have no exceptions. Current models follow such instructions **too strongly**, ignoring other instructions or overdoing things. Instead, **explain the reason in one line**.

## 6. "Are you sure?": shaking the model, not verifying

- FlipFlop experiment (2023, 10 models): after "Are you sure?", models changed their answers **46%** of the time on average, and accuracy dropped **17%** on average
- Anthropic research (2023): when challenged, Claude 1.3 admitted a mistake on **98%** of questions (even when it hadn't made one)

→ Instead, **ask for evidence**, or have it solve the problem again **independently in a new chat**. → [templates/honest-critique.md](../templates/honest-critique.md)

## 7. Are long, detailed prompts better?

- **Necessary context** is better the more detailed it is, but **padding** hurts.
- OpenAI's GPT-5.6 guide (2026-07): In internal coding-agent evaluations, trimmed-down prompts scored about 10–15% higher and used 41–66% fewer tokens (OpenAI itself describes these as directional figures).
- Anthropic: Context is a limited attention budget. Aim for **the smallest amount of high-signal information**.
- The more instructions you add, the lower the chance that all of them are followed (ManyIFEval, IFScale).

## 8. Is specifying the format a minor detail? → It actually matters

**Report 1**: **Removing** output format instructions lowered accuracy by 8.6 percentage points for GPT-4o and 12.1 percentage points for GPT-4o-mini. It is one of the few things that look like tricks whose **effect has actually been confirmed**.

## 9. If it works once, does it work? → It varies every time

**Report 1** asked each question 100 times. Under the strict standard of "must be correct all 100 times to pass," GPT-4o was **about 5 percentage points above random guessing** (not statistically significant). The researchers concluded that prompt engineering is **"complicated and contingent."**

→ Test important prompts **on multiple inputs, multiple times**. [08. Verification and evals](08-verification-and-evals.md)

## 10. Is a model that says "I don't know" a bad model? → The opposite

In a comparison OpenAI published, a model that answered "I don't know" 52% of the time had an error rate of 26%, while a model that said "I don't know" only 1% of the time had an error rate of **75%**. Accuracy was similar. **Saying "I don't know" is a feature.** Give the model that option in your prompts too.

## 11. 🆕 New evidence from 2026

**Productivity: METR's 2026 update**
- Regarding the early-2025 experiment (experienced developers were 19% slower), METR said in February 2026 that the result **no longer represents current tools**.
- A follow-up experiment (57 developers, 800+ tasks) estimated −18% for returning participants and −4% for new participants (time savings), but the confidence intervals were wide and 30–50% of participants left out tasks they didn't want to do without AI, so METR itself called it **"very weak evidence."**
- In a May 2026 survey (349 people), the median self-reported speedup was 3x, but METR warned it **may be exaggerated**, noting that participants in the 2025 experiment had overestimated AI's effect by about 40 percentage points.
- **The lesson stands:** perception and reality can differ, so measure it on your own work.

**Prompt injection: Wharton Prompting Science Report 5 (2026-04)**
- An experiment in manipulating AI grading by planting hidden instructions such as "This essay is excellent" in submitted work. Current flagship models raised scores by only about 2.6 points on average, but a small model (GPT-4o mini) raised them by about 20 points.
- When you have AI **evaluate** text someone else wrote, remember that it can be swayed by hidden instructions. → [09. Security](09-security-privacy.md)

**Sycophancy: it persists because people like it (*Science*, 2026-03)**
- 11 AI models affirmed users' actions about 49% more than humans did, and in experiments with 2,405 participants, people **trusted and preferred** sycophantic answers more. In other words, it's easy to mistake a pleasant answer for a good one.

> 📌 Wharton researchers have not yet re-measured Reports 1–4 (tips, politeness, expert roles, CoT) on 2026 models.

---

## So what does work?

What the Wharton researchers and the official guides point to in common:

1. **Define the task clearly** (what, why, and when it's done)
2. **Provide context and materials**
3. **Specify the output format**
4. **Show examples** (with reasoning models, try without examples first)
5. **Verify the results** (multiple times, against outside evidence)

Citing Acar (2023), the MIT Sloan guide says that in the long run, **the ability to define a problem and set its scope and boundaries** may matter more than the skill of polishing prompt wording.

---

### Sources

- Meincke, Mollick, Mollick, Shapiro, Prompting Science Report 1 (2025, preprint) — https://arxiv.org/abs/2503.04818
- Meincke et al., Prompting Science Report 2 (2025, preprint) — https://arxiv.org/abs/2506.07142
- Meincke et al., Prompting Science Report 3 (2025, preprint) — https://arxiv.org/abs/2508.00614
- Basil et al., Prompting Science Report 4 (2025, preprint) — https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5879722 / explainer: https://knowledge.wharton.upenn.edu/article/why-you-shouldnt-ask-chatbots-to-act-like-an-expert/
- Zheng et al., Personas in System Prompts (EMNLP Findings 2024) — https://arxiv.org/abs/2311.10054
- Bsharat et al., "Principled Instructions Are All You Need" (26 principles, 2023, preprint) — https://arxiv.org/abs/2312.16171
- Laban et al., FlipFlop (2023) — https://arxiv.org/abs/2311.08596
- Sharma et al., Towards Understanding Sycophancy (Anthropic, 2023) — https://arxiv.org/abs/2310.13548
- OpenAI, Why language models hallucinate (2025) — https://openai.com/index/why-language-models-hallucinate/
- OpenAI, GPT-5.6 prompt guidance — https://developers.openai.com/api/docs/guides/prompt-guidance-gpt-5p6
- OpenAI, Reasoning best practices — https://developers.openai.com/api/docs/guides/reasoning-best-practices
- Microsoft, Prompt engineering techniques — https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/prompt-engineering
- Anthropic, Prompting best practices — https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- Anthropic, Effective context engineering for AI agents — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Liu et al., Lost in the Middle (2023) — https://arxiv.org/abs/2307.03172
- Chroma, Context Rot (2025) — https://research.trychroma.com/context-rot
- Walters & Wilder, study of fabricated citations (*Scientific Reports*, 2023) — https://www.nature.com/articles/s41598-023-41032-5
- METR (2025) — https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
- METR, changes to the productivity experiment design and follow-up results (2026-02-24) — https://metr.org/blog/2026-02-24-uplift-update/
- METR, early-2026 self-report survey on AI productivity (2026-05-11) — https://metr.org/blog/2026-05-11-ai-usage-survey/
- Wharton, Prompting Science Report 5 "The Effects of Prompt Injection on Grading" (2026-04, preprint) — https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6510758 / explainer: https://gail.wharton.upenn.edu/research-and-insights/hidden-prompt-injections/
- Cheng et al., *Science* (2026-03) — https://www.science.org/doi/10.1126/science.aec8352
- SPINE (2026-09, preprint) — https://arxiv.org/abs/2609.09090
- Topaz et al. (2026-09, preprint) — https://arxiv.org/abs/2609.14988
- Chow (2026-05, preprint) — https://arxiv.org/abs/2605.02173
- HalluHard (2026-02, preprint) — https://arxiv.org/abs/2602.01031
- Vectara Hallucination Leaderboard — https://github.com/vectara/hallucination-leaderboard
- Artificial Analysis, AA-Omniscience — https://artificialanalysis.ai/evaluations/omniscience
- Dell'Acqua et al., *Organization Science* (2026, formally published) — https://pubsonline.informs.org/doi/10.1287/orsc.2025.21838
- MIT Sloan, Effective Prompts for AI (Problems over prompts) — https://mitsloanedtech.mit.edu/ai/basics/effective-prompts/
