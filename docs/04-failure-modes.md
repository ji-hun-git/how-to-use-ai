# 04. Three ways AI gets things wrong: Misunderstanding, Omission, Fabrication

> Most AI failures fall into one of three failure modes, plus a fourth, sycophancy, when you ask the AI for its judgment. **Diagnose a failure by its type**, and the fix becomes clear.
>
> - **Misunderstanding**: it interpreted the request differently
> - **Omission**: it left out something it should have done
> - **Fabrication (hallucination)**: it made up something that doesn't exist
>
> As a bonus, we also cover **sycophancy** (going along with the user), which often shows up alongside the three.

---

## 2026 update: how current models fare

Many of the studies in the main text below measured 2023–2025 models. **The causes and remedies still hold**, but the numbers may differ for current models. Here is what 2026 measurements on current models found.

| Failure | 2026 measurement | What it means |
|---|---|---|
| **Fabrication: summarizing material** | On tasks that summarize provided material, 2026 flagship models hallucinate at about 7–14% (Vectara leaderboard, 2026-10). In many cases newer, larger models are **no better** than smaller, older ones | Even when you provide the material, **you still need to check against the source** |
| **Fabrication: questions it can't answer** | Asked about facts they didn't know, 26 models guessed wrong 22–94% of the time (Stanford AI Index 2026). As of October 2026, some of the latest models are down sharply to 4–11%, with a **stronger tendency to say they don't know** (Artificial Analysis) | "If you don't know, say so" is still key |
| **Fabrication: references** | In an experiment generating medical references with 26 models, 55.4% of responses contained fake references. **Five models released in 2026 still hit 35.3%** (Topaz et al., 2026-09, preprint). The model with the lowest rate (10.2%) got there by refusing 52% of requests | **Always check sources the AI cites yourself, even now** |
| **Fabrication: even with web search on** | On hard questions requiring inline citations, even top models with web search on hallucinated about 30% of the time. Errors accumulated later in the conversation (HalluHard, 2026-02, preprint) | Search helps, but it's not a cure-all |
| **Fabrication: courtroom incidents** | **2,266** cases in which AI-fabricated case law or similar material was submitted to courts (as of 2026-11-05; 1,535 in the US). Up about 40% in five months from about 1,600 in June 2026 | Even as models improve, incidents keep rising because of **people who don't check** |
| **Sycophancy** | 11 AI systems endorsed users' actions **about 49% more often** than humans did, and people trusted and preferred sycophantic answers more (Cheng et al., *Science*, 2026-03, peer-reviewed) | Sycophancy persists **because people like it** |
| **Sycophancy: long conversations** | When a wrong claim was pushed repeatedly on current flagship models, the rate of caving within 5 turns was 0–57% → **20–97% within 25 turns**. Even when models caved, the correct answer often remained in their reasoning (SPINE, 2026-09, preprint) | The longer and more emotionally charged the pressure, the more it goes along → **start a new chat** |
| **Sycophancy: framing as your belief** | Stating something false as **"I believe ..."** collapses accuracy (GPT-4o 98.2% → 64.4%). The same content attributed to a third party gets filtered out well (AI Index 2026) | Don't lead with your own view when you ask |
| **Omission: long input** | Finding a single sentence within 1 million tokens: **100%** for the top three models. But on tasks that chain several pieces of information, performance drops as length grows, and some models fall sharply between 512K and 1M tokens (Chow, 2026-05, preprint) | **Retrieval is solved; synthesis is not.** Including only the material you need still matters |
| **Omission: simultaneous constraints** | In an experiment with 15 models, the rate of following every constraint dropped sharply once simultaneous constraints **exceeded 5–6**. A model with a 41% per-constraint pass rate at 8 constraints followed all 8 only 5.7% of the time (Vasileva, 2026-08, preprint) | Cut constraints, and if there are many, **split into steps** |
| **Misunderstanding: multiple turns** | Spreading requirements across multiple turns lowered performance by 39% on average (Laban et al.). **Formally published at ICLR 2026**. No re-measurement with 2026 models yet | Give all requirements up front |

> **The 2026 takeaway:** Current models have gotten better at saying "I don't know," but they are still weak at **fabricating sources, sycophancy in long conversations, and following many constraints at once**. And real-world incidents are actually rising. The better models get, the more your verification habits matter.

---

## At a glance

