# Domain 4 ad-hoc set — 14 August (15 questions)

Written 14 August, taken the same day: **13/15**. Missed Q6 and Q11 — both Block A schema design,
both the same error (applying a rule in one direction only). See weak points 16–17 in `LOG.md`.

Balanced key, all six task statements. Deliberately avoids the framings in `drill-domain-4.md`, so
that drill stays usable as a separate test.

Three questions ask for **two answers**.

**The questions use exam-level English.** The explanations are in simple English.

Time: 30 minutes. Answers below — cover them while you work.

---

**Q1.** Your extraction pipeline reads research papers. Some cite sources inline, others use a
bibliography; some have a dedicated methodology section, others describe the method across several
paragraphs. The model invents methodology descriptions for the second group and omits citations
for the first. Detailed written instructions about both cases have not changed the behaviour. What
is the most effective next step?

A. Expand to roughly a dozen examples, one for every document layout observed so far.
B. Instruct the model to be conservative and extract only what it is confident is present.
C. Add two to four few-shot examples covering the differing document structures, including one where the methodology is spread through the text.
D. Split the work into two prompts, one per document structure, and route documents between them.

---

**Q2.** A workflow currently runs an agentic loop: the model calls `search_index`, reads the
result, then calls `fetch_document` based on what it found. Finance wants this moved to the
Message Batches API for the cost saving. What is the correct assessment?

A. Supported, provided each turn is submitted with its own `custom_id`.
B. Supported, but each turn may take up to 24 hours, so the loop could take 72 hours end to end.
C. Supported only when `tool_choice` is set to `any`.
D. The Batches API does not support tool calling across multiple turns within one request, so the loop cannot run inside a batch as written.

---

**Q3.** Your `contract_type` field is an enum of six known types. About 7% of documents are
genuinely ambiguous — the model picks the nearest value, and downstream teams cannot tell which
classifications were guesses. Which schema change addresses this?

A. Add an `"unclear"` value to the enum.
B. Make the field nullable, so ambiguous documents produce `null`.
C. Add a numeric `classification_confidence` field and route anything below 0.8 to manual review.
D. Replace the enum with a free-text string and classify downstream.

---

**Q4.** Your review agent reports three categories. The concurrency category is accurate and has
caught real defects. The "unnecessary abstraction" category produces a high proportion of false
alarms. Developers have now started ignoring the agent's comments entirely, including the
concurrency findings. Which two actions address this? **(Select two.)**

A. Lower the severity assigned to abstraction findings so they appear less prominently.
B. Temporarily disable the abstraction category while its prompt is improved, leaving the accurate categories running.
C. Add an instruction to report abstraction issues only when the model is highly confident they are genuine.
D. Add a `detected_pattern` field to each finding recording which code pattern triggered it, so dismissed findings can be analysed.

---

**Q5.** Validation rejects a portion of your extractions. Your current retry sends the original
document again with the same prompt; the second attempt succeeds only slightly more often than the
first. What should the retry request contain?

A. The original document plus an instruction to be more careful this time.
B. The failed extraction and the validation errors only, to keep the request small.
C. The original document, the failed extraction, and the specific validation errors.
D. The original document and a stricter version of the schema.

---

**Q6.** You extract fields from payment-processor confirmations. These are machine-generated and
always contain a transaction ID in a fixed position. Downstream reconciliation breaks whenever the
extraction output omits `transaction_id`. What is the correct schema design for that field?

A. Mark it required.
B. Mark it nullable, because nullable fields prevent fabricated values.
C. Mark it nullable and add a validation rule that rejects a null value.
D. Mark it required with a default value of an empty string.

---

**Q7.** Your agent has two tools: `search_tickets` (open tickets in the current sprint) and
`query_ticket_archive` (tickets closed more than 90 days ago). For about 30% of current-sprint
questions, the model calls the archive tool and returns nothing useful. A colleague proposes adding
four few-shot examples of correct tool selection. What should you do?

