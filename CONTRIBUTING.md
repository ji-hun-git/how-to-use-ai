# Contributing

Thanks for helping keep this guide accurate. The most useful contributions are reports of things that are wrong, outdated or broken.

## Report an issue

[Open an issue](https://github.com/ji-hun-git/how-to-use-ai/issues/new/choose) and pick the form that fits:

| Form | Use it when |
|---|---|
| **Wrong or outdated claim** | A statement, number or recommendation is incorrect, or newer evidence or an official guide has changed it |
| **Broken link** | A link is dead, moved, or points somewhere that no longer says what the text claims |
| **Skill problem** | A skill or rule misfires: it triggers when it shouldn't, doesn't trigger, or makes the answer worse |
| **Suggestion** | A missing topic, a better example, or a source worth adding |

## What makes a report easy to act on

- **Quote the exact text** and give the file (a link to the line is best).
- **Link the source.** For claims, link the paper, official documentation or changelog, and say what it says. Primary sources beat summaries.
- **For skills, include the input.** Paste the request you gave, the agent and model you used, what happened and what you expected. A case that reproduces the problem can go straight into the [eval suite](evals/README.md).

## How changes are made

This repository has a single maintainer and doesn't accept pull requests. Every report is read; accepted fixes are made by the maintainer, checked with `python scripts/validate.py`, and recorded in the [CHANGELOG](CHANGELOG.md). Skill changes are re-tested with the [with-vs-without harness](evals/README.md#skill-evaluations-with-vs-without) before they ship.

## Ground rules

- Evidence over opinion: claims need a source, and old statistics are labeled as historical.
- Plain English, short sentences, and no hype.
- Be respectful. See the [code of conduct](CODE_OF_CONDUCT.md).
