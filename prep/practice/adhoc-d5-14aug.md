# Domain 5 ad-hoc set — 14 August (15 questions)

Written 14 August, taken the same day: **14/15**. Missed Q4 only — and chose *both* wrong options,
which is what identified the cross-domain pattern in weak point 19 of `LOG.md`.

Balanced key, all six task statements. Deliberately avoids the framings in `drill-domain-5.md`, so
that drill stays usable as a separate test.

Three questions ask for **two answers**.

**The questions use exam-level English.** The explanations are in simple English.

Time: 30 minutes. Answers below — cover them while you work.

---

**Q1.** A developer on your team builds a support agent that sends only the newest user message on
each API request, along with a `session_id`, on the basis that "the API keeps track of the
conversation". The agent has no recollection of anything said earlier in the session. What is the
correct explanation and fix?

A. The `session_id` must be passed in a `conversation_id` field for the server to associate the turns.
B. The API is stateless; the full conversation history must be sent with every request, and the application is responsible for holding it.
C. Prompt caching must be enabled, which is what persists conversation state between calls.
D. The session needs `/compact` to be run periodically so earlier turns are retained in compressed form.

---

**Q2.** A customer asks for the delivery status of a shipment. The agent calls the carrier tracking
tool three times; each call returns an authorisation failure. No other tool exposes the status. The
customer has been polite throughout and has not asked to speak to anyone. What should the agent do?

A. Keep retrying the carrier tool with exponential backoff for the remainder of the session.
B. Continue without escalating — the customer is calm and has not requested a human.
C. Escalate to a human, because the agent cannot make progress on the request.
D. Tell the customer to contact the carrier directly and close the conversation.

---

**Q3.** Your document-search subagent returns the same response — an empty result set — in two
different situations: when a query genuinely matches nothing, and when the repository rejects the
request for lack of permission. The coordinator treats both as "searched, nothing found". What is
the correct design?

A. Distinguish the two: zero matches is a successful search with an empty result set, while an access failure is an error that may warrant a retry or a different route and must be reported as one.
B. Treat both as failures and have the coordinator retry each of them once before continuing.
C. Treat both as empty results, and have the coordinator verify permissions separately at the start of every run.
D. Return `null` in both cases and let the coordinator infer the difference from how long the call took.

---

**Q4.** Your synthesis agent cannot tell whether a "42% adoption" figure came from a 2021 survey or
a 2026 one, and cannot tell whether a claim originated in a peer-reviewed study or a vendor's
marketing page. The subagents return well-written prose summaries. Which two requirements address
this? **(Select two.)**

A. Instruct the synthesis agent to weigh sources by credibility when findings disagree.
B. Require every subagent output to carry publication or data-collection dates.
C. Require every subagent output to carry the source location and the methodology behind each finding.
D. Have the synthesis agent re-fetch each source at synthesis time to establish its date and type.

---

**Q5.** Your research report covers three kinds of content: quarterly revenue figures for six
competitors, recent market news, and benchmark results from a technical evaluation. A reviewer asks
you to render all of it as bullet lists, for visual consistency. What is the correct approach?

A. Adopt bullet lists throughout, as the reviewer suggests.
B. Adopt tables throughout, since tables are the densest format.
C. Adopt prose throughout, since prose carries nuance the other formats lose.
D. Match the format to the content: financial data as tables, news as prose, technical findings as structured lists.

---

**Q6.** Six research subagents each return roughly 3,000 words of prose, including their reasoning.
The final synthesis agent now runs out of context before it reaches the last two reports. What is
the correct fix?

A. Change the earlier agents to return structured data — key facts, citations, relevance scores — instead of long prose and reasoning.
B. Insert an intermediate summarisation agent that compresses each report before synthesis.
C. Run the synthesis step on a model with a larger context window.
D. Run synthesis on two reports at a time and merge the partial syntheses.

---

