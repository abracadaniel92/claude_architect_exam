# Mock 1 — Full-length exam simulation (60 questions)

**Take this timed and cold. Do not read the answer file first.**

| | |
|---|---|
| Questions | 60 |
| Time | 120 minutes |
| Format | 4 scenarios × 15 questions, as on the real exam |
| Multiple-response | 10 questions, each marked **(Select two.)** |
| Working pass mark | 43 / 60 (the real exam scales to 720 / 1000) |
| Answer key | `mock-01-answers.md` — with a per-domain score sheet |

Domain spread: D1 15 · D2 11 · D3 12 · D4 12 · D5 10 (blueprint is 16/11/12/12/9).

Write your answers on paper, one line per question. Note the time when you finish.
The scenario text is background only — every question is self-contained.

---

## Scenario A — Customer Support Resolution Agent

*A retailer has built a support agent on the Claude Agent SDK. It handles returns, billing
disputes and account problems through four MCP tools: `get_customer`, `lookup_order`,
`process_refund` and `escalate_to_human`. The target is 80%+ first-contact resolution, with
reliable handoff to human agents when needed.*

**1.** The team's agentic loop continues whenever `stop_reason` is not `"end_turn"`. In
production the loop occasionally continues after the agent has already answered the customer, and
occasionally terminates while a tool result is still outstanding. Which loop condition should the
implementation use?

- A. Continue while `stop_reason` is `"tool_use"`; stop when it is `"end_turn"`
- B. Continue while the assistant message contains no text block
- C. Continue until the model calls an explicit `task_complete` tool
- D. Continue until a configured maximum iteration count is reached

**2.** In one turn Claude returns three `tool_use` blocks: `get_customer`, `lookup_order` and a
second `lookup_order`. How must the results be returned?

- A. As three separate user messages, in the order the tools were called
- B. As one user message containing the first result, with the remainder sent on later turns
- C. As one user message containing all three `tool_result` blocks, each carrying its
  `tool_use_id`
- D. As one user message containing a text summary of all three results

**3.** Post-incident review finds that in roughly 4% of conversations `process_refund` executed
before the customer's identity was verified. The system prompt already instructs the agent to
verify identity first. Which approach guarantees the sequence?

- A. Restate the instruction at the top of the system prompt in emphatic language
- B. Add four few-shot examples showing verification preceding every refund
- C. Reorder the tool definitions so `get_customer` is declared before `process_refund`
- D. Add a prerequisite gate that blocks `process_refund` until `get_customer` has returned a
  verified customer ID

**4.** When a case is escalated, the human agent receives the case in a separate console and
cannot see the agent's conversation. **(Select two.)** Which two elements must the handoff
summary contain?

- A. A sentiment score describing the customer's tone during the conversation
- B. The root cause analysis produced during the investigation
- C. The complete untrimmed output of every `lookup_order` call made
- D. The recommended action, including the refund amount under discussion

**5.** A customer's first message reports three separate problems: a missing delivery, a duplicate
charge, and a login failure. How should the agent handle the message?

- A. Ask the customer which problem should be addressed first
- B. Split the message into separate items, investigate them in parallel using shared context,
  and return one combined response
- C. Resolve the problems sequentially, closing each one before beginning the next
- D. Escalate to a human, because multiple simultaneous issues exceed the agent's designed scope

**6.** Company policy states that refunds above $500 must never be issued without human approval.
Which implementation satisfies this?

- A. A tool call interception hook that blocks `process_refund` above $500 and routes the case to
  `escalate_to_human`
- B. A `PostToolUse` hook that reverses any refund above $500 after it has been issued
- C. A system prompt section stating the $500 limit and the escalation requirement
- D. A `max_amount` parameter in the `process_refund` schema that the agent is instructed to
  respect

**7.** Logs show the agent frequently calls `lookup_order` when it needs customer account data,
and `get_customer` when it needs shipment status. Both tool descriptions are a single sentence.
What is the most effective first step?

