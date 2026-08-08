# Domain 5 — Context Management & Reliability (15%)

About 9 of the 60 questions come from here. There are 6 task statements.

This is the smallest domain by weight. But it appears in **four of the six exam scenarios**, so
you meet it often.

---

## 5.1 Keeping important information during long conversations

### Three problems to know by name

**1. Progressive summarization risk**
When you keep summarising a conversation, you lose the details: numbers, percentages, dates, and
what the customer said they expected. Those details are exactly what you need later.

**2. The "lost in the middle" effect**
Models handle the **beginning** and the **end** of a long input well. They may miss things in the
**middle**.

**3. Tool results fill up the context**
Tool output uses many tokens, and most of it is not useful. The guide's example: an order lookup
returns **more than 40 fields** when only 5 matter.

### The fixes

| Problem | Fix |
|---|---|
| Summarising loses details | Pull the facts (amounts, dates, order numbers, statuses) into a **"case facts" block**. Include it in every prompt, **outside** the summarised history |
| Sessions with several issues | Pull structured issue data (order IDs, amounts, statuses) into a **separate context layer** |
| Tool output is too long | **Trim it to the useful fields before it enters the context.** Do this early, not later |
| Lost in the middle | Put a **summary of key findings at the beginning**. Organise the details with clear section headings |
| Later agents lose meaning | Require subagents to include **metadata** in their output: dates, source locations, methodology |
| A later agent has little context space | Change the **earlier** agents to return **structured data** (key facts, citations, relevance scores) instead of long text and reasoning |

Also: the API has no memory. Send the full conversation history with every request.

---

## 5.2 When to escalate to a human

### Three valid reasons to escalate

1. The customer **asks for a human**.
2. There is a **policy gap or exception** — the policy does not cover this request.
3. The agent **cannot make progress**.

Note the second one carefully. It is *policy gaps*, not simply "difficult cases."

### Two signals that are always wrong

- **Sentiment analysis.** How angry the customer sounds does not tell you how difficult the case
  is.
- **The model's own confidence score.** It is not well calibrated. The agent is already
  overconfident on the hard cases it is getting wrong.

These two appear as wrong answers throughout the exam.

### Specific situations to remember

