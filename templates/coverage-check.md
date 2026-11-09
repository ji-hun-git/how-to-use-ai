# Snippets to prevent omission (Coverage Check)

> **Omission**: skipping some of the requirements, missing content in the middle of long material, or cutting the output off partway.
> Causes and evidence are covered in [docs/04-failure-modes.md](../docs/04-failure-modes.md#2-omission).

The more instructions you give, the lower the chance that all of them are followed. In long material, the **middle section** is what gets missed most often (Lost in the Middle).

---

## A. Number the requirements and get a coverage table

```text
Requirements:
R1. ...
R2. ...
R3. ...

Add the table below at the end of your output.
| Requirement | Covered? (✅/⚠️/❌) | Where it's addressed | Notes |
```

> A **numbered list** makes each requirement easy to see and check off; requirements buried in long sentences are easier to miss.

## B. Long documents: have it quote the relevant parts first

```xml
<documents> ...long material... </documents>

First, extract the sentences relevant to the question, word for word, inside <quotes> tags.
Then write your <answer> using only the <quotes> as evidence.
```

## C. Process it section by section

```text
This document is long, so processing it all at once may cause parts to be missed.
Step 1: First, create only the table of contents (a list of sections).
Step 2: When I say "continue," process one section at a time.
```

Don't have the AI write a long report or a long translation in one pass; generate it **section by section**. That way you avoid the end getting cut off by output length limits.

## D. Cross-check when it's done

```text
Compare the output you just produced against my original request, line by line, and give me three separate lists:
(1) anything missing, (2) anything you added that I didn't ask for, (3) anything you handled vaguely.
```

## E. Final human check

- [ ] Does the number of requirements match the number reflected in the output?
- [ ] Is content from the **middle** of the material (e.g., pages 20–35 of a 50-page document) reflected?
- [ ] Does the output end abruptly or trail off with "…etc."?
- [ ] Do tables and lists have the same number of items as the source?