**Q7.** Your document-analysis subagent receives a 503 from the storage service on its first call
and immediately returns a structured error to the coordinator, which re-dispatches the task. This
happens on roughly one task in eight, and the round trips are slowing the whole workflow. What is
the correct design?

A. Move retry logic to the coordinator, which should retry any failed task with exponential backoff.
B. Have the coordinator ignore transient failures and proceed with whatever partial results exist.
C. Have the subagent resolve transient failures itself, reporting only what it cannot resolve, and including what it tried and any partial results.
D. Escalate repeated transient failures to a human operator for manual dispatch.

---

**Q8.** An audit of your support agent finds two things: it escalates about a third of cases it was
capable of resolving, and it fails to escalate several cases where the policy did not cover the
customer's request. What is the correct fix?

A. Train a classifier on historical transcripts and let it make the escalation decision.
B. Add explicit escalation criteria to the system prompt, with few-shot examples showing when to escalate and when to resolve.
C. Escalate whenever the model's confidence in resolving the case falls below a set threshold.
D. Route on a sentiment score, escalating the cases where the customer appears most dissatisfied.

---

**Q9.** You are mapping an unfamiliar 400-file service. The main agent's context fills with
directory listings, grep output and file dumps, and by the third hour its answers about components
it examined earlier have become vague. Which two practices apply? **(Select two.)**

A. Delegate noisy discovery work — "find every file that touches the billing queue" — to subagents, so the main agent retains the high-level picture.
B. Move to a model with a larger context window and continue as before.
C. Ask the product owner to narrow the scope of the mapping exercise.
D. Record key findings in a scratchpad file as they are discovered, and have the agent read from it when answering later questions.

---

**Q10.** A subagent in your pipeline is written so that any internal failure returns an empty
findings array with the status `complete`, on the grounds that this keeps the pipeline from
breaking. What is the correct assessment?

A. Sound design — the pipeline stays resilient and no downstream agent has to handle error states.
B. Acceptable, provided the failure is written to an external log that engineers can inspect afterwards.
C. Unsound — a failing subagent should terminate the workflow so the failure cannot be missed.
D. Unsound — reporting an error as a successful empty result makes recovery impossible and produces a final output that looks complete when it is not.

---

**Q11.** Two credible sources report different figures for the same quantity, and the coordinator
has decided both belong in the final report. How should the report present them?

A. In separate sections for well-established findings and contested findings, preserving each source's original wording and methodology.
B. As a single figure with a footnote noting that a disagreement exists in the literature.
C. As a range spanning the two values, which covers both sources without privileging either.
D. In the body as a single figure, with the disagreement documented in an appendix for readers who need it.

---

**Q12.** Human reviewer capacity covers about 15% of your daily extraction volume. Your confidence
scores are field-level and calibrated against a labelled validation set. Which extractions should
be routed to the reviewers?

A. The longest documents, since error rate rises with document length.
B. Extractions with low calibrated confidence, together with those from source documents that are ambiguous or contradict themselves.
C. A fixed random 10% of all extractions, plus any the model flags spontaneously.
D. Extractions from the vendors most recently added to the system, since they have the least processing history.

---

**Q13.** Two tool calls into diagnosing a billing discrepancy — an issue the agent has the tools and
authority to resolve — the customer writes: "Can you just put me through to a person?" What should
the agent do?

A. Complete the diagnostic steps first, so the human receives a full handover.
B. Offer to resolve it now, since the issue is solvable, and escalate only if the customer asks a second time.
C. Escalate immediately.
D. Ask the customer what they would like the human to do, then decide whether escalation is warranted.

---

**Q14.** A long code-migration session shows two problems. Files that were explicitly excluded from
the migration at the outset reappear in the agent's later proposals. And when phase two begins
tomorrow, its agents have no knowledge of what phase one concluded. Which two changes address
these? **(Select two.)**

A. Maintain a persistent constraints block — target version, excluded paths, deadline — included in every prompt, outside the summarised history.
B. Instruct the model at the start of the session to treat the constraints as permanent and never revise them.
C. Write a phase-one summary of decisions and findings, and inject it into the starting context of phase two.
D. Increase how often the history is automatically summarised, so the constraints are restated more frequently.

