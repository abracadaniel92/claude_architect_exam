# Mock 4 — Full-length exam simulation, repeat-miss paper (60 questions)

**Take this timed and cold. Budget 75 minutes for the first pass — 75 seconds per question — then
a second pass over flagged questions only. Mock 1 was finished in under 30 minutes and that is
what produced its misses. Finishing early is the failure mode, not a result.**

| | |
|---|---|
| Questions | 60 |
| Time | 120 minutes |
| Format | 4 scenarios × 15 questions, as on the real exam |
| Multiple-response | 10 questions, each marked **(Select two.)** |
| Working pass mark | 43 / 60 (the real exam scales to 720 / 1000) |
| Answer key | `mock-04-answers.md` — with a per-domain score sheet |

Domain spread: D1 16 · D2 11 · D3 12 · D4 12 · D5 9 (the blueprint weighting).

**How this set differs from Mocks 1–3.** It is built from the facts that have survived every
previous paper, plus the two mechanical triggers that have never fired:

- **The repair verb.** Post-process, validate, reconcile, re-fetch, downstream. That family has
  taken **four** marks (weak point 42) and appears here as a distractor in six questions — and
  once as the *correct* answer, because a hook really is the right place to normalise a tool
  result. Halting on the verb is not the same as rejecting it.
- **Domain 3 grouping.** Seven questions, five different correct mechanisms. Two are written with
  deliberately misleading nouns: one says *packages* where the content governs a file pattern, one
  says *the lead decides* where the content governs a whole folder.
- **Crash recovery = manifests**, missed twice with two different wrong answers. It appears twice
  here, and the other three context mechanisms — Explore subagent, `/compact`, scratchpad — each
  appear as the correct answer to their own question, so feel will not separate them.
- **The loop reads one value.** `stop_reason` appears twice: once directly, once as `max_tokens`
  arriving mid-run.
- **Invented features**, four of them, in four different questions. Step 2 of the 30-second method
  deletes each on sight.

Scenarios A–D are a pairing not used in Mocks 1–3. Every question is self-contained; the scenario
text is background only.

---

## Scenario A — Structured Data Extraction

*A freight forwarder extracts structured records from shipping paperwork — bills of lading,
customs declarations and carrier invoices — arriving from more than 200 carriers as PDFs and
scans. The output feeds a billing system.*

**1.** Dates arrive as `14/03/26`, `March 14 2026` and `2026-03-14`; amounts as `1.250,00 EUR`,
`$1,250.00` and `1250 usd`. The schema already declares a date type and a decimal amount, and
extractions still return mixed representations. What is the correct fix?

- A. Add a post-processing normalisation layer that rewrites each variant after extraction
- B. Put explicit format normalisation rules in the prompt, alongside the strict schema
- C. Change the date and amount fields to plain strings and reconcile them downstream
- D. Require the carriers to standardise their paperwork before sending it

**2.** Carrier invoices are machine-generated, and every one of them prints the invoice number in a
fixed header block. In about 4% of extractions the `invoice_number` field is absent from the output
entirely. What should the schema do?

- A. Mark `invoice_number` required
- B. Keep it nullable and add a validation rule that rejects null
- C. Make it optional with a default empty string, to be filled in later
- D. Keep it nullable and add a post-processing step that re-reads the header block

**3.** Bills of lading may or may not carry a special-handling clause; most shipments have none.
The field is currently required, and the model produces plausible handling instructions that do not
appear in the document. What should the schema do?

- A. Keep it required and add "leave it blank if absent" to the prompt
- B. Keep it required and reject any value not found verbatim in the source text
- C. Make the field optional and nullable, so absence is representable
- D. Keep it required and add an enum with an `absent` member

**4.** A customs declaration is submitted for a commodity code the destination country prohibits.
The API is healthy, the payload is well-formed, and the caller is authorised. Which error category?

- A. Transient
- B. Validation
- C. Permission
- D. Business

**5.** Two problems. On some invoices the line items do not sum to the stated invoice total, and
nobody notices until billing. And on about 3% of shipments the bill of lading and the customs
declaration state different gross weights, and the pipeline silently keeps whichever it read last.
**(Select two.)**

- A. Extract `calculated_total` alongside `stated_total` so the two can be compared
- B. Add a post-processing arithmetic check that recomputes totals after extraction
- C. Reject any document whose stated total does not match its line items
- D. Add a `conflict_detected` boolean and record both weights with their source documents

