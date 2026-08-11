# Domain 5 Drill — Context Management & Reliability (15 questions)

**15% of the exam**, about 9 of 60 questions — but it appears in **four of the six scenarios**,
so you meet it often.

You scored 2/4 on Domain 5 in Set 1. One miss was the **escalation trap** (a frustrated customer
versus a customer who explicitly asks for a human). It is retested here, in different clothes.

Three questions ask for **two answers**.

**The questions use exam-level English.** The explanations are in simple English.

Time: 30 minutes. Answers below — cover them while you work.

---

### Scenario: Customer Support Resolution Agent

**Q1.** In sessions where a customer raises several issues, your agent's later responses misstate
the refund amount agreed earlier and attach an order number that belongs to a different issue.
The conversation history is summarised automatically as the session grows. What is the correct
architectural fix?

A. Instruct the model, in the system prompt, to treat monetary amounts and order numbers as high-priority information that must never be altered.
B. Extract transactional facts — amounts, dates, order numbers, statuses — into a persistent case-facts block included in every prompt, outside the summarised history.
C. Disable summarisation entirely so no information can be lost.
D. Increase `max_tokens` so the summaries can be longer and retain more detail.

---

**Q2.** Each `lookup_order` call returns 42 fields, of which about five are relevant to a return.
In multi-issue sessions the context fills before the third issue is addressed. Where in the
pipeline does the correct fix apply?

A. After the session: compress the completed transcript before archiving it.
B. In the system prompt: instruct the model to ignore fields that are not relevant to the current issue.
C. At the model tier: move to a model with a larger context window.
D. At the tool boundary: trim each result to the return-relevant fields **before** it enters the conversation context.

---

**Q3.** Your coordinator aggregates twelve subagent reports into one long synthesis input. Spot
checks show the synthesis reliably reflects the first and last reports but repeatedly omits
findings that appear in the middle of the input. Which restructuring addresses the cause?

A. Place a summary of the key findings at the **beginning** of the aggregated input, and organise the detailed results under explicit section headers.
B. Randomise the order of the reports on each run, so no report is systematically disadvantaged.
C. Increase `max_tokens` on the synthesis request so the output can cover more reports.
D. Instruct the synthesis agent to give equal attention to every section of the input.

---

**Q4.** A customer's first message reads: "This is the second time this order has arrived broken.
Absolutely useless. I need this replaced before Friday." The issue is a routine replacement the
agent can complete. The agent escalates to a human, citing the customer's frustration. What is
the correct behaviour?

A. The agent is right: strong frustration signals a complex case, and complex cases escalate.
B. Run sentiment analysis and escalate only when the score crosses a defined threshold.
C. Acknowledge the frustration and offer to resolve the replacement now — escalating only if the customer then asks for a human.
D. Resolve the replacement without acknowledging the frustration, since sentiment must not influence agent behaviour.

---

**Q5.** Your returns policy defines price adjustments when an item is discounted on your own site
within 14 days of purchase. A customer requests a price match against a competitor's advertised
price. The policy says nothing about competitor prices. What should the agent do?

A. Escalate to a human — the policy has a gap, and policy gaps are an escalation trigger.
B. Refuse the request, because the policy does not authorise competitor matching.
C. Apply the own-site adjustment rule as the closest available match.
D. Offer a small goodwill discount within the agent's refund authority instead.

---

**Q6.** `get_customer` returns three records matching the name the customer gave. The agent
selects the record with the most recent order and proceeds with the account operation. What
should it have done?

A. Selected the record whose details had the highest similarity score to the conversation so far.
B. Run the operation against all three records and discard the two that fail.
C. Proceeded as it did, but flagged the assumption in its reply.
D. Asked the customer for an additional identifier — an email address or order number — before touching any account.

---

### Scenario: Multi-Agent Research System

**Q7.** Whatever goes wrong inside your document-analysis subagent — a timeout, a corrupt file, an
unsupported format — the coordinator receives the same status: `"analysis unavailable"`. The
coordinator has no basis for deciding whether to retry, reroute, or continue. What should the
subagent's failure report contain?