- A. Merge both tools into one `lookup_entity` tool that accepts any identifier type
- B. Set `tool_choice` to `{"type": "any"}` so the agent is forced to select a tool
- C. Expand both descriptions to state accepted input formats, example queries, edge cases, and
  when to use each tool instead of the other
- D. Add a routing layer that inspects each customer message and selects the tool before the model
  is called

**8.** `process_refund` currently returns `{"isError": true, "message": "Operation failed"}` for
every failure. What should it return instead?

- A. `isError: true` with the raw stack trace from the payment service
- B. A successful response with an empty result object, so the conversation can continue
- C. `isError: true` with the message text expanded to describe the failure in more detail
- D. `isError: true` with an error category, a retryable flag, and a human-readable message

**9.** A refund is rejected because the order was delivered 45 days ago and the return window is
30 days. How should the tool classify this failure?

- A. Transient, retryable, because the window may be extended by a later promotion
- B. Business, not retryable, accompanied by a customer-friendly explanation of the policy
- C. Permission, not retryable, because the agent lacks authority for this refund
- D. Validation, retryable once the input has been corrected

**10.** Four tool failures occur during one shift. Which one can be resolved by retrying the
identical call?

- A. `lookup_order` returns a gateway timeout after 30 seconds
- B. `process_refund` is rejected because the order falls outside the return window
- C. `get_customer` is rejected because the credential lacks the `customers:read` scope
- D. `lookup_order` is rejected because the order ID does not match the expected format

**11.** Two behaviours are reported in the same week: the agent sometimes replies with a written
description of what it would look up instead of calling any tool, and when it does call a tool it
sometimes selects the wrong one of two similar tools. **(Select two.)** Which two changes address
these behaviours?

- A. Set `tool_choice` to `{"type": "any"}` for turns where a lookup is required
- B. Set `tool_choice` to `{"type": "auto"}` for every turn
- C. Rewrite the overlapping tool descriptions so each states what it returns and when it should be
  chosen over the other
- D. Reduce `max_tokens` so the model has less room to produce prose

**12.** The team has grown the agent to 18 tools, including several belonging to the fulfilment
and analytics teams. Tool selection has become unreliable, and the agent occasionally runs
analytics queries during refund conversations. What should the architect do?

- A. Add a system prompt section listing which tools belong to which workflow
- B. Set `tool_choice` to `{"type": "any"}` so the agent commits to a tool each turn
- C. Scope the agent to the 4–5 tools its role requires, adding a narrow tool for any cross-role
  action it genuinely needs
- D. Consolidate the 18 tools into 5 general tools, each taking a `mode` parameter

**13.** In conversations longer than about 30 turns, two problems appear. Summarised history loses
order numbers, refund amounts and promised dates. Separately, each `lookup_order` call returns
more than 40 fields, of which 5 are used. **(Select two.)** Which two changes address these
problems?

- A. Summarise the conversation more frequently, so less raw history accumulates
- B. Maintain a case-facts block of order IDs, amounts, dates and statuses, included in every
  prompt outside the summarised history
- C. Trim each `lookup_order` response to the relevant fields before it enters the context
- D. Move the conversation to a model with a larger context window

**14.** Fifteen minutes into a billing investigation, the customer writes: "Stop. I want to speak
to a real person." The agent is two tool calls away from identifying the duplicate charge. What
should it do?

- A. Complete the diagnosis first, then escalate with a full root cause analysis
- B. Offer one further attempt, and escalate only if the customer repeats the request
- C. Assess the message sentiment and escalate if it is strongly negative
- D. Escalate immediately, passing the structured handoff summary

**15.** `get_customer` returns three customer records matching the name and postcode given. What
should the agent do?

- A. Select the record with the most recent order activity and continue
- B. Ask the customer for an additional identifier, such as an order number or email address
- C. Process the request against all three records and report the combined result
- D. Escalate to a human, because ambiguous identity is a policy gap

---

## Scenario B — Multi-Agent Research System

*A coordinator agent delegates work to specialised subagents: web search, document analysis,
synthesis, and report generation. The system produces detailed research reports with citations
for analysts.*