---

**Q15.** Ten minutes into a new session, you ask how the `RetryQueue` class handles poison messages.
The agent replies with a description of "how retry queues typically handle poison messages". Context
usage is under 15%. What is happening?

A. Context degradation — start a scratchpad file and record findings as they are discovered.
B. Context pressure from discovery output — run `/compact` before continuing.
C. The context window is too small for a codebase of this size — move to a larger-context model.
D. Nothing has degraded — the agent has never read the class and is answering from general knowledge. Direct it to locate and read the actual implementation first.

---
---

# Answers

**Q1 — B.** The API is **stateless**. It has no memory between requests, so the application must
send the full conversation history every time.

- **A** — invents a field. No such server-side association exists.
- **C** — prompt caching reduces the cost of re-sending a long prefix. It does not remove the need to send it, and it is not conversation state.
- **D** — `/compact` is a Claude Code session tool, not an API mechanism, and it reduces context rather than preserving it.

**Q2 — C.** **Inability to make progress** is one of the three valid escalation triggers, alongside
an explicit request for a human and a policy gap. None of them mentions the customer's tone. The
question makes the customer calm on purpose, to see whether you tie escalation to sentiment.

- **A** — the failure is authorisation, not transient. Retrying cannot fix a permission problem.
- **B** — the trap: no explicit request, so no escalation. But that is only one of three triggers.
- **D** — hands the customer your integration problem.

**Q3 — A.** An **access failure is not an empty result**. Zero matches is a successful search; a
permission failure or timeout is an error that may deserve a retry or another route. Collapsing
them removes the coordinator's ability to recover.

- **B** — retrying a genuine zero-match query wastes a call and returns the same answer.
- **C** — a start-of-run permission check does not help when access fails mid-run, and it still leaves the two cases indistinguishable.
- **D** — inferring an error from latency is guessing at something the subagent already knew.

**Q4 — B and C. ✗ Missed — chose A and D.** Subagents must record **dates** (**B**) and **source
location and methodology** (**C**) in structured output. Only the agent that held the source can
record these.

Both chosen answers tried to repair the loss **downstream**, which is the same shape as the two
Domain 4 misses on the same day:

- **A** — the chosen answer. Asks the synthesis agent to weigh credibility using information it cannot see. The scenario states it cannot distinguish a study from a vendor page.
- **D** — the chosen answer. Re-fetching reconstructs metadata after the fact; what you find later is not reliably where the claim came from, and it re-does work the subagent could have recorded for free.

**Provenance travels as structure from the agent that held the source.** It is never restored by
instruction and never reconstructed afterwards.

**Q5 — D.** Match the format to the content: financial data as **tables**, news as **prose**,
technical findings as **structured lists**. The guide is explicit that converting everything into
one format is wrong.

- **A**, **B**, **C** — all the same error, just three different single formats. Consistency of format is not the goal; fitness for the content is.

**Q6 — A.** When a later agent has too little context space, change the **earlier** agents to
return **structured data** — key facts, citations, relevance scores — rather than long prose and
reasoning. The reasoning was for the subagent's own use and does not need to travel.

- **B** — an extra summarisation step is another place attribution is lost, and it costs a model call per report.
- **C** — a bigger window postpones the problem while six agents keep emitting prose.
- **D** — merging partial syntheses loses the cross-report comparison that synthesis exists to do.

**Q7 — C.** **Local recovery**: a subagent resolves transient failures itself and reports only what
it cannot fix — with what it tried and any partial results. A 503 is the textbook transient failure.

- **A** — plausible engineering, wrong level. The round trip to the coordinator is the cost you are trying to remove, and the coordinator has less information about the failure than the subagent does.
- **B** — discards recoverable work and silently reduces coverage.
- **D** — a human dispatching retries for a transient service error.

