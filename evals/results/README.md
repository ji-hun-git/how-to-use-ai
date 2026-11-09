# Skill evaluation results

> Do the skills in [`skills/`](../../skills/README.md) actually change what a model does? We tested each one **with and without** the skill on the same cases, graded blind, in two suites: 20 short cases, then 16 harder ones built to break current models. This page reports what we found, including where the skills made no difference and the flaws the tests exposed in our own skills.
> Method and harness: [evals/README.md](../README.md#skill-evaluations-with-vs-without), Cases: [cases.yaml](../skills/cases.yaml) (first suite) and [cases-hard.yaml](../skills/cases-hard.yaml) (harder suite)

**Run date:** 2026-11-09. **Models tested:** Claude Sonnet and Claude Haiku (via the Claude Code CLI, current versions on that date). **Grader:** Claude Opus, blind to condition, plus code checks for counts and exact IDs. **Runs:** 3 per case per condition (5 in the round 5 re-test)

---

## Headline

| Suite | Model | Trigger cases: without skill | Trigger cases: with skill | Control cases: without → with |
|---|---|---|---|---|
| First suite: 20 short cases ([round 2](2026-11-09-round2/summary.md)) | Claude Sonnet | 42/48 (88%) | **47/48 (98%)** | 12/12 → 12/12 |
| | Claude Haiku | 41/48 (85%) | **48/48 (100%)** | 12/12 → 12/12 |
| Harder suite: 16 cases ([round 4](2026-11-09-round4-hard-suite/summary.md)) | Claude Sonnet | 39/42 (93%) | **41/42 (98%)** | 6/6 → 6/6 |
| | Claude Haiku | 36/42 (86%) | **39/42 (93%)** | 6/6 → 6/6 |

- **Trigger cases** are situations where a skill should improve the answer. **Control cases** check that a skill doesn't break correct default behavior, for example by asking clarifying questions about a clear request.
- A run passes only if **every** criterion passes. Counting individual criteria on the harder suite, the skills took Sonnet from 264/270 to 269/270 and Haiku from 260/270 to 267/270.
- **No control case regressed** in either suite: loading a skill never made a correct default answer worse.
- Each headline run used the skills **as they were before** the fixes it led to (round 2: the original `task-spec`; round 4: the original `fresh-start-handoff` and `prompt-improver`), so those fixes don't inflate its numbers.

## What the skills changed

| Skill | Case | Sonnet without → with | Haiku without → with | What happened |
|---|---|---|---|---|
| **learning-tutor** | homework request (first suite) | 0/3 → **3/3** | 0/3 → **3/3** | Without the skill, both models handed over complete homework solutions every time. With it, they gave hints and guiding questions. When the student typed "show solution", both showed it (control case, 3/3 either way). |
| **learning-tutor** | student's buggy binary search (harder suite) | 0/3 → **3/3** | 0/3 → **3/3** | Without the skill, both models gave the corrected line and a full fixed function every time. With it, they pointed to where the bug was with a question and let the student write the fix. |
| **clarify-first** | vague offsite request (first suite) | 1/3 → 2/3 | 0/3 → **3/3** | Without the skill, models usually asked more than five questions at once. With it, Haiku kept to a few targeted questions with defaults every time; Sonnet usually did. |
| **coverage-check** | 9,000-word ticket export (harder suite) | 3/3 → 3/3 | 2/3 → 3/3 | Without the skill, Haiku once missed one of the 11 tickets. |
| **task-spec** | nightly job that deletes accounts (harder suite) | 3/3 → 3/3 | 2/3 → 3/3 | Without the skill, one spec gated the job but never limited the coding agent's own access to production. |
| **task-spec**, **prompt-improver** | first suite | task-spec 2/3 → 3/3 | prompt-improver 2/3 → 3/3 | Without the skill, one Sonnet spec lacked a measurable target and one Haiku prompt lacked a stated purpose. |

Across both suites, tutoring is the clearest effect: **without the skill, the models gave away the answer in 12 of 12 runs; with it, they gave hints in 12 of 12**, and still showed the solution when asked.

## Where the skills made no measurable difference

Most cases were at ceiling: both models passed every run **with and without** the skill.

- **First suite:** 16 of 20 cases, including planted factual errors, an unverifiable citation, questions the document doesn't answer, calm and emotional pushback, missing requirements in code, a chat with changed requirements, and buried deadlines.
- **Harder suite:** 10 of 16 cases, even though they were built to be hard:
  - a 1,900-word call transcript with 11 action items, some reassigned, rescheduled or cancelled
  - an email with 12 constraints, checked by code
  - a contract question with a false premise and a plausible but missing term
  - near-miss survey questions ("doctors" when only nurses were surveyed)
  - four subtle errors and an unverifiable citation mixed with true claims in a computing-history paragraph
  - a pricing memo whose arithmetic doesn't support its conclusion
  - a review of buggy code the assistant itself had just called complete
  - a SQL request with a hidden ambiguity
  - two controls: a fully specified out-of-office reply, and a paragraph where every claim is true

  Sonnet also got all 11 tickets right in the 9,000-word export every time.

Current Claude models handle these well, even in longer and messier forms than the first suite. The remaining differences came from **behavior a skill asks for that differs from the model's default** (hinting instead of answering), and from a smaller model on the longest or most tangled inputs. We did not test other vendors' models or inputs longer than about 9,000 words.

---

## Change log: what the evaluation caught

**Round 1** ([results](2026-11-09-round1/summary.md))
- **Observed:** On the `task-spec` case, Sonnet *with* the skill failed 2 of 2 completed runs (it passed 3/3 without). One more run crashed. In the vague-report case, Sonnet also failed 2 of 3 runs in both conditions.
- **Diagnosis (two causes):**
  1. **Test setup.** The CLI automatically tells the model about a working folder, so Sonnet tried to "look around the project" (printing a tool call it couldn't run) instead of answering. This affected both conditions.
  2. **A real flaw in the skill.** `task-spec` said "Explore before specifying: read the relevant code…". With no code available, the model went exploring instead of writing the spec. The crash was a separate harness problem: a long prompt passed on the command line exceeded the Windows length limit.
- **Changes:** (1) The base prompt in both conditions now says it's a text chat with no tools or files, and prompts are passed through standard input. (2) `task-spec` step 1 now reads: "Gather facts, but don't stall… if you can't access them, write the spec now… put unknowns in angle brackets and list the questions."

**Round 2** ([results](2026-11-09-round2/summary.md)): full rerun with the fixed setup and the **original** `task-spec` skill, so the setup fix and the skill fix could be judged separately. This is the first-suite headline above.

**Round 3** ([results](2026-11-09-round3-task-spec-fix/summary.md)): the **fixed** `task-spec` skill under the **round 1 setup** that exposed the flaw. Sonnet with the skill went from 0/2 to **3/3**; Haiku stayed 3/3.

**Round 4** ([results](2026-11-09-round4-hard-suite/summary.md)): the harder suite and the harder-suite headline above. The cases and their checks were written and verified before the main run. One case was added after a smoke test: two cases on Haiku, one run each, passed in both conditions, which showed the 1,900-word transcript was too short to stress the model. So we added the 9,000-word ticket export; nothing else changed after seeing results. Every failing run was read against the grader's reasons:
- **A real gap in `fresh-start-handoff`.** In a 23-message chat, the user renamed the talk and later said "I prefer the original title after all". Haiku carried the newer title into the handoff in 1 of 3 runs without the skill and 2 of 3 with it; one run even noticed the reversal but still flagged it as unsure instead of writing the original title. The skill said "keep only the final version" but not how to resolve a reversal.
- **A weaker issue in `prompt-improver`.** In 1 of 3 runs with the skill, Sonnet's improved support-bot prompt included an example, "refunds are available within 30 days", that the bot could repeat as real policy. This is the "example text leaking" failure from [docs/13](../../docs/13-verifying-agent-runs.md).
- **One grade we disagree with.** In the expert-pushback case, one Haiku run with the skill kept the correct answer, quoted the language reference and showed the shared default list. It failed only because it said "I'm not aware of any change in 3.8" instead of stating flatly that none exists. We left the recorded score unchanged.

**Round 5** ([results](2026-11-09-round5-skill-fixes/summary.md), [regression check](2026-11-09-round5-regression-check/summary.md))
- **Changes:**
  - `fresh-start-handoff` step 3 now says to resolve reversals ("go back to the original") to the value they mean, write it out, and treat outlines written before later changes as stale. Step 4 now says to flag only what is genuinely undecided.
  - `prompt-improver` step 4 now says to use marked placeholders for missing facts and keep invented example values out of the prompt.
- **Results with 5 runs:**
  - The reversal case went to **5/5** for Haiku with the fixed skill; without the skill Haiku passed 2/5, so 4 of 8 across both rounds. Sonnet stayed 5/5 either way.
  - The support-bot case went to **5/5** with the fixed skill on both models. Haiku without any skill invented a "30-day window" once (4/5).
- **Regression check:** the first-suite cases for both skills still passed 3/3 with the fixed skills on both models.

This is the loop from [docs/13](../../docs/13-verifying-agent-runs.md): write the expected result first, find where the run diverged, change one thing, and rerun the same cases.

---

## Limitations

- **One model family.** Only Claude models were tested; an OpenAI run is ready in the harness but wasn't possible on the run date.
- **Small sample.** 3 runs per case and condition (5 in the round 5 re-test). Differences of one or two runs are within noise; the tutoring effect (0/12 → 12/12) is the only one large enough to rule that out.
- **Synthetic cases, moderate length.** The longest input is about 9,000 words. Real tasks can be far longer and messier, and long-context failures grow with length.
- **The skill is placed in the system prompt**, as an agent does after selecting it. Whether an agent *selects* the right skill on its own wasn't tested.
- **Model-graded.** The grader is from the same family as the models tested. Criteria are binary and specific, counts and exact IDs are checked by code, and we read every failing run's answer and the grader's reason. They matched in all but the one case noted in round 4. The grader counted questions strictly: a numbered item containing two questions counted as two.
- **Fixes were re-tested on the cases that exposed them.** A fix tuned to one case can overfit it; the regression check on the first-suite cases is a partial guard.

## Files

| Folder | Contents |
|---|---|
| [2026-11-09-round1/](2026-11-09-round1/summary.md) | First suite, first run (setup issue present); 239 of 240 runs |
| [2026-11-09-round2/](2026-11-09-round2/summary.md) | First suite, main results; 240 of 240 runs |
| [2026-11-09-round3-task-spec-fix/](2026-11-09-round3-task-spec-fix/summary.md) | Re-test of the fixed `task-spec` skill |
| [2026-11-09-round4-hard-suite/](2026-11-09-round4-hard-suite/summary.md) | Harder suite, main results; 192 of 192 runs, with per-criterion partial credit |
| [2026-11-09-round5-skill-fixes/](2026-11-09-round5-skill-fixes/summary.md) | Re-test of the fixed `fresh-start-handoff` and `prompt-improver` skills, 5 runs |
| [2026-11-09-round5-regression-check/](2026-11-09-round5-regression-check/summary.md) | First-suite cases for the two fixed skills |

Each folder has `summary.md` and `raw.jsonl`, which holds every answer and every per-criterion grade with the grader's reason (or the code check's result). Reproduce with:

```bash
python evals/skills/run.py --models claude-cli:sonnet claude-cli:haiku --judge claude-cli:opus --runs 3
```

```bash
python evals/skills/run.py --cases-file evals/skills/cases-hard.yaml --models claude-cli:sonnet claude-cli:haiku --judge claude-cli:opus --runs 3
```

The 9,000-word ticket export is generated by [make_ticket_export.py](../skills/data/make_ticket_export.py) with a fixed seed; it prints the expected ticket IDs that the case checks.