**16.** A report on "the impact of automation on regional labour markets" covers manufacturing
thoroughly and omits logistics, retail and agriculture. Coordinator logs show the topic was split
into three subtasks, all concerning manufacturing. Each subagent returned complete, accurate work
for the subtask it was given. What is the cause?

- A. The synthesis subagent over-weighted the earliest source set it received
- B. The coordinator's task decomposition was too narrow
- C. The web search subagent issued queries that were too generic
- D. Attention dilution in the report generation subagent

**17.** Four subagents currently run one after another, and a full research run takes 20 minutes.
Their work is independent. How are they run in parallel?

- A. Set a `parallel: true` field in each AgentDefinition
- B. Call `fork_session` before dispatching each subagent
- C. Issue several Task tool calls within a single assistant response
- D. Raise `max_tokens` so more tool calls fit into one response

**18.** A newly configured coordinator cannot start any subagent at all; every attempt fails
before a subagent runs. What is the most likely cause?

- A. The coordinator's `allowedTools` does not include `"Task"`
- B. The subagents' AgentDefinitions are missing their system prompts
- C. The coordinator has been configured with a model that cannot delegate
- D. The subagent server has not been declared in `.mcp.json`

**19.** The synthesis subagent produces generic statements that do not reflect the specific
findings gathered earlier, and the citations in the final report cannot be traced back to
individual claims. **(Select two.)** Which two changes address these problems?

- A. Increase the synthesis subagent's context window
- B. Include the web search results and document analysis output directly in the synthesis
  subagent's prompt
- C. Allow the synthesis subagent to call the web search tool so it can recover missing detail
- D. Require an output format that separates each finding from its source metadata: URL, document
  name and page reference

**20.** An engineer proposes letting the document analysis subagent send its findings straight to
the synthesis subagent, bypassing the coordinator, to reduce token usage. How should the architect
respond?

- A. Accept, because it removes an unnecessary hop and lowers cost
- B. Accept, because the two subagents can then resolve disagreements between sources themselves
- C. Reject, because routing all messages through the coordinator preserves visibility, keeps
  error handling in one place, and controls what information flows where
- D. Reject, because the Task tool cannot transfer messages between subagents

**21.** The coordinator prompt is a numbered procedure of eleven steps. When a research topic
does not match the expected shape, subagents follow the procedure anyway and return work that does
not fit the question. What should change?

- A. Extend the procedure with additional steps covering the failing cases
- B. Replace the subagents with a single agent holding the full procedure
- C. Move the procedure into each subagent's AgentDefinition so it is applied locally
- D. Rewrite the coordinator prompt to state goals and quality standards rather than step-by-step
  instructions

**22.** After the decomposition is corrected, coverage of some subtopics is still thin, and this
is only visible once the synthesis is read. What should the coordinator do?

- A. Run an iterative refinement loop: review the synthesis, identify gaps, dispatch targeted
  follow-up tasks to the search and analysis subagents, then re-run synthesis
- B. Run synthesis twice and report only the findings that both runs produce
- C. Give the synthesis subagent a larger context window so it can consider more sources at once
- D. Add a fixed fourth subtask to every research run to increase coverage

**23.** The synthesis subagent needs to verify facts as it writes. Analysis shows 85% of these
checks are simple confirmations of dates, names and figures; the remainder need full source
retrieval. What is the appropriate design?

- A. Give the synthesis subagent the complete web search toolset
- B. Give the synthesis subagent a narrow `verify_fact` tool for the simple checks, and route the
  remainder through the coordinator
- C. Route every verification through the coordinator, to keep the hub-and-spoke pattern intact
- D. Merge the synthesis and web search subagents into a single agent

**24.** The document analysis subagent repeatedly calls tools simply to discover which document
collections and schemas exist before it can begin work. What should the MCP server expose?

- A. A static list of collections written into the coordinator's system prompt
- B. A `list_everything` tool that returns all documents in all collections
- C. A cache in front of the discovery calls, so repeated exploration is cheaper
- D. The collection catalogue as MCP resources, so the agent can see what exists without
  exploratory tool calls

