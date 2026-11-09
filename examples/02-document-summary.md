# Example 2. Summarizing a long document: preventing omission and fabrication at once

> When you summarize a 30-page set of meeting notes or a report, the most common failures are **dropping content from the middle (omission)** and **adding conclusions that aren't in the document (fabrication)**.

---

## The usual approach

```text
(paste document)
Summarize this.
```

- The summary focuses on the beginning and end of the document. The middle is poorly reflected (Lost in the Middle).
- Sometimes it adds **conclusions that aren't in the document**, such as "The team therefore agreed to …".
- With no length or audience specified, it's needlessly long.

---

## Improved prompt

```xml
<documents>
<document index="1" source="2026-11-05 weekly meeting notes">
(paste the full document)
</document>
</documents>

<context>
This summary is for an executive who missed the meeting and needs to grasp the decisions within 2 minutes.
</context>

<task>
1. First, extract the sentences in the document that relate to "decisions," "owners," "deadlines," and "open issues,"
   word for word and numbered, inside <quotes>. Go through the document from beginning to end without skipping anything.
2. Using only the <quotes> as evidence, write a summary in the format below.
</task>

<format>
## One-line bottom line
## Decisions (table: Decision | Owner | Deadline | Supporting quote number)
## Open issues (bullets, up to 5)
## Not confirmed in the document
(e.g., items with no deadline set, items with no owner)
</format>

<constraints>
- Don't add interpretations or conclusions that aren't in the document. Mark anything that requires inference as [inference].
- If an owner or deadline isn't in the document, write "TBD." Don't guess to fill it in.
</constraints>
```

---

## Why it's written this way

| Technique | Problem it prevents | Basis |
|---|---|---|
| Document on top, question below | Omission | Anthropic: putting long material first and the question last improves quality by up to 30% |
| Extract quotes first | Fabrication, omission | A technique recommended in Anthropic's "Reduce hallucinations" documentation |
| "Go through it from beginning to end" | Omission in the middle | Lost in the Middle (Liu et al., 2023) |
| "Write TBD" | Fabrication | Gives the model permission to say it doesn't know |
| "Not confirmed" section | Exposes omissions | Makes gaps visible instead of hiding them |
| Stating the audience and purpose | Misunderstanding | Length and perspective adjust automatically |

---

## Final human check (1 minute)

- [ ] I picked 2–3 **supporting quote numbers** from the decisions table and compared them with the original
- [ ] I checked that at least one decision from the **middle** of the document appears in the table
- [ ] I searched (Ctrl+F) to confirm that items marked "TBD" really aren't in the document

## When the document is very long (100+ pages)

Don't put it in all at once; process it **in parts**.

```text
Step 1: Extract only the list of sections in this document and the page range of each section.
Step 2: Extract the decisions and issues section by section. (Move to the next section when I say "next.")
Step 3: Combine the results from all sections into a final summary.
```
