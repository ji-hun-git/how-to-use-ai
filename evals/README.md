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