**25.** The team needs the research system to read and comment on issues in the company's Jira
instance, using Jira's standard fields and workflows. What is the appropriate approach?

- A. Build a custom MCP server, because the team's Jira usage is unique
- B. Expose Jira through Bash commands wrapping the REST API
- C. Use an existing community MCP server for Jira, and build custom servers only for workflows
  specific to the team
- D. Add Jira credentials to the coordinator's system prompt and let it call the API directly

**26.** A specialised MCP search tool has been added, but the agents keep using the built-in Grep
tool for the same work, producing worse results. The MCP tool is registered correctly and works
when called. What should be done first?

- A. Improve the MCP tool's description so the agents understand what it can do and when to prefer
  it
- B. Force the MCP tool with `tool_choice: {"type": "tool", "name": ...}` on every turn
- C. Remove Grep from the agents' allowed tools
- D. Rename the MCP tool so that it sorts before Grep in the tool list

**27.** The web search subagent times out. It currently returns the message "search unavailable",
and the coordinator halts the entire research run. **(Select two.)** Which two changes should be
made?

- A. Have the subagent return structured error context: the failure type, the query attempted, any
  partial results, and alternative approaches
- B. Have the subagent return an empty result set marked as successful, so the run completes
- C. Have the subagent retry the identical query until it succeeds
- D. Have the coordinator continue with the remaining subagents and annotate the affected topics as
  coverage gaps in the final report

**28.** Synthesis flags a contradiction between two figures for the same indicator. On inspection,
one figure is from a 2019 survey and the other from a 2025 survey; they do not conflict. What is
the correct fix?

- A. Have the synthesis subagent re-fetch each source at synthesis time to check its date
- B. Require every subagent to record publication or collection dates, source location and
  methodology in its structured output
- C. Instruct the synthesis subagent to weigh sources by credibility when figures differ
- D. Add a `conflict_detected` flag to the report generation schema

**29.** Two equally credible sources report different values for the same market size, and both
are current. What should the document analysis subagent do?

- A. Report the value from the source with the larger sample
- B. Omit the figure and note that the market size could not be established
- C. Request a third source and report the value supported by two of the three
- D. Record both values with their sources, clearly marked, and leave the decision to the
  coordinator before synthesis runs

**30.** Analysts report that the final report's most important findings are frequently
overlooked, because they sit in the middle of a long document. What is the correct structural
fix?

- A. Place a summary of the key findings at the beginning, and organise the remaining detail under
  clear section headings
- B. Order the findings by the time at which they were retrieved
- C. Increase the context window used by the report generation subagent
- D. Instruct the model to re-read the middle section before finalising the report

---

## Scenario C — Code Generation with Claude Code

*A 40-engineer platform team uses Claude Code for feature work, refactoring, debugging and
documentation across a monorepo. They maintain shared configuration in the repository, and they
also run Claude Code non-interactively inside their CI pipeline.*

**31.** A newly onboarded engineer reports that Claude Code ignores the team's naming and error
handling conventions, while every other engineer's sessions apply them correctly. All engineers
work from the same clone of the repository. What is the cause?

- A. The new engineer has not run `/memory` to load the team's files
- B. The conventions are in `.claude/rules/` without a `paths` frontmatter entry
- C. The conventions are stored in `~/.claude/CLAUDE.md`, which is not shared through version
  control
- D. The repository's CLAUDE.md exceeds the size that Claude Code loads automatically

**32.** The monorepo has 12 packages. Four shared standards documents exist — API design, testing,
security review and release process — and each package needs a different subset of them. The
standards must apply to all work in a package without anyone having to invoke anything, and the
documents must not be duplicated. What should the team implement?

- A. A skill for each standards document, invoked when the engineer judges it relevant
- B. A CLAUDE.md per package that uses `@import` to reference only the standards documents that
  apply to it
