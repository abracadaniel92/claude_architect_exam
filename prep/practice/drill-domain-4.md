# Domain 4 Drill — Prompt Engineering & Structured Output (15 questions)

**20% of the exam**, about 12 of 60 questions.

**This is your weakest domain.** You scored 1 out of 5 in Set 1. All three misses were flat facts:
`tool_choice` values, required schema fields, and which errors a retry can fix. Those three facts
are tested again here, in different clothes.

Four questions ask for **two answers**. The real exam is about one in five, so this matches.

**The questions use exam-level English.** The explanations are in simple English.

Time: 30 minutes. Answers below — cover them while you work.

---

### Scenario: Structured Data Extraction

**Q1.** Your extraction schema marks `contract_end_date` as required. Reviewing 400 processed
contracts, you find that for the ~15% that are open-ended agreements with no end date, the model
has populated the field with dates that appear nowhere in the source document — most commonly one
year after the start date. Which change stops this?

A. Add a validation rule rejecting any `contract_end_date` exactly 365 days after `contract_start_date`.
B. Add a system prompt instruction: "Do not infer or calculate dates that are not explicitly stated in the document."
C. Add few-shot examples showing open-ended contracts extracted with the date field empty.
D. Make `contract_end_date` optional and nullable in the schema.

---

**Q2.** Your pipeline handles three document types — invoices, receipts and purchase orders — each
with its own extraction tool and schema. The type is not known until the document is read. You
observe that roughly a quarter of requests return a paragraph describing the document rather than
calling any tool. What is the correct configuration?

A. `tool_choice: {"type": "any"}`
B. `tool_choice: {"type": "auto"}` with a stronger system prompt instruction to always extract.
C. `tool_choice: {"type": "tool", "name": "extract_invoice"}`, since invoices are the most common type.
D. Merge the three tools into one with a `document_type` enum parameter.

---

**Q3.** Your enrichment pipeline must call `extract_metadata` before `lookup_vendor_details`,
because the vendor lookup depends on the country code that metadata extraction produces. In
production, the model occasionally calls them in the wrong order. Which approach enforces the
ordering?

A. `tool_choice: {"type": "any"}` on the first request.
B. Describe the dependency in both tool descriptions.
C. `tool_choice: {"type": "tool", "name": "extract_metadata"}` on the first request, then handle the enrichment steps in follow-up turns.
D. List `extract_metadata` before `lookup_vendor_details` in the `tools` array.

---

**Q4.** After switching from free-text JSON output to tool use with a strict JSON schema, your
malformed-JSON error rate drops from 3% to zero. However, your finance team reports that invoice
line items still sometimes fail to sum to the stated total, and occasionally the tax amount
appears in the shipping field. Which two statements are correct? **(Select two.)**

A. The remaining failures indicate the schema was not marked `strict: true` correctly.
B. Strict schemas eliminate syntax errors but do not prevent semantic errors.
C. Switching back to free-text JSON with a stronger prompt would fix the field placement.
D. Extracting `calculated_total` alongside `stated_total` would let you detect the summing problem.

---

**Q5.** Validation fails on 8% of your extractions. Investigating a sample, you identify two
causes: some documents express amounts as "1.2M" where the schema expects a number, and some
documents genuinely do not contain the requested vendor registration number — it exists only in a
separate supplier master file you do not pass to the model. You implement a retry loop that
resends the document, the failed extraction, and the specific validation error. What should you
expect?

A. Both causes resolve, because the model can self-correct when given the specific error.
B. Neither resolves, because retries cannot correct schema-level failures.
C. The missing registration numbers resolve; the formatting cases require a schema change.
D. The "1.2M" formatting cases resolve; the missing registration numbers do not.

---

**Q6.** Your extraction handles supplier documents from twelve countries. The `payment_terms`
field currently uses a free-text string, and downstream systems cannot process the variety. You
want a constrained field that still handles terms you have not anticipated. What schema design
achieves this?

A. A nullable enum, so unrecognised terms produce `null`.
B. An enum of the known payment terms, plus an `"other"` value and a separate detail string field.
C. A required string field with format normalisation rules in the prompt.
D. An enum of the known payment terms, with validation rejecting anything unrecognised.

---