| | Misunderstanding | Omission | Fabrication (hallucination) | Sycophancy |
|---|---|---|---|---|
| **Symptoms** | A plausible answer headed in the wrong direction | Some requirements missing, content from the middle of a document left out, output cut off partway | Nonexistent facts, numbers, sources, case law, functions | Agrees with your opinion; flips even a correct answer when you push back |
| **Main causes** | Vague request + the AI assumes instead of asking | Misses the middle of long input; drops some instructions as they multiply; output length limits | Training and evaluation reward guessing when unsure | Training that rates answers people like more highly |
| **Prevention** | Context, goals, and done criteria; questions first; confirm understanding | Numbered requirements; material on top, question at the bottom; split the work | The right to say "I don't know"; provide material; quotes first | Hide your opinion; ask for criticism; set criteria first |
| **Detection** | Have it surface its assumptions; have it restate the request | Coverage table; compare against the source | Open sources yourself; ask several times and compare; verification questions | Cross-check in a new chat or with another model |
| **Recovery** | Summarize, then start a new chat | Ask again only for what's missing | Make it retract unsupported claims | Ask for evidence (never just "Really?") |
| **Template** | [clarify-first](../templates/clarify-first.md) | [coverage-check](../templates/coverage-check.md) | [grounded-answer](../templates/grounded-answer.md) | [honest-critique](../templates/honest-critique.md) |

---

## 1. Misunderstanding

### Symptoms

- You said "fix it" and got only suggested fixes (or the reverse)
- You wanted an explanation for a new hire and got a document written for experts
- The output looks plausible, but **it's not what you wanted in the first place**

### Why it happens

1. **Requests are full of gaps.** People often leave important conditions unstated.
2. **AI isn't good at noticing ambiguity.** On a benchmark built from about 12,000 ambiguous questions (CLAMBER, 2024), models' ability to recognize ambiguous questions and ask for clarification fell short of practical use. Chain-of-thought and examples brought only minor improvements and sometimes even led to **overconfidence**.
3. **It carries early assumptions all the way through.** In a study that simulated more than 200,000 conversations across 15 models (Laban et al., 2025), giving the same requirements **spread across multiple turns** lowered performance by **39% on average** compared with giving them all at once. The models formed assumptions early and failed to recover from them.
4. **Even questions that look clear can be read differently.** Simply having the model rephrase the question itself (Rephrase and Respond, 2023) substantially improved performance across many tasks. In other words, a question that's clear to a person may not be clear to a model.

### Prevention

| Method | Example prompt | Evidence |
|---|---|---|
| **Name the action with a precise verb** | "Make the edits directly," not "suggest changes" | Anthropic: if you ask "Can you suggest some changes?", it may only suggest them rather than actually make them |
| **State the purpose and the reason** | "This email turns down their offer, but I want to keep the relationship" | Anthropic: knowing the reason helps it target more precisely |
| **Write done criteria** | "Done when a non-technical executive can decide within a minute" | Anthropic: define success criteria |
| **Give all requirements up front** | Don't tack them on over several turns | Laban et al. 2025 |
| **Allow questions, but cap the number** | "Ask at most 3 questions, only the important ones" | Asking only the necessary questions works better than asking about everything (Zhang & Choi, 2023) |
| **Show examples** | → [03. Teaching with examples](03-examples-few-shot.md) | Anthropic, Google |
| **Separate material and instructions with tags** | `<document>` / `<task>` | Anthropic: separating them reduces misinterpretation |

### Detection

```text
Before answering, restate my request in your own words in 2–3 sentences, and list the assumptions you're making as bullets.
```

Once its understanding is on screen, you can catch a wrong interpretation **before the real answer arrives**.

### Recovery

If the conversation has gone off track, don't keep asking for fixes in the same conversation. Laban et al. recommend:

1. Ask, "Consolidate everything I've told you so far into a single request."
2. Edit that summary and paste it into a **new chat**.

→ Snippet collection: [templates/clarify-first.md](../templates/clarify-first.md)

---

## 2. Omission

### Symptoms

- Only 5 of 7 requirements are addressed
- You summarized a 50-page document, and pages 20–35 are missing
- Long output gets cut off midway or trails off with "...and so on"
- The table has fewer rows than the source

### Why it happens