**6.** A scanned invoice fails validation on the first attempt — three fields have the wrong
structure. What should the retry request contain?

- A. The schema and the list of specific errors
- B. The document, the failed extraction, and the specific errors
- C. The document and an instruction to be more careful with structure
- D. The same prompt with a higher `max_tokens`

**7.** 40,000 backlogged documents must be reprocessed; no person is waiting on any of them. Which
statement about the Message Batches API is correct?

- A. Same cost as standard requests, but completion within 24 hours is guaranteed
- B. 50% cheaper, with a guaranteed 24-hour completion time
- C. 50% cheaper, up to 24 hours, with no speed guarantee
- D. 50% cheaper, and requires the `--batch` flag

**8.** The team wants to move its multi-step pipeline — extract, call a tariff-lookup tool, then
refine the extraction using the tariff result — into the Batches API. What blocks this?

- A. Multi-turn tool calling is not supported in batch requests
- B. Batch requests cannot use structured output schemas
- C. Batch results cannot be matched back to their inputs
- D. Batch requests are limited to one document each

**9.** After moving to tool use with a strict schema, every output parses cleanly. QA still finds
records where the consignee and the shipper have been swapped. What does this show?

- A. The schema is missing a required field
- B. The retry logic is not firing on those documents
- C. Temperature is set too high for extraction
- D. Schema enforcement removes syntax errors; it does not remove semantic ones

**10.** A single `document_operation` tool takes a `mode` enum with eight values — `extract`,
`validate`, `classify`, `split`, and four more. The model picks the wrong mode in roughly 15% of
calls. What is the fix?

- A. Force this tool with `tool_choice` on every turn
- B. Split it into purpose-specific tools, each with its own input contract
- C. Reduce the enum from eight modes to three broader modes
- D. Move mode selection into the system prompt with examples

**11.** Two problems. Every carrier-portal tool call returns 60-plus fields where five are used,
and the context fills after about a dozen documents. And the agent repeatedly calls a listing tool
to discover which document types and schemas the portal supports. **(Select two.)**

- A. Move to a model with a larger context window
- B. Trim the tool output to the fields actually used, before it enters the context
- C. Expose the portal's document types and schemas as an MCP resource catalogue
- D. Run `/compact` after every twelve documents

**12.** A call to the customs API returns an authentication failure. The pipeline records the
shipment as "0 records found — status: success" and moves on. What is the defect?

- A. An access failure was reported as an empty successful result
- B. The pipeline should have halted the entire run on the failure
- C. Zero matches should be treated as an error rather than a success
- D. The call should have been retried until it eventually succeeded

**13.** Field-level accuracy averages 97% across twelve document types, and one type is quietly
broken. Review currently covers only the extractions the model flagged as low confidence. What do
you add?

- A. Increase the review sample uniformly across all extractions
- B. Review every low-confidence extraction a second time
- C. A stratified random sample of the high-confidence extractions, analysed by document type and
  by field
- D. Raise the confidence threshold until the flagged group is larger

**14.** Requirement: the agent must never file a customs declaration with a declared duty above
€50,000 without a licensed broker's sign-off. Which implementation meets it?

- A. State the rule in the system prompt with a worked example
- B. State the rule in the `file_declaration` tool description
- C. Extract the duty value into a required schema field and check it during review
- D. A `PreToolUse` hook that blocks the call and routes it to broker sign-off

**15.** Three carrier APIs return timestamps in three different shapes, and the model handles each
inconsistently. You want them normalised before the model ever reads them. Which mechanism?

- A. A `PreToolUse` hook that rewrites the outgoing request
- B. A `PostToolUse` hook that normalises the tool result before the model reads it
- C. Format normalisation rules in the prompt
- D. A stricter output schema on the extraction step

---

## Scenario B — Developer Productivity with Claude

*A platform organisation of about 300 engineers is rolling Claude Code out across a monorepo of
fourteen packages and several deployed services.*

**16.** Accessibility conventions apply to every React component file — `**/*.tsx` — and those
files exist in twelve of the fourteen packages. Engineers should see the conventions whenever they
edit one. Where do they belong?

- A. A file in `.claude/rules/` with `paths: "**/*.tsx"`
- B. An `@import` of the accessibility document in each of the twelve packages' CLAUDE.md
- C. A CLAUDE.md in every package that contains component files
- D. A skill the engineer invokes when working on a component

