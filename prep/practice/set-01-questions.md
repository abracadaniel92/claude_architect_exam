# Practice Set 1 — Diagnostic (20 items)

Blueprint-weighted: D1 ×5 · D2 ×4 · D3 ×4 · D4 ×4 · D5 ×3.
Target time: **40 minutes** (2 min/item). Select one response unless stated otherwise.

Write your answers down before checking `set-01-answers.md`. Score by domain — the point of
this set is to find your weak domain, not to feel good.

---

### Scenario: Customer Support Resolution Agent

**Q1.** Your support agent calls `lookup_order` with a customer-supplied order number, and the
MCP tool times out because the orders service is briefly unavailable. The tool currently
returns `{"isError": true, "message": "Operation failed"}`. The agent responds by telling the
customer their order does not exist. What change most directly prevents this failure mode?

A. Return structured error metadata including `errorCategory`, an `isRetryable` boolean, and a human-readable description.
B. Have the tool return an empty result set so the agent treats it as a no-match case and asks for clarification.
C. Increase the tool's timeout so transient outages resolve before the call returns.
D. Add a system prompt instruction telling the agent never to claim an order doesn't exist unless it is certain.

---

**Q2.** Your agent has an 88% first-contact resolution rate but audit review finds that in
several cases it processed refunds for a customer whose identity had been verified in a
*different* conversation earlier that day. Refunds must never be issued without verification
in the current session. What is the correct fix?

A. Reduce the agent's tool set so `process_refund` is only enabled after a routing classifier detects a refund intent.
B. Implement a programmatic prerequisite that blocks `process_refund` until `get_customer` has returned a verified customer ID in the current session.
C. Add a few-shot example showing the agent re-verifying identity at the start of every session.
D. Add a `session_verified` boolean to the system prompt context and instruct the agent to check it.

---

**Q3.** A customer writes: "This is the third time I've contacted you about this broken
blender. Just give me a human, I'm done explaining this." Your agent has full capability to
process the replacement. What should it do?

A. Run a sentiment check and escalate if negative sentiment exceeds the configured threshold.
B. Acknowledge the frustration, offer to process the replacement immediately, and escalate only if the customer reiterates their preference.
C. Escalate to a human immediately, compiling a structured handoff summary.
D. Process the replacement without escalating, since resolving it is the fastest path to satisfaction.

---

**Q4.** Your `lookup_order` MCP tool returns 43 fields per order. The agent only ever needs
order status, item names, purchase date, refund eligibility, and total. Over long multi-issue
conversations, context fills with order payloads and the agent starts giving inconsistent
answers about earlier issues. Which two changes address this? **(Select two.)**

A. Instruct the agent in the system prompt to ignore irrelevant fields in tool results.
B. Trim the tool's output to the relevant fields before the results enter the conversation context.
C. Switch to a model with a larger context window so the full payloads fit comfortably.
D. Extract structured issue data (order IDs, amounts, statuses) into a separate persistent context layer.

---

### Scenario: Multi-Agent Research System

**Q5.** Your coordinator delegates to a document-analysis subagent, which returns excellent
summaries. But the final reports attribute claims to the wrong sources, and some claims have
no source at all. The document-analysis subagent's output is a well-written prose summary of
each document. What is the most likely root cause?

A. The coordinator is not passing source URLs to the synthesis subagent.
B. The report-generation subagent is reformatting citations incorrectly.
C. The synthesis subagent lacks instructions to preserve attribution when merging findings.
D. The document-analysis subagent returns prose without structured claim-source mappings, so attribution is lost at the summarization step.

---

**Q6.** Your coordinator agent is configured with `allowedTools: ["Read", "Grep", "WebSearch"]`
and a system prompt instructing it to delegate document analysis to a specialized subagent.
In testing, it never delegates — it analyzes documents itself. What is the cause?

A. `allowedTools` does not include `"Task"`, so the coordinator has no mechanism to spawn subagents.
B. Subagents must be registered in `.mcp.json` before a coordinator can invoke them.
C. The subagent's AgentDefinition description is too vague for the coordinator to select it.
D. The coordinator's system prompt needs stronger language emphasizing that delegation is mandatory.

---

**Q7.** Two credible sources in your research report state different figures for the same
market size: one says $4.2B (published 2024, surveying North America) and one says $6.8B
(published 2026, global). Your synthesis agent currently picks the more recent figure. What
should it do instead?

A. Discard both and re-delegate to the web-search subagent for a third, tie-breaking source.
B. Average the two figures and note the range in a footnote.
C. Preserve both values with source attribution and methodological context, and structure the report to distinguish well-established from contested findings.
D. Route the conflict to the coordinator, which selects the figure from the more authoritative source.

---

**Q8.** Your coordinator delegates four research subtasks. It currently emits one Task tool
call, waits for the result, then emits the next. Total latency is 4× a single subagent run.
What change enables parallel execution?

A. Use `fork_session` to create four branches from the coordinator's baseline analysis.
B. Increase the coordinator's `allowedTools` limit so it can hold more concurrent tool calls.
C. Configure each subagent's AgentDefinition with a `parallel: true` flag.
D. Emit all four Task tool calls in a single coordinator response.

---

### Scenario: Code Generation with Claude Code

**Q9.** Your team's monorepo has three packages, each with distinct API conventions. You want
each package's maintainers to control which shared standards documents apply to their package,
without duplicating those documents. What is the most maintainable approach?

A. Create a skill per package in `.claude/skills/` containing that package's standards.
B. Place a CLAUDE.md in each package directory that uses `@import` to reference the relevant standards files.
C. Create `.claude/rules/` files with `paths:` globs for each package directory.
D. Concatenate all standards into the root CLAUDE.md under per-package headers.