A. An `errorCategory` and an `isRetryable` flag, and nothing else, to keep the protocol small.
B. The failure type, what was attempted, any partial results, and alternative approaches that might work.
C. The subagent's full session log, so the coordinator has every detail available.
D. A recommendation to terminate the workflow, since the analysis cannot be trusted.

---

**Q8.** During a research run, two of the source repositories were unreachable, so several
subtopics rest on a single source. The final report presents every finding with the same
authority, and its readers cannot tell the difference. What is the correct fix?

A. Exclude the thinly-sourced subtopics, so the report contains only well-supported claims.
B. Have the synthesis agent fill the thin subtopics from its general knowledge.
C. Require the synthesis output to carry coverage annotations — which findings are well supported, and which topic areas have gaps because sources were unavailable.
D. Append a general disclaimer stating that research results may be incomplete.

---

**Q9.** Your pipeline summarises findings at three points before the report is written. The
finished reports contain confident claims that nobody can trace back to a source, and adding a
"cite your sources" instruction to the report generator has not helped. What is the structural
fix?

A. Require subagents to output structured claim-source mappings — the claim, the relevant excerpt, and the source URL or document name — which every downstream agent preserves and merges.
B. Have the report generator search the sources again after writing, attaching the best match for each claim.
C. Move the "cite your sources" instruction from the report generator to every subagent.
D. Reduce the three summarisation steps to one, so less attribution is lost.

---

**Q10.** Two credible industry reports state different figures for the same market's annual
growth. A subagent's summary silently adopted one of them. Separately, you notice subagent
outputs carry no dates, so a 2023 figure and a 2026 figure look like a contradiction. Which two
changes are correct? **(Select two.)**

A. Adopt the more recently published figure and discard the other, since newer data supersedes older.
B. Record both values, each with its source attribution and explicitly marked as conflicting, and let the coordinator decide how to reconcile them before synthesis.
C. Average the two figures, so the report carries a single defensible number.
D. Require publication or data-collection dates in every subagent's structured output, so temporal differences are not misread as contradictions.

---

### Scenario: Developer Productivity with Claude

**Q11.** Four hours into a codebase exploration session, you ask how the payment retry queue
works. The agent describes "a typical retry queue implementation" — although it read the actual
`RetryQueue` class in hour one. What is happening, and what is the direct fix?

A. The model is hallucinating; reduce the temperature so answers stay grounded.
B. The class was too complex for the model tier; switch to a larger model and ask again.
C. Restart the session and re-explore from zero for each new question, so every answer is fresh.
D. Context degradation; maintain a scratchpad file recording key findings as they are discovered, and have the agent reference it for later questions.

---

**Q12.** Your overnight multi-agent analysis crashed at hour three, and the rerun started from
zero because nothing of the completed work survived the crash. How should the system be designed
so a restart can continue rather than begin again?

A. Wrap the pipeline in a retry loop with exponential backoff, restarting from the beginning on each failure.
B. Have each agent export its state to a known location as it works; on resume, the coordinator loads the manifest and injects it into the agents' prompts.
C. Keep all intermediate state inside the coordinator's conversation history, which is the single source of truth.
D. Run `/compact` on a schedule, so that less context is lost whenever a crash occurs.

---

**Q13.** You are midway through a long exploration session. The context is filling with verbose
discovery output and response quality is dropping, but the session must continue — and phase two
of the exploration starts tomorrow. Which two practices apply? **(Select two.)**

A. Use `/compact` now, to reduce context usage so the current session can continue productively.
B. Move to a model with a larger context window and continue accumulating output.
C. Summarise phase one's key findings before phase two begins, and inject that summary into the next phase's starting context.
D. Instruct the agent to remember the important findings and forget the rest.

---

### Scenario: Structured Data Extraction

**Q14.** Your claims-extraction system reports 96% aggregate accuracy, and leadership wants to
drop human review for high-confidence extractions. Which two practices must precede that
decision? **(Select two.)**

A. Analyse accuracy by document type and by field, confirming every segment performs well — an average can hide one badly failing type.
B. Accept the aggregate figure: 96% exceeds the 95% threshold the business set.
C. Rely on the model to flag its own uncertain extractions for review.
D. Implement stratified random sampling of the high-confidence group, so its real error rate keeps being measured after review is reduced.