**17.** Two documents need a home. A shared security-review standard, maintained centrally, which
each service's maintainer selects for their own service with no copying. And a quarterly
dependency-upgrade procedure — long, precise, and run four times a year. **(Select two.)**

- A. `@import` the security standard from each service's CLAUDE.md
- B. Put the dependency-upgrade procedure in a skill
- C. Paste the security standard into each service's CLAUDE.md
- D. Put both in `.claude/rules/` files with `paths:` globs

**18.** `services/payments/` has its own testing approach, fixture conventions and review
checklist. They apply to everything inside that folder and to nothing outside it. The payments lead
decides what goes in and keeps it updated. Where does it belong?

- A. `.claude/rules/payments.md` with `paths: "services/payments/**"`
- B. A skill the payments team invokes before working in the service
- C. A CLAUDE.md inside `services/payments/`
- D. An `@import` of a payments document in the root CLAUDE.md

**19.** The commit-message format and the branch-naming scheme apply to every engineer, in every
package, on every task, with no exceptions. Where do they belong?

- A. `.claude/rules/git.md` with `paths: "**/*"`
- B. A skill invoked before committing
- C. `~/.claude/CLAUDE.md` on each engineer's machine
- D. The root CLAUDE.md

**20.** A release skill must ask the developer for a target version when none is supplied, and its
long output should stay out of the main conversation. Which frontmatter keys does it need?

- A. `argument-hint` and `context: fork`
- B. `paths` and `allowed-tools`
- C. `argument-hint` and `paths`
- D. `context: fork` and `paths`

**21.** An engineer keeps personal shortcuts and a preferred commit style that must not reach
teammates. Where do they go?

- A. `.claude/CLAUDE.md`, in a section marked personal
- B. `~/.claude/CLAUDE.md`
- C. A `.claude/rules/` file that is git-ignored
- D. The root CLAUDE.md, under "personal preferences"

**22.** Two problems with the automated review. The "possible race condition" category is a false
alarm about 70% of the time, and engineers have started ignoring review comments altogether. And a
prose instruction describing how to rewrite callback code as async/await produces different results
on different runs. **(Select two.)**

- A. Add "be conservative when unsure" to the review prompt
- B. Run the review three times and keep findings that appear in at least two runs
- C. Turn the race-condition category off until it is fixed, leaving the others on
- D. Replace the prose description with two or three concrete input/output examples

**23.** The team wants one command every engineer can run — `/new-service` — which takes a service
name, and engineers keep forgetting to supply it. What do you build?

- A. A command in `~/.claude/commands/` with the service name hard-coded
- B. A skill in `.claude/skills/` with `allowed-tools` set
- C. A command in `.claude/commands/` with `argument-hint` in its frontmatter
- D. An entry under `commands` in `.claude/config.json`

**24.** A dependency upgrade touches a known list of 22 packages, and each package needs the same
four checks. Which pattern?

- A. Dynamic decomposition — let the agent map the work first
- B. One parallel subagent per package, issued in a single response
- C. One prompt containing all 22 packages and all four checks
- D. Prompt chaining — one pass per package, then one pass across packages

**25.** A "comprehensive audit" of a 900-file legacy monolith for hard-coded credentials. Nobody
knows where configuration is loaded or how many patterns are in use. Which pattern?

- A. Prompt chaining — one pass per file, then one across files, because it is an audit
- B. Dynamic decomposition — map where configuration is loaded, then plan from the map
- C. A single pass with a larger context window
- D. A fixed split by top-level directory, decided up front

**26.** A staff engineer must specify a caching layer in a subsystem they have never worked in.
They are unsure what to specify, and their drafts keep omitting things like invalidation and
failure modes. What helps most?

- A. The interview pattern — have Claude ask questions before any design work
- B. Plan mode, run against the current draft specification
- C. A longer system prompt listing everything a caching design must cover
- D. Two or three few-shot examples of good caching designs

**27.** Two problems. Asked to find code, the agent picks the wrong search tool about a third of
the time. And the agent, whose job is code review, has begun running deployment tools when a
change it reviewed looks urgent. **(Select two.)**

- A. Rewrite the search tool descriptions with inputs, example queries, edge cases, and when to use
  each one instead of the other
- B. Set `tool_choice` to force a specific tool on each turn
- C. Remove the deployment tools from this agent's tool set
- D. Merge the search tools into one tool with a `mode` enum

