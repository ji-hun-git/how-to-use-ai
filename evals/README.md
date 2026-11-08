# Evals: test your prompts instead of trusting them

> "It worked when I tried it once" is not evidence. In one controlled study the same question was asked 100 times per prompt, and results varied a lot between runs ([Wharton Prompting Science Report 1](https://arxiv.org/abs/2503.04818)).
> This folder is a small, runnable example of the evaluation habit described in [docs/08](../docs/08-verification-and-evals.md).

## What it tests

Two prompts answer customer questions from the same short policy document ([data/policy.txt](data/policy.txt)):

| Prompt | What it does |
|---|---|
| [baseline.txt](prompts/baseline.txt) | A typical prompt: role + document + question |
| [grounded.txt](prompts/grounded.txt) | Document first, purpose stated, cite-or-say-it's-not-covered rule, false-premise rule, format |

Six test cases target the failure modes from [docs/04](../docs/04-failure-modes.md):

| Case | Failure it probes |
|---|---|
| Return window | Basic correctness |
| Cites the section | Grounding (every claim traceable) |
| Shipping to Canada | **Fabrication**: the policy doesn't say, so any answer is invented |
| Return window + restocking fee | **Omission / fabrication**: half answerable, half not |
| "Since refunds take 60 days…" | **Sycophancy**: does it accept a false premise? |
| Unwrapped mattress | Applying an exception correctly |

## Run it

Requires Node.js and an API key for the model you test (for the default config, `ANTHROPIC_API_KEY`).

```bash
npx promptfoo@latest eval -c evals/promptfooconfig.yaml
```

```bash
npx promptfoo@latest view
```

The view opens a side-by-side table of both prompts across all cases, with pass/fail per assertion. To test another model, change the `providers` entry in [promptfooconfig.yaml](promptfooconfig.yaml) (see the [promptfoo provider docs](https://www.promptfoo.dev/docs/providers/)).

> Note: results depend on the model and change between runs and model versions. Newer models often pass more baseline cases than older ones; the point is to **measure** rather than assume. Run each case a few times (`--repeat 3`) before drawing conclusions.

## Skill evaluations: with vs. without

[`skills/run.py`](skills/run.py) measures what each of the 10 [skills](../skills/README.md) changes. Every case in [`skills/cases.yaml`](skills/cases.yaml) is answered twice per model, once with a plain assistant prompt and once with the skill's `SKILL.md` loaded, and a grader model checks each criterion as pass/fail without seeing which condition produced the answer.

- **20 cases, 2 per skill.** 16 *trigger* cases where the skill should improve the result (vague requests, planted factual errors, unsupported citations, pushback on a correct answer, missing requirements, changed requirements in a long chat, homework requests). 4 *control* cases where correct default behavior must not break (a clear request shouldn't get clarifying questions, correct code shouldn't get invented issues, "show solution" should show it).
- **Binary criteria**, all of which must pass.

```bash
python evals/skills/run.py --dry-run
```

```bash
python evals/skills/run.py --models openai:gpt-6.1-terra openai:gpt-6-luna --judge openai:gpt-6.1-sol --runs 3
```

Other providers: `anthropic:<model>` (needs `ANTHROPIC_API_KEY`) or `claude-cli:<alias>` (uses a logged-in Claude Code CLI and your plan's usage). The run resumes if interrupted, and writes `evals/results/<date>/summary.md` plus `raw.jsonl` with every answer and every per-criterion grade.

**Cost:** the example above makes 240 answers and 240 grading calls; at November 2026 list prices that's roughly a few US dollars. Use `--cases` to run one skill, or `--runs 1` for a quick check.

**What it doesn't test:** whether an agent *selects* the skill on its own. To check triggering, install the skills, then send a few requests that should and shouldn't activate each one, and see which skill the agent reports using.

**Results:** [evals/results/README.md](results/README.md). On 2026-11-09 the skills raised Claude Haiku from 41/48 to 48/48 and Claude Sonnet from 42/48 to 47/48 on trigger cases, with no control-case regressions. They made no measurable difference on 16 of the 20 cases, and the run caught a flaw in `task-spec` that we fixed and re-tested.

## Make it yours

1. Replace `data/policy.txt` with your own document and the prompts with your own.
2. Collect 20 or so real inputs, especially ones that failed before (Anthropic recommends starting with 20–50 tasks drawn from real failures).
3. Write pass/fail checks: exact checks (`icontains`, `regex`) where possible, `llm-rubric` only where judgment is needed, and spot-check the grader against your own judgment.
4. Re-run the suite whenever you change the prompt or switch models. Keep passing cases as a regression set.

## Sources

- promptfoo (open-source prompt testing) — https://github.com/promptfoo/promptfoo
- Anthropic, Demystifying evals for AI agents (2026-01) — https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- Hamel Husain & Shreya Shankar, LLM Evals FAQ — https://hamel.dev/blog/posts/evals-faq/
- Anthropic, Reduce hallucinations (the techniques used in grounded.txt) — https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations
