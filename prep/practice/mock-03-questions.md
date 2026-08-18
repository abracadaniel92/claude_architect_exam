# Mock 3 — Full-length exam simulation, gap-targeted (60 questions)

**Take this timed and cold. Budget 75 minutes for the first pass — 75 seconds per question — then
a second pass over flagged questions only. Finishing in 30 minutes is the failure mode, not a
result.**

| | |
|---|---|
| Questions | 60 |
| Time | 120 minutes |
| Format | 4 scenarios × 15 questions, as on the real exam |
| Multiple-response | 10 questions, each marked **(Select two.)** |
| Working pass mark | 43 / 60 (the real exam scales to 720 / 1000) |
| Answer key | `mock-03-answers.md` — with a per-domain score sheet |

Domain spread: D1 16 · D2 11 · D3 12 · D4 12 · D5 9 (the blueprint weighting).

**How this set differs from Mocks 1 and 2.** It is aimed at the five facts that have now been
missed **twice or more**, and each of them appears twice here, in different disguises:

- Domain 3 mechanism selection — `@import` vs `.claude/rules/` vs a directory CLAUDE.md vs the
  root CLAUDE.md vs a skill. Six questions, five different correct mechanisms.
- Parallel subagents = several Task calls in **one response**. Once as a single answer, once as
  half of a select-two.
- Coverage annotations, and the stratified sample of the **high-confidence** group.
- Required vs nullable, both directions, in the same paper.
- Step 6 — the component that held the information when it was lost, not the place the failure
  appeared.

Two scenarios use a different pair from Mock 2, so the dressing is unfamiliar. Every question is
still self-contained; the scenario text is background only.

---

## Scenario A — Multi-Agent Research System

*A coordinator gives work to specialised subagents — web search, document analysis, synthesis and
report generation. The system produces detailed reports with citations.*

**1.** A team is implementing the agentic loop and must decide the exit condition. Which is
correct?

- A. Continue while `stop_reason` is `"tool_use"`; that value alone drives the loop
- B. Continue whenever `stop_reason` is anything other than `"end_turn"`
- C. Exit when the assistant message contains a text block and no `tool_use` block
- D. Exit when the model calls a `task_complete` tool

**2.** One assistant message contains three `tool_use` blocks. Two tools succeed; the third fails
permanently with an authentication error. What must the next user message contain?

- A. Two `tool_result` blocks, plus a text note explaining that the third tool failed
- B. Three `tool_result` blocks, sent as three separate user messages
- C. Three `tool_result` blocks in one user message, each carrying its matching `tool_use_id`, the
  failed one carrying the error
- D. Two `tool_result` blocks now, and the third on the following turn

**3.** Three document-analysis subagents cover three independent subtopics. They currently run one
after another and the total run takes 18 minutes. What makes them run concurrently?

- A. Set `parallel: true` in each AgentDefinition
- B. Issue the three Task tool calls within a single assistant response
- C. Raise `max_tokens` so all three fit inside one turn
- D. Enable `fork_session` on the coordinator

**4.** A report on renewable energy financing omits tax-credit structures entirely. The
coordinator's logs show it split the topic into three subtasks, and each subagent covered its
assigned subtask completely and correctly. Which component is at fault?

- A. The synthesis agent's system prompt
- B. The web-search subagent's tool descriptions
- C. The report generator's output schema
- D. The coordinator's decomposition of the topic

**5.** Two problems with the research system. Every subagent begins by re-searching facts the
coordinator already established earlier in the run. And subagents working on related subtopics
attempt to hand findings to each other directly, and those findings do not appear in the final
report. **(Select two.)**

- A. Include the facts already established in each subagent's prompt
- B. Add a `shared_memory: true` flag to the AgentDefinitions
- C. Enable direct subagent-to-subagent messaging for related subtopics
- D. Route every message through the coordinator, which is the only component that sees all results

**6.** An analyst has one completed literature review in a session and now wants two competing
report structures developed from that same review, so they can be compared side by side.

- A. Two Task tool calls in a single response
- B. `fork_session`
- C. Two fresh sessions, pasting a summary of the review into each
- D. `--resume` twice under different session names

**7.** The synthesis agent cannot tell whether a market-size figure came from a 2019 vendor white
paper or a 2026 peer-reviewed study, and treats old and new numbers as a contradiction.

- A. Each search subagent records publication date, source location and methodology alongside every
  finding
- B. The synthesis agent re-fetches each source at synthesis time to establish its provenance
- C. The synthesis agent is instructed to weigh sources by credibility
- D. A review step after synthesis annotates the report with source quality

**8.** Two of the six sources were unreachable for the whole run. The delivered report reads as
though the topic was covered completely.

- A. Retry the unreachable sources until they respond, before releasing the report
- B. Omit the affected subtopics from the report
- C. Mark in the report which findings are well supported and which subtopics have gaps because
  sources were unavailable
- D. Record the outage in the pipeline run log

**9.** The synthesis agent needs to check individual claims frequently, and currently invokes the
full web-search subagent for each check, which is slow and returns far more than it needs.

- A. Give the synthesis agent the full search toolset
- B. Give the synthesis agent one small `verify_fact` tool
- C. Force `tool_choice` to the search subagent for verification turns
- D. Have the coordinator verify every claim before synthesis begins

**10.** Before reading anything, the document-analysis subagent makes a long series of exploratory
calls to discover which documents exist and how they are organised.

- A. Cache the results of the exploratory calls between runs
- B. Add a `list_all_documents` tool that returns every document
- C. Expose the documentation structure as an MCP resource, so the catalogue is available without
  exploratory calls
- D. Describe the documentation layout in the coordinator's system prompt

**11.** A regulatory question must be answered from a corpus of 900 filings. Nobody knows which
filings mention the obligation, how many do, or where in each filing it appears; what each step
finds determines where to look next.

- A. Prompt chaining: one pass per filing, then one pass across filings
- B. A single pass covering the whole corpus, for consistency
- C. One subagent per filing, with the results concatenated
- D. Dynamic decomposition: map the corpus first, then a plan that adapts as findings arrive

**12.** An engineer proposes replacing the loop's `stop_reason` check with a hard cap of 25
iterations, arguing that a cap is more predictable in production. What is the correct response?

- A. Correct — a fixed cap is the recommended primary termination mechanism
- B. Correct, provided the cap is tuned for each workload
- C. Incorrect — a cap is acceptable only as a safety limit; `stop_reason` must drive the loop
- D. Incorrect — no cap is needed, because `end_turn` always arrives eventually

**13.** Two sources give different figures for the same market: one published in 2021, one in 2026.

- A. Record both figures, each with its source and publication date
- B. Keep the more recent figure and discard the older one
- C. Average the two and report the range
- D. Ask the coordinator to decide which source is more credible

**14.** Two problems with a long research pipeline. It crashed at hour three and four hours of work
was lost. And the final synthesis agent has almost no context space left by the time it runs.
**(Select two.)**

- A. Each agent writes its state to a known location, and the coordinator loads the manifest when
  work resumes
- B. Run `/compact` at fixed intervals throughout the run
- C. Give the synthesis agent a model with a larger context window
- D. Have the earlier agents return structured findings — key facts, citations, relevance scores —
  instead of long prose

**15.** A user asks a one-line factual question that a single search answers. The coordinator
invokes all five subagents and the reply takes 40 seconds.

- A. Run the five subagents in parallel to cut the total latency
- B. Merge the five subagents into one general-purpose agent
- C. Cache answers so repeated questions are faster
- D. Have the coordinator choose which subagents to invoke based on the complexity of the request

---

## Scenario B — Code Generation with Claude Code

*A team uses Claude Code for writing code, refactoring, debugging and documentation across a
monorepo, with custom commands, project configuration and plan mode.*

**16.** A `/review-pr` command must be available to every engineer who clones the repository.