---

**Q10.** A developer reports that Claude Code applies your team's commit-message conventions
inconsistently — sometimes correct, sometimes not, across sessions on the same repo. What
should they run first to diagnose it?

A. `/doctor`
B. `/compact`
C. `/memory`
D. `claude --resume`

---

**Q11.** You've built a skill that performs a full-codebase dependency analysis. It produces
several thousand lines of output. Developers report that after invoking it, Claude Code seems
to lose track of the task they were working on. Which SKILL.md frontmatter option addresses
this?

A. `context: fork`
B. `paths: ["**/*"]`
C. `allowed-tools: [Read, Grep, Glob]`
D. `argument-hint: <package-name>`

---

**Q12.** You are assigned to add a null check to a single utility function after a stack trace
identified the exact line. Which approach is appropriate?

A. Plan mode, because any change to a shared utility has architectural implications.
B. Direct execution, but only after spawning an Explore subagent to map the utility's usage.
C. Plan mode, to explore whether other call sites have the same problem before changing anything.
D. Direct execution.

---

### Scenario: Structured Data Extraction

**Q13.** Your extraction tool's JSON schema marks `vendor_tax_id` as required. Processing a
batch of invoices, you find the model populates plausible-looking but fabricated tax IDs for
the ~20% of invoices that don't print one. What is the correct fix?

A. Add a system prompt instruction: "Never fabricate values that are not present in the source document."
B. Make `vendor_tax_id` optional and nullable in the schema.
C. Add a validation-retry loop that re-requests extraction when the tax ID fails a checksum.
D. Add few-shot examples showing invoices without tax IDs.

---

**Q14.** Your pipeline processes three document types with three different extraction schemas.
The document type is not known until the model reads the document. Occasionally the model
returns a conversational text response instead of calling any extraction tool. What
configuration fixes this?

A. `tool_choice: {"type": "any"}`
B. `tool_choice: {"type": "none"}` with an output schema instead
C. `tool_choice: {"type": "auto"}`
D. `tool_choice: {"type": "tool", "name": "extract_invoice"}`

---

**Q15.** Extraction validation fails on 6% of documents. Investigating, you find two distinct
causes: (a) the model formats dates as `03/04/2026` when the schema expects ISO 8601, and (b)
the requested purchase-order number appears only in a separate document not supplied to the
model. You implement a retry loop that resends the document, the failed extraction, and the
validation error. What outcome should you expect?

A. Cause (b) resolves; cause (a) does not, because format errors require a schema change.
B. Both causes resolve, since the model can self-correct given specific validation errors.
C. Cause (a) resolves; cause (b) does not, because the information is absent from the source.
D. Neither resolves, because retries cannot fix schema-level failures.

---

**Q16.** Your team runs two Claude workloads: a nightly test-generation job whose output is
reviewed the next morning, and a pre-commit hook that must return before the developer's
commit completes. A cost review proposes moving both to the Message Batches API for the 50%
savings. What is the correct assessment?

A. Keep both synchronous; the Batches API cannot correlate responses to requests reliably.
B. Move both; poll for completion and the batches typically finish in minutes.
C. Move both, with a timeout fallback to the synchronous API if a batch exceeds five minutes.
D. Move the nightly test generation only; keep the pre-commit hook on the synchronous API.

---

### Scenario: Claude Code for Continuous Integration

**Q17.** Your CI code review flags 40% false positives in the "unused variable" category and
about 5% in the "SQL injection risk" category. Developers have started ignoring all automated
comments, including the security ones. What should you do first?

A. Temporarily disable the unused-variable category while you improve its prompt, keeping the security category active.
B. Require two independent review passes and post only findings that appear in both.
C. Add a confidence score to each finding and post only those above 0.8.
D. Add "only report findings you are highly confident about" to the review prompt.

---

**Q18.** Your CI job runs `claude "Review this diff for security issues" --output-format json`
and the job never completes; logs show it waiting for input. What is the fix?

A. Set `CLAUDE_HEADLESS=true` in the job environment.
B. Add `--no-interactive`.
C. Add the `-p` flag.
D. Add `--json-schema` so the process knows to terminate after producing valid output.

---

**Q19.** After a new commit, your CI re-runs the review on the updated PR. Developers complain
that every previously-reported issue is posted again as a new comment, burying the new
findings. What is the appropriate fix?

A. Reduce review frequency to once per PR, at open time.
B. Include the prior review findings in context and instruct Claude to report only new or still-unaddressed issues.
C. Deduplicate comments in the posting script by hashing the finding text.
D. Only run the review on the incremental diff since the last review.

---

### Scenario: Developer Productivity with Claude

**Q20.** Your agent has both the built-in `Grep` tool and an MCP-provided
`search_code_semantically` tool that returns semantically ranked matches with surrounding
context. In practice the agent almost always uses `Grep`, even for conceptual queries where
semantic search would be far better. The MCP tool's description reads: "Searches code."
What is the most effective first step?

A. Add a system prompt instruction: "CRITICAL: Always prefer `search_code_semantically` over `Grep`."
B. Remove `Grep` from the agent's allowed tools so it must use the MCP tool.
C. Add 6–8 few-shot examples demonstrating conceptual queries routing to the MCP tool.
D. Expand the MCP tool's description to detail its capabilities, output format, example queries, and when to use it versus text search.

---

**Scoring:** record which domain each miss falls in. Any domain where you miss more than one
third of its items goes on your day-10 focus list.