**Q7.** You are processing a batch of 100 scanned documents through the Message Batches API.
Eighteen fail. Investigating, you find twelve exceeded the context limit and six hit a transient
service error. Which two actions are correct? **(Select two.)**

A. Resubmit only the eighteen failed documents, identified by their `custom_id` values.
B. Resubmit the entire batch of 100, since partial resubmission risks inconsistent processing.
C. Match the results to requests by their position in the response array.
D. Chunk the twelve oversized documents before resubmitting them.

---

**Q8.** Your nightly extraction job processes about 8,000 documents. Documents arrive continuously
throughout the day, and your commitment to the downstream team is that any document is processed
within 30 hours of arrival. You use the Message Batches API. What submission cadence meets the
commitment?

A. Submit every 4 hours.
B. Submit once daily at midnight.
C. Submit every 12 hours.
D. Submit each document individually as it arrives.

---

**Q9.** Before running a 10,000-document batch, what is the most cost-effective preparation step?

A. Increase `max_tokens` so no extraction is truncated.
B. Run the same batch twice and compare, to identify non-deterministic extractions.
C. Refine the prompt against a small sample set to maximise the first-pass success rate.
D. Split the batch into ten batches of 1,000 to reduce the impact of any single failure.

---

### Scenario: Claude Code for Continuous Integration

**Q10.** Your automated review flags 34% false positives in its "unnecessary abstraction" category.
Your team lead suggests adding "only report issues you are highly confident are genuine problems"
to the review prompt. What is wrong with this suggestion, and what should you do instead?

A. The instruction is correct but must be paired with a numeric confidence threshold in the output schema.
B. General confidence instructions do not improve precision. Define specific categorical criteria for what to report and what to skip.
C. The instruction is correct but should be placed in CLAUDE.md rather than the review prompt.
D. Nothing is wrong; confidence-based instructions are the documented approach for precision.

---

**Q11.** Your review produces severity ratings that are inconsistent between runs — the same class
of issue is rated "high" in one review and "low" in another. What produces consistent
classification?

A. Reducing the severity scale from five levels to two.
B. Instructing the model to be consistent with previous reviews of the same repository.
C. Having a second review pass re-rate the severities assigned by the first.
D. Defining explicit severity criteria with concrete code examples for each severity level.

---

**Q12.** Your review comments are technically accurate but developers say they are hard to act on
— the format varies between findings, and some omit the file location or the suggested fix.
Detailed written instructions about the required format have not fixed it. Which two changes
address this? **(Select two.)**

A. Increase `max_tokens` so findings are not truncated mid-format.
B. Add few-shot examples demonstrating the exact output shape: location, issue, severity, suggested fix.
C. Enforce the output shape with a JSON schema via tool use.
D. Add "IMPORTANT: always include the file location" to the top of the prompt.

---

**Q13.** Your team runs two Claude workloads. The first is a pre-merge review that blocks the merge
button until it returns. The second is a weekly architecture-drift report, read at Monday's
planning meeting. Finance asks you to cut costs. What do you do?

A. Move the weekly report to the Batches API; keep the pre-merge review synchronous.
B. Move both to the Batches API, with a fallback to the synchronous API if a batch takes longer than 10 minutes.
C. Move both to the Message Batches API for the 50% saving.
D. Keep both synchronous, because batch results cannot be reliably matched to requests.

---

**Q14.** Your CI generates code and then, in the same session, reviews that generated code before
opening the pull request. Reviewers report the automated review rarely finds problems that later
turn out to be real. What is the underlying cause, and what fixes it?

A. Extended thinking is not enabled on the review step. Enable it so the model reasons more carefully.
B. The review prompt lacks explicit criteria; add categorical criteria for what to report.
C. The model retains its reasoning context from generation and does not question its own decisions. Use a separate, independent instance to review.
D. The review runs before tests, so it lacks failure information. Reorder the pipeline.

---

**Q15.** A pull request touches 18 files in the payments module. Your single review pass produces
detailed findings for the first few files, thin findings for the rest, and in two cases flags a
pattern as a defect in one file while approving the identical pattern in another. Which two
changes address this? **(Select two.)**

