# Skill evaluation results (2026-11-09-round3-task-spec-fix)

- Models under test: `claude-cli:sonnet`, `claude-cli:haiku`
- Grader: `claude-cli:opus` (blind to condition)
- Base system prompt (both conditions): "You are a helpful assistant."
- Cases: 1 (1 trigger, 0 control), runs per case and condition: 3
- A run passes only if every criterion passes. **without** = plain assistant; **with** = SKILL.md loaded.
- Trigger cases test whether the skill improves the result; control cases test that it doesn't break correct default behavior.

## Overall

| Model | Case type | Without | With |
|---|---|---|---|
| `claude-cli:sonnet` | trigger | 3/3 | 3/3 |
| `claude-cli:sonnet` | control | 0/0 | 0/0 |
| `claude-cli:haiku` | trigger | 3/3 | 3/3 |
| `claude-cli:haiku` | control | 0/0 | 0/0 |

## By skill (trigger and control cases combined)

| Skill | `claude-cli:sonnet` without → with | `claude-cli:haiku` without → with |
|---|---|---|
| task-spec | 3/3 → 3/3 | 3/3 → 3/3 |

## By case

| Case | Kind | `claude-cli:sonnet` without → with | `claude-cli:haiku` without → with |
|---|---|---|---|
| spec-vague-coding-task | trigger | 3/3 → 3/3 | 3/3 → 3/3 |

## Limitations

- Small sample: a few runs per case. Treat differences of one or two runs as noise.
- The skill is placed in the system prompt, as an agent would after activating it; whether an agent selects the skill on its own is not tested here.
- A model grades the answers. Criteria are binary and specific, but spot-check `raw.jsonl` against your own judgment.
- Cases are synthetic and short; real tasks are longer and messier.

Raw answers and per-criterion grades: [raw.jsonl](raw.jsonl). Cases: [cases.yaml](../../skills/cases.yaml).
