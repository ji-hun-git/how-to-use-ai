---
name: prompt-improver
description: Turns a rough request or weak prompt into a strong one. Use when the user asks to write, improve, review or debug a prompt, system prompt, custom instructions, an agent's instructions, or a reusable template; or when a prompt keeps producing poor results. Checks the six elements (role, context, instruction, format, constraints, examples), predicts likely failures, and returns a tested, leaner prompt.
license: MIT
---

# Prompt improver

Good prompts are not long; they leave little for the model to guess. Improve prompts by filling the gaps that cause failures and deleting what doesn't help.

## Steps

1. **Understand the job.** Identify the task, audience, where the output will be used, and what "done" looks like. If these are missing and matter, ask (at most three questions).
2. **Check the six elements** and note what's missing or weak:
   - **Context** (most important): purpose, audience, situation, source material
   - **Instruction**: the exact action and the done criteria
   - **Format**: structure, length, tone
   - **Constraints**: only the rules that truly matter (about five or fewer), each with a reason
   - **Examples**: 2–5 varied examples if style or format is hard to describe (try none first for reasoning models)
   - **Role**: only for tone or perspective; it doesn't improve accuracy
3. **Predict failures.** List the most likely ways the prompt could fail: misunderstanding (ambiguity), omission (too many requirements, buried in a long input), fabrication (no source, no permission to say "I don't know"), sycophancy (asking for opinions on "my" work).
4. **Rewrite.** Return the improved prompt in a code block. Put long documents first and the question last; separate parts with consistent tags or headings; add "If something isn't in the material, say so" where facts matter. Use clearly marked placeholders for facts you don't have (policies, prices, limits, names), and keep invented example values out of the prompt: the model will treat them as real.
5. **Trim.** Remove ALL-CAPS emphasis, "think step by step" for reasoning models, threats, tips, flattery of the model, and duplicate rules.
6. **Explain and test.** Give a short table of what changed and why, and suggest 3–5 test inputs (including an edge case) to compare old vs. new.

## Evidence

- Prompt components and ordering: Anthropic prompting best practices — https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices ; OpenAI prompt engineering guide — https://developers.openai.com/api/docs/guides/prompt-engineering
- Format instructions measurably help; tips, threats and expert personas don't reliably help: Wharton Prompting Science Reports — https://arxiv.org/abs/2503.04818 , https://arxiv.org/abs/2508.00614 ; personas: https://arxiv.org/abs/2311.10054
- "Think step by step" adds little for reasoning models (2025): https://arxiv.org/abs/2506.07142
- More in the guide: https://github.com/ji-hun-git/how-to-use-ai/blob/main/docs/02-prompt-anatomy.md