A. Run a separate review pass per file, for issues local to that file.
B. Run the review three times and report only findings that appear in at least two runs.
C. Run an additional pass across all files, examining data flow between them.
D. Move to a model with a larger context window so all 18 files fit comfortably.

---
---

# Answers

**Q1 — D.** A **required** field forces the model to produce a value. When the document does not
contain one, it invents a plausible one — here, start date plus a year. Making the field optional
and nullable removes the pressure. This is the guide's stated skill: design fields as nullable
when source documents may not contain the information, to prevent the model fabricating values.

- **A** — catches one fabrication pattern after it happens. The model will simply invent a
  different date. You are validating a symptom.
- **B** — an instruction fighting against a structural requirement. The schema still demands a
  value, so the instruction and the schema are in conflict, and the schema usually wins.
- **C** — few-shot examples might reduce the rate, but they cannot resolve a schema that requires
  a field the document does not have. Fix the schema first.

**Q2 — A.** `"any"` forces the model to call a tool while letting it choose which one. That is
exactly the case here: several schemas, type unknown at request time.

- **B** — `auto` **permits a text response**. That is the reported failure. A stronger instruction
  does not change what `auto` allows.
- **C** — forcing one tool means every receipt and purchase order is extracted with the invoice
  schema. Worse than the original problem.
- **D** — a real design option, but it discards three purpose-built schemas to solve a
  configuration problem. One line of config beats a schema rewrite.

**Q3 — C.** Forced tool selection guarantees a named tool is called first; the remaining steps
happen in follow-up turns. The guide names this exact use — forcing `extract_metadata` before
enrichment tools.

- **A** — `any` guarantees **a** tool call, not **that** tool. The model could still call the
  vendor lookup first.
- **B** — descriptions influence selection; they do not enforce sequence. The scenario says it
  already goes wrong occasionally, which is what "influence" produces.
- **D** — array order carries no guarantee. This is a plausible-sounding assumption with no basis.

**Q4 — B and D.** **B** is the core fact: strict schemas guarantee the JSON is well-formed and
matches the shape, and guarantee nothing about whether the values are correct. **D** is the
guide's named self-correction design — extract `calculated_total` alongside `stated_total` so a
mismatch is visible.

- **A** — the syntax errors went to zero, which is exactly what `strict` does. Nothing here
  suggests it is misconfigured.
- **C** — going back to free-text JSON would restore the 3% syntax error rate and still not fix
  field placement. It trades one problem for two.

**Q5 — D.** Retries fix **format and structural** problems, because the model can correct itself
when shown the specific error. "1.2M" to a number is a format problem. Retries cannot produce
information that is **not in the document** — the registration number exists only in a file the
model never sees, so it will fail identically every time, or fabricate.

- **A** — the trap. Assumes retries are universally effective.
- **B** — inverts the truth. Format problems are precisely the retryable class.
- **C** — reversed on both counts.

**Q6 — B.** Enum plus an `"other"` value plus a detail string is the guide's named pattern for
**extensible categorisation**. Known terms are constrained; unanticipated ones are captured in the
detail field rather than lost.

- **A** — `null` records that something was there but discards what it was. The `"other"` plus
  detail pattern keeps the information.
- **C** — free text is what the downstream systems already cannot process.
- **D** — rejecting unrecognised terms fails the document rather than extracting it. You lose data
  from exactly the cases you were trying to handle.

**Q7 — A and D.** Resubmit only the failures, identified by `custom_id` (**A**), with the
modification each failure requires — chunking the documents that exceeded the context limit
(**D**). The guide names both.

- **B** — resubmitting all 100 pays for 82 successful extractions a second time.
- **C** — **the important wrong answer.** Batch results do **not** arrive in request order. Match
  them by `custom_id`, never by position. Relying on position produces silently mismatched data,
  which is worse than an error.

**Q8 — A.** Work backwards from the commitment. A document waits at most one submission interval
before it is sent, then batch processing takes **up to 24 hours**. So the interval plus 24 hours
must fit inside 30 hours. Every 4 hours leaves a margin; this is the guide's own worked example.

- **B** — worst case 24 hours waiting plus 24 hours processing = 48 hours. Fails.
- **C** — worst case 12 plus 24 = 36 hours. Fails.
- **D** — individual submission is the synchronous API, which discards the 50% saving that made
  batching worthwhile.

