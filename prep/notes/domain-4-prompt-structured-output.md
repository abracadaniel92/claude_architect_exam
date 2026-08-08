# Domain 4 — Prompt Engineering & Structured Output (20%)

About 12 of the 60 questions come from here. There are 6 task statements.

**This is your weakest domain.** You scored 1 out of 5 in the day-1 test. The three questions you
missed were all facts, not reasoning. Facts are quick to fix. Use
`practice/daily-facts-domain-4.md` every day.

Two ideas run through this domain:

1. **Clear, specific criteria work. Vague instructions do not.**
2. **Tool use with a JSON schema is the reliable way to get structured output.**

---

## 4.1 Write specific criteria, not vague instructions

| ❌ Vague | ✅ Specific |
|---|---|
| "Check that comments are accurate" | "Flag a comment only when the behaviour it describes **contradicts** what the code does" |
| "Be conservative" | Name the categories to report and the categories to skip |
| "Only report high-confidence findings" | Report bugs and security issues. Skip minor style and local patterns |

### Filtering by confidence does not work

Instructions like "be conservative" or "only report what you are sure about" do **not** improve
precision. Specific categories do.

On the exam, any answer that filters by the model's own confidence is probably wrong.

### False alarms damage trust in everything

If one category produces many false alarms, developers stop trusting the **accurate** categories
too.

**The fix from the guide:** temporarily turn off the category with many false alarms. Keep the
good categories running. Improve the bad category's prompt, then turn it back on.

### Consistent severity levels

Define each severity level with **concrete code examples**. Then classification stays consistent.

---

## 4.2 Few-shot prompting

**Few-shot** means putting a small number of examples in the prompt.

The guide says few-shot examples are the most effective technique when you need consistent,
well-formatted output and detailed instructions alone are not working.

### The rules

- Use **2 to 4 examples**.
- Aim them at the **unclear cases**, not the obvious ones.

### What few-shot examples achieve

- They show how to handle **unclear situations** (which tool to pick for an ambiguous request;
  gaps in branch-level test coverage).
- They let the model **apply the same judgement to new situations** it has not seen. It does not
  only copy the examples.
- They **reduce invented information** in extraction tasks (informal measurements, documents with
  different structures).
- They show the **reasoning** for choosing one action instead of another reasonable one.
- They fix the **output format** (location, issue, severity, suggested fix).
- They separate **acceptable code patterns from real problems**, which reduces false alarms.
- They handle **different document structures**: inline citations vs a bibliography; a methodology
  section vs details spread through the text.
- They fix **empty or null values in required fields**, by showing correct extraction from
  documents with different layouts.

### When few-shot is the wrong answer

- When the real problem is a **tool description**. Sample Q2 says few-shot "adds token overhead
  without fixing the underlying issue."
- When the rule **must always work**. Sample Q1: few-shot is still probabilistic, so it fails
  sometimes.

---

## 4.3 Structured output with tool use and JSON schemas

Using **tool use with a JSON schema** is the most reliable way to guarantee output that matches
your schema. It removes JSON syntax errors.

### The important detail

Strict schemas remove **syntax** errors. They do **not** remove **semantic** errors.

- **Syntax error:** the JSON is broken. Schemas fix this.
- **Semantic error:** the JSON is valid, but the content is wrong. Line items do not add up to
  the total. A value is in the wrong field. Schemas do **not** fix this.

Any answer claiming schemas guarantee correct content is wrong.

### `tool_choice` again, in this context

| Value | What happens | How the exam uses it |
|---|---|---|
| `auto` | The model **may return text** instead of calling a tool | The default. Never the fix when the model returns text instead of extracting |
| `any` | Must call a tool, chooses which | **You have several schemas and do not know the document type yet** |
| `{"type":"tool","name":"..."}` | Must call that specific tool | **Force `extract_metadata` to run before enrichment**, then continue in later turns |
| `none` | Cannot use tools | Real, but the guide does not test it |

### Schema design rules

**Make fields optional or nullable when the document might not contain them.**

This is the most tested schema fact. A **required** field forces the model to produce something.
If the value is not in the document, the model invents one.

Other rules:
- Use an enum with an **`"other"` value plus a detail string** for categories that may grow.
- Add an **`"unclear"`** enum value for ambiguous cases.
- Put **format normalisation rules in the prompt**, next to the strict schema. This handles
  source documents with inconsistent formatting.

---

## 4.4 Validation, retries, and feedback

### How to retry correctly

