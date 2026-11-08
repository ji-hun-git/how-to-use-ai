<!--
  Project memory file template
  - Coding agents read this file automatically at the start of every session.
  - File name: AGENTS.md (an open standard read by many tools, including Codex, Cursor, and Gemini CLI) or CLAUDE.md (Claude Code)
  - Copy this template, save it as AGENTS.md in your project root, and fill it in.
    (It's named AGENTS.template.md so that it isn't picked up as a real AGENTS.md.)

  Writing principles (shared recommendations from Anthropic, OpenAI, and agents.md)
  1. Keep it short. For CLAUDE.md, under 200 lines is recommended. If it's long, important rules get buried.
  2. Don't write things the agent can learn by reading the code (folder structure, languages used, etc.).
  3. Add one line each time the agent repeats the same mistake.
  4. Instead of ALL-CAPS emphasis like "IMPORTANT" or "NEVER!!!", add a one-line reason.
  5. Enforce rules that must always be followed with hooks, CI, or permission settings, not with this file.
     What's in this file is only a request that is "mostly followed."
-->

# AGENTS.md

## Commands
- Install: `pnpm install`
- Test (single file): `pnpm test path/to/file.test.ts`  ← the full suite takes 5 minutes, so prefer single files
- Lint/type check: `pnpm lint && pnpm typecheck`
- Run locally: `pnpm dev` (port 3000)

## Code rules (only what you can't tell from the code)
- For dates, use the wrapper in `src/lib/time.ts`, not `dayjs` (to prevent time zone bugs)
- Define API response types only in `src/types/api.ts`
- Ask before adding a new dependency

## How to work
- Before making changes, run the relevant tests first to check the current state
- For bug fixes, start by writing a reproduction test
- Commit messages use the Conventional Commits format (`feat:`, `fix:` …)

## Common mistakes (add as you find them)
- Don't modify the `legacy/` folder. An external system references it directly
- Only create new migration files; never modify existing ones

## More detailed docs (read only when needed)
- Deployment procedure: `docs/deploy.md`
- Architecture decision records: `docs/adr/`
