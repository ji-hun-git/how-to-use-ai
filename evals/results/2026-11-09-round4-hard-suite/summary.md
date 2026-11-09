# Skill evaluation results (2026-11-09-round4-hard-suite)

- Models under test: `claude-cli:sonnet`, `claude-cli:haiku`
- Grader: `claude-cli:opus` (blind to condition)
- Base system prompt (both conditions): "You are a helpful assistant in a text chat. In this conversation you cannot run tools, browse, or read files; answer in text."
- Case file: `cases-hard.yaml`
- Cases: 16 (14 trigger, 2 control), runs per case and condition: 3
- A run passes only if every criterion passes. **without** = plain assistant; **with** = SKILL.md loaded.
- Trigger cases test whether the skill improves the result; control cases test that it doesn't break correct default behavior.

## Overall

| Model | Case type | Without | With |
|---|---|---|---|
| `claude-cli:sonnet` | trigger | 39/42 | 41/42 |
| `claude-cli:sonnet` | control | 6/6 | 6/6 |
| `claude-cli:haiku` | trigger | 36/42 | 39/42 |
| `claude-cli:haiku` | control | 6/6 | 6/6 |

## By skill (trigger and control cases combined)

| Skill | `claude-cli:sonnet` without → with | `claude-cli:haiku` without → with |
|---|---|---|
| clarify-first | 6/6 → 6/6 | 6/6 → 6/6 |
| coverage-check | 9/9 → 9/9 | 8/9 → 9/9 |
| fresh-eyes-review | 3/3 → 3/3 | 3/3 → 3/3 |
| fresh-start-handoff | 3/3 → 3/3 | 2/3 → 1/3 |
| grounded-answer | 6/6 → 6/6 | 6/6 → 6/6 |
| honest-critique | 6/6 → 6/6 | 6/6 → 5/6 |
| learning-tutor | 0/3 → 3/3 | 0/3 → 3/3 |
| prompt-improver | 3/3 → 2/3 | 3/3 → 3/3 |
| task-spec | 3/3 → 3/3 | 2/3 → 3/3 |
| verify-claims | 6/6 → 6/6 | 6/6 → 6/6 |

## By case

| Case | Kind | `claude-cli:sonnet` without → with | `claude-cli:haiku` without → with |
|---|---|---|---|
| clarify-hidden-ambiguity-sql | trigger | 3/3 → 3/3 | 3/3 → 3/3 |
| clarify-detailed-request | control | 3/3 → 3/3 | 3/3 → 3/3 |
| coverage-long-transcript | trigger | 3/3 → 3/3 | 3/3 → 3/3 |
| coverage-ticket-export | trigger | 3/3 → 3/3 | 2/3 → 3/3 |
| coverage-twelve-constraints | trigger | 3/3 → 3/3 | 3/3 → 3/3 |
| grounded-long-contract | trigger | 3/3 → 3/3 | 3/3 → 3/3 |
| grounded-near-miss-survey | trigger | 3/3 → 3/3 | 3/3 → 3/3 |
| verify-subtle-errors | trigger | 3/3 → 3/3 | 3/3 → 3/3 |
| verify-all-true | control | 3/3 → 3/3 | 3/3 → 3/3 |
| critique-pricing-memo | trigger | 3/3 → 3/3 | 3/3 → 3/3 |
| critique-expert-pushback | trigger | 3/3 → 3/3 | 3/3 → 2/3 |
| review-own-code-subtle-bugs | trigger | 3/3 → 3/3 | 3/3 → 3/3 |
| handoff-reversals | trigger | 3/3 → 3/3 | 2/3 → 1/3 |
| improve-support-bot-prompt | trigger | 3/3 → 2/3 | 3/3 → 3/3 |
| spec-destructive-job | trigger | 3/3 → 3/3 | 2/3 → 3/3 |
| tutor-debug-attempt | trigger | 0/3 → 3/3 | 0/3 → 3/3 |

## Criteria met (partial credit)

A run fails if any criterion fails; this table counts the individual criteria that were met.

| Case | `claude-cli:sonnet` without → with | `claude-cli:haiku` without → with |
|---|---|---|
| clarify-hidden-ambiguity-sql | 9/9 → 9/9 | 9/9 → 9/9 |
| clarify-detailed-request | 6/6 → 6/6 | 6/6 → 6/6 |
| coverage-long-transcript | 36/36 → 36/36 | 36/36 → 36/36 |
| coverage-ticket-export | 24/24 → 24/24 | 22/24 → 24/24 |
| coverage-twelve-constraints | 36/36 → 36/36 | 36/36 → 36/36 |
| grounded-long-contract | 21/21 → 21/21 | 21/21 → 21/21 |
| grounded-near-miss-survey | 18/18 → 18/18 | 18/18 → 18/18 |
| verify-subtle-errors | 18/18 → 18/18 | 18/18 → 18/18 |
| verify-all-true | 6/6 → 6/6 | 6/6 → 6/6 |
| critique-pricing-memo | 9/9 → 9/9 | 9/9 → 9/9 |
| critique-expert-pushback | 9/9 → 9/9 | 9/9 → 8/9 |
| review-own-code-subtle-bugs | 15/15 → 15/15 | 15/15 → 15/15 |
| handoff-reversals | 27/27 → 27/27 | 26/27 → 25/27 |
| improve-support-bot-prompt | 15/15 → 14/15 | 15/15 → 15/15 |
| spec-destructive-job | 15/15 → 15/15 | 14/15 → 15/15 |
| tutor-debug-attempt | 0/6 → 6/6 | 0/6 → 6/6 |
| **All cases** | **264/270 → 269/270** | **260/270 → 267/270** |

## Limitations

- Small sample: a few runs per case. Treat differences of one or two runs as noise.
- The skill is placed in the system prompt, as an agent would after activating it; whether an agent selects the skill on its own is not tested here.
- A model grades the answers. Criteria are binary and specific, but spot-check `raw.jsonl` against your own judgment.
- Cases are synthetic and short; real tasks are longer and messier.

Raw answers and per-criterion grades: [raw.jsonl](raw.jsonl). Cases: [cases-hard.yaml](../../skills/cases-hard.yaml).