**Q8 — B.** Explicit escalation criteria in the system prompt, **with few-shot examples** showing
when to escalate and when to resolve. Both symptoms — over-escalating and missing policy gaps — are
symptoms of criteria that were never stated.

- **A** — a classifier is a second system to build, train and maintain, for a decision the prompt can state.
- **C** — self-reported confidence, on the always-wrong list for escalation.
- **D** — sentiment, also on the always-wrong list.

**Q9 — A and D.** Two guide-named techniques for exactly this: **delegate noisy exploration to
subagents** so the main agent keeps the high-level picture (**A**), and keep a **scratchpad file**
of key findings to read from later (**D**) — the direct fix for context degradation.

- **B** — a larger context window does not fix attention quality. Permanent wrong answer.
- **C** — moves the problem to a person and abandons part of the task.

**Q10 — D.** **Hiding an error as a successful empty result** is one of the four named wrong
approaches: recovery becomes impossible, and the final output looks complete when it is not. Return
structured error context and let the coordinator decide.

- **A** — describes the anti-pattern as if it were the benefit.
- **B** — a log entry the coordinator cannot see does not help it recover, and the report is still silently wrong.
- **C** — the opposite anti-pattern: stopping the whole workflow because one agent failed.

**Q11 — A.** Separate sections for **well-established** and **contested** findings, keeping each
source's original wording and methodology.

- **B** — a footnote on a chosen figure still means one source was silently picked.
- **C** — a range is a number neither source reported, and it hides that they disagree.
- **D** — puts the contested status where the reader deciding on the number will not see it.

**Q12 — B.** Route on **low calibrated confidence** plus **ambiguous or self-contradictory source
documents**. Both are named, and they spend limited reviewer time where errors actually cluster.

- **A** — length is a proxy that was never validated against error rate.
- **C** — uniform sampling spreads scarce capacity evenly across a population where errors do not occur evenly, and "any the model flags spontaneously" is uncalibrated self-report.
- **D** — vendor age is another unvalidated proxy.

**Q13 — C.** An **explicit request for a human** is an immediate escalation trigger. Do not finish
investigating first.

- **A** — the most tempting wrong answer, because a full handover sounds considerate. The customer asked to be transferred, not to wait.
- **B** — the correct handling for a *frustrated* customer who has **not** asked. Applying it here is the escalation trap in reverse.
- **D** — questioning the request instead of honouring it.

**Q14 — A and C.** Two symptoms of different kinds, so two different fixes. Constraints drifting out
of the summary → a **persistent constraints block** in every prompt, outside the summarised history
(**A**). Phase two starting blind → a **phase summary** injected into its starting context (**C**).

- **B** — an instruction cannot protect facts that summarisation has already removed.
- **D** — more frequent summarisation loses detail faster, which is the cause rather than the cure.

**Q15 — D.** Nothing has degraded. The session is ten minutes old and under 15% context, and the
agent never read the class — it is answering from general knowledge. The fix is to make it read the
implementation.

The "typical patterns" phrasing is the textbook signal of context degradation, and the question
supplies it deliberately, then removes every precondition for that diagnosis. **A rule that fires on
a symptom needs its preconditions checked before it applies.**

- **A**, **B**, **C** — three fixes for a problem the question rules out. C is also the permanent wrong answer about context windows.

---

## Score

**14/15 on 14 August.** Q4, Q9 and Q14 needed two answers each; Q9 and Q14 correct, Q4 the one miss.

Both escalation directions correct in the same sitting — Q2 (no progress, calm customer) and Q13
(explicit request mid-investigation). The Set 1 escalation trap is closed. Q15's over-application
trap was not taken.

**The single miss is the important one.** Both chosen answers were wrong, and both mapped cleanly
onto the two symptoms in the scenario — so the select-two counting habit worked and still produced
two answers from the wrong family. Counting symptoms and judging content are separate steps.

Retake this cold if Mock 1 shows Domain 5 below 70%.
