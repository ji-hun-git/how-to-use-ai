# Skill evaluation results (2026-11-09-round5-regression-check)

- Models under test: `claude-cli:sonnet`, `claude-cli:haiku`
- Grader: `claude-cli:opus` (blind to condition)
- Base system prompt (both conditions): "You are a helpful assistant in a text chat. In this conversation you cannot run tools, browse, or read files; answer in text."
- Case file: `cases.yaml`
- Cases: 2 (2 trigger, 0 control), runs per case and condition: 3
- A run passes only if every criterion passes. **without** = plain assistant; **with** = SKILL.md loaded.
- Trigger cases test whether the skill improves the result; control cases test that it doesn't break correct default behavior.

## Overall

| Model | Case type | Without | With |
|---|---|---|---|
| `claude-cli:sonnet` | trigger | 6/6 | 6/6 |
| `claude-cli:sonnet` | control | 0/0 | 0/0 |
| `claude-cli:haiku` | trigger | 5/6 | 6/6 |
| `claude-cli:haiku` | control | 0/0 | 0/0 |

## By skill (trigger and control cases combined)

| Skill | `claude-cli:sonnet` without → with | `claude-cli:haiku` without → with |
|---|---|---|
| fresh-start-handoff | 3/3 → 3/3 | 3/3 → 3/3 |
| prompt-improver | 3/3 → 3/3 | 2/3 → 3/3 |

## By case

| Case | Kind | `claude-cli:sonnet` without → with | `claude-cli:haiku` without → with |
|---|---|---|---|
| handoff-changed-requirements | trigger | 3/3 → 3/3 | 3/3 → 3/3 |
| improve-weak-prompt | trigger | 3/3 → 3/3 | 2/3 → 3/3 |

## Criteria met (partial credit)

A run fails if any criterion fails; this table counts the individual criteria that were met.

| Case | `claude-cli:sonnet` without → with | `claude-cli:haiku` without → with |
|---|---|---|
| handoff-changed-requirements | 9/9 → 9/9 | 9/9 → 9/9 |
| improve-weak-prompt | 12/12 → 12/12 | 11/12 → 12/12 |
| **All cases** | **21/21 → 21/21** | **20/21 → 21/21** |

## Limitations

- Small sample: a few runs per case. Treat differences of one or two runs as noise.
- The skill is placed in the system prompt, as an agent would after activating it; whether an agent selects the skill on its own is not tested here.
- A model grades the answers. Criteria are binary and specific, but spot-check `raw.jsonl` against your own judgment.
- Cases are synthetic and short; real tasks are longer and messier.

Raw answers and per-criterion grades: [raw.jsonl](raw.jsonl). Cases: [cases.yaml](../../skills/cases.yaml).