- C. One root CLAUDE.md containing all four documents, separated by package headings
- D. A `.claude/rules/` file per standards document, each with `paths` globs listing the package
  directories it applies to

**33.** Two complaints arrive in the same retrospective. Engineers say that every session loads
instructions for parts of the stack they are not touching. Separately, a contractor who cloned the
repository does not receive the team's test conventions at all. **(Select two.)** Which two
changes address these complaints?

- A. Move the shared conventions out of user-level configuration and into the repository
- B. Consolidate every convention into the root CLAUDE.md under clear headings
- C. Split the conventions into `.claude/rules/` files with `paths` globs, so each loads only when
  a matching file is edited
- D. Convert each set of conventions into a skill that engineers invoke when relevant

**34.** The team wants a `/review` command that every engineer receives automatically when they
clone the repository. Where should it be defined?

- A. `.claude/commands/review.md`, committed to the repository
- B. `~/.claude/commands/review.md` on each engineer's machine
- C. A `commands` array in `.claude/config.json`
- D. A "Slash commands" section in the root CLAUDE.md

**35.** A skill that maps the dependency graph of a service produces several thousand lines of
intermediate output. Engineers find that their main conversation is consumed by this output before
the actual task begins. Which SKILL.md frontmatter key addresses this?

- A. `allowed-tools`
- B. `argument-hint`
- C. `context: fork`
- D. `paths`

**36.** Which key does **not** belong in SKILL.md frontmatter?

- A. `allowed-tools`
- B. `argument-hint`
- C. `context`
- D. `paths`

**37.** During a long refactoring session, an engineer notices that after about two hours the
agent answers questions about "typical patterns in codebases like this" rather than referring to
the specific classes and call sites it examined earlier in the session. What is the direct fix?

- A. Have the agent write key findings to a scratchpad file during exploration and read that file
  back when it needs them
- B. Switch to a model with a larger context window
- C. Instruct the agent to re-read the relevant source files before answering each question
- D. Raise `max_tokens` so responses can carry more detail

**38.** The CI job that runs Claude Code shows two defects: the job hangs until the runner's
timeout is reached, and when it is killed the partial output cannot be parsed by the script that
posts pull request comments. **(Select two.)** Which two changes are required?

- A. Set `CLAUDE_HEADLESS=true` in the job environment
- B. Run Claude Code with `-p` / `--print`
- C. Add the `--batch` flag so the job does not wait for a session
- D. Use `--output-format json` together with `--json-schema`

**39.** The team must migrate from one HTTP client library to another across 45 files, with three
call sites requiring redesign because the new library handles retries differently. Which approach
is correct?

- A. Direct execution, because each individual file change is mechanical
- B. Plan mode, because the change spans many files and includes decisions with architectural
  consequences
- C. Direct execution first, switching to plan mode if unexpected complexity appears
- D. Forty-five separate sessions, one per file, to keep each context small

**40.** An engineer finds that Claude Code applies different conventions in two checkouts of the
same repository on the same machine. What is the first diagnostic step?

- A. Run `/compact` to clear accumulated context in the affected session
- B. Compare the two working trees for uncommitted changes to CLAUDE.md
- C. Re-clone the repository to rule out corruption
- D. Run `/memory` to verify which memory files are loaded in each session

**41.** An engineer has described in prose how log lines should be transformed into structured
events. The output is inconsistent between runs. What is the most effective way to make the
transformation consistent?

- A. Provide two or three concrete input/output examples of the transformation
- B. Rewrite the prose description at greater length and in more precise language
- C. Move the description into plan mode so the approach is agreed before implementation
- D. Convert the description into a skill so it is applied the same way each time

**42.** The automated reviewer runs again after new commits are pushed to an open pull request,
and posts the same comments a second time on findings that have not yet been addressed. What
should change?

- A. Post comments only on the files touched by the newest commit
- B. Suppress any comment whose text matches an earlier comment
- C. Include the earlier findings in the context and instruct the reviewer to report only new or
  still-unfixed issues
- D. Run the reviewer only once, when the pull request is opened