A. Add the four few-shot examples as proposed.
B. Set `tool_choice` to force `search_tickets`.
C. Merge both tools into one with a `scope` enum parameter.
D. Rewrite both tool descriptions to state explicitly which time range each one covers.

---

**Q8.** Your team measured the Batches API over two weeks: batches usually complete in about 20
minutes. On that basis, someone proposes moving the pre-merge review — which blocks the merge
button — onto batches for the 50% saving. What is the correct assessment?

A. Acceptable, since the observed latency is comfortably inside the review SLA.
B. Not acceptable: batch processing has no guaranteed speed and a window of up to 24 hours, and an observed average is not a guarantee.
C. Acceptable if you poll for results every 30 seconds and fall back to the standard API after five minutes.
D. Not acceptable, because batch results cannot be reliably matched back to the pull request that produced them.

---

**Q9.** Insurance claim documents sometimes contradict themselves: the numeric amount differs from
the amount written in words, and the incident date in the header differs from the date in the
narrative. Today the model silently picks one value and the downstream team never learns there was
a disagreement. Which two schema changes address this? **(Select two.)**

A. Add a `conflict_detected` boolean so contradictory source data is flagged rather than silently resolved.
B. Add a prompt rule to always prefer the numeric amount and the header date.
C. Extract both readings into separate fields, so the mismatch is visible downstream.
D. Reject any document with an internal contradiction at ingestion and route it to manual entry.

---

**Q10.** You are designing a verification pass that re-checks findings produced by an earlier
review pass, so that a human reviewer knows which findings to inspect first. How should model
confidence be used?

A. Not at all — self-reported confidence is unreliable and should never appear in output.
B. The verification pass should discard any finding whose confidence falls below a set threshold.
C. The verification pass should attach a confidence level to each finding, so reviewers can prioritise, while every finding is still reported.
D. The verification pass should hand a finding to a human only when it reports low confidence in its own verdict.

---

**Q11.** Source documents express dates as "03/04/2025", "4 March 2025" and "2025-03-04", and
amounts as "USD 1,200.00", "$1200" and "1.200,00 EUR". You already use tool use with a strict,
typed schema, and the values still arrive inconsistently. What fixes this?

A. Change the date and amount fields to plain strings and normalise downstream.
B. Add a post-processing normalisation layer between extraction and storage.
C. Add a retry loop that re-sends the document whenever format validation fails.
D. State explicit format normalisation rules in the prompt alongside the strict schema.

---

**Q12.** A compliance rule states that every extraction mentioning a named individual must set
`contains_pii` to true. There are no exceptions, and the behaviour is audited. A colleague proposes
three few-shot examples demonstrating the rule. What is the correct assessment?

A. Correct approach — few-shot is the most effective technique for consistent output, and three examples is the right number.
B. Few-shot examples remain probabilistic and will fail some of the time; a rule that must always hold needs programmatic enforcement.
C. The approach is right but needs at least eight examples to reach the required reliability.
D. Use `tool_choice: {"type": "any"}`, which guarantees the field is populated correctly.

---

**Q13.** You are choosing few-shot examples for a test-generation prompt. Which selection is most
effective?

A. Two to four examples aimed at the cases the model currently gets wrong, such as uncovered branches in error-handling paths.
B. Ten examples, one per test type, spanning the full range from simple to complex.
C. Three examples of the most common and most straightforward test cases, to establish the baseline pattern.
D. A random sample from the existing test suite, so the examples reflect the real distribution of the codebase.

---

**Q14.** Two complaints come back about your review agent. First, it mixes style preferences the
team does not care about in with genuine defects. Second, the same class of missing null check is
rated "critical" in one review and "minor" in another. Which two changes address these?
**(Select two.)**

A. Add "be conservative and report only genuine problems" to the review prompt.
B. Reduce the severity scale from five levels to two.
C. Name the categories to report (correctness, security) and the categories to skip (formatting, local style preferences).
D. Define each severity level with concrete code examples.

