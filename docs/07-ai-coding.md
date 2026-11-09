# 07. AI coding: from vibe coding to agentic engineering

> **Coding agents** such as Claude Code, Codex, Gemini CLI, and Cursor read files, run commands, and edit code.
> Since late 2025, as agents came to be seen as reliable enough to hand off large chunks of work (Karpathy), the core skill has shifted from "writing code" to **"specifying, verifying, and taking responsibility."**

---

## 1. Vibe coding vs agentic engineering

| | Vibe coding | Agentic engineering |
|---|---|---|
| Coined by | Karpathy (2025-02-02) | Proposed by Karpathy in his one-year retrospective on vibe coding (2026-02-04); turned into a practical guide by Simon Willison |
| Definition | Move forward by looking only at results, **without reading** the code the AI wrote | Delegate to agents, but **a human is responsible** for the spec, plan review, diff checks, tests, and permission management |
| Good fit | Weekend projects, prototypes, learning experiments | Real services, team projects, code that ships |
| Karpathy's framing | Raises the floor (anyone can build) | Raises the ceiling (experts can do far more) |

> Simon Willison's rule (2025): **Don't commit code you couldn't explain to someone else.**

### What changed in 2026: from reading every line to verifying with evidence

In 2026, practitioners' advice moved a step further.

- **Karpathy (2026-10, HackerTube):** He used Claude Code to build, in about 2 hours, a site that collects 6,454 videos from about 40,000 Hacker News comments. All he did himself was set up the API keys, server, and domain; the agent handled deployment and even security hardening. He says he no longer reads or writes code directly.
- **Simon Willison (2026-05):** He admitted that as agents became reliable, he stopped reviewing even production code line by line, and said this makes him **uncomfortable**. He worries about risky practices gradually hardening into normal ones ("normalization of deviance"). He also points out that because agents now produce tests, documentation, and clean commits cheaply, those things alone **are no longer evidence of care**.
- **Simon Willison (2026-08):** He sums up the core skill as **giving clear instructions and confidently verifying they were carried out**, and says reading line by line was never the most effective way to verify a change.

**This repo's recommendation:** The direction is not "you don't need to read the code" but **"you must be able to say how you verified it."**