- A. `~/.claude/commands/review-pr.md`
- B. `.claude/commands/review-pr.md`
- C. `.claude/skills/review-pr/SKILL.md`
- D. `.claude/rules/review-pr.md`

**17.** One engineer has personal preferences about commit-message wording and verbosity that
nobody else should receive.

- A. `~/.claude/CLAUDE.md`
- B. `CLAUDE.md` in the repository root
- C. `.claude/CLAUDE.md`
- D. `.claude/rules/commit-style.md`

**18.** The team has conventions for test files. Test files sit beside the code they cover, so they
appear in every package, and the conventions apply to nothing else.

- A. A CLAUDE.md inside each package
- B. `@import` in the root CLAUDE.md
- C. A `.claude/rules/` file with `paths: ["**/*.test.ts"]`
- D. A skill that engineers invoke when writing tests

**19.** The `packages/checkout/` package has its own state-management and error-handling
conventions. They apply to every file inside that package and to nothing outside it.

- A. A `.claude/rules/` file with `paths: ["**/*.tsx"]`
- B. A CLAUDE.md inside `packages/checkout/`
- C. A "Checkout" section in the root CLAUDE.md
- D. A skill that engineers invoke when working in checkout

**20.** There are six shared standards documents. The security document must apply to every
package. Each package's maintainer decides which of the other five apply to their package. No text
may be duplicated anywhere.

- A. Six `.claude/rules/` files, each with `paths` globs listing the packages it covers
- B. Copy the applicable documents into each package's CLAUDE.md
- C. The security document in the root CLAUDE.md, and each package's CLAUDE.md using `@import` for
  the others it needs
- D. Six skills, invoked by engineers as they become relevant

**21.** A `/deploy` skill must never be able to run destructive shell commands. Which frontmatter
key handles this?

- A. `allowed-tools`
- B. `paths`
- C. `context: fork`
- D. `argument-hint`

**22.** A dependency-audit skill produces very long output, and running it fills the main
conversation with material nobody needs afterwards.

- A. `allowed-tools`
- B. `argument-hint`
- C. `paths`
- D. `context: fork`

**23.** A `/scaffold` skill needs a component name, and engineers keep invoking it without one.

- A. `paths`
- B. `argument-hint`
- C. `allowed-tools`
- D. `context: fork`

**24.** An engineer wants Claude Code's output in a form a script can parse. Which of these is a
real capability?

- A. `--batch`
- B. `.claude/config.json` with a `commands` list
- C. `--output-format json`
- D. `--no-interactive`

**25.** The team must move a shared authentication module out of the monolith and into its own
package, changing call sites in roughly forty files across six packages.

- A. Direct execution, switching to plan mode if it turns out to be complex
- B. Plan mode
- C. An Explore subagent, then direct execution
- D. A skill holding the restructuring steps

**26.** An engineer must find which of about 400 configuration files set a particular feature flag.
The search will produce a large amount of output that is of no use once the answer is found.

- A. Run `Grep` in the main session and `/compact` afterwards
- B. `fork_session` before searching, then discard the branch
- C. Move to a model with a larger context window
- D. Dispatch an Explore subagent, so the discovery output stays out of the main context

**27.** Two problems in a long session. Three hours in, the agent starts describing "typical
patterns" for the framework instead of the specific classes it found earlier in the session. And
each MCP call returns more than forty fields when five are used, so the context fills quickly.
**(Select two.)**

- A. Write the key findings to scratchpad files as the session proceeds
- B. Move to a model with a larger context window
- C. Trim the tool output to the fields actually used, before it enters the context
- D. Summarise the conversation every thirty minutes

**28.** An engineer returns to a session after two days. Three files named in the earlier analysis
have changed; the rest of the analysis still holds.

- A. `--resume`, naming the three changed files so they are re-read
- B. Start a fresh session with a written summary of what still holds
- C. `fork_session` from the old session
- D. `/compact`, then continue in the same session

**29.** A prose instruction describing how to convert legacy configuration objects into the new
format produces a different result on each run.

