# Skills: install the guide into your AI agent

These are [Agent Skills](https://agentskills.io): folders with a `SKILL.md` that compatible agents (Claude Code, Codex, GitHub Copilot, Gemini/Antigravity CLI, Cursor and others) load **automatically when the task calls for them**. Only each skill's name and description sit in context until it's needed, so installing all ten costs almost nothing.

Each skill turns one evidence-backed technique from this guide into agent behavior, and lists its sources at the bottom.

| Skill | Prevents | What it makes the agent do | Kicks in when… |
|---|---|---|---|
| [clarify-first](clarify-first/SKILL.md) | Misunderstanding | Ask ≤3 questions with defaults, restate goal and done criteria | A request is vague, large or multi-step |
| [coverage-check](coverage-check/SKILL.md) | Omission | Number requirements, work section by section, end with a coverage table | Many requirements or long inputs/outputs |
| [grounded-answer](grounded-answer/SKILL.md) | Fabrication | Quote evidence first, cite every claim, say what's missing, retract unsupported claims | Answering from documents, facts, citations |
| [verify-claims](verify-claims/SKILL.md) | Fabrication | Split a draft into atomic claims and check each independently | Fact-checking before something is used or published |
| [honest-critique](honest-critique/SKILL.md) | Sycophancy | Criteria first, biggest problems first, change position only on new evidence | Reviews, feedback, pushback |
| [fresh-eyes-review](fresh-eyes-review/SKILL.md) | Sycophancy, omission | Review the result against the spec as a reviewer who didn't make it | Before declaring work done |
| [fresh-start-handoff](fresh-start-handoff/SKILL.md) | Misunderstanding, sycophancy | Consolidate everything into one prompt for a new chat | Long or derailed conversations |
| [prompt-improver](prompt-improver/SKILL.md) | All four | Check the six elements, predict failures, return a leaner prompt | Writing or fixing prompts and agent instructions |
| [task-spec](task-spec/SKILL.md) | Misunderstanding, omission | Write Goal / Context / Constraints / Done when with a runnable check | Before delegating coding or agent work |
| [learning-tutor](learning-tutor/SKILL.md) | Skill loss | Hints before answers, check understanding | Studying, practicing, "teach me" |

---

## Install

### Claude Code (plugin, recommended)

```text
/plugin install how-to-use-ai --marketplace ji-hun-git/how-to-use-ai
```

On older versions, add the marketplace first, then install:

```text
/plugin marketplace add ji-hun-git/how-to-use-ai
```

```text
/plugin install how-to-use-ai@how-to-use-ai
```

### Any agent that supports skills (one command)

Uses the open-source [`skills`](https://github.com/vercel-labs/skills) installer, which supports dozens of agents:

```bash
npx skills add ji-hun-git/how-to-use-ai
```

### Manual install (copy the folders)

```bash
git clone https://github.com/ji-hun-git/how-to-use-ai.git
```

Then copy the folders inside `skills/` (each folder that has a `SKILL.md`) to the location your agent reads:

| Agent | Project-level folder | Personal (all projects) |
|---|---|---|
| Claude Code | `.claude/skills/` | `~/.claude/skills/` |
| Codex | `.agents/skills/` | `~/.agents/skills/` |
| GitHub Copilot | `.github/skills/` or `.agents/skills/` | `~/.copilot/skills/` or `~/.agents/skills/` |
| Gemini CLI | `.gemini/skills/` or `.agents/skills/` | `~/.gemini/skills/` or `~/.agents/skills/` |
| Other agents following the open standard | `.agents/skills/` | `~/.agents/skills/` |

For example, to install every skill for Claude Code in all your projects:

```bash
mkdir -p ~/.claude/skills && cp -r how-to-use-ai/skills/*/ ~/.claude/skills/
```

### Claude.ai and the Claude apps

Zip a skill folder (for example `grounded-answer/`, with `SKILL.md` at the top of the folder) and upload it in the **Skills** section of Settings. Menu names can change; check your app's help pages if it isn't there.

### Chat apps without skill support

Use the short rules in [drop-in/custom-instructions.md](../drop-in/custom-instructions.md), or paste a skill's steps into your project or custom instructions.

---

## Use

- Skills trigger automatically from their descriptions. You can also ask for one by name, e.g. "use grounded-answer for this", or in Claude Code type `/` and pick it (plugin skills appear as `/how-to-use-ai:<skill>`).
- They are deliberately small and single-purpose. Combine them: `task-spec` → work → `fresh-eyes-review`.

## Write your own

To build a skill for your own work, start from [templates/skill-template.md](../templates/skill-template.md) and the guide [docs/12. Writing decision rules](../docs/12-writing-decision-rules.md): a useful skill holds rules that change the result depending on the input, not just a tone and a layout.

## Format and validation

Each skill follows the [Agent Skills specification](https://agentskills.io/specification): a folder whose name matches the `name` field, YAML frontmatter with `name` and `description` (≤1024 characters, saying what it does and when to use it), and a Markdown body well under 500 lines. `python scripts/validate.py` checks these rules locally, and CI runs it on every push.

## Sources

- Agent Skills specification — https://agentskills.io/specification
- Claude Code skills and plugin marketplaces — https://code.claude.com/docs/en/skills , https://code.claude.com/docs/en/plugin-marketplaces
- Codex skills — https://learn.chatgpt.com/docs/build-skills
- GitHub Copilot agent skills — https://docs.github.com/en/copilot/concepts/agents/about-agent-skills
- Gemini CLI skills — https://geminicli.com/docs/cli/skills/
- `skills` installer — https://github.com/vercel-labs/skills