---

**Q15.** You route extractions to human review whenever the model's self-reported confidence
falls below 0.8. Audits keep finding errors in extractions the model scored above 0.9. Reviewer
capacity is limited. What is the correct routing design?

A. Raise the routing threshold to 0.95, so more of the doubtful extractions reach a reviewer.
B. Route by document length instead, since long documents produce more errors.
C. Have the model output field-level confidence scores, calibrate the routing thresholds against a labelled validation set, and route low-calibrated-confidence and ambiguous-source documents to review.
D. Abandon confidence-based routing and review a uniform random sample of all extractions.

---
---

# Answers

**Q1 — B.** This is the guide's named skill: pull the transactional facts into a **persistent
"case facts" block**, sent with every prompt, **outside** the summarised history. Summaries can
then stay vague without losing the numbers.

- **A** — an instruction cannot protect information the summary has already deleted. By the time
  the model answers, the exact amount is gone.
- **C** — without summarisation the context simply fills and the session dies earlier. The
  history layer is *supposed* to be lossy; that is why the facts live in a separate layer.
- **D** — `max_tokens` limits the **output**, not what survives in context.

**Q2 — D.** Trim tool output to the useful fields **before it enters the context** — early, not
later. The guide's example is exactly this: an order lookup returning 40+ fields when only five
matter.

- **A** — after the session, the damage is already done; the context filled during it.
- **B** — the model may ignore the fields while reasoning, but the tokens still occupy context.
  Instructions do not reduce the size of what was stored.
- **C** — a larger window postpones the fill; it does not stop 37 useless fields per call from
  accumulating.

**Q3 — A.** The "lost in the middle" effect: models reliably process the beginning and end of a
long input and may omit the middle. The guide's fix is a **key-findings summary at the start**
plus **explicit section headers** organising the detail.

- **B** — randomising means a *different* report is lost each run. The effect is positional; the
  fix is positional structure, not shuffling.
- **C** — the findings are being missed on the way **in**. Output budget does not change that.
- **D** — "pay equal attention" is a vague instruction against a mechanical position effect.

**Q4 — C.** The escalation trap, retested. Frustrated-but-solvable: **acknowledge the
frustration, offer to resolve**, and escalate only if the customer then asks for a human. Only an
**explicit request** for a human escalates immediately.

- **A** — frustration is not complexity. This customer never asked for a human.
- **B** — sentiment-based escalation is on the always-wrong list. How angry someone sounds does
  not tell you how hard the case is.
- **D** — the opposite over-correction. Sentiment must not *decide escalation*; acknowledging the
  customer's frustration is still good handling.

**Q5 — A.** A **policy gap** — the policy is silent on competitor matching — is one of the three
valid escalation triggers, and this is the guide's own example. The agent must not invent policy
in either direction.

- **B** — refusing invents a "no" the policy never states.
- **C** — applying the own-site rule invents a "yes" by analogy. Both B and C are the agent
  making policy.
- **D** — a goodwill discount neither answers the request nor involves the human who can.

**Q6 — D.** Multiple matches → **ask for an additional identifier**. Never select by heuristic.
Account operations against a guessed identity are exactly the class of action that must not run
on a guess.

- **A** and **C** — heuristic selection, with and without a disclaimer. A flagged assumption is
  still the wrong customer's account.
- **B** — runs the operation against two wrong accounts to find the right one.

**Q7 — B.** Structured error context has **four parts**: the failure type, what was attempted,
any partial results, and alternative approaches. With those, the coordinator can retry
differently, reroute, or continue with partial results.

- **A** — the category-and-flag pair is the Domain 2 *tool* error shape. Between agents, the
  coordinator also needs what was tried and what partially succeeded — "and nothing else"
  is what makes this wrong.
- **C** — the full log buries the four useful facts in noise and burns the coordinator's context.
- **D** — the subagent deciding to kill the workflow is the "stop everything" anti-pattern.

**Q8 — C.** The guide's named skill: synthesis output carries **coverage annotations** — which
findings are well supported, which topics have gaps because sources were unavailable. The reader
learns exactly where the report is weak.