- A. Build a skill holding the conversion rules
- B. Rewrite the prose description in more detail
- C. Give two or three concrete input/output examples of the conversion
- D. Force `tool_choice` on a formatting tool

**30.** An engineer must design an event-sourcing scheme for a domain they have never worked in,
and does not know what to specify.

- A. Use plan mode with the specification they have
- B. Ask for three candidate designs and pick one
- C. Generate an implementation, then review it critically
- D. Have Claude ask them questions first, so it raises the considerations they have not thought of

---

## Scenario C — Claude Code in Continuous Integration

*Claude Code runs inside a CI/CD pipeline performing automated review, test generation and pull
request feedback. Feedback must be trustworthy, with few false alarms.*

**31.** The CI job never finishes; it sits until the runner's timeout kills it.

- A. `-p` / `--print`
- B. `CLAUDE_HEADLESS=true` in the job environment
- C. The `--no-interactive` flag
- D. `--output-format json`

**32.** The reviewer's instruction is "report anything that looks wrong", and it flags formatting
preferences and naming opinions as defects.

- A. Instruct the reviewer to report only high-confidence findings
- B. Suppress findings the model scores below 80% confidence
- C. Train a classifier on the findings developers have dismissed
- D. Replace the instruction with explicit criteria stating what counts as a defect

**33.** The same session that generates a module also reviews it, and it approves its own design
decisions every time.

- A. Instruct the session to be critical of its own code
- B. Run the review in a separate instance that has no knowledge of writing the code
- C. Enable extended thinking for the review step
- D. Run the review twice and keep only findings that appear both times

**34.** Two complaints about the reviewer. Its "style" category produces so many false alarms that
developers have started ignoring the other categories too. And severity labels are applied
inconsistently between runs, so the same defect is *high* one day and *low* the next.
**(Select two.)**

- A. Raise the global confidence threshold so fewer findings are reported
- B. Disable the style category while its criteria are rewritten, leaving the others running
- C. Ask developers to mark the findings they consider irrelevant
- D. Define each severity level with concrete code examples

**35.** A pre-merge check must run on every pull request, and the merge is blocked until it returns.

- A. The real-time API, because a developer is waiting on the result
- B. The Message Batches API, because it is 50% cheaper
- C. The Message Batches API, submitted at merge time with a webhook on completion
- D. The Message Batches API, with the pipeline polling until results appear

**36.** Nightly test generation is submitted to the Message Batches API, which may take up to 24
hours. The team has committed to delivering generated tests within 30 hours of a merge. What
submission cadence meets that?

- A. Every 12 hours
- B. Every 24 hours
- C. Every 4 hours
- D. Every 30 hours

**37.** Extracted supplier contracts sometimes state a renewal clause and sometimes do not. When
the clause is absent, the extraction produces a plausible-looking one.

- A. Make the field required, so it is never omitted
- B. Constrain the field to an enum of the common clause types
- C. Add a post-processing check against the contract text
- D. Make the field optional and nullable

**38.** Build reports are machine-generated and always contain a commit SHA. In 2% of extractions
the `commit_sha` field is absent from the output, and those records are rejected downstream.

- A. Keep the field nullable and add a validation rule rejecting nulls
- B. Make the field required in the schema
- C. Fill the missing value from the CI job metadata afterwards
- D. Add a few-shot example showing the SHA being extracted

**39.** On a 14-file pull request the reviewer's depth varies by file — thorough on the first few,
shallow by the end — and it flags a pattern as a defect in one file while approving the same
pattern in another. **(Select two.)**

- A. Move to a model with a larger context window
- B. Review each file in its own focused pass
- C. Add one further pass across all the files, to catch contradictions between them and data flow
  that crosses file boundaries
- D. Run three passes and report only findings that appear in at least two

**40.** A batch of 2,000 review jobs completes with 5% failures. Some failed because the diff
exceeded the length limit; the rest failed validation on a field the prompt handles poorly.

- A. Resubmit the whole batch once the prompt has been revised
- B. Send the failures through the real-time API, to get them back sooner
- C. Resubmit the failures unchanged, since batch failures are usually transient
- D. Resubmit only the failed items, identified by `custom_id`, splitting the over-long diffs first

