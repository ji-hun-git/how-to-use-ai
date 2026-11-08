# Meta-prompts: have the AI write your prompts

> Writing a good prompt from scratch is hard. **Letting the AI interview you or revise your draft** is much faster.
> Even so, adopt an AI-polished prompt only **after you've tested it and compared the results yourself**.

---

## A. Interview style: build the prompt by answering questions

```text
I want to hand off a ___ task to an AI, and I'd like to build a good prompt together.
Ask me about any missing information among Role, Context, Instruction, Format, Constraints, and Examples, one question at a time.
Once you have enough, give me a final, ready-to-use prompt in a code block.
```

## B. Improvement style: fix my prompt

```text
Improve the prompt below.
1) First, predict 3 bad results this prompt could produce. (Think in terms of misunderstanding / omission / fabrication.)
2) Give me a revised version that prevents those problems.
3) Summarize what you changed and why in a table.

<prompt>
(my prompt)
</prompt>
```

## C. Reverse-engineering style: extract a prompt from a good output

```text
Below is an output at the level I want. Write a prompt that can produce output like this again.
First analyze its audience, tone, structure, length, and unstated rules, then turn that analysis into a prompt.

<good_output>
...
</good_output>
```

## D. Turn it into a reusable template

```text
Based on what worked well in this conversation, create a reusable prompt template I can use the next time I do something similar.
Mark the parts that change as {{variable_name}}.
```

> Save templates you use often in each service's Projects, Custom GPTs, Gems, or Skills features so you don't have to paste them in every time.

---

## Caveats

- AI-polished prompts tend to get long and wordy. In its GPT-5.6 guide (2026-07), OpenAI reported that **prompts with the filler removed** scored about 10–15% better on internal coding-agent evaluations (a figure that shows direction).
- If "never," "always," or ALL-CAPS emphasis has crept in, take it back out. Current models follow this kind of emphasis too strictly.
- Run the before and after versions on **the same 3–5 inputs** and compare the results. ([docs/08-verification-and-evals.md](../docs/08-verification-and-evals.md))
