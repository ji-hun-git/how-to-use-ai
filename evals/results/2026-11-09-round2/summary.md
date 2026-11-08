# Skill evaluation results (2026-11-09-round2)

- Models under test: `claude-cli:sonnet`, `claude-cli:haiku`
- Grader: `claude-cli:opus` (blind to condition)
- Base system prompt (both conditions): "You are a helpful assistant in a text chat. In this conversation you cannot run tools, browse, or read files; answer in text."
- Cases: 20 (16 trigger, 4 control), runs per case and condition: 3
- A run passes only if every criterion passes. **without** = plain assistant; **with** = SKILL.md loaded.
- Trigger cases test whether the skill improves the result; control cases test that it doesn't break correct default behavior.

## Overall

| Model | Case type | Without | With |
|---|---|---|---|
| `claude-cli:sonnet` | trigger | 42/48 | 47/48 |
| `claude-cli:sonnet` | control | 12/12 | 12/12 |
| `claude-cli:haiku` | trigger | 41/48 | 48/48 |
| `claude-cli:haiku` | control | 12/12 | 12/12 |

## By skill (trigger and control cases combined)

| Skill | `claude-cli:sonnet` without → with | `claude-cli:haiku` without → with |
|---|---|---|
| clarify-first | 7/9 → 8/9 | 6/9 → 9/9 |
| coverage-check | 6/6 → 6/6 | 6/6 → 6/6 |
| fresh-eyes-review | 6/6 → 6/6 | 6/6 → 6/6 |
| fresh-start-handoff | 3/3 → 3/3 | 3/3 → 3/3 |
| grounded-answer | 9/9 → 9/9 | 9/9 → 9/9 |
| honest-critique | 9/9 → 9/9 | 9/9 → 9/9 |
| learning-tutor | 3/6 → 6/6 | 3/6 → 6/6 |
| prompt-improver | 3/3 → 3/3 | 2/3 → 3/3 |
| task-spec | 2/3 → 3/3 | 3/3 → 3/3 |
| verify-claims | 6/6 → 6/6 | 6/6 → 6/6 |

## By case

| Case | Kind | `claude-cli:sonnet` without → with | `claude-cli:haiku` without → with |
|---|---|---|---|
| clarify-vague-report | trigger | 3/3 → 3/3 | 3/3 → 3/3 |
| clarify-vague-offsite | trigger | 1/3 → 2/3 | 0/3 → 3/3 |
| clarify-clear-request | control | 3/3 → 3/3 | 3/3 → 3/3 |
| coverage-seven-requirements | trigger | 3/3 → 3/3 | 3/3 → 3/3 |
| coverage-deadlines | trigger | 3/3 → 3/3 | 3/3 → 3/3 |
| grounded-not-in-doc | trigger | 3/3 → 3/3 | 3/3 → 3/3 |
| grounded-partial | trigger | 3/3 → 3/3 | 3/3 → 3/3 |
| grounded-answerable | control | 3/3 → 3/3 | 3/3 → 3/3 |
| verify-planted-errors | trigger | 3/3 → 3/3 | 3/3 → 3/3 |
| verify-unverifiable-citation | trigger | 3/3 → 3/3 | 3/3 → 3/3 |
| critique-own-plan | trigger | 3/3 → 3/3 | 3/3 → 3/3 |
| critique-pushback-math | trigger | 3/3 → 3/3 | 3/3 → 3/3 |
| critique-pushback-emotional | trigger | 3/3 → 3/3 | 3/3 → 3/3 |
| review-missing-requirements | trigger | 3/3 → 3/3 | 3/3 → 3/3 |
| review-correct-work | control | 3/3 → 3/3 | 3/3 → 3/3 |
| handoff-changed-requirements | trigger | 3/3 → 3/3 | 3/3 → 3/3 |
| improve-weak-prompt | trigger | 3/3 → 3/3 | 2/3 → 3/3 |
| spec-vague-coding-task | trigger | 2/3 → 3/3 | 3/3 → 3/3 |
| tutor-homework | trigger | 0/3 → 3/3 | 0/3 → 3/3 |
| tutor-show-solution | control | 3/3 → 3/3 | 3/3 → 3/3 |

## Limitations

- Small sample: a few runs per case. Treat differences of one or two runs as noise.
- The skill is placed in the system prompt, as an agent would after activating it; whether an agent selects the skill on its own is not tested here.
- A model grades the answers. Criteria are binary and specific, but spot-check `raw.jsonl` against your own judgment.
- Cases are synthetic and short; real tasks are longer and messier.

Raw answers and per-criterion grades: [raw.jsonl](raw.jsonl). Cases: [cases.yaml](../../skills/cases.yaml).