**41.** The reviewer handles clear defects consistently, but treats borderline cases — a nullable
value dereferenced after an early return, for instance — differently on each run.

- A. Add two to four examples covering the borderline cases
- B. Add twenty examples, one for each borderline pattern seen last quarter
- C. Instruct the reviewer to take more care with borderline cases
- D. Raise the confidence threshold for borderline findings

**42.** Two failures in one pipeline run. The linter MCP server was unreachable, and the job
reported "review complete" with zero findings. Later in the same run a second tool errored and the
pipeline aborted before the remaining checks ran. **(Select two.)**

- A. Return an empty findings list marked successful, so the pipeline is not disrupted
- B. Return structured error context: the failure type, what was attempted, any partial results, and
  alternative approaches
- C. Continue with the remaining checks and mark the areas that were not covered
- D. Abort the pipeline whenever any tool errors, so no failure is ever missed

**43.** The pipeline's credential does not carry the scope needed to post review comments, and the
call is rejected. How should the tool classify this?

- A. Transient — retry with backoff
- B. Validation — correct the request, then retry
- C. Permission — not retryable; escalate to whoever can grant the scope
- D. Business — not retryable; explain the rule

**44.** The linter MCP server returns 503 while that service is being redeployed. How should the
tool classify this?

- A. Permission — not retryable; escalate
- B. Transient — retryable once the service recovers
- C. Validation — correct the input, then retry
- D. Business — not retryable; explain the rule

**45.** The reviewer's findings are 96% precise overall, and the team proposes stopping human
review of the findings it reports with high confidence. **(Select two.)**

- A. Analyse precision separately by finding category and by file type
- B. Take a stratified random sample of the high-confidence findings, since that is the group review
  would stop covering
- C. Increase the review sample uniformly across all findings
- D. Use the reviewer's own confidence scores to decide which findings still need review

---

## Scenario D — Customer Support Resolution Agent

*An agent built with the Claude Agent SDK handles returns, billing disputes and account problems,
using MCP tools for customer lookup, orders, refunds and escalation.*

**46.** An `account_action` tool takes a `mode` enum with seven values: `freeze`, `unfreeze`,
`close`, `reopen`, `merge`, `transfer`, `relabel`. The agent frequently picks the wrong mode.

- A. Reduce the seven modes to three broader ones
- B. Add a table to the system prompt mapping customer intents to modes
- C. Force `tool_choice` to `account_action` so the model commits to the tool
- D. Split it into purpose-specific tools, each with its own input and output contract

**47.** The agent must always call one of the three lookup tools before answering a question about
an order, choosing the right one itself, instead of answering from what it remembers of the
conversation.

- A. `tool_choice: {"type": "auto"}`
- B. `tool_choice: {"type": "any"}`
- C. `tool_choice: {"type": "tool", "name": "lookup_order"}`
- D. `tool_choice: {"type": "none"}`

**48.** The agent confuses `get_customer` and `lookup_order`. Both descriptions are a single short
line.

- A. Expand both descriptions: inputs, example queries, edge cases, and when to use each instead of
  the other
- B. Force `tool_choice` per request type
- C. Merge them into one `lookup` tool with a `type` parameter
- D. Add a routing layer that inspects the customer's message before every turn

**49.** One engineer runs an experimental MCP server that nobody else on the team should receive.

- A. `.mcp.json`, committed, with the server disabled by default
- B. `.claude/rules/mcp.md`
- C. A `.mcp.json` kept out of version control through `.gitignore`
- D. `~/.claude.json`

**50.** The shared support MCP server needs an API token, and the token must not appear in version
control.

- A. Commit the token in `.mcp.json` and rotate it monthly
- B. Store the token in the root CLAUDE.md
- C. Reference it as `${SUPPORT_API_TOKEN}` in `.mcp.json`, so the file can be committed safely
- D. Have each engineer paste the token at the start of every session