**Q9 — C.** Refine the prompt on a sample first. A higher first-pass success rate across 10,000
documents avoids the cost of resubmitting failures — the guide's stated skill.

- **A** — may be sensible, but it addresses one failure mode rather than overall success rate.
- **B** — doubles the cost of the entire run to measure something you can measure on a sample.
- **D** — smaller batches do not change how many extractions fail; they only change the blast
  radius. The failures still cost the same to reprocess.

**Q10 — B.** General confidence instructions — "be conservative", "only report what you are
confident about" — do **not** improve precision. Specific categorical criteria do: name which
issue classes to report (bugs, security) and which to skip (minor style, local patterns).

- **A** — adds a numeric threshold on top of an approach that does not work. Self-reported
  confidence is unreliable for this.
- **C** — moving an ineffective instruction to a different file does not make it effective.
- **D** — states the opposite of the guide.

**Q11 — D.** Explicit severity criteria **with concrete code examples for each level** is the
guide's stated method for consistent classification. Examples anchor the judgement; adjectives
do not.

- **A** — fewer levels reduces how visible the inconsistency is. It does not make the judgement
  more consistent.
- **B** — the model has no access to previous reviews unless you provide them, and "be consistent"
  is the same vague instruction that failed in Q10.
- **C** — adds a second layer of the same unanchored judgement.

**Q12 — B and C.** The guide names few-shot examples as **the most effective technique** for
consistently formatted, actionable output when detailed instructions alone have not worked (**B**)
— and specifies the exact fields: location, issue, severity, suggested fix. Tool use with a JSON
schema (**C**) enforces the shape structurally, so a required field cannot be omitted at all.

- **A** — the findings are inconsistently *shaped*, not cut off. Nothing suggests truncation.
- **D** — emphasis is not the missing ingredient. The instructions already exist and are detailed;
  the question tells you they did not work.

**Q13 — A.** The Batches API is 50% cheaper with a window of up to 24 hours and **no guaranteed
latency**. A weekly report read on Monday morning is ideal for it. A pre-merge check where a
developer is waiting is not.

- **B** — adds a fallback path, duplicate spend and extra complexity, when matching each API to
  its own use case is simpler and cheaper.
- **C** — blocks the merge button for up to 24 hours.
- **D** — a misconception. `custom_id` correlates results reliably.

**Q14 — C.** A model that generated the code **retains its reasoning context** and is less likely
to question its own decisions. An independent instance, with no memory of writing it, is more
effective than either self-review instructions or extended thinking.

- **A** — the guide states specifically that independent review beats extended thinking here.
  Thinking harder about your own reasoning does not make you doubt it.
- **B** — explicit criteria are valuable, but they do not address why *this* reviewer is blind.
  The same criteria given to an independent instance would find more.
- **D** — plausible pipeline engineering, but nothing in the question points at missing test
  information.

**Q15 — A and C.** The pattern is one pass per file for local issues, **plus** a separate pass
across files for data flow. Both halves are needed: per-file passes give consistent depth, and
only the integration pass catches problems that span files.

- **B** — consensus voting **suppresses real bugs** that are only caught intermittently. Also on
  the permanent wrong-answer list.
- **D** — larger context windows do **not** solve attention quality. This is stated directly in
  the guide and is a permanent wrong answer.

---

## Score

___ / 15 · Q4, Q7, Q12 and Q15 need two answers each. You need both for the point.

**The three facts from Set 1, retested:**

| Set 1 miss | Retested here |
|---|---|
| Q13 — required fields cause invented values | **Q1** |
| Q14 — `auto` permits a text response | **Q2** |
| Q15 — retries cannot find absent information | **Q5** |

If you got all three right, the daily fact drill is working. If you missed any, that fact is not
yet learned — write it on the cheat sheet by hand and drill it separately.

- **Below 10** — do not move on. Re-read `notes/domain-4-prompt-structured-output.md`, then take
  this drill again in three days.
- **10–12** — check whether your mistakes cluster in schemas and `tool_choice` (Q1–Q4, Q6) or in
  batches (Q7–Q9, Q13). Drill that half.
- **13 or more** — Domain 4 is no longer your weakest domain. Confirm it on the 23 August mock.