When validation fails, send a follow-up request containing three things:
1. The original document
2. The failed extraction
3. The **specific** validation errors

Then the model can correct itself.

### When retries work, and when they do not

| Retry works | Retry does not work |
|---|---|
| Format is wrong (dates, currency) | The information is **not in the document at all** |
| The output structure is wrong | The information is only in another document you did not provide |

This is simple but easy to forget. Format problems are fixable. Missing information is not.

### Two kinds of validation error

- **Semantic errors** — values do not add up, a value is in the wrong field. Tool use does not
  prevent these.
- **Syntax errors** — broken JSON. Tool use does prevent these.

### Two schema patterns for self-checking

- Extract **`calculated_total` next to `stated_total`**. If they differ, you have found a problem.
- Add a **`conflict_detected`** boolean for source data that contradicts itself.

### Analysing false alarms

Add a **`detected_pattern`** field to each finding. It records which code pattern triggered the
finding. Later you can look at which patterns developers usually dismiss.

---

## 4.5 The Message Batches API

Learn this table.

| Property | Value |
|---|---|
| Cost | **50% cheaper** |
| Processing time | **Up to 24 hours** |
| Guaranteed speed | **None** |
| Matching responses to requests | **`custom_id`** |
| Tool calling across several turns in one request | **Not supported** |

**Good for:** work that can wait — overnight reports, weekly audits, nightly test generation.

**Bad for:** work that blocks someone — a pre-merge check where a developer is waiting.

### Sample Q11

Use batch for the overnight technical-debt report. Keep real-time for the blocking pre-merge
check.

The wrong answers:
- Batch both, because batches are "often faster" → not acceptable when someone is waiting
- Keep both real-time because of result ordering → wrong; `custom_id` matches results correctly
- Batch both with a timeout fallback → unnecessary complexity

### Three more batch skills

1. **Calculate how often to submit**, based on your SLA. Example: with a 24-hour processing
   window, submit every 4 hours to guarantee a 30-hour SLA.
2. **Resubmit only the failed documents.** Find them by `custom_id`. Change them first if needed
   — for example, split documents that were too long.
3. **Test your prompt on a small sample first**, before sending a large batch. This raises the
   first-attempt success rate and reduces the cost of resubmitting.

*(Extra detail beyond the guide: results come back in any order, so match them by `custom_id`,
never by position. A batch can hold up to 100,000 requests or 256 MB. Results are kept 29 days.)*

---

## 4.6 Reviewing with several passes or several instances

### Why a model reviewing its own work is weak

It still remembers why it wrote the code that way. So it does not question its own decisions.

### What works better

A **separate, independent instance** with no memory of writing the code. This works better than
telling the model to check itself, and better than extended thinking.

### Multi-pass review for large changes

- **One pass per file** → finds local issues, with consistent depth
- **One separate pass across files** → finds data-flow issues between files

This prevents **attention dilution** (quality dropping when there is too much to review at once)
and contradictory findings — for example, flagging a pattern as a bug in one file while approving
the same pattern in another file of the same pull request.

### Sample Q12 — the wrong answers

- A bigger model or bigger context window → "larger context windows don't solve attention
  quality."
- Ask developers to split their pull requests → moves the work to people, does not fix the system.
- Run three passes and report only issues found in at least two → **hides real bugs** that are
  only caught sometimes.

### One place where confidence is allowed

In a verification pass, the model can report a confidence level **next to each finding**. This
helps you decide which findings a human should look at first.

Compare with section 5.2, where self-reported confidence is **rejected** as a reason to escalate.
The difference: here it directs a reviewer's attention. There it decides whether the agent acts
alone.

---

## Quick review list for Domain 4

1. Specific categories beat "be conservative" and confidence filters.
2. A category with many false alarms damages trust in the good ones. Turn it off while you fix it.
3. Few-shot: 2 to 4 examples, aimed at unclear cases. They allow the model to generalise.
4. Tool use + JSON schema removes **syntax** errors, not **semantic** ones.
5. `auto` may return text · `any` guarantees a tool call · forced picks the tool.
6. Optional or nullable fields stop invented values. Use `"other"` + detail, and `"unclear"`.
7. Retry with: the document + the failed extraction + the specific errors. Retry cannot find
   missing information.
8. `calculated_total` vs `stated_total`; `conflict_detected`; `detected_pattern`.
9. Batches: 50% cheaper, up to 24 hours, no speed guarantee, `custom_id`, no multi-turn tool
   calling.
10. Independent instance beats self-review. One pass per file + one pass across files.