**51.** The team needs the agent to work with Zendesk, a standard integration with a maintained
community MCP server, and also with their own internal returns workflow, which is unique to them.

- A. Use the community server for the standard integration, and build custom only for the team's own
  workflow
- B. Build custom servers for both, for full control of the tool contracts
- C. Wrap the vendor's REST API in `Bash` calls
- D. Expose the vendor API as an MCP resource rather than as tools

**52.** A refund request is well formed and the service is healthy, but the amount exceeds the
per-order limit written in the refund policy. How should the tool classify this?

- A. Transient — retry later, when limits reset
- B. Validation — correct the amount, then retry
- C. Permission — the agent's credential does not allow refunds of this size
- D. Business — not retryable; explain the policy to the customer

**53.** Two requirements for the agent. Refunds above $500 must never be issued without supervisor
approval. And three backend services return dates in three different formats, so the agent quotes
wrong delivery windows. **(Select two.)**

- A. A system prompt section stating the $500 rule and describing each service's date format
- B. A `PreToolUse` hook that intercepts `process_refund` calls above $500 and redirects them to
  approval
- C. A nightly reconciliation job that reverses refunds issued above the limit
- D. A `PostToolUse` hook that normalises the three services' responses into one date format before
  the model reads them

**54.** The agent's tone varies between replies — formal with some customers, casual with others.
No money, identity or policy decision is involved.

- A. A `PreToolUse` hook that inspects outgoing messages before they are sent
- B. A rewriting service that corrects replies that do not match the house style
- C. System prompt guidance on the intended tone, with two to four examples
- D. A forced `tool_choice` on a `format_reply` tool for every reply

**55.** `process_refund` must never run before `verify_identity` has returned for that caller.

- A. A prerequisite gate that blocks `process_refund` until `verify_identity` has returned
- B. A system prompt rule requiring verification first
- C. Few-shot examples showing verification before every refund
- D. A daily audit that reverses refunds issued without verification

**56.** A dispute case produces a billing analysis that is internally consistent but useless. The
coordinator's logs show it passed only the customer ID to the billing subagent, omitting the
dispute history the customer had described. The billing subagent's output was correct for the input
it received.

- A. The billing subagent's system prompt defines its scope too narrowly
- B. The coordinator did not include the required context in the subagent's prompt
- C. The billing subagent lacks access to the dispute-history tool
- D. The synthesis step dropped the dispute history when combining results

**57.** Halfway through an investigation the customer says they want to speak to a person. The case
is solvable and the agent is close to an answer.

- A. Complete the investigation, then escalate with the findings attached
- B. Continue, since the case is solvable and escalation is unnecessary
- C. Escalate only if the customer asks a second time
- D. Escalate immediately, without finishing the investigation

**58.** Two problems with escalation. Human agents receive cases with no usable context and have to
start again. And when the policy handbook is silent on a request, the agent decides the matter
itself. **(Select two.)**

- A. Attach the full transcript and the raw tool output to every escalation
- B. Escalate whenever the customer's language turns strongly negative
- C. Include a structured handoff summary: customer ID, root cause, amount involved, recommended
  action
- D. Escalate when the request falls outside what the policy covers, instead of deciding it

**59.** A coordinator is configured to dispatch three investigation subagents, but every dispatch
fails silently and the coordinator answers directly instead.

- A. The subagents' `allowedTools` lists are empty
- B. The coordinator's `allowedTools` does not include `"Task"`
- C. `fork_session` has not been enabled for the coordinator
- D. The subagent definitions are missing a `parallel` field

**60.** Two problems with the coordinator. Replies take 45 seconds because the three independent
checks — order status, payment history, shipping — run one after another. And on cases that need
only one of the three, all three still run. **(Select two.)**

- A. Issue the Task calls for the independent checks within a single assistant response
- B. Set `parallel: true` on the three AgentDefinitions
- C. Have the coordinator select which checks to invoke based on what the case requires
- D. Merge the three checks into one general-purpose subagent

---

*End of Mock 3. Record your finish time, then mark against `mock-03-answers.md`.*