| Situation | Correct behaviour |
|---|---|
| The customer clearly asks for a human | Escalate **immediately**. Do not investigate first |
| The customer is frustrated, but the agent can solve the problem | Acknowledge the frustration, offer to solve it. Escalate only if the customer **asks again** |
| The policy does not mention this case (example: matching a competitor's price, when the policy only covers your own site) | Escalate |
| A tool returns several matching customers | **Ask for another identifier.** Never guess |

The first two rows look similar and are easy to confuse. The difference: did the customer
**explicitly ask** for a human?

### Fixing bad escalation decisions (Sample Q3)

Add explicit escalation criteria to the system prompt, **with few-shot examples** showing when to
escalate and when to solve.

Not a classifier. Not sentiment. Not self-reported confidence.

---

## 5.3 Reporting errors between agents

When a subagent fails, it should return **structured error context** so the coordinator can
decide what to do.

Four parts:
1. **What kind of failure it was**
2. **What it tried** (the query)
3. **Any partial results**
4. **Other approaches that might work**

With this, the coordinator can retry with a different query, try another route, or continue with
partial results.

### Four wrong approaches

| Wrong approach | Why it is wrong |
|---|---|
| A generic message like "search unavailable" | Hides useful information from the coordinator |
| **Hiding the error** — return empty results and call it a success | Recovery becomes impossible, and the final output looks complete when it is not |
| **Stopping the whole workflow** because one agent failed | Unnecessary. Other approaches might still work |
| Treating an **access failure** and a **valid empty result** as the same | A timeout may need a retry. Zero matches is a successful search |

### Local recovery

A subagent fixes transient failures itself. It only reports what it cannot fix — and when it
does, it includes what it tried and any partial results.

### Coverage annotations

The synthesis output should say which findings are **well supported** and which topics have
**gaps**, because sources were unavailable.

---

## 5.4 Managing context while exploring a large codebase

### The symptom to recognise

In long sessions, the model starts giving **inconsistent answers**. It talks about **"typical
patterns"** instead of the specific classes it found earlier.

If an exam question describes this, it is asking about context degradation.

### Five techniques

| Technique | What it does |
|---|---|
| **Scratchpad files** | Save key findings to a file. Read the file later. This is the direct fix for context degradation |
| **Subagent delegation** | Send noisy exploration to a subagent ("find all test files", "trace the refund flow"). The main agent keeps the high-level picture |
| **Phase summaries** | Summarise one phase before starting the next. Put the summary into the next agents' starting context |
| **Manifests** | For crash recovery. Each agent saves its state to a known location. The coordinator loads the manifest when work resumes, and puts it into the agents' prompts |
| **`/compact`** | Reduces context usage during a long session filled with discovery output |

---

## 5.5 Human review and confidence calibration

### The main risk

**An average accuracy number can hide a failing part.** 97% overall accuracy can hide one
document type or one field performing very badly.

So: check accuracy **by document type and by field** before you reduce human review.

### Four techniques

1. **Stratified random sampling** of high-confidence extractions.
   You sample the high-confidence group on purpose. That is the group you are about to stop
   reviewing, so you need to know its real error rate. It also finds new kinds of error.

2. **Accuracy analysis by document type and field.**
   Confirm every segment performs well, not just the average.

3. **Field-level confidence scores, calibrated with labelled validation sets.**
   Calibration against labelled data is what makes confidence usable here.

4. **Route to human review** when model confidence is low, or when the source document is
   ambiguous or contradicts itself. This uses limited reviewer time well.

### How this fits with section 5.2

- Self-reported confidence is **rejected** as a reason to escalate or act alone.
- It is **accepted** for deciding which items a reviewer should check first — but only when it is
  **calibrated with labelled data**.

Uncalibrated confidence is never the right answer.

---

## 5.6 Keeping track of sources

### How source information gets lost

It is lost during **summarisation**, when findings are compressed without keeping the link between
each claim and its source.

### What to require

- Subagents must output **structured claim-source mappings**: source URL, document name, and the
  **relevant excerpt**. Later agents must keep and merge these.
- Subagents must include **publication or collection dates**. Without dates, two numbers from
  different years look like a contradiction when they are not.

### When two credible sources disagree

- **Record both values with their sources.** Never pick one at random.
- Document analysis should finish with **both conflicting values included and clearly marked**.
  The **coordinator** then decides how to handle them, before synthesis runs.
- Structure the report with separate sections for **well-established findings** and **contested
  findings**. Keep the original wording and methodology of each source.

### Formatting the output

Use the right format for each type of content:
- Financial data → **tables**
- News → **prose**
- Technical findings → **structured lists**

Do not convert everything into one format.

---

## Quick review list for Domain 5

1. Keep a "case facts" block in every prompt, outside the summarised history.
2. Lost in the middle → key findings first, clear section headings.
3. Trim tool output **before** it enters the context (40+ fields → 5).
4. Escalate when: the customer asks, the policy has a gap, or progress stops. Never sentiment.
   Never self-reported confidence.
5. Several matching customers → ask for another identifier. Do not guess.
6. Error context = failure type + what was tried + partial results + alternatives.
7. Never: generic error messages, hidden errors, stopping the whole workflow, or treating an
   access failure as an empty result.
8. "Typical patterns" instead of specific classes = context degradation → use scratchpad files.
9. Crash recovery = manifests, loaded by the coordinator when work resumes.
10. 97% average can hide a broken segment → stratified sampling + analysis by type and field.
11. Confidence is usable only when **calibrated with labelled data**, and only for routing review.
12. Conflicts → record both with sources. Dates are required. Tables, prose, or lists by content
    type.