**43.** An engineer wants a personal variant of a shared team skill, with different defaults,
without affecting teammates. What should they do?

- A. Edit the shared skill and add a conditional section for their own use
- B. Create the variant in `~/.claude/skills/` under a different name
- C. Copy the shared skill into `.claude/skills/` with an added personal suffix
- D. Override the skill's frontmatter in `~/.claude/CLAUDE.md`

**44.** An engineer returns after two days to a session in which the agent analysed a 40-file
service. Three of those files have been modified since, and the engineer knows which three. What
is the most efficient way to continue?

- A. Start a fresh session, because tool results from two days ago cannot be trusted
- B. Start a fresh session and paste the previous session's final summary
- C. Resume the session and ask the agent to re-read all 40 files
- D. Resume the session with `--resume`, stating which three files changed so only those are
  re-read

**45.** The team wants to add test coverage to a legacy service nobody currently understands. The
module boundaries, the dependency structure and the risky areas are all unknown at the outset.
Which decomposition approach fits?

- A. Prompt chaining: one review pass per file, then one pass across files
- B. A fixed three-phase chain: map, generate, verify — applied identically to every module
- C. Dynamic decomposition: map the structure first, identify the risky areas, then build a plan
  that adapts as dependencies are discovered
- D. A single pass over the whole service, to keep the analysis consistent

---

## Scenario D — Structured Data Extraction

*A finance operations team extracts structured records from supplier invoices, contracts and
remittance advice. Documents arrive as PDFs from several hundred suppliers, in inconsistent
layouts. Extracted records are validated against JSON schemas and pushed into an ERP system.*

**46.** The current implementation asks for JSON in the prompt and parses the reply, retrying when
parsing fails. Roughly 3% of responses fail to parse. What is the most reliable way to guarantee
that responses conform to the schema?

- A. Lower the temperature and instruct the model to emit only JSON
- B. Define the schema as a tool and use tool use to produce the structured output
- C. Add a JSON repair library to the post-processing step
- D. Add three few-shot examples of correctly formatted JSON to the prompt

**47.** Remittance advice documents are generated by supplier systems and always contain a
remittance reference. In about 2% of extractions the `remittance_reference` field is absent from
the output entirely, and those records are rejected downstream. What is the correct schema change?

- A. Make `remittance_reference` a required field
- B. Keep the field nullable and add a validation rule that rejects null values
- C. Add a few-shot example showing the reference being extracted
- D. Fill the field during post-processing from the payment file

**48.** Contracts sometimes include a purchase order number and sometimes do not. When it is
absent, the model produces plausible-looking values that do not exist. What is the correct schema
change?

- A. Add a prompt instruction not to invent purchase order numbers
- B. Add a regex pattern constraint to the field
- C. Add a validation rule rejecting purchase order numbers absent from the ERP
- D. Make the field optional and nullable

**49.** Five document types arrive on the same intake queue, each with its own extraction schema
defined as a separate tool. The type is not known before the model reads the document, and the
model sometimes replies with a prose description of the document instead of extracting anything.
Which configuration is correct?

- A. `tool_choice: {"type": "auto"}`
- B. `tool_choice: {"type": "tool", "name": "extract_invoice"}`
- C. `tool_choice: {"type": "any"}`
- D. `tool_choice: {"type": "none"}` followed by manual routing

**50.** Every document must have `extract_metadata` run against it before any enrichment tool is
called. Which configuration enforces this?

- A. Declare `extract_metadata` first in the tools array
- B. Force `tool_choice: {"type": "tool", "name": "extract_metadata"}` on the first turn, then
  continue in subsequent turns
- C. Set `tool_choice: {"type": "any"}` and describe the required order in the system prompt
- D. Merge metadata extraction into each enrichment tool's schema

**51.** Validation is failing on two distinct groups of documents. In the first group, dates and
totals are structurally wrong. In the second, the failing field does not appear anywhere in the
source document. **(Select two.)** Which two responses are correct?

- A. For the first group, resend the original document, the failed extraction, and the specific
  validation errors