**① The middle of a long input is the easiest part to miss (Lost in the Middle)**
- Models find the answer well when the relevant document sits at the **beginning or end** of the input, but performance drops sharply when it's in the **middle** (Liu et al., 2023). In one experiment, when the answer document was in the middle of 20 documents, GPT-3.5 did worse than **when it was given no documents at all (56.1%)**.
- Recent measurements look similar. In an experiment requiring the model to find information that shares no words with the question (NoLiMa, 2025), GPT-4o's accuracy fell from 99.3% on short inputs to 69.7% at 32K tokens. Chroma's 2025 report (Context Rot), which tested 18 models, also found that as input grows longer, performance becomes unstable **even on simple tasks**.
- **Adding more material doesn't make it better.** Increasing the retrieved documents from 20 to 50 raised accuracy by only 1–1.5% (Liu et al.).

**② The more instructions, the more get dropped**
- As the number of instructions grows, **the chance of following them all falls steadily** (ManyIFEval, 2025). In an experiment with 500 instructions (IFScale, 2025), even the best model followed only 68%, and models tended to **follow earlier instructions better**.

**③ Output length has limits**
- In a 2024 study (LongWriter), models of the time could read 100,000 tokens but struggled to write more than 2,000 words, because their training data contained few answers that long. When asked to write **section by section**, they produced coherent text of 20,000+ words. Current models have higher limits, but the principle is the same.

### Prevention

| Method | Explanation |
|---|---|
| **Number the requirements** | Writing R1, R2, R3... makes it easy to check for gaps |
| **Put key constraints first, and repeat them at the end** | Combines the tendency to follow earlier instructions with the tendency to remember the beginning and end best (an inference from combining research findings) |
| **Long material on top, question at the very bottom** | Anthropic: up to 30% better quality |
| **Have it quote the relevant parts first** | Anthropic: helps it focus on what's relevant and ignore the rest |
| **Only the material you need** | More doesn't make it better |
| **Split the work** | Long documents section by section; long outputs as outline → sections |
| **More than 5–6 constraints? Split into steps** | Prompt chaining → [06. Workflows](06-workflows.md) |
| **A per-section tracking table** | "Every section must appear in the table. If there's no relevant content, write 'N/A'" → prevents silent skipping |

### Detection

```text
Add a table at the end of the output: | Requirement | Addressed? (✅/⚠️/❌) | Where |
```

```text
Compare the output you just wrote against my original request line by line, and tell me what's missing and anything you added that I didn't ask for.
```

> [!TIP]
> **2026 caveat:** Anthropic advises that Claude Opus 5 reviews its own work well without being told to, so verification instructions written for older models can cause **over-verification** (this guidance applies to Opus 5 specifically; self-checking itself is still recommended). Self-check instructions help most **when there are many requirements or you're using a smaller model**.

### Recovery

Don't have it rewrite everything; ask **only for the missing parts**. A full rewrite may drop something else this time.

```text
R4 and R6 are missing. Leave everything else as is, and give me a version that adds just those two items.
```

→ Snippet collection: [templates/coverage-check.md](../templates/coverage-check.md)

---

## 3. Fabrication (hallucination)

### Symptoms

- Papers, court cases, statistics, or URLs that don't exist
- It cites a real source, but **that source doesn't say that**
- Library functions or API options that don't exist
- Conclusions added that aren't in the material
- Wrong calculations

### Why it happens

OpenAI researchers (Kalai et al., 2025) explain why hallucinations happen:

1. **Pretraining:** rare facts with no pattern, like birthdays, can't be told apart from plausible wrong answers, so errors are statistically inevitable.
2. **Evaluation and training:** most benchmarks give zero points for "I don't know," so **models that guess score better.** It's like a student for whom guessing beats leaving an answer blank.

A comparison OpenAI published shows this clearly.

| Model | Abstention rate | Accuracy | Error rate |
|---|---|---|---|
| gpt-5-thinking-mini | 52% | 22% | 26% |
| o4-mini | 1% | 24% | **75%** |

> The model that guesses (o4-mini) has slightly higher accuracy, but its **error rate is three times higher**. Judged on accuracy alone, it even looks better.
> (Source: OpenAI, "Why language models hallucinate" (2025); figures checked against the original page on 2026-11-09.)