---

**Q15.** A colleague objects to your few-shot approach: "The model will just pattern-match on the
four examples and miss anything that does not look like them." What is the accurate response?

A. The objection is correct — few-shot helps only when new inputs closely resemble the examples, so use an explicit rules list instead.
B. Examples that show the reasoning for choosing one action over another let the model apply the same judgement to situations the examples do not cover.
C. The objection is correct, and the mitigation is to raise the example count to around fifteen.
D. The objection holds only when examples are placed in the system prompt rather than as prior message turns.

---
---

# Answers

**Q1 — C.** Few-shot examples are the guide's named technique for handling **different document
structures** when detailed instructions have not worked — inline citations versus a bibliography, a
methodology section versus details spread through the text. Two to four, aimed at the unclear cases.

- **A** — a dozen examples is past the guide's range and adds token cost without adding coverage.
- **B** — filtering by the model's own confidence does not improve precision. Near-permanent wrong answer.
- **D** — you would have to know the structure before choosing the prompt, which is the thing you cannot determine up front.

**Q2 — D.** Straight from the guide's appendix: the Batches API does **not** support tool calling
across several turns within one request. A client-side agentic loop cannot run inside a batch.

- **A** — `custom_id` matches results to requests. It does not create multi-turn capability.
- **B** — invents a per-turn latency model for something that is not supported at all.
- **C** — `tool_choice` governs whether a tool is called, not how many turns a batch request supports.

**Q3 — A.** The `"unclear"` enum value is the guide's named pattern for ambiguous cases. The
ambiguity becomes data instead of a silent guess.

- **B** — `null` conflates "not present in the document" with "present but ambiguous". Those need different handling downstream.
- **C** — uncalibrated self-reported confidence, used as a gate. Wrong for the same reason throughout the exam.
- **D** — discards the constraint the enum was giving you and pushes the whole problem downstream.

**Q4 — B and D.** A category with many false alarms damages trust in the accurate categories too —
the scenario states exactly that. The guide's fix is to **turn the bad category off**, keep the good
ones running, improve the prompt, then re-enable (**B**). **D** is the named analysis design: a
`detected_pattern` field on each finding records which code pattern triggered it, so you can see
which patterns developers dismiss.

- **A** — the false alarms are still there, just quieter. Trust does not come back.
- **C** — a confidence filter. Does not improve precision.

**Q5 — C.** A retry request contains three things: the original document, the failed extraction,
and the **specific** validation errors. With all three the model can correct itself.

- **A** — "be more careful" gives the model nothing it did not already have.
- **B** — without the document the model cannot check what the correct value should have been.
- **D** — changes the schema rather than correcting this extraction, and a stricter schema does not fix a value that is already wrong.

**Q6 — A. ✗ Missed — chose C.** **Required** is right here. The rule cuts both ways, and this is
the direction that is easy to forget:

| The source | Use | Because |
|---|---|---|
| **May not** contain the value | nullable | required forces the model to **invent** one |
| **Always** contains the value | **required** | it guarantees the field cannot be **omitted** |

The question tells you these are machine-generated with the ID in a fixed position, and that the
failure is **omission**, not fabrication.

- **B** — applies the fabrication rule to a source that always has the value. Nothing to fabricate.
- **C** — the chosen answer, and the worst of both: nullable removes the guarantee, and rejecting null now **fails** documents that would have extracted correctly.
- **D** — an empty string satisfies the schema while breaking reconciliation exactly as before.

**Q7 — D.** When the model picks the wrong tool, the **tool description** is the first thing to
fix. The guide is explicit that few-shot here "adds token overhead without fixing the underlying
issue".

- **A** — treats a description problem with a prompting technique.
- **B** — forcing one tool breaks every legitimate archive query.
- **C** — merging into a `mode`/`scope` enum is the tool-granularity anti-pattern from Domain 2.