- **A** — hides the gap by hiding the topic. The reader now does not know the subtopic exists.
- **B** — fills the gap with uncited model knowledge in a cited research product.
- **D** — a blanket disclaimer marks nothing in particular, so it changes no reading decision.
  The close-but-generic option.

**Q9 — A.** Attribution is lost during **summarisation**, so it must travel as **structure**:
claim-source mappings (claim, excerpt, source) that downstream agents are required to preserve
and merge. Provenance is preserved, never reconstructed.

- **B** — reconstructs citations after the fact; the best match found later is not necessarily
  where the claim came from.
- **C** — the subagents may well cite; the summarisation steps between them and the report still
  strip it. Instructions do not survive compression — structure does.
- **D** — fewer steps lose attribution more slowly. The remaining step still loses it.

**Q10 — B and D.** Conflicts are information: **record both values with attribution, explicitly
marked**, and the **coordinator** reconciles before synthesis (**B**). And **dates are
required** in structured outputs, so figures measured at different times stop masquerading as
contradictions (**D**).

- **A** — recency is context for the coordinator's decision, not an override rule.
- **C** — an average is a number neither source reported.

**Q11 — D.** "Typical patterns" instead of the specific classes it discovered = **context
degradation**. The direct fix is a **scratchpad file**: key findings written down as they are
found, and referenced for later questions.

- **A** — not hallucination in the temperature sense; the specific knowledge has degraded out of
  usable context. Temperature does not restore it.
- **B** — the model read the class successfully in hour one. Capability was never the problem.
- **C** — works, at the cost of re-paying the whole exploration per question. The scratchpad
  keeps the findings without the re-exploration.

**Q12 — B.** Crash recovery = **manifests**: each agent exports structured state to a known
location as it works; on resume the coordinator loads the manifest and injects it into the
agents' prompts. Restart becomes continuation.

- **A** — retries the crash without preserving anything; every attempt starts from zero.
- **C** — the conversation history is what the crash destroys. State that must survive a crash
  cannot live only there.
- **D** — `/compact` manages context size within a live session. It persists nothing.

**Q13 — A and C.** Both are guide-named skills for exactly these two moments: **`/compact`**
reduces context usage mid-session when discovery output has filled it (**A**), and **phase
summaries** — summarise phase one's key findings and inject them into the next phase's starting
context (**C**).

- **B** — a bigger window postpones degradation and fixes nothing. Permanent wrong answer.
- **D** — "remember the important things" is not a mechanism.

**Q14 — A and D.** Before cutting review: **segment the accuracy** by document type and field —
an aggregate can hide one failing segment (**A**) — and set up **stratified random sampling** of
the high-confidence group, because that is the group about to lose its reviewers, so its real
error rate must keep being measured (**D**).

- **B** — trusts exactly the number that masks segment failures.
- **C** — self-flagged uncertainty misses the errors the model is confidently wrong about — the
  same reason Q15's routing fails.

**Q15 — C.** Self-reported confidence is not calibrated — the audit is showing confidently-wrong
extractions above 0.9. Confidence becomes usable for routing only when **field-level scores are
calibrated against a labelled validation set**; then route the low-calibrated-confidence and
ambiguous-source documents to the limited reviewers.

- **A** — moves the threshold on a signal the audit just proved unreliable.
- **B** — length does not correlate with error the way calibrated confidence does.
- **D** — uniform sampling spends scarce reviewer time evenly across a population where errors
  cluster. Routing exists to spend it where they cluster.

---

## Score

___ / 15 · Q10, Q13 and Q14 need two answers each. You need both for the point.

**The Set 1 misses, retested:**

| Set 1 miss | Retested here |
|---|---|
| Q3 — the escalation trap (frustrated vs explicit ask) | **Q4** |
| Q5 — blaming the wrong component | **Q11** (name the mechanism before picking the fix) |

- **Below 10** — re-read `notes/domain-5-context-reliability.md`, then retake in three days.
- **10–12** — check where the misses cluster: context management (Q1–Q3, Q11–Q13), escalation
  (Q4–Q6), or reliability and provenance (Q7–Q10, Q14–Q15). Drill that third.
- **13 or more** — Domain 5 is covered. Confirm it on the 23 August mock.