**28.** An engineer needs to find where the application decides whether a user may export data.
There is no agreed name for it — entitlement, permission, capability, something else — and grepping
the candidate names returns nothing useful. Which tool?

- A. `Glob`, for files whose names contain "export"
- B. `Grep`, with a widened regex covering all four candidate names
- C. `Grep` for "export", then read every match
- D. Semantic search for the concept

**29.** A session from two weeks ago analysed a service. Since then the service has been
restructured, most modules have moved and the API surface has changed. The engineer wants to
continue that work. What should they do?

- A. `--resume` the session and name the files that changed
- B. `--resume` the session and run `/compact` first
- C. Start a fresh session with a written summary of what still holds
- D. `fork_session` from the old session

**30.** A prompt that triages incoming bug reports gets the clear cases right and is inconsistent
on ambiguous ones. Which few-shot approach?

- A. Ten examples spanning the whole range, mostly clear cases
- B. Two to four examples aimed at the unclear cases
- C. One example per category, using the clearest instance of each
- D. As many examples as the context window allows

---

## Scenario C — Multi-Agent Research System

*A regulatory-intelligence platform runs a coordinator over specialised subagents — jurisdiction
search, document analysis, synthesis and briefing writing — and produces cited briefings on
regulatory change.*

**31.** The team is implementing the agentic loop and must fix the continue condition. Which is
correct?

- A. Continue only while `stop_reason` is `"tool_use"`; every other value stops the loop
- B. Continue while `stop_reason` is anything other than `"end_turn"`
- C. Continue while the assistant message contains a `tool_use` block, whatever `stop_reason` says
- D. Continue until the model calls a `research_complete` tool

**32.** One assistant message issues four `tool_use` blocks. Three succeed; the fourth returns a
503 from a gazette API. What must the next user message contain?

- A. Three `tool_result` blocks now, and the fourth after a retry
- B. Four `tool_result` blocks, sent as four separate user messages
- C. One user message with four `tool_result` blocks, each carrying its matching `tool_use_id`, the
  failed one carrying the error
- D. One `tool_result` block summarising all four outcomes

**33.** Two problems. Four jurisdiction-search subagents cover four independent jurisdictions and
the run takes 22 minutes because they execute one after another. And two of them try to hand
findings to each other directly; those findings never reach the briefing. **(Select two.)**

- A. Set `parallel: true` in each AgentDefinition
- B. Issue the four Task calls within a single assistant response
- C. Give the subagents a `shared_memory` channel
- D. Route every message through the coordinator, which passes findings on

**34.** The coordinator's attempts to delegate fail and nothing reaches the subagents. What is the
most likely cause?

- A. `fork_session` has not been enabled on the coordinator
- B. The AgentDefinitions are missing a `parallel` field
- C. `max_tokens` is too low to fit the delegation
- D. The coordinator's `allowedTools` does not include `"Task"`

**35.** A document-analysis subagent re-establishes facts the coordinator had already confirmed,
and ignores a scope constraint the coordinator agreed with the user. Why?

- A. Subagents inherit nothing; everything they need must be in their prompt
- B. The coordinator's `max_tokens` is too low to pass the context along
- C. Subagents inherit the coordinator's context only when `fork_session` is set
- D. The subagents need read access to the coordinator's session file

**36.** A briefing on EU battery regulation omits end-of-life recycling duties entirely. The logs
show the coordinator created three subtasks, and each subagent covered its subtask completely and
correctly. Which component is at fault?

- A. The synthesis agent's system prompt
- B. The briefing writer's output schema
- C. The coordinator's decomposition — the three subtasks did not cover the topic
- D. The jurisdiction-search tool descriptions

**37.** The team wants to compare two synthesis approaches — one chronological, one grouped by
regulator — both starting from the same completed analysis, without repeating the analysis. What do
they use?

- A. Two Task calls in one response, each re-running the analysis
- B. `fork_session` twice from the session that holds the analysis
- C. `--resume` the analysis session twice in sequence
- D. `/compact`, then ask for both approaches in one turn

**38.** The synthesis agent cannot tell whether a cited requirement is current, or whether it came
from a regulator's own text or from a law firm's blog. What fixes this?

- A. Each subagent records publication date, source location and methodology as structured fields
  with every finding
