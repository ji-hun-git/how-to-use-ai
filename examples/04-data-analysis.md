# Example 4. Data analysis: compute with code, surface the assumptions

> Language models are tools for generating "words," so they're **bad at mental math.** When working with numbers, always have them run code.
> Karpathy also recommends using code-execution tools for calculations and data work in "How I use LLMs" (2025).

---

## ❌ The usual approach

```text
(paste an Excel table as text)
Tell me the average sales and growth rate by region.
```

- The model calculates in its head, so **the numbers can be wrong.**
- It **silently ignores** data problems such as blanks, duplicate rows, and units (dollars vs. thousands of dollars).
- It **decides on its own** what "growth rate" means (year over year? month over month?) (misunderstanding).

---

## ✅ Improved prompt

```xml
<context>
The attached sales_2026.csv contains monthly sales data by region for 2025–2026. (Unit: thousands of dollars)
I'm building a table for the quarterly report.
</context>

<task>
0. Before analyzing, check the data and report on it: number of rows/columns, missing values, duplicate rows, outliers (outside mean ±3σ), unit anomalies.
   If there are problems, only propose how to handle them, and proceed after I confirm.
1. Average monthly sales by region for Q1–Q3 2026
2. Growth rate by region = (Q1–Q3 2026 total / Q1–Q3 2025 total) - 1
3. The top 3 and bottom 3 regions by growth rate
</task>

<constraints>
- Do every calculation by running Python code. Show me the code you used.
- When you use a metric I haven't defined, state its definition first.
- For interpretation (why something went up), if the data alone can't tell you, write "can't tell from the data."
</constraints>

<format>
1) Data check results (bullets)
2) Results table (Region | Average monthly sales | Growth rate | Rank)
3) 3 notable points (one line each, with supporting numbers)
4) Code used
</format>
```

---

## Why it's written this way

| Technique | Problem it prevents |
|---|---|
| "Calculate by running code" | Calculation errors (a form of fabrication) |
| Step-0 data check + confirmation | Ignoring missing values and duplicates (omission) |
| Defining the growth rate yourself | Misreading the metric's definition (misunderstanding) |
| Allowing "can't tell from the data" | Inventing plausible causes (fabrication) |
| Showing the code | Lets a human verify the work |

---

## Human verification

- [ ] I recalculated 1–2 numbers from the table in Excel myself and they matched
- [ ] I read the code to check that the filter conditions (period, region) match my intent
- [ ] I checked that the supporting numbers in "notable points" actually appear in the table

> 💡 Upload data containing personal information or company secrets only to AI services your company has approved. For details, see [docs/09-security-privacy.md](../docs/09-security-privacy.md).
