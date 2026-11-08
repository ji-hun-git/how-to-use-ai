# 13. Verifying agent runs: when "it finished" doesn't mean "it worked"

> An agent can finish without a single error and still hand you something wrong: a missing row, a number from the wrong column, a placeholder that was never replaced. This guide covers how to tell a finished run from a correct one, the silent failures to look for, and how to improve an agent without breaking what already worked.

---

## 1. The problem: failures that don't announce themselves

Two familiar habits catch most problems with a chat answer: **fact-checking** (does this claim hold up?) and **debugging** (read the error, fix, rerun). Agents add a third kind of problem that neither habit catches: the run completes, the output looks polished, and there's no error message, but the content is wrong.

There is nothing to paste into a search box and nothing that looks off at a glance. The only way to catch it is to **compare the output with what the tools actually returned and with what you expected before you ran it.**

---

## 2. Three levels of "done"

"It works" can mean three different things. Say which one you've checked.

| Level | What's true | What's still unknown |
|---|---|---|
| **1. It ran** | The run finished without errors or crashes | Whether the tools returned real data, and whether the content is right |
| **2. It has the right shape** | The report, table or draft exists in the requested format | Whether the numbers, names and judgments inside it are correct |
| **3. It's right** | The output reflects the actual input data and tool results, every rule was applied, and you could use it as-is | — |

Only level 3 counts as done. To judge level 3 fairly, **write down what the output must contain before you look at it.** If you decide after seeing the result, a fluent, well-formatted answer pulls you toward "good enough". A list written in advance doesn't move. Section 4 shows how.

A real end-to-end run means: start from a real (or realistically structured) input, let the agent read it with its tools, apply its rules, and produce the result, all in one pass. A run that stops halfway, or ends in generic text that could have been written without the input, hasn't reached level 3.

---

## 3. Five silent failures

When a run "worked" but the output feels off, check these in order.