- B. The synthesis agent re-fetches each source at synthesis time
- C. The synthesis agent's prompt instructs it to weigh sources by credibility
- D. A post-processing step annotates each citation with a credibility score

**39.** Two problems. Two of the six jurisdiction databases were unreachable for the whole run, and
the briefing reads as a complete picture of all six. And when one subagent hit a rate limit it
reported upward immediately, and the coordinator halted the entire run. **(Select two.)**

- A. Annotate the output with which findings are well supported and which jurisdictions have gaps
- B. Have the subagent retry the rate-limited call itself, reporting upward only what it cannot
  resolve
- C. Retry the unreachable databases until they respond, before producing any output
- D. Summarise the affected jurisdictions more aggressively so the gaps do not show

**40.** In a long synthesis session, conclusions the coordinator established early are being
contradicted later, and material from the middle of the context is being ignored. What is the fix?

- A. Move to a model with a larger context window
- B. Summarise progressively at each step to keep the context small
- C. Put the established key findings at the beginning of the context, and keep a case-facts block
  outside the summary
- D. Instruct the model to re-read the entire history before each step

**41.** A run takes nine hours across dozens of subagent tasks. The machine restarted at hour
seven, everything was lost, and the run began again from zero. What prevents that?

- A. Run `/compact` at fixed intervals during the run
- B. Have each subagent write its findings to a scratchpad file
- C. Increase the context window so less has to be re-derived
- D. Have subagents write manifests of completed work that the coordinator loads when the run
  resumes

**42.** Before deciding what to analyse, the coordinator must survey which of 400 filings mention a
particular directive. The survey output is large, mostly irrelevant, and it crowds the plan out of
the context. What do you do?

- A. Delegate the survey to an Explore subagent and take back only the shortlist
- B. Run `/compact` immediately after the survey
- C. Write the full survey to a scratchpad file and keep it in the context
- D. Ask for the survey in a separate turn of the same session

**43.** A subagent cannot reach a national gazette, and its retries do not help. What must its
report to the coordinator contain?

- A. That the subtask failed, and nothing further, so the coordinator decides what to do
- B. The failure and a request for fresh credentials
- C. The failure type, what was attempted, any partial results, and possible alternatives
- D. The partial results only, presented as the finding

**44.** The system needs to read filings from a widely used public regulatory database with a
documented, stable API that many organisations already integrate with. What is the right approach?

- A. Build a custom MCP server, so the team controls the contract
- B. Use an existing community MCP server for that integration
- C. Give the agent a general `fetch_url` tool and let it navigate the site
- D. Have engineers export the filings manually into the repository

**45.** Two problems. Two sources give different effective dates for the same rule, and the
briefing prints one of them with no sign the other exists. And the agent that drafts the briefing
also reviews it; reviews come back clean while readers find errors. **(Select two.)**

- A. Run the review three times and keep findings that appear in at least two runs
- B. Instruct the drafting agent to prefer the most recent source
- C. Record both effective dates with their sources and dates, and flag the conflict
- D. Have a separate, independent instance review the briefing

---

## Scenario D — Code Generation with Claude Code

*A team uses Claude Code interactively in the terminal and non-interactively in CI, to generate
tests and to review pull requests.*

**46.** The CI job that invokes Claude Code hangs until the runner times out. The same command
works locally. What fixes it?

- A. Set `CLAUDE_HEADLESS=true` in the job environment
- B. Pass `--no-interactive`
- C. Shorten the prompt so the job finishes inside the timeout
- D. Run it in non-interactive mode with `-p` / `--print`

**47.** The CI step must parse Claude Code's output to decide whether to fail the build, and needs
that output to conform to a fixed shape. What do you use?

- A. A regex over the terminal transcript
- B. `--output-format json` together with `--json-schema`
- C. `--batch` with a schema file
- D. A `.claude/config.json` entry that defines the output shape

**48.** In CI, the generated tests are low value: they restate what the code does, ignore the
team's fixture conventions, and duplicate tests that already exist. What fixes this?

- A. Put the testing standards, fixture conventions and review criteria in CLAUDE.md, and supply
  the module's existing test files
- B. Append the standards to the prompt string in the pipeline script
- C. Raise the temperature so the generated tests vary more
- D. Add a skill the pipeline invokes that lists the standards

**49.** One engineer wants a personal MCP server — a local scratch database — available in their
own sessions, without adding it for the team. Where is it configured?

