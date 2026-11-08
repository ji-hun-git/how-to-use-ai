# Skill evaluation results

> Do the skills in [`skills/`](../../skills/README.md) actually change what a model does? We tested each one **with and without** the skill on the same cases, graded blind. This page reports what we found, including where the skills made no difference and a bug the evaluation caught in one of them.
> Method and harness: [evals/README.md](../README.md#skill-evaluations-with-vs-without) · Cases: [skills/cases.yaml](../skills/cases.yaml)

**Run date:** 2026-11-09 · **Models tested:** Claude Sonnet and Claude Haiku (via the Claude Code CLI, current versions on that date) · **Grader:** Claude Opus, blind to condition · **Runs:** 3 per case per condition

---

## Headline (round 2)

| Model | Trigger cases: without skill | Trigger cases: with skill | Control cases: without → with |
|---|---|---|---|
| Claude Sonnet | 42/48 (88%) | **47/48 (98%)** | 12/12 → 12/12 |
| Claude Haiku | 41/48 (85%) | **48/48 (100%)** | 12/12 → 12/12 |

- **Trigger cases** (16) are situations where a skill should improve the answer. **Control cases** (4) check that a skill doesn't break correct default behavior, for example by asking clarifying questions about a clear request.
- A run passes only if **every** criterion passes.
- **No control case regressed:** loading a skill never made a correct default answer worse.

## What the skills changed

| Skill | Sonnet without → with | Haiku without → with | What happened |
|---|---|---|---|
| **learning-tutor** | 0/3 → **3/3** | 0/3 → **3/3** | Without the skill, both models handed over complete homework solutions every time. With it, they gave hints and guiding questions. When the student typed "show solution", both showed it (control case, 3/3 either way). |
| **clarify-first** | 1/3 → 2/3 (offsite) | 0/3 → **3/3** (offsite) | Without the skill, models usually asked more than five questions at once on a vague request (counting questions bundled inside numbered items). With it, Haiku kept to a few targeted questions with defaults every time; Sonnet usually did. |
| **prompt-improver** | 3/3 → 3/3 | 2/3 → 3/3 | Haiku once left the improved prompt without a stated purpose; with the skill it didn't. |
| **task-spec** | 2/3 → 3/3 | 3/3 → 3/3 | Without the skill, one spec lacked a measurable target ("fast enough" undefined). |

## Where the skills made no measurable difference

On **16 of the 20 cases** (12 of the 16 trigger cases plus all 4 controls), both models passed 3/3 **with and without** the skill. The trigger cases at this ceiling:

- a vague report request (clarify-first)
- planted factual errors (verify-claims)
- an unverifiable citation (verify-claims)
- questions the document doesn't answer (grounded-answer)
- pushback on a correct answer, calm and emotional (honest-critique)
- critique of a flawed plan (honest-critique)
- missing requirements in code (fresh-eyes-review)
- a long chat with changed requirements (fresh-start-handoff)
- many requirements and deadlines buried in long notes (coverage-check)

Current Claude models already handle these short, clear-cut versions well. That matches the 2026 evidence in [docs/04](../../docs/04-failure-modes.md#-2026-update-how-current-models-fare): failures concentrate in **longer conversations, many simultaneous constraints and reference-heavy tasks**, which these short cases don't stress. We did not test smaller or other-vendor models here; based on the Haiku results, skills likely matter more as models get smaller.

---

## Change log: what the evaluation caught

**Round 1** ([results](2026-11-09-round1/summary.md))
- **Observed:** On the `task-spec` case, Sonnet *with* the skill failed 2 of 2 completed runs (it passed 3/3 without). One more run crashed. In the vague-report case, Sonnet also failed in both conditions.
- **Diagnosis (two causes):**
  1. **Test setup.** The CLI automatically tells the model about a working folder, so Sonnet tried to "look around the project" (printing a tool call it couldn't run) instead of answering. This affected both conditions.
  2. **A real flaw in the skill.** `task-spec` said "Explore before specifying: read the relevant code…". With no code available, the model went exploring instead of writing the spec. The crash was a separate harness problem: a long prompt passed on the command line exceeded the Windows length limit.
- **Changes:** (1) The base prompt in both conditions now says it's a text chat with no tools or files, and prompts are passed through standard input. (2) `task-spec` step 1 now reads: "Gather facts, but don't stall… if you can't access them, write the spec now… put unknowns in angle brackets and list the questions."

**Round 2** ([results](2026-11-09-round2/summary.md)): full rerun with the fixed setup and the **original** `task-spec` skill, so the setup fix and the skill fix could be judged separately. This is the headline above.

**Round 3** ([results](2026-11-09-round3-task-spec-fix/summary.md)): the **fixed** `task-spec` skill under the **round 1 setup** that exposed the flaw. Sonnet with the skill went from 0/2 to **3/3**; Haiku stayed 3/3.

This is the loop from [docs/13](../../docs/13-verifying-agent-runs.md): write the expected result first, find where the run diverged, change one thing, and rerun the same cases.

---

## Limitations

- **One model family.** Only Claude models were tested; an OpenAI run is ready in the harness but wasn't possible on the run date.
- **Small sample.** 3 runs per case and condition. Differences of one or two runs are within noise.
- **Short, synthetic cases.** Real tasks are longer and messier, which is where the 2026 research finds models fail most.
- **The skill is placed in the system prompt**, as an agent does after selecting it. Whether an agent *selects* the right skill on its own wasn't tested.
- **Model-graded.** The grader is from the same family as the models tested. Criteria are binary and specific, and we read every failing run's answer and the grader's reason (they matched). The grader counted questions strictly: a numbered item containing two questions counted as two.

## Files

| Folder | Contents |
|---|---|
| [2026-11-09-round1/](2026-11-09-round1/summary.md) | First run (setup issue present); 239 of 240 runs |
| [2026-11-09-round2/](2026-11-09-round2/summary.md) | Main results; 240 of 240 runs |
| [2026-11-09-round3-task-spec-fix/](2026-11-09-round3-task-spec-fix/summary.md) | Re-test of the fixed `task-spec` skill |

Each folder has `summary.md` and `raw.jsonl`, which holds every answer and every per-criterion grade with the grader's reason. Reproduce with:

```bash
python evals/skills/run.py --models claude-cli:sonnet claude-cli:haiku --judge claude-cli:opus --runs 3
```
