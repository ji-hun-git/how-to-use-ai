# Skill evaluation results (2026-11-09-round5-skill-fixes)

- Models under test: `claude-cli:sonnet`, `claude-cli:haiku`
- Grader: `claude-cli:opus` (blind to condition)
- Base system prompt (both conditions): "You are a helpful assistant in a text chat. In this conversation you cannot run tools, browse, or read files; answer in text."
- Case file: `cases-hard.yaml`
- Cases: 2 (2 trigger, 0 control), runs per case and condition: 5
- A run passes only if every criterion passes. **without** = plain assistant; **with** = SKILL.md loaded.
- Trigger cases test whether the skill improves the result; control cases test that it doesn't break correct default behavior.

## Overall

| Model | Case type | Without | With |
|---|---|---|---|
| `claude-cli:sonnet` | trigger | 10/10 | 10/10 |
| `claude-cli:sonnet` | control | 0/0 | 0/0 |
| `claude-cli:haiku` | trigger | 6/10 | 10/10 |
| `claude-cli:haiku` | control | 0/0 | 0/0 |

## By skill (trigger and control cases combined)

| Skill | `claude-cli:sonnet` without → with | `claude-cli:haiku` without → with |
|---|---|---|
| fresh-start-handoff | 5/5 → 5/5 | 2/5 → 5/5 |
| prompt-improver | 5/5 → 5/5 | 4/5 → 5/5 |

## By case

| Case | Kind | `claude-cli:sonnet` without → with | `claude-cli:haiku` without → with |
|---|---|---|---|
| handoff-reversals | trigger | 5/5 → 5/5 | 2/5 → 5/5 |
| improve-support-bot-prompt | trigger | 5/5 → 5/5 | 4/5 → 5/5 |

## Criteria met (partial credit)

A run fails if any criterion fails; this table counts the individual criteria that were met.

| Case | `claude-cli:sonnet` without → with | `claude-cli:haiku` without → with |
|---|---|---|
| handoff-reversals | 45/45 → 45/45 | 42/45 → 45/45 |
| improve-support-bot-prompt | 25/25 → 25/25 | 24/25 → 25/25 |
| **All cases** | **70/70 → 70/70** | **66/70 → 70/70** |

## Limitations

- Small sample: a few runs per case. Treat differences of one or two runs as noise.
- The skill is placed in the system prompt, as an agent would after activating it; whether an agent selects the skill on its own is not tested here.
- A model grades the answers. Criteria are binary and specific, but spot-check `raw.jsonl` against your own judgment.
- Cases are synthetic and short; real tasks are longer and messier.

Raw answers and per-criterion grades: [raw.jsonl](raw.jsonl). Cases: [cases-hard.yaml](../../skills/cases-hard.yaml).