| Situation | How to verify |
|---|---|
| Learning, or an unfamiliar codebase | **Read and understand it yourself** (understanding can't be outsourced) |
| Work with good tests and verification tooling | Verify with test results, execution evidence, review agents, and working demos |
| Work involving money, personal data, security, or deployment | Evidence + **a human reviews the critical parts directly** |
| In every case | You must be able to answer "How did I confirm this change is correct?" |

---

## 2. Four reasons sessions disappoint

The official Claude Code documentation (2026) says a disappointing session almost always comes down to one of these four causes.

| Cause | Fix |
|---|---|
| ① **Information was missing** that the repo alone couldn't reveal | Provide symptoms, reproduction steps, intent, and constraints in the prompt or `AGENTS.md` |
| ② The agent **had no way to check its own work** | Provide criteria that yield pass/fail: tests, builds, linters, screenshot comparisons |
| ③ Rules that must never be broken **weren't enforced by tools** | Enforce them with hooks, permission deny rules, and CI, not prompts |
| ④ The default setup **cost more than the task was worth** | Scale reasoning effort and process to the size of the task |

### Two kinds of instructions

| Kind | Examples | Nature |
|---|---|---|
| **Requests** (non-deterministic) | Prompts, `CLAUDE.md`/`AGENTS.md`, skills | The model follows them most of the time, but **not 100%** |
| **Enforcement** (deterministic) | Hooks, permission deny rules, tests, CI | Applied **every single time** |

> Writing "Don't read `.env` files" in `CLAUDE.md` is a request. If it must hold, block it with **permission settings**.

---

## 3. The basic loop

```
0. Prepare        Short AGENTS.md, block access to secret files, sandbox, an approval mode that asks before risky actions
1. Explore/spec   Have it read the code (plan mode); if requirements are fuzzy, get interviewed and write SPEC.md
2. Plan           For multi-step work, review the plan before any code is written
3. Implement      Failing test first (Red → Green), plus criteria it can check on its own
4. Verify         Require evidence (commands run and their output, screenshots) + independent review by a new session or subagent
5. Merge          Only small PRs that state how they were verified
6. Learn          Add recurring mistakes to AGENTS.md, skills, or hooks
```

### Task template (OpenAI Codex's recommended four sections)

```markdown
## Goal
## Context       Relevant files, docs, exact error messages
## Constraints   Standards, rules, what not to touch
## Done when     Tests that must pass, how to verify
```

→ Full template: [templates/coding-task.md](../templates/coding-task.md), Full example: [examples/05-coding-agent.md](../examples/05-coding-agent.md)

### Give specific instructions

| ❌ | ✅ |
|---|---|
| Fix the login bug | Logging in after a session expires returns a 500 error. Look at the token refresh logic in `src/auth/`, write a failing test that reproduces it first, then fix it |
| Build this feature | (Tends to stop at a minimal implementation) → **State the level you want**, e.g., "Go beyond the basics and make it polished." The Claude Code docs say agents tend to build **the smallest thing** that satisfies the request |
| (Describing it in words) | Pass `@file` references, screenshots, and error logs **directly** |

---

## 4. Give it a way to check its own work (most important)

Agents often say "Done" when the work doesn't actually function. Give them **criteria that yield pass/fail**, and they will fix problems on their own as they go.

| Loose → strict | Example |
|---|---|
| Type checks, linters | `pnpm typecheck` |
| Existing tests | `pytest tests/cart` |
| A newly written failing test (Red → Green) | A test that reproduces the bug |
| A script that compares against expected output | Diff the output file against the answer file |
| Comparing browser screenshots with the mockup | UI work |

Whatever method you use, **demand evidence**. Ask to see **the commands that were run and their output**, not just "Tests passed."

> [!WARNING]
> Agents sometimes **hard-code values or edit the tests** to make tests pass. Anthropic recommends telling the agent that tests only check correctness and don't define the solution, and that if it thinks a test is wrong, it should report that instead of working around it.

### Red/Green TDD

This is Simon Willison's summary. Write the test **first** and confirm it fails (Red), then implement until it passes (Green). Confirming the failure first weeds out **tests that don't actually exercise the new code**. Good models understand the single phrase "use red/green TDD."

---

## 5. Plan mode and spec-driven development

### Plan mode

Most coding agents have a plan mode that **reads but doesn't edit** (both Claude Code and Codex support it). Start in plan mode for work that touches multiple files or has ambiguous requirements. You can also ask the agent to **interview you and push back on your assumptions**.

### Spec-Driven Development (SDD)

You write a spec first and implement against it. GitHub's [Spec Kit](https://github.com/github/spec-kit) is the best-known example (`constitution → specify → plan → tasks → implement`).

**Caveats (Birgitta Böckeler, Thoughtworks, 2025):**
- Using a heavy process for a small bug is overkill (in one case, a small bug ballooned into 4 user stories and 16 acceptance criteria)
- There are too many Markdown documents to review
- Agents sometimes **ignore** the spec, which can create an illusion of control

**Recommendation:** Match the process to the size of the work. SDD for large features, a one-paragraph prompt for small bugs. Spec Kit itself says no step is mandatory and suggests starting with **the smallest thing you need**.

---

## 6. Project memory files: AGENTS.md / CLAUDE.md

These are files the agent reads automatically at the start of every session. `AGENTS.md` is an open standard shared by many tools (maintained by the Agentic AI Foundation under the Linux Foundation), and Claude Code reads `CLAUDE.md`.

**Shared recommendations (Anthropic, OpenAI and agents.md)**
- **Keep it short.** Under 200 lines is recommended for CLAUDE.md
- **Don't write down what the code already tells you.** The Claude Code docs say explicitly that architecture overviews are no longer needed
- **Add one line each time a mistake recurs**
- Always include the build and test **commands** (a common mistake OpenAI cites: not telling the agent how to build and test)
- Move long procedures into skills

→ Template: [templates/AGENTS.template.md](../templates/AGENTS.template.md)

---

## 7. Tool changes in 2026

| Change | Details |
|---|---|
| **`/goal`: set a completion condition** | Introduced by Claude Code (2026-05), Codex (spring 2026), and Cursor (2026-08). Write the **outcome, constraints, and how to verify** in the goal, and the agent keeps working until the condition is met. The Codex docs note that starting a goal does not widen the agent's access permissions |
| **A ladder of enforcement** (Claude Code) | Write it in the prompt → `/goal` (another model checks the condition after every turn) → **Stop hook** (blocks the agent from finishing until the check passes) → `/code-review` (a fresh subagent reviews). The further along, the stronger the enforcement |
| **Auto mode is now the default** | Since 2026-08-14, Claude Code has made auto mode the default on the Pro, Max, and Team plans. According to Anthropic's announcement, in an experiment with 1,053 people, humans caught 13.6% of dangerous commands while the classifier caught about 89%. On the other hand, security researcher Johann Rehberger reported about an 80% success rate at inducing malware execution in Opus 5 auto mode (2026-08; the test designs differ, so a direct comparison isn't possible). The classifier beats approval fatigue but can be wrong, so put **"never" rules in deny rules, hooks, and sandboxes** |
| **All your agents at a glance** | Manage several running agents on one screen, as with `claude agents`, `codex agents`, and GitHub Copilot cloud |
| **Gemini CLI → Antigravity CLI** | Starting 2026-06-18, Google moved Gemini CLI for individual users to Antigravity CLI. Gemini CLI for enterprise and API-key users continues to ship. Skills, hooks, and subagents carry over |
| **"Use subagents to protect context" is outdated advice** | It was added to the "things you no longer need to do" table in the Claude Code docs. Use subagents for **parallel work, independent review, and separation of permissions**. (Simon Willison's guide still lists context protection as a main reason, so this is a point where opinions differ) |

> The basic principles (spec → plan → means of checking → evidence → learn) haven't changed. What changed is that **tools now support those principles directly**. `/goal` turns "done criteria" into a tool feature, the Stop hook does the same for "enforcement," and `/code-review` does it for "independent review."

---

## 8. Running a session

| Situation | What to do |
|---|---|
| The first minute | **Watch** whether the agent heads in the wrong direction. Stop it right away (Esc) and redirect |
| Still failing after two corrections | `/clear`, then write a **new prompt** that reflects what you learned |
| The topic changes | New session |
| Parallel work | Separate the workspaces with git worktree. Don't let two agents edit the same file at the same time |
| Independent review | A **new session/subagent**, not the one that wrote the code, reviews it against the spec |
| Too many review findings | Ask for "only issues that affect correctness." If you tell it it **must** find problems, it will find something, and fixing everything leads to over-engineering |

### Five questions before running unattended (Claude Code docs)

1. Does it know what "done" means?
2. Can it check the result on its own?
3. What is it allowed to touch?
4. What makes it stop? (maximum number of turns, budget limit)
5. Where do the results go, and who approves them?

---

## 9. Common mistakes (OpenAI Codex guide + Willison)

- Writing long-lived rules only in prompts instead of putting them in `AGENTS.md` or skills
- Not explaining how to build and test
- Skipping the plan on multi-step work
- Granting **full permissions** before understanding how the agent works
- Not using worktrees for parallel work
- Putting tasks on an automated schedule when they aren't reliable even when done by hand
- Running an entire project in a single chat
- **Opening PRs with agent code you haven't verified** → this pushes the real review burden onto your colleagues (Willison). In the PR, note how you verified it (test results, manual testing notes, screenshots or video)

---

## 10. Realistic expectations about productivity

- In METR's early-2025 experiment, experienced open-source developers were **19% slower** when using AI. They themselves felt 20% faster.
- In February 2026, METR said this result **no longer represents current tools**. A follow-up experiment (57 people, 800+ tasks) estimated time savings of 18% and 4%, but the confidence intervals were wide and participant selection bias was large, so METR itself called it "very weak evidence." In a May 2026 survey, the median self-reported speedup was 3x, but METR warned that this, too, may be an overestimate.
- Karpathy says that from around December 2025, agent output became large, coherent, and reliable enough that the unit of work shifted from "a few lines of code" to "delegating large units such as features, refactors, and tests." Still, he stresses that **agents are interns who make frequent mistakes**, and that the spec, review, and accountability remain the human's job.
- In October 2026, Karpathy gave three reasons people experience AI capability so differently: ① the size and duration of the problems they hand off, ② the domain (AI is strongest in coding and math, which tests can verify), and ③ the tier of tool they use (free vs paid vs internal). Someone who has only asked a free chatbot small questions and someone who has handed big tasks to a paid agent tool **are looking at different AIs**.

> Bottom line: Don't trust how fast it feels. **Measure it on your own work.**

---

### Sources

- Claude Code, Best practices (2026) — https://code.claude.com/docs/en/best-practices
- OpenAI Codex, Best practices — https://learn.chatgpt.com/guides/best-practices
- AGENTS.md open standard — https://agents.md/
- Anthropic, Prompting best practices (warning about hard-coding to pass tests) — https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- Anthropic, Effective harnesses for long-running agents (2025-11-26) — https://www.anthropic.com/research/effective-harnesses-for-long-running-agents
- GitHub Spec Kit — https://github.com/github/spec-kit
- Birgitta Böckeler, "Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl" (2025-10-15) — https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
- Karpathy, "vibe coding" post (2025-02-02) — https://x.com/karpathy/status/1886192184808149383
- Karpathy, Sequoia Ascent 2026 summary (2026-04-30) — https://karpathy.bearblog.dev/sequoia-ascent-2026/
- Simon Willison, "Not all AI-assisted programming is vibe coding" (2025-03-19) — https://simonwillison.net/2025/Mar/19/vibe-coding/
- Simon Willison, "Here's how I use LLMs to help me write code" (2025-03-11) — https://simonwillison.net/2025/Mar/11/using-llms-for-code/
- Simon Willison, Agentic Engineering Patterns (2026–) — https://simonwillison.net/guides/agentic-engineering-patterns/
- METR, Early-2025 AI study of experienced open-source developers (2025-07-10) — https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/

**2026 update (checked 2026-11-09)**
- Karpathy, post proposing "agentic engineering" (2026-02-04) — https://x.com/karpathy/status/2019137879310836075
- Karpathy, HackerTube (2026-10-31) — https://karpathy.bearblog.dev/hacker-tube/
- Karpathy, post on the gap in how people experience AI ("sharp funnel") (2026-10-11) — https://x.com/karpathy/status/2109361546505966046
- Simon Willison, "Vibe coding and agentic engineering are getting closer than I'd like" (2026-05-06) — https://simonwillison.net/2026/May/6/vibe-coding-and-agentic-engineering/
- Simon Willison, "More than just code review" (2026-08-22) — https://simonwillison.net/2026/Aug/22/more-than-just-code-review/
- Simon Willison, Subagents chapter — https://simonwillison.net/guides/agentic-engineering-patterns/subagents/
- Claude Code, What's new — https://code.claude.com/docs/en/whats-new
- Claude blog, auto mode becomes the default in Claude Code (2026-08) — https://claude.com/resources/articles/auto-mode-default-in-claude-code
- Simon Willison, attack case against Opus 5 auto mode (2026-08-27) — https://simonwillison.net/2026/Aug/27/breaking-claude-code-opus-5-auto-mode/
- OpenAI Codex, Long-running work (`/goal`) — https://learn.chatgpt.com/docs/long-running-work
- OpenAI Cookbook, Using Goals in Codex — https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex
- Cursor Changelog — https://cursor.com/changelog
- Google Developers Blog, transitioning Gemini CLI to Antigravity CLI (2026-05-19) — https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/
- GitHub Changelog, the connected Copilot cloud experience (2026-10-28) — https://github.blog/changelog/2026-10-28-work-from-anywhere-with-a-new-connected-copilot-cloud-experience
- METR, follow-up results from the productivity experiment (2026-02-24) — https://metr.org/blog/2026-02-24-uplift-update/
- METR, early-2026 self-report survey (2026-05-11) — https://metr.org/blog/2026-05-11-ai-usage-survey/
