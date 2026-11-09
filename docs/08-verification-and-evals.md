# 08. Verification and evals: from "looks good" to "is good"

> Verification checks whether **a single answer** is correct. Evaluation (evals) checks whether **a prompt or workflow** keeps working well.
> Both are easy to skip, but in the end this is where the quality of your AI use is decided.

---

## Part 1. Verifying a single answer

### 1. Basic principles of verification

| Principle | Why |
|---|---|
| **Check against outside evidence, not the AI's word** | Asking the same model "Is that right?" is not verification |
| **Don't ask "Are you sure?"** | Models changed their answers 46% of the time and accuracy dropped 17% (FlipFlop, 2023) |
| **Have it redo the work independently** | Solving it fresh, without seeing the earlier answer, avoids bias (Chain-of-Verification) |
| **Run whatever can be run** | Run the code, recalculate the numbers, open the links |
| **Scale verification to the risk** | You can't verify every answer to the same degree |

> Anthropic's official documentation also says that hallucination-reduction techniques **don't eliminate the problem entirely**, and advises always checking high-stakes information yourself.

### 2. The verification ladder

| Risk | Examples | What to do |
|---|---|---|
| **Low** | Ideas, drafts, personal notes | Skim + "What did you leave out, or what are you unsure about?" |
| **Medium** | Internal documents, reports, code review | + a requirements coverage table + check quotes against your own materials + a second opinion in a **new chat** |
| **High** | Legal, medical, or financial matters; anything published externally; production code | + **open every source** + lateral reading for every key claim + recalculate numbers yourself + run the tests + break it into atomic facts and check each |

### 3. The verification toolbox

**① Lateral reading**
Instead of reading deeply within a single page, professional fact-checkers **leave the page to see what other independent sources say**. The same goes for AI answers. Don't look only at the sources the AI gave you; look up the same fact **by a different route**.

**② Break it into atomic facts**
Break a long text into **one fact per sentence**, such as "X was founded in 2023" or "Revenue grew 12%," then check each one. This is the standard method used in research (FActScore, 2023).

```text
Break the answer above into verifiable atomic facts and number them.
Next to each fact, mark it as [sourced / from memory / inferred].
```

**③ Chain-of-Verification**
1. Draft → 2. Write verification questions → 3. Answer them independently, **without looking at the earlier answer** → 4. Revise based on the differences

**④ Multiple runs, multiple models**
Ask the same question in 2–3 new chats, or to models from other companies. **Where the answers differ** is the most suspect spot. (Agreement doesn't prove correctness.)

**⑤ Have it critique (red team)**
In a **different chat** from the one that wrote the answer, ask "Find the problems with this answer." Ask it to **find problems**, not to confirm.

**⑥ Execute**
- Code: run it and run the tests
- Numbers: recalculate in a spreadsheet or in code
- Links: click them yourself
- Quotes: Ctrl+F in the original

---

## Part 2. Evaluating prompts and workflows (evals)

For prompts you use often, templates your team shares, or agents you build yourself, create an **eval set**. That's how you know whether a prompt change **actually made things better**. For runnable examples, see [evals/](../evals/README.md): a promptfoo comparison of two prompts, and the with-vs-without tests this repo uses for its own skills.

### 1. First: success criteria

Anthropic says you need three things **before** you start refining a prompt:

1. A clear definition of your **success criteria**
2. A **way to test** against those criteria
3. A first **draft prompt**

If you don't have them, start there.

### 2. The lightest eval loop

```
1. Collect 20 real cases                    Mostly cases where the AI failed (Anthropic recommends 20–50)
2. Read the outputs yourself                A short note per failure → group similar ones → count them
3. Define pass/fail criteria                Pass/fail instead of a 5-point scale (recommended by Hamel Husain)
4. Revise the prompt → rerun everything     Fixing one thing can break another
5. Turn passing cases into regression tests Keep checking them on future revisions
```

### 3. Key advice from practitioners

**Hamel Husain & Shreya Shankar (Evals FAQ)**
- **Error analysis comes first.** Read real outputs (traces), classify the failure types, and count them. This is **the most important activity** in evals.
- **Grade only pass/fail.** Compared with a 5-point scale, decisions become clearer and consistency goes up.
- Review about 100, but annotate at least the first 30 **yourself**. Stop when no new failure types show up.
- General-purpose metrics such as ROUGE or BERTScore don't fit most LLM apps.

**Anthropic ("Demystifying evals for AI agents", 2026-01)**
- **Grade the outcome, not the process.** Not whether the agent said "I made the reservation," but whether the reservation actually exists in the database.
- Distinguish **capability evals** (low pass rate at first, a hill to climb) from **regression evals** (kept near 100%). Tasks that pass a capability eval "graduate" into the regression eval.
- **pass@k vs pass^k:** The probability of succeeding **at least once** in k tries is different from the probability of succeeding **every time** in k tries. If the single-try success rate is 75%, the chance of succeeding all 3 times is about 42%. For work that must be reliable every time, look at pass^k.
- **Read the transcripts.**

### 4. When AI does the grading (LLM-as-judge)

- Use it only for criteria that require judgment; check whatever code can check with code.
- First confirm the judge AI is trustworthy **by comparing it with human grading** (true positive rate, true negative rate).
- Write a separate judge prompt for each failure type.
- Example rubric: factual accuracy, citation accuracy, completeness, source quality (the criteria Anthropic's research system used).

```text
You are a grader. Judge pass/fail using only the single criterion below.
Criterion: Does every number in the answer actually appear in the <source> document?
Output: {"pass": true/false, "reason": "if it fails, which numbers are not in the document"}
```

### 5. The same question gives different answers each time

Wharton's Prompting Science Report 1 (2025) asked each question 100 times. Under the strict standard of "must be correct all 100 times to pass," GPT-4o scored only **about 5 percentage points above random guessing** (not statistically significant). That is why you shouldn't decide "it works" after trying once or twice.

---

> For agents (multi-step runs with tools), see [docs/13. Verifying agent runs](13-verifying-agent-runs.md): three levels of "done", five silent failures, and a test plan you rerun after every change.

### Sources

- Laban et al., FlipFlop "Are You Sure?" (2023) — https://arxiv.org/abs/2311.08596
- Dhuliawala et al., Chain-of-Verification (2023) — https://arxiv.org/abs/2309.11495
- Min et al., FActScore (2023) — https://arxiv.org/abs/2305.14251
- Civic Online Reasoning, Teaching Lateral Reading — https://cor.inquirygroup.org/curriculum/collections/teaching-lateral-reading/
- Anthropic, Reduce hallucinations — https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations
- Anthropic, Prompt engineering overview (success criteria first) — https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview
- Anthropic, Demystifying evals for AI agents (2026-01-09) — https://www.anthropic.com/research/demystifying-evals-for-ai-agents
- Anthropic, How we built our multi-agent research system (grading rubric) — https://www.anthropic.com/research/multi-agent-research-system
- Hamel Husain & Shreya Shankar, LLM Evals FAQ — https://hamel.dev/blog/posts/evals-faq/
- OpenAI, Prompt optimizer (narrowly defined graders) — https://developers.openai.com/api/docs/guides/prompt-optimizer
- Simon Willison, "Here's how I use LLMs to help me write code" (testing is the user's job) — https://simonwillison.net/2025/Mar/11/using-llms-for-code/
- Meincke et al., Prompting Science Report 1 (Wharton, 2025, preprint) — https://arxiv.org/abs/2503.04818