**Sources are especially risky.**
- A 2023 study checked 636 citations in 84 literature reviews written by ChatGPT and found that **55%** of GPT-3.5's citations and **18%** of GPT-4's did not exist. Even among the citations that **did exist**, 43% (GPT-3.5) and 24% (GPT-4) contained content errors (Walters & Wilder, *Scientific Reports*). *(Based on 2023 models. For a 2026 measurement, see Topaz et al. in the table above: even models released in 2026 included fake references in 35.3% of responses.)*
- In law, since Mata v. Avianca (2023), cases in which AI-fabricated case law was submitted to courts have kept rising, reaching **2,266** (2026-11-05) according to Damien Charlotin's database.
- Stanford researchers reported that even **specialized legal AI tools** hallucinated on 17–34% of queries (Journal of Empirical Legal Studies, 2025. *Based on 2024 tools*).

### Prevention

| Method | Example prompt | Evidence |
|---|---|---|
| **The right to say "I don't know"** | "If you're not sure, write 'Unknown.' That's better than a wrong answer." | Anthropic: allowing uncertainty greatly reduces false information / Kalai et al.: offsets the incentive to guess |
| **Provide the material directly** | Paste in documents, manuals, data | Google: grounding reduces hallucinations and makes sources traceable |
| **Ground it only in the material** | "Answer using only the documents I provided" | Anthropic, "external knowledge restriction" |
| **Quotes first, answer second** | "Extract the relevant sentences verbatim, then answer based only on them" | Anthropic, "direct quotes for factual grounding" |
| **Retract what it can't cite** | "Attach a supporting quote to each claim, and delete any claim you can't find one for" | Anthropic, "verify with citations" |
| **Turn on search** | Questions that need current information, statistics, or sources | Karpathy: use search tools for facts |
| **Calculate with code** | "Calculate this in Python and show the code" | Karpathy: use code execution for math and data |
| **No guessing about what it hasn't opened** | (Coding) "Don't speculate about code you haven't opened; read the file first" | Anthropic agentic coding guide |
| **Mark confidence** | "Tag each claim as [verified] / [from memory] / [guess]" | Makes uncertainty visible (a method inferred from the research) |

### Detection

| Method | How | Evidence |
|---|---|---|
| **Open the sources yourself** | Click the links, search the paper titles, look up the case numbers. Check **not only that a source exists but that it actually says that** | Walters & Wilder: many errors even in real citations |
| **Ask several times and compare** | Ask the same question in 2–3 new chats. Names, dates, and numbers that change from answer to answer are the most suspect | SelfCheckGPT, self-consistency, Anthropic "Best-of-N" |
| **Chain of verification questions** | Draft → generate verification questions → answer them **independently**, from sources or search where possible → revise | Chain-of-Verification (Meta AI, 2023) |
| **Break it into atomic facts** | Split long text into "atomic facts" and check each one | FActScore (2023): only 58% of the facts in ChatGPT-written biographies were supported |
| **Lateral reading** | Check against **other independent sources**, not the AI's own words | The method professional fact-checkers use (Civic Online Reasoning) |

> [!WARNING]
> Getting **the same answer several times does not prove it's true.** Models can be consistently wrong. Consistency checks are only **a tool for finding suspicious spots**.

### Recovery

```text
Find supporting evidence for each claim in the answer above. Delete any claim you can't find evidence for and mark it [deleted].
```

→ Snippet collection: [templates/grounded-answer.md](../templates/grounded-answer.md)

> Anthropic's official documentation also says these techniques **don't eliminate hallucinations completely**. Always **verify important information yourself**, especially information that feeds high-stakes decisions.

---

## 4. Bonus: Sycophancy

### Symptoms

- Show it your proposal and it starts with praise
- Ask "Are you sure?" and it changes a correct answer to a wrong one
- State a false premise and it runs with it

### Why it happens

- When models are trained on human preference ratings, people rate **pleasant-sounding answers** higher, so models learn to go along. In Anthropic's research (Sharma et al., 2023), both humans and preference models **preferred well-written sycophantic answers over correct ones a non-negligible fraction of the time**.
- In Google's research (Wei et al., 2023), sycophancy **increased** with model scale and instruction tuning. Models agreed with a user who said a wrong addition was correct, even though they knew it was wrong.
- There has been a real incident, too. OpenAI rolled back a GPT-4o update it had shipped on April 25, 2025, just three days later. OpenAI explained that relying more on users' thumbs-up/thumbs-down feedback as a training signal had amplified an overly agreeable tendency.

