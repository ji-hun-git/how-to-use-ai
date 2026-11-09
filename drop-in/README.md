# Drop-in rules: one file that changes how your AI works

One short rules file, packaged for each tool. 18 rules, each aimed at a documented failure mode (misunderstanding, omission, fabrication, sycophancy), with the research behind them listed at the bottom of the file.

| File | For |
|---|---|
| [AGENTS.md](AGENTS.md) | Codex, Cursor, Copilot, Gemini/Antigravity CLI and other coding agents (the open AGENTS.md standard) |
| [AGENTS.md](AGENTS.md) saved as `CLAUDE.md` | Claude Code |
| [cursor/how-to-use-ai.mdc](cursor/how-to-use-ai.mdc) | Cursor project rules |
| [custom-instructions.md](custom-instructions.md) | ChatGPT, Claude, Gemini and other chat apps (short and long versions) |

## Install in one line

Run these in your project's root folder.

**Codex, Copilot, Gemini CLI and other AGENTS.md agents** (if you already have an AGENTS.md, paste the rules into it instead):

```bash
curl -fsSL https://raw.githubusercontent.com/ji-hun-git/how-to-use-ai/main/drop-in/AGENTS.md -o AGENTS.md
```

**Claude Code** (if you already have a CLAUDE.md, append instead by changing `-o CLAUDE.md` to `>> CLAUDE.md`):

```bash
curl -fsSL https://raw.githubusercontent.com/ji-hun-git/how-to-use-ai/main/drop-in/AGENTS.md -o CLAUDE.md
```

**Cursor:**

```bash
mkdir -p .cursor/rules && curl -fsSL https://raw.githubusercontent.com/ji-hun-git/how-to-use-ai/main/drop-in/cursor/how-to-use-ai.mdc -o .cursor/rules/how-to-use-ai.mdc
```

**Chat apps:** open [custom-instructions.md](custom-instructions.md) and paste the short or long version into your app's instructions field.

> Want behavior that activates only when needed instead of always-on rules? Install the [skills](../skills/README.md).

## Instead of… write…

| Instead of | Write | Why |
|---|---|---|
| "Be accurate." | "If you can't verify something, say so and mark it unverified." | Gives the model permission to abstain, which counters its incentive to guess |
| "NEVER make mistakes!!!" | "Run the tests and show me the output before saying it's done." | A check the model can run beats emphasis; current models over-apply ALL-CAPS rules |
| "Think step by step." (to a reasoning model) | "Done when: …" plus the reasoning-effort setting | Reasoning models already think; they need a target |
| "You are a world-class expert." | "The reader is a non-technical manager deciding by Friday." | Personas don't reliably improve accuracy; audience and purpose do |
| "What do you think of my plan?" | "Another team wrote this plan. Find its 3 biggest weaknesses." | Hiding authorship reduces sycophancy |
| "Are you sure?" | "Check that against the source (or a test, or a calculation) and tell me what changes." | "Are you sure?" flips correct answers, and self-review with nothing new to check against tends to make answers worse |

## How to know it's working

- The agent asks one or two questions on vague tasks, and none on clear ones.
- It reports what it ran ("ran `npm test`: 42 passed") instead of "should work now".
- It says "I haven't opened that file" or "not in the documents" instead of guessing.
- Multi-part tasks end with a requirement checklist.
- When you push back without a reason, it explains why it's keeping its answer.

## Tradeoffs

Always-on rules add a little length and the occasional question. If your tasks are tiny and low-stakes, keep only rules 7–13 (fabrication and verification). Keep the file short: long instruction files are followed less reliably, so add project-specific lines sparingly and move must-never-break rules into hooks or permission settings.