**Q8 — B.** The Batches API has **no guaranteed speed**, and a window of up to 24 hours. An
observed average is not a guarantee, and the pre-merge review blocks a person.

- **A** — treats measured behaviour as a contract.
- **C** — a fallback path means paying for both, plus complexity, to save 50% on a workload that must be synchronous anyway.
- **D** — a misconception. `custom_id` matches results reliably.

**Q9 — A and C.** `conflict_detected` is the guide's named boolean for source data that
contradicts itself (**A**), and extracting both readings into separate fields is the same shape as
`calculated_total` beside `stated_total` — the mismatch becomes visible instead of being resolved
silently (**C**).

- **B** — resolves the conflict by rule and destroys the signal. A document whose two amounts disagree is a document someone should look at.
- **D** — sends the whole document to manual entry when the extraction itself succeeded.

**Q10 — C.** This is the one place confidence is allowed: **next to each finding**, so a human can
decide what to inspect first. Compare Domain 5, where self-reported confidence is rejected as a
reason for the agent to act or escalate alone. The difference is whether confidence **directs a
reviewer's attention** or **decides the outcome**.

- **A** — over-corrects. The guide names this use explicitly.
- **B** — confidence deciding what gets reported. That is the rejected use.
- **D** — escalation on self-reported confidence, the Domain 5 wrong answer.

**Q11 — D. ✗ Missed — chose B.** Format normalisation rules belong **in the prompt, next to the
strict schema**. The schema fixes the **type**; the prompt fixes the **format**. A strict schema
cannot tell you whether `03/04/2025` is March or April.

- **A** — throws away the typing that is working.
- **B** — the chosen answer. Defensible engineering, which is why it is the distractor: it needs a parser branch per variant and breaks on the first layout you did not anticipate. The prompt rule generalises to unseen variants.
- **C** — retries a format the model was never told to produce, so it produces the same output again.

**Q12 — B.** A rule that must **always** hold cannot rest on a prompting technique. Few-shot is
probabilistic and fails some of the time; auditable compliance rules need programmatic enforcement.
This is the Domain 1 principle appearing inside Domain 4.

- **A** — few-shot is the most effective technique for *consistency*, not for *guarantees*.
- **C** — more examples reduce the failure rate without removing it. "No exceptions" is not a rate.
- **D** — `any` guarantees a tool is called, not that a field within it is correct.

**Q13 — A.** Two to four examples, aimed at the **unclear** cases — the guide's named example is
gaps in branch-level test coverage. Examples of what the model already gets right teach nothing.

- **B** — ten is outside the range, and "simple to complex" spends most of the examples on cases that already work.
- **C** — the straightforward cases are precisely the ones not to spend examples on.
- **D** — a random sample is dominated by the common, easy cases.

**Q14 — C and D.** Two distinct symptoms, so two answers. Noise from unwanted categories → **name
the categories to report and the categories to skip** (**C**). Inconsistent severity → **define
each level with concrete code examples** (**D**).

- **A** — "be conservative" is the instruction the guide says does not work.
- **B** — fewer levels makes the inconsistency less visible without making the judgement more consistent.

**Q15 — B.** Few-shot examples that show the **reasoning** for choosing one action over another
let the model apply the same judgement to situations the examples do not cover. The guide states
this directly: they are not limited to literal copying.

- **A** — the objection as stated, accepted. It is wrong.
- **C** — pushes past the 2–4 range to fix a problem that does not exist.
- **D** — invents a placement rule that changes nothing about generalisation.

---

## Score

**13/15 on 14 August.** Q4, Q9 and Q14 needed two answers each — all three correct.

**Both misses were Block A schema design, and both were the same error:** taking a rule in one
direction only. Required-vs-nullable has a discriminator now — *does the source always contain this
value?* — and format normalisation has a one-liner — *the schema fixes the type, the prompt fixes
the format.* Both are on the cheat sheet and the revision card.

Retake this cold if Mock 1 shows Domain 4 below 70%.
