# Security policy

This repository ships instructions that run inside AI agents: [skills](skills/README.md), [rules files](drop-in/README.md) and [templates](templates/). A security problem here is anything in them that could lead an agent to cause harm, for example:

- a skill or rule that could make an agent leak secrets, run destructive commands or skip a safety check
- wording that makes a skill easier to hijack with prompt injection from documents, web pages or tool output
- a recommendation in the guides that is unsafe, such as advice on permissions or sandboxing

## Reporting

Please report privately using GitHub's [private vulnerability reporting](https://github.com/ji-hun-git/how-to-use-ai/security/advisories/new) rather than a public issue. Include the file, the input or scenario, and what could go wrong.

You'll get a response on the report itself. Confirmed problems are fixed in the affected files and noted in the [CHANGELOG](CHANGELOG.md).

## Scope

The scripts in this repository (`scripts/`, `evals/`) are development tools that run locally and in CI; report problems with them the same way. Vulnerabilities in the AI tools themselves (Claude Code, Codex, Cursor and others) should go to their vendors.
