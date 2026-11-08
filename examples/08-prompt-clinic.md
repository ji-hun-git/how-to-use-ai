# Example 8. Prompt clinic: 12 common prompts, diagnosed and fixed

> Each case: the prompt people actually write → what goes wrong (and which failure mode) → a fixed version → the evidence.
> Failure modes: 🎯 misunderstanding · 📋 omission · 🔍 fabrication · 🪞 sycophancy. Background: [docs/04](../docs/04-failure-modes.md).

---

### 1. "Summarize this." 🎯📋
**What goes wrong:** No reader, purpose or length, so you get a generic summary that over-weights the start and end of the document and may add conclusions that aren't in it.
**Fixed:**
```text
<document>…</document>
For a manager who missed the meeting and needs the decisions in 2 minutes: quote the sentences about decisions, owners and deadlines (whole document, including the middle), then summarize only from those quotes. Write "TBD" for anything not stated.
```
**Evidence:** long documents first, question last (up to 30% better in Anthropic's tests); middle content is used worst ([Lost in the Middle](https://arxiv.org/abs/2307.03172)). → [Example 2](02-document-summary.md)

### 2. "Give me 5 studies on X with links." 🔍
**What goes wrong:** Without search, the model produces plausible-looking but invented references. Even 2026-released models fabricated references in 35% of responses in one study (preprint).
**Fixed:**
```text
Use web search. Find studies on X published since 2023. Only list papers you actually opened; give title, authors, year, venue, URL and the one sentence that supports my question. If you find fewer than 5, list fewer.
```
**Evidence:** [Topaz et al., 2026](https://arxiv.org/abs/2609.14988); 2,266 court cases involving AI-fabricated citations ([database](https://www.damiencharlotin.com/hallucinations/)). → [Example 3](03-research-with-sources.md)

### 3. "Are you sure?" 🪞
**What goes wrong:** It reads as social pressure. In a 2023 study, models changed their answer 46% of the time and accuracy dropped 17%.
**Fixed:**
```text
Re-solve this from scratch without assuming your first answer is right or wrong. If the new result differs, show exactly where the first one went wrong.
```
**Evidence:** [FlipFlop](https://arxiv.org/abs/2311.08596); current models still collapse under sustained pushback ([SPINE, 2026 preprint](https://arxiv.org/abs/2609.09090)).

### 4. "I wrote this. What do you think?" 🪞
**What goes wrong:** Stating authorship and asking an open question invites praise. People also trust flattering answers more ([*Science*, 2026](https://www.science.org/doi/10.1126/science.aec8352)).
**Fixed:**
```text
Another team submitted this proposal. First define 5 criteria a strong proposal for {{audience}} must meet. Then score it 1–5 per criterion and give the 3 biggest weaknesses with fixes. If there are no serious problems, say so.
```
→ [templates/honest-critique.md](../templates/honest-critique.md)

### 5. "You are a world-class marketing genius. Write our launch post." 🎯
**What goes wrong:** The persona doesn't improve accuracy, and the real information (product, audience, goal, tone, length) is missing.
**Fixed:**
```text
Write a launch post for {{product}}, aimed at {{audience}} who care about {{benefit}}. Goal: get them to {{action}}. Tone: plain and confident. 150 words, one headline, one call to action. Facts to use: {{facts}}. Don't add claims beyond these facts.
```
**Evidence:** expert personas didn't reliably improve factual accuracy ([Wharton Report 4](https://gail.wharton.upenn.edu/research-and-insights/playing-pretend-expert-personas/); [Zheng et al.](https://arxiv.org/abs/2311.10054)).

### 6. "IMPORTANT!!! NEVER use jargon!!! ALWAYS be concise!!!" 🎯
**What goes wrong:** Current models over-apply emphasized rules and become rigid; the reason for the rule is missing, so they can't generalize it.
**Fixed:**
```text
Readers are new customers with no technical background, so use everyday words and keep it under 150 words. If a technical term is unavoidable, define it in a few words.
```
**Evidence:** explain the why; reserve absolute words for true invariants ([Anthropic best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices); [OpenAI GPT-5.6 guide](https://developers.openai.com/api/docs/guides/prompt-guidance-gpt-5p6)).

### 7. "Think step by step." (to a reasoning model) 🎯
**What goes wrong:** Reasoning models already reason. In a 2025 study the phrase changed their accuracy by only +3.1 to −3.3 points while making answers 20–80% slower.
**Fixed:** State the goal and the done criteria, and raise the app's reasoning-effort setting if the problem is hard.
**Evidence:** [Wharton Report 2](https://arxiv.org/abs/2506.07142). → [docs/05](../docs/05-models-and-reasoning.md)

### 8. A 20-rule prompt 📋
**What goes wrong:** The more constraints a prompt has, the less likely all are met; reliable compliance broke down beyond about 5–6 simultaneous constraints in a 2026 preprint.
**Fixed:** Keep the ~5 rules that matter most, number them, ask for a coverage table at the end, and move the rest to a second pass.
**Evidence:** [Vasileva, 2026](https://arxiv.org/abs/2608.12426); [IFScale](https://arxiv.org/abs/2507.11538). → [templates/coverage-check.md](../templates/coverage-check.md)

### 9. Adding requirements one message at a time 🎯
**What goes wrong:** The model locks in early assumptions; performance dropped 39% on average when the same request was spread across turns.
**Fixed:**
```text
Consolidate everything I've asked for so far into one complete prompt.
```
Then paste it into a new chat.
**Evidence:** [Laban et al., ICLR 2026](https://arxiv.org/abs/2505.06120). → [skills/fresh-start-handoff](../skills/fresh-start-handoff/SKILL.md)

### 10. "What's the average growth rate in this table?" 🔍🎯
**What goes wrong:** Mental arithmetic errors, and an undefined metric (year over year? compound?).
**Fixed:**
```text
Compute growth as (2026 total / 2025 total) − 1 per region by running code. Check the data for blanks and duplicates first and show me the code.
```
→ [Example 4](04-data-analysis.md)

### 11. "Fix the login bug." (to a coding agent) 🎯🔍
**What goes wrong:** No symptom, location or definition of fixed; the agent guesses, and may "fix" something else or claim success without testing.
**Fixed:**
```text
Login returns 500 after the session expires. Look at src/auth/. First write a failing test that reproduces it and show it fails; then make the minimal fix; then run the auth tests and show the output. Don't edit the test.
```
**Evidence:** [Claude Code best practices](https://code.claude.com/docs/en/best-practices). → [Example 5](05-coding-agent.md)

### 12. "Explain this to me." (while studying) 🎯
**What goes wrong:** A full answer feels like learning but can reduce what you can do on your own: unrestricted AI help raised practice scores but cut later exam scores by 17% in one trial.
**Fixed:**
```text
I'm learning this. Give me one hint at a time, ask me to explain my reasoning, and show the full solution only if I type "show solution".
```
**Evidence:** [Bastani et al., *PNAS* 2025](https://knowledge.wharton.upenn.edu/article/without-guardrails-generative-ai-can-harm-education/); [Anthropic, 2026](https://www.anthropic.com/research/AI-assistance-coding-skills). → [Example 6](06-learning-with-ai.md)

---

**Pattern across all 12:** the fix is almost never a magic phrase. It's missing context, a done criterion, a source to ground in, a check to run, or a fresh start.