- B. For the first group, retry the identical request up to three times with a higher temperature
- C. For the second group, route the document to human review rather than retrying
- D. For the second group, retry with an instruction to search the document more carefully

**52.** Some extracted invoices are valid against the schema, but the line items do not sum to the
stated total. Which schema design surfaces this?

- A. Extract `calculated_total` alongside `stated_total` so the two can be compared
- B. Mark `total` as required, so the model cannot omit it
- C. Constrain `total` with a numeric minimum and maximum
- D. Rely on tool use, which prevents this class of error

**53.** Dates arrive as `03/04/2026`, `4 March 2026` and `2026-03-04`, and currency amounts arrive
with and without symbols and thousands separators. The schema types are already strict. What is the
correct fix?

- A. Widen the schema types to strings and clean the values downstream
- B. Add a post-processing normalisation layer between extraction and the ERP
- C. Reject non-conforming documents and request corrected copies from suppliers
- D. State the normalisation rules in the prompt, alongside the strict schema

**54.** The team runs two workloads. A nightly reconciliation over about 40,000 archived documents
must be ready by the following morning. A pre-approval check runs while a finance analyst waits on
screen. How should these be assigned?

- A. Both through the Message Batches API, for the cost saving
- B. Both through the real-time API, so results arrive in a predictable order
- C. The nightly reconciliation through the Message Batches API; the pre-approval check through the
  real-time API
- D. Both through the Message Batches API, with a real-time fallback when a batch is slow

**55.** The team is preparing its first large batch submission. **(Select two.)** Which two
statements about the Message Batches API are correct?

- A. Batch processing guarantees completion within one hour for batches under 10,000 requests
- B. Batch processing costs approximately 25% more than equivalent real-time requests
- C. Responses must be matched to requests by `custom_id`, not by position
- D. A single batch request cannot run a multi-turn tool-calling loop

**56.** About 1,200 documents arrive daily and are processed in batches. Batch processing may take
up to 24 hours, and the team has committed to a 30-hour SLA from arrival to ERP delivery. What
submission cadence meets the commitment?

- A. Submit every 4 hours
- B. Submit once per day at midnight
- C. Submit every 30 hours, matching the SLA
- D. Submit continuously, one document per request

**57.** Supplier categories are drawn from a fixed enum, but new categories appear every few
months, and some documents describe the category in terms that match none of the existing values.
What is the correct schema design?

- A. Remove the enum and accept free text for the category
- B. Keep the enum, add an `"other"` value with an accompanying detail string, and add an
  `"unclear"` value for ambiguous cases
- C. Keep the enum and require the model to select the closest existing value
- D. Maintain the enum and reject documents whose category is unmatched

**58.** Overall extraction accuracy is 97%, and the team proposes to reduce human review.
**(Select two.)** Which two checks should be performed first?

- A. Analyse accuracy separately by document type and by field
- B. Take a stratified random sample of high-confidence extractions and review them
- C. Reduce review to the extractions the model flags as low confidence
- D. Increase the overall sample size uniformly across all extractions

**59.** After the analysis, the team wants to route only some documents to human review. Which
approach is sound?

- A. Route documents whose extraction the model reports as low confidence, using the model's
  self-reported score directly
- B. Route documents from suppliers who have complained previously
- C. Route documents using field-level confidence scores calibrated against a labelled validation
  set, together with documents that are ambiguous or internally contradictory
- D. Route a fixed 10% of documents chosen at random

**60.** The document-store MCP tool returns an empty array both when a search legitimately matches
nothing and when the store is unreachable. Downstream, records are marked complete in both cases.
What should the tool return?

- A. An empty array in both cases, with a warning written to the server log
- B. An error in both cases, so no result is ever silently treated as complete
- C. An empty array for both, plus a `count` field the agent can check
- D. A successful empty result when nothing matches, and `isError` with a transient error category
  when the store is unreachable

---

*End of Mock 1. Record your finish time, then mark against `mock-01-answers.md`.*