| # | Failure | What happens | How to catch it | Typical fix |
|---|---|---|---|---|
| 1 | **Filling an empty result** | A tool call succeeds but returns nothing (empty search, no matching rows, unreadable file), and the agent writes plausible content anyway | Open the raw tool output in the run log, or ask the agent to show exactly what each tool returned | Add a rule: "If a tool returns nothing, say 'no results' and why; never fill the gap" |
| 2 | **Wrong source or wrong number** | It cites an off-topic document, or copies a figure from the wrong row or column | Pick one or two key numbers and sources and check them against the original; if one is wrong, check them all | Quote-first and cite-or-retract rules ([grounded-answer](../skills/grounded-answer/SKILL.md)); compute with code |
| 3 | **Example text leaking into output** | Sample values from your own instructions (a placeholder company, a sample date) appear in the result in place of the real input | Plant a value that exists only in this test input (a distinctive client name, an order ID) and check it appears in the output | Mark examples clearly as examples, keep them different from real data, or remove them |
| 4 | **Inconsistent decisions** | The same input gets a different label or priority on a second run | Run the same input twice and compare the key decisions (wording may differ; decisions shouldn't) | Replace vague conditions with observable ones ([docs/12](12-writing-decision-rules.md)) |
| 5 | **Skipped step or approval** | It jumps to a final answer without running a required step (a calculation, a lookup, saving a record) or without asking for approval | List the required steps and check each one off against the run log | Make the step a hard requirement; enforce approvals with tool settings, not just instructions ([docs/11](11-skills-and-agent-rules.md)) |

> **Connected is not the same as used.** A tool only counts as used if the call succeeded, it returned non-empty data, *and* that data shows up in the output. Failure 1 is exactly the case where the first condition holds and the other two don't.

Failure 1 is the agent version of fabrication; a 2026 benchmark found that even with web search, errors compound over later turns of a conversation (HalluHard, preprint). Failure 4 is expected to some degree: in one study the same question asked 100 times gave different answers often enough that "worked once" was weak evidence ([Wharton Report 1](https://arxiv.org/abs/2503.04818)).

---

## 4. A test set you rerun after every change

When you fix one thing, something that used to work can quietly break. Guard against this with a small **test set** whose expected results you write *before* running, and rerun it after every change to a skill, tool or instruction. Fact-checking looks once; a test set looks again, the same way, every time.

### Three cases to start with

| Case | Input | What it checks |
|---|---|---|
| **Typical** | Your most common, well-formed input | The full path works and the required output items are present |
| **Missing or ambiguous** | An input missing a required field, or one that fits no rule cleanly | It asks or flags instead of guessing; exceptions and human sign-off work |
| **Key rule** | An input that a plain summary or search would get wrong, where your main rule must change the result | Your rule actually fires (this is usually a case that failed before) |

The key-rule case matters most: it's how you know a past failure stays fixed.

### Write three lines per case before running

> **Input:** the exact request or test file
> **Must include:** the labels, numbers (from tool results), sources or sections that must appear
> **Must not include:** things that mean failure, such as an unverified source, a sample value from your instructions, a number not in the data, an action taken without approval

The "must not include" line is the one people skip, and it's the one that catches the most. "Fails if the placeholder client name appears" catches failure 3 automatically; "fails if anything is sent without approval" catches failure 5.

**Example (an agent that summarizes a folder of supplier invoices):**
- **Input:** "Read the 12 invoices in /invoices/2026-10 and list totals by supplier, flagging duplicates."
- **Must include:** all 12 invoice numbers accounted for; a total per supplier that matches a recomputation; the two planted duplicate invoices flagged.
- **Must not include:** any supplier not present in the files; any total that doesn't match the sum of its invoices; the sample supplier name used in the instructions.

Start with three cases. Grow the set with every real failure you find, and keep cases that pass as regression checks. Anthropic recommends starting agent evaluations with 20–50 tasks drawn from real failures and grading what the agent actually produced, not what it said it did; this repo's [skill evaluations](../evals/README.md#skill-evaluations-with-vs-without) follow the same approach.

---

## 5. Preparing test data

| Situation | What to do |
|---|---|
| **You can use real data** | Replace names, contact details, account numbers and amounts with realistic fakes. Keep the format identical |
| **You can't use real data** | Build synthetic data with the **same structure**: same columns, same value formats (dates, ID lengths), similar sizes. Tests on differently shaped data pass and then fail on the real thing |
| **Always** | Include one deliberately broken file: blank cells, dates in the wrong format, text where a number should be. Clean data can't test error handling |
| **No time to build it** | Ask the AI to generate it, with a specific mix: "Create 20 rows with the same columns and formats as this sample, using fictional values: 15 normal, 3 duplicates, 2 with a missing amount." Then check the file before using it |

---

## 6. Finding the cause: work backwards, change one thing

When a result doesn't match the expected output, don't change several things at once. Narrow it down:

1. **Write the gap as one sentence.** Not "the output is weird" but "invoice INV-2207 should be flagged as a duplicate of INV-2198, but it's listed as normal." That sentence is also what you give the AI when asking for a fix.
2. **Walk backwards from the output** to the first step where the data went wrong: the final output, the input to the last step, the step before that. Typical findings:
   - The tool was **never called** → the tool's description or the instructions don't make clear when to use it.
   - The tool was called but **returned nothing** → a tool, permission or file-access problem.
   - The tool returned the **right data but the decision is wrong** → the rule's condition is missing or vague.
   Asking the agent to "show what each step received and produced" makes this much faster.
3. **Change one thing and rerun the same input.** If you edit the rule, the tool and the instructions together, you won't know which change helped (or hurt). A different input can't tell you whether the fix worked or you got lucky.

If something that used to work suddenly fails, suspect the most recent change first, and revert it if needed. If the whole pipeline is too tangled to diagnose, shrink it: run only the first step, check its output, then add the next step, until you see where it breaks.

---

## 7. Keep a change log

Whenever testing makes you change the design, a rule or a tool, record it in three parts:

> **Observed:** which input, what went wrong (or what limitation you hit)
> **Diagnosis:** which step or setting caused it, and why you think so
> **Change and result:** what you changed, and what happened when you reran the same test

The log helps when the same problem returns in a different form, keeps your written design in sync with what the agent actually does, and its "diagnosis" lines are often missing rules you can move straight into the skill.

**Example 1: changing how the work is done**
- **Observed:** asked the agent to write a 60-row reconciliation table directly in its reply; the table came back with 41 rows, and rows from the middle were missing.
- **Diagnosis:** long tables written out as text are prone to dropped rows; this is a known weakness of long outputs (see [LongWriter](https://arxiv.org/abs/2408.07055) and [Lost in the Middle](https://arxiv.org/abs/2307.03172)).
- **Change and result:** had the agent write and run code that reads the source file and writes the full table to a file instead; rerun: 60 of 60 rows, totals match.

**Example 2: adding an exception rule**
- **Observed:** in the supplier test, a scanned invoice with no readable total was included with a total of $0.
- **Diagnosis:** the skill said what to do with readable invoices but nothing about unreadable ones, so the agent filled in a value.
- **Change and result:** added "If an invoice's total can't be read, list it under 'Needs manual check' and exclude it from totals." Rerun: the invoice moved to the manual-check list; totals unchanged otherwise.

**A real example from this repo:** the [skill evaluation log](../evals/results/README.md#change-log-what-the-evaluation-caught) records how a first run exposed both a test-setup problem and a flaw in the `task-spec` skill, and how each was fixed and re-tested separately.

Keep the log next to the design or skill it changes (for example, in the repository, or a `CHANGELOG.md`), not in a separate scratch note that gets forgotten.

---

## 8. Measuring whether it's worth it

Judge an agent by comparing it with how the work is done today, on the **same inputs**:

| Step | What to measure | Example |
|---|---|---|
| **Baseline** | The current way: time taken, items processed, errors or omissions | Reconciling 12 invoices by hand: 50 minutes, 1 duplicate missed |
| **With the agent** | The same inputs, **including the time a person spends checking the result** | 15 minutes including review, 0 duplicates missed |
| **Qualitative judgments** | Use a rubric written in advance (e.g., "every total traceable to an invoice", "all duplicates flagged"), and ideally have someone else score the output | Not "I'd rate it 4 out of 5" |

Prefer numbers (time, omissions, error rate) over impressions. People are poor judges of their own speedup: in METR's 2025 study, experienced developers believed AI made them faster while measured time went up, and METR's 2026 survey warns that self-reported gains are likely inflated ([METR 2025](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/), [METR 2026](https://metr.org/blog/2026-05-11-ai-usage-survey/)).

---

## 9. Before you call it done

| Check | Question |
|---|---|
| **End-to-end run** | Did a realistic input go through reading, rules, tools and output in one pass? |
| **Tools really used** | Did each tool return non-empty data, and does that data appear in the output? |
| **Key rule fires** | Does the key-rule test case come out the way your rule says it should? |
| **No leftover examples** | Is the output free of sample names, dates or text from your instructions? |
| **Consistent** | Does running the same input twice give the same key decisions and required items? |
| **Exceptions and approvals** | Does it stop and flag missing information instead of inventing it? Did outward actions wait for approval? |
| **Design matches reality** | Are the changes you made during testing recorded and reflected in the written design or skill? |
| **Measured** | Did you compare with the current way of working, on the same inputs, with numbers first? |

If the first two are "no", fix those before polishing anything else: without them the run hasn't reached level 3.

---

## 10. When you're stuck

1. **Is there an error message?** If so, debug the usual way: read it, look it up or ask, fix, rerun.
2. **If not,** write the gap as one sentence: what should have appeared, and what appeared instead.
3. **Check the five silent failures** in order: empty result, wrong source or number, leftover example, inconsistency, skipped step.
4. **Walk backwards** from the output to the first step where the data went wrong.
5. **Change one thing,** rerun the test set, and write the three-line log entry.

Two or three passes through this loop solve most problems. If not, shrink the run to its first step and add steps back one at a time until you find where it breaks.

---

### Sources
- Anthropic, Demystifying evals for AI agents (2026-01: grade outcomes, not paths; start with 20–50 tasks from real failures; read the transcripts) — https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- Hamel Husain & Shreya Shankar, LLM Evals FAQ (error analysis first; binary pass/fail) — https://hamel.dev/blog/posts/evals-faq/
- Claude Code best practices (give the agent a check it can run; ask for evidence; hard controls vs instructions) — https://code.claude.com/docs/en/best-practices
- Anthropic, Harness design for long-running apps (2026-03: separate generator and evaluator; change one harness piece at a time) — https://www.anthropic.com/engineering/harness-design-long-running-apps
- HalluHard (2026-02, preprint: errors compound over turns, even with search) — https://arxiv.org/abs/2602.01031
- Meincke et al., Prompting Science Report 1 (2025: same question, 100 runs, results vary) — https://arxiv.org/abs/2503.04818
- Bai et al., LongWriter (2024: long outputs are bounded; split the work) — https://arxiv.org/abs/2408.07055
- Liu et al., Lost in the Middle (2023) — https://arxiv.org/abs/2307.03172
- METR, early-2025 developer study and 2026 self-report survey — https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ , https://metr.org/blog/2026-05-11-ai-usage-survey/