**Pushing back with "Are you sure?" actually does harm.**

| Study | Result |
|---|---|
| FlipFlop (2023, 10 models) *older models* | After "Are you sure?", models changed their answers **46%** of the time on average, and final accuracy fell **17%** on average |
| Sharma et al. (2023) *older models* | When challenged, Claude 1.3 admitted to a mistake on **98%** of questions even though it hadn't made one |
| SycEval (2025) | Sycophancy observed in 58% of cases. Models were most likely to be pulled toward a wrong answer when the user **pushed back by citing sources** |
| **SPINE (2026, current flagship models)** | When a wrong claim was pushed repeatedly, 20–97% caved within 25 turns. **Emotional appeals** were most strongly linked to caving |
| **Cheng et al. (*Science*, 2026)** | 11 AI systems endorsed users' actions about 49% more than humans did. People trusted sycophantic answers more |

### Prevention and detection

| Method | Example |
|---|---|
| **Hide your opinion and your authorship** | "I wrote this. What do you think?" → "Another team submitted this proposal. Find its weaknesses." |
| **Don't frame questions as your beliefs** | "I believe A is right, isn't it?" → "Judge whether A is right, with evidence" (AI Index 2026: framing it as your belief sharply lowers accuracy) |
| **Don't keep pushing in long conversations** | The longer the conversation and the more emotional the pressure, the more models cave (SPINE 2026). Make important judgments in a **new chat** |
| **Ask for criticism explicitly** | "The 3 weakest points, with evidence" |
| **Set the evaluation criteria first** | Scoring against criteria set in advance makes it less swayed by the mood of the conversation |
| **Point to evidence instead of pushing back** | "Really?" ❌ → "Your step 3 gives 42, but the table says 24. Which is right, and why?" ✅ Self-review with no outside evidence tends to lower accuracy ([Huang et al., ICLR 2024](https://arxiv.org/abs/2310.01798)) |
| **Get a second opinion in a new chat or from another model** | Let it judge without knowing what you think |
| **Treat "You're right!" as a signal** | If the AI agrees right after you push back, that's a **signal to check for yourself** |

→ Snippet collection: [templates/honest-critique.md](../templates/honest-critique.md)

> [!NOTE]
> We have not yet found a controlled study that directly measures whether phrases like "Be honest" or "Don't flatter me" reduce sycophancy in current models. The methods above are based on the **mechanisms** that produce sycophancy.

---

## 5. Match verification effort to the risk

You don't need to verify every answer with the same rigor. Match it to **the cost of being wrong**.

| Risk | Examples | Minimum verification |
|---|---|---|
| **Low** | Ideas, drafts, personal notes | Skim it + ask once, "What did you leave out, or what are you unsure about?" |
| **Medium** | Internal documents, draft reports, code review | Requirements coverage table + check quotes against your own material + a second opinion in a new chat |
| **High** | Legal, medical, or financial work; public-facing material; production code | **Open every source**, do lateral reading on every key claim, recalculate numbers yourself, run tests on code, and don't count agreement from the same model as evidence |

→ More detail: [08. Verification and evaluation](08-verification-and-evals.md)

---

### Sources

**2026 update (checked 2026-11-09)**
- Vectara Hallucination Leaderboard (updated 2026-10-22) — https://github.com/vectara/hallucination-leaderboard
- Stanford HAI, AI Index 2026 Ch.3 Responsible AI — https://hai.stanford.edu/ai-index/2026-ai-index-report/responsible-ai
- Artificial Analysis, AA-Omniscience (live leaderboard) — https://artificialanalysis.ai/evaluations/omniscience
- Topaz et al., "Biomedical Reference Generation Remains Unreliable across 26 Large Language Models" (2026-09, preprint) — https://arxiv.org/abs/2609.14988
- HalluHard (2026-02, preprint) — https://arxiv.org/abs/2602.01031
- Cheng et al., "Sycophantic AI decreases prosocial intentions and promotes dependence" (*Science*, 2026-03) — https://www.science.org/doi/10.1126/science.aec8352
- SPINE: multi-turn sycophancy collapse (2026-09, preprint) — https://arxiv.org/abs/2609.09090
- Chow, retrieval and multi-step reasoning in 1M-token contexts (2026-05, preprint) — https://arxiv.org/abs/2605.02173
- Vasileva, "Large Language Models Can Follow Instructions, But Not Many at Once" (2026-08, preprint) — https://arxiv.org/abs/2608.12426
- Laban et al., ICLR 2026 (oral) record on OpenReview — https://openreview.net/forum?id=VKGTGGcwl6

**Misunderstanding**
- Laban et al., "LLMs Get Lost In Multi-Turn Conversation" (2025) — https://arxiv.org/abs/2505.06120
- Zhang et al., CLAMBER (2024) — https://arxiv.org/abs/2405.12063
- Zhang & Choi, "Clarify When Necessary" (2023) — https://arxiv.org/abs/2311.09469
- Andukuri et al., STaR-GATE (2024) — https://arxiv.org/abs/2403.19154
- Deng et al., "Rephrase and Respond" (2023) — https://arxiv.org/abs/2311.04205
- Anthropic, Prompting best practices — https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices

**Omission**
- Liu et al., "Lost in the Middle" (2023, TACL 2024) — https://arxiv.org/abs/2307.03172
- Hsieh et al., RULER (2024) — https://arxiv.org/abs/2404.06654
- Modarressi et al., NoLiMa (2025) — https://arxiv.org/abs/2502.05167
- Hong, Troynikov, Huber, "Context Rot" (Chroma, 2025) — https://research.trychroma.com/context-rot
- Zhou et al., IFEval (2023) — https://arxiv.org/abs/2311.07911
- Harada et al., "When Instructions Multiply" (ManyIFEval, 2025) — https://arxiv.org/abs/2509.21051
- Jaroslawicz et al., IFScale (2025) — https://arxiv.org/abs/2507.11538
- Bai et al., LongWriter (2024) — https://arxiv.org/abs/2408.07055

**Fabrication (hallucination)**
- Kalai et al., "Why Language Models Hallucinate" (OpenAI, 2025) — https://arxiv.org/abs/2509.04664 / blog: https://openai.com/index/why-language-models-hallucinate/
- Anthropic, Reduce hallucinations — https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations
- Google Cloud, Grounding overview — https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/grounding/overview
- Huang et al., hallucination survey (2023) — https://arxiv.org/abs/2311.05232
- Min et al., FActScore (2023) — https://arxiv.org/abs/2305.14251
- Dhuliawala et al., Chain-of-Verification (2023) — https://arxiv.org/abs/2309.11495
- Wang et al., Self-Consistency (2022) — https://arxiv.org/abs/2203.11171
- Manakul et al., SelfCheckGPT (2023) — https://arxiv.org/abs/2303.08896
- Farquhar et al., Semantic entropy (*Nature*, 2024) — https://www.nature.com/articles/s41586-024-07421-0
- Walters & Wilder, fabricated citations study (*Scientific Reports*, 2023) — https://www.nature.com/articles/s41598-023-41032-5
- Mata v. Avianca sanctions decision (2023-06-22) — https://law.justia.com/cases/federal/district-courts/new-york/nysdce/1:2022cv01461/575368/54
- AI Hallucination Cases database (Damien Charlotin) — https://www.damiencharlotin.com/hallucinations/
- Stanford, study of hallucinations in legal AI tools — https://law.stanford.edu/publications/hallucination-free-assessing-the-reliability-of-leading-ai-legal-research-tools

**Sycophancy**
- Sharma et al., "Towards Understanding Sycophancy in Language Models" (Anthropic, 2023) — https://arxiv.org/abs/2310.13548
- Perez et al., "Discovering Language Model Behaviors with Model-Written Evaluations" (2022) — https://arxiv.org/abs/2212.09251
- Wei et al., "Simple synthetic data reduces sycophancy" (Google, 2023) — https://arxiv.org/abs/2308.03958
- Laban et al., FlipFlop "Are You Sure?" (2023) — https://arxiv.org/abs/2311.08596
- SycEval (2025) — https://arxiv.org/abs/2502.08177
- OpenAI, "Sycophancy in GPT-4o" (2025-04-29) — https://openai.com/index/sycophancy-in-gpt-4o/
- OpenAI, "Expanding on what we missed with sycophancy" (2025-05) — https://openai.com/index/expanding-on-sycophancy/

**Verification**
- Civic Online Reasoning, "Teaching Lateral Reading" — https://cor.inquirygroup.org/curriculum/collections/teaching-lateral-reading/