- A. In the committed `.mcp.json`, disabled by default
- B. In `.claude/rules/` with a `paths` glob
- C. In `~/.claude.json`
- D. In `.mcp.json`, with that file git-ignored

**50.** The team's `.mcp.json` needs an API token for a shared server, and the file is committed to
the repository. What is correct?

- A. Commit the token and rotate it monthly
- B. Keep the token in `~/.claude/CLAUDE.md`
- C. Have each engineer edit `.mcp.json` locally and never commit it
- D. Reference the token as `${VAR}` in `.mcp.json` and set the variable in the environment

**51.** Two problems with the code-generation tools. Failures come back as one generic message, so
callers cannot tell a timeout from a bad path. And when a request is refused because the repository
is frozen for release, the agent retries it eleven times. **(Select two.)**

- A. Return `errorCategory`, `isRetryable` and a readable message with every failure
- B. Retry every failure with exponential backoff, capped at three attempts
- C. Return the freeze refusal as a business error with `isRetryable: false` and a friendly
  explanation
- D. Raise a single exception type and log the details server-side

**52.** The agent's merge request is refused because the repository requires two approvals and only
one exists. The token is valid and the API is healthy. Which category, and is it retriable?

- A. Permission, not retriable
- B. Transient, retriable
- C. Validation, not retriable
- D. Business, not retriable

**53.** The agent must change a block of generated code, but the surrounding text occurs several
times in the file and `Edit` keeps failing on the ambiguous match. What should it do?

- A. Retry `Edit` with a longer surrounding snippet until the match is unique
- B. `Read` the file and `Write` it back with the change applied
- C. `Grep` for the block, then `Edit` by line number
- D. Regenerate the whole module from scratch

**54.** A one-line fix in a single file. Both the cause and the fix are already known. What is the
right approach?

- A. Execute it directly
- B. Plan mode first, then execute
- C. Delegate it to a subagent for isolation
- D. Dynamic decomposition, mapping the file first

**55.** Two requirements for the generation agent. It must never open a pull request touching
`infra/` without an SRE reviewer. And generated code should follow the team's preference for named
exports over default exports. How are they implemented?

- A. Both in the system prompt, with examples
- B. Both enforced by hooks
- C. A hook for the `infra/` rule; the export preference in CLAUDE.md and the prompt
- D. A hook for the export preference; the `infra/` rule in CLAUDE.md

**56.** During a long generation task, one turn returns `stop_reason: "max_tokens"`. What should
the loop do?

- A. Treat it like `"tool_use"` and continue, because the turn is unfinished
- B. Re-send the identical request until it returns `"end_turn"`
- C. Continue, because the value is not `"end_turn"`
- D. Stop the loop — only `"tool_use"` continues it — and handle the truncation

**57.** Two problems in a six-hour session. The agent has begun describing "the typical repository
pattern" instead of the three repository classes it actually read. And each test-runner call
returns a 900-line report of which only the failing test names are used, pushing the plan out of
the context. **(Select two.)**

- A. Switch to a model with a larger context window
- B. Write findings to scratchpad files that the agent re-reads
- C. Run the generation three times and keep what two runs agree on
- D. Trim the test-runner output to the failing test names before it enters the context

**58.** An overnight generation run across 60 modules died at module 41 when the runner was
recycled, and the morning rerun started again at module 1. What should have been in place?

- A. `/compact` at intervals, so less context was at risk
- B. The whole plan in a scratchpad file the agent re-reads each turn
- C. A manifest of completed modules that the coordinator loads on resume
- D. `--resume` on the session, relying on the transcript

**59.** The team requires that no generated change can be committed unless the full test suite
passes — no exceptions, ever. How is that implemented?

- A. A line in CLAUDE.md stating that tests must pass before committing
- B. A prerequisite gate implemented as a hook, blocking the commit until the suite passes
- C. A checklist in the review skill the agent invokes before committing
- D. A required `tests_passed` boolean in the agent's output schema

**60.** The organisation's licence-header and dependency-approval standards must apply to every task
in every repository, automatically, whether or not anyone remembers them. Where do they belong?

- A. The root CLAUDE.md
- B. A skill each engineer invokes at the start of a task
- C. A skill with `context: fork`, so it is cheap enough to always run
- D. `.claude/rules/` with `paths: "**/*"`

---

**Stop the clock. Then open `mock-04-answers.md`.**
