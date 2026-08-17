# Mock 2 — Full-length exam simulation, reverse-direction (60 questions)

**Take this timed and cold. At least 75 minutes — if you finish sooner you are pattern-matching,
not reasoning.**

| | |
|---|---|
| Questions | 60 |
| Time | 120 minutes |
| Format | 4 scenarios × 15 questions, as on the real exam |
| Multiple-response | 10 questions, each marked **(Select two.)** |
| Working pass mark | 43 / 60 (the real exam scales to 720 / 1000) |
| Answer key | `mock-02-answers.md` — with a per-domain score sheet |

Domain spread: D1 16 · D2 11 · D3 12 · D4 12 · D5 9.

**How this set differs from Mock 1.** It is built against the failure mode Mock 1 exposed:
answering on recognition. Nearly every question offers a **defensible late fix**, a **plausible
feature that does not exist**, or a **rule you know, running in the opposite direction** to the
version you last saw. Reading quickly will not get you through it.

The scenario text is background only — every question is self-contained.

---

## Scenario A — Developer Productivity

*An agent helps engineers explore unfamiliar codebases, trace legacy behaviour and automate
repetitive work, using the built-in tools and MCP servers.*

**1.** An engineer must find the code that decides whether a user's session is renewed. They do not
know what it is called; `refreshSession`, `renewToken` and `extendAuth` all return no matches.

- A. `Glob` for `**/*session*`
- B. `Grep` for `renew`
- C. Semantic search for the concept of session renewal
- D. `Read` every file under the auth directory in turn

**2.** An engineer must find every call site of `deprecatedFetch(` before removing it.

- A. `Grep` for the exact string `deprecatedFetch(`
- B. `Glob` for `**/*.ts`
- C. Semantic search for "the old fetch helper"
- D. `Read` each file in the network module

**3.** `Edit` fails on a change because the target block appears identically in seven places in the
file. What should be done?

- A. Insert a unique comment above the target block first, then run `Edit`
- B. Use `Bash` with `sed` to apply the change by line number
- C. `Grep` for the block, then retry `Edit` with the line number as context
- D. `Read` the file and `Write` it back with the change applied

**4.** The team wants a Jira MCP server available to everyone who clones the repository,
authenticated with a token that must not appear in version control. One engineer also runs an
experimental server nobody else should get. **(Select two.)**

- A. Declare the Jira server in `.mcp.json`, committed to the repository
- B. Declare the Jira server in `~/.claude.json` and have each engineer add it themselves
- C. Reference the token as `${JIRA_TOKEN}` so the file can be committed safely
- D. Commit the token in `.mcp.json` and rotate it monthly

**5.** A `manage_repository` tool takes a `mode` enum with six values: `branch`, `merge`, `tag`,
`revert`, `archive`, `restore`. The agent frequently selects the wrong mode.

- A. Reduce the enum from six modes to three broader ones
- B. Split it into purpose-specific tools, each with its own input and output contract
- C. Add a table to the system prompt mapping intents to modes
- D. Force `tool_choice` to `manage_repository` so the model commits to the tool

**6.** An engineer asks the agent to explain how a payment webhook is processed in a codebase it has
not seen. What is the correct exploration strategy?

- A. `Read` every file in `src/` to build a complete picture first
- B. `Glob` for all files, then `Read` them in alphabetical order
- C. Ask the engineer for an architecture diagram before starting
- D. `Grep` to locate entry points, then `Read` to follow imports, repeating as the trace deepens

**7.** The `services/billing/` package has error handling and logging conventions that apply to
every file inside it and to nothing outside it. Where should they live?

- A. A "Billing" section in the root CLAUDE.md
- B. A CLAUDE.md inside `services/billing/`
- C. A `.claude/rules/` file with `paths: ["**/*.ts"]`
- D. A skill that engineers invoke when working on billing

**8.** The monorepo has four standards documents. The security document must apply to every package.
The other three apply only where each package's maintainer says so. No text may be duplicated
anywhere.

- A. Four `.claude/rules/` files, each with `paths` globs listing the packages it applies to
- B. Four skills, invoked by engineers as relevant
- C. The security document in the root CLAUDE.md, plus a per-package CLAUDE.md using `@import` to
  reference the others it needs
- D. Copy the applicable documents into each package's CLAUDE.md

**9.** A deployment skill needs a target environment, and engineers frequently invoke it without
one. Which frontmatter key handles this?

- A. `argument-hint`
- B. `allowed-tools`
- C. `context: fork`
- D. `paths`

**10.** Three hours into a session, the context is dominated by exploration output. The engineer
wants to keep working in the same session with the findings so far intact.

- A. `/memory`
- B. `--resume`
- C. `fork_session`
- D. `/compact`

**11.** An engineer has completed a detailed analysis of a service and now wants to develop two
competing refactoring approaches from that same analysis, and compare them.

- A. Two Task tool calls in a single response
- B. `fork_session`
- C. Run `--resume` twice against the same session name
- D. Two fresh sessions, pasting the analysis summary into each

**12.** An engineer returns to a session after three weeks. The service has since been
re-architected: most files have moved, several modules were deleted, and the earlier analysis is
largely obsolete.

- A. Start a new session and provide a written structured summary of what still holds
- B. Resume with `--resume`, naming the files that changed
- C. Resume with `--resume` and ask the agent to re-read the whole service
- D. `fork_session` from the old session to keep the earlier reasoning available

**13.** A subagent is dispatched with the instruction "continue the analysis from where we left off"
and returns output unrelated to the work so far.

- A. The subagent's `allowedTools` is missing `Read`
- B. Subagent sessions expire after one hour of inactivity
- C. Subagents receive none of the coordinator's history, so the required context must be in the
  prompt
- D. The subagent's context window is too small for the accumulated analysis

**14.** A long-running multi-agent job crashes after four hours, and the work is lost. What should
be added?

- A. Run `/compact` more frequently to reduce the chance of failure
- B. Increase the timeout on each agent
- C. A scratchpad file per engineer holding their session notes
- D. Each agent writes its state to a known location, and the coordinator loads the manifest when
  work resumes

**15.** Two problems appear at the end of a long research pipeline: the final agent has little
context space left by the time it runs, and readers cannot tell which of its conclusions rest on
solid evidence. **(Select two.)**

- A. Give the final agent a larger context window
- B. Change the earlier agents to return structured data — key facts, citations, relevance scores —
  instead of long prose and reasoning
- C. Summarise the final output more aggressively before delivery
- D. Annotate the synthesis with which findings are well supported and which topics have gaps

---

## Scenario B — Claude Code in Continuous Integration

*Claude Code runs inside a CI/CD pipeline performing automated review, test generation and pull
request feedback. Feedback must be trustworthy, with few false alarms.*

**16.** The CI job never completes; it sits until the runner's timeout.

- A. Run with `-p` / `--print`
- B. Add the `--no-interactive` flag
- C. Redirect stdin from `/dev/null`
- D. Set `CLAUDE_HEADLESS=true` in the job environment

**17.** Which of the following is a real Claude Code capability?

- A. `--batch`
- B. `CLAUDE_HEADLESS=true`
- C. `--json-schema`
- D. `.claude/config.json` with a `commands` list

**18.** The automated reviewer suggests tests that ignore the team's fixture conventions and
re-test scenarios already covered by the existing suite.

- A. Append the conventions to the prompt inside the CI script on every run
- B. Record the testing standards, fixture conventions and review criteria in CLAUDE.md, and supply
  the existing test files
- C. Create a skill holding the conventions and have the pipeline invoke it
- D. Post-process the output to drop suggestions that duplicate existing tests

**19.** The same session that generated a module also reviews it, and consistently approves its own
design decisions.

- A. Instruct the session to be critical of its own work
- B. Enable extended thinking for the review step
- C. Run the review three times and report only findings that appear in at least two runs
- D. Run the review in a separate instance with no memory of writing the code

**20.** A production bug has a clear stack trace pointing at one function in one file; the fix is a
missing null check.

- A. Direct execution
- B. Plan mode, because every production change should be planned
- C. Direct execution, switching to plan mode if complexity appears
- D. An Explore subagent first, to confirm the stack trace

**21.** An engineer must design a caching layer in a domain they do not know well, and is unsure
what to specify.

- A. Ask for three candidate designs and pick one
- B. Use plan mode with the specification they have
- C. Let Claude interview them first, so it raises considerations such as invalidation and failure
  modes
- D. Generate an implementation, then review it critically

**22.** A service has three defects: a race condition on startup, a retry policy that amplifies it,
and a log line that masks it. Each one affects the others.

- A. Three separate messages, one defect at a time
- B. One detailed message covering all three, because they interact
- C. Fix the log line first so the others become visible
- D. A separate session per defect, to keep each context focused

**23.** A skill used by the pipeline must be prevented from running destructive shell commands.

- A. `context: fork`
- B. A `PreToolUse` entry in the skill's frontmatter
- C. `paths`
- D. `allowed-tools`

**24.** The reviewer's instruction is "check that comments are accurate", and it produces many false
positives on comments that are merely terse.

- A. Replace it with an explicit rule: flag a comment only when the behaviour it describes
  contradicts what the code does
- B. Instruct it to be conservative and report only high-confidence findings
- C. Train a classifier on the comments developers have dismissed
- D. Report only findings above a confidence threshold

**25.** Two complaints about the reviewer: the "possible performance issue" category produces so
many false alarms that developers have started ignoring all categories, and severity labels are
applied inconsistently between runs. **(Select two.)**

- A. Raise the global confidence threshold to reduce total findings
- B. Disable the performance category while its prompt is improved, keeping the others running
- C. Ask developers to filter the findings they consider irrelevant
- D. Define each severity level with concrete code examples

**26.** In a verification pass, the team wants reviewers to know which findings deserve attention
first.

- A. Suppress findings the model reports below 80% confidence
- B. Report a confidence level next to each finding, so reviewers can triage
- C. Route low-confidence findings out of the report entirely
- D. Use the confidence score to decide when the pipeline may merge without review

**27.** On a 14-file pull request the reviewer's depth varies by file, and it flags a pattern as a
defect in one file while approving the same pattern in another. **(Select two.)**

- A. Run one review pass per file
- B. Move to a model with a larger context window
- C. Run three passes and report only findings that appear in at least two
- D. Run one additional pass across files, to catch data-flow issues and contradictions between
  files

**28.** The team wants to learn which kinds of finding developers routinely dismiss.

- A. Survey the developers monthly
- B. Log the full text of every finding and cluster it later
- C. Add a `detected_pattern` field to each finding, recording which code pattern triggered it
- D. Attach a confidence score to each finding and compare it against dismissals

**29.** A CI script sends only the newest message on each turn. The agent loses track of what it
established earlier in the run.

- A. Enable session persistence on the API request
- B. Increase `max_tokens` so more can be carried per response
- C. Use `--resume` between pipeline stages
- D. Send the full conversation history with every request, because the API holds no state

**30.** A linter MCP tool is unreachable during a run. The job reports "review complete" with zero
findings. Later in the same run a second tool fails, and the pipeline aborts entirely.
**(Select two.)**

- A. Return structured error context: the failure type, what was attempted, any partial results,
  and alternative approaches
- B. Continue with the remaining checks and mark the unchecked areas as not covered
- C. Return an empty findings list marked successful, so the pipeline is not disrupted
- D. Fail the whole pipeline whenever any tool errors, so failures are never missed

---

## Scenario C — Customer Support Resolution Agent

*An agent handles returns, billing disputes and account problems, with MCP tools for customer
lookup, orders, refunds and escalation.*

**31.** Three backend services return timestamps differently: one Unix epoch, one ISO 8601, one a
numeric status code with an implied date. The agent misreads dates and quotes wrong delivery
windows.

- A. A `PreToolUse` hook that rejects calls to services returning non-standard formats
- B. A `PostToolUse` hook that normalises every response into one format before the model sees it
- C. System prompt guidance explaining how to interpret each service's format
- D. A post-processing step that corrects dates after the conversation ends

**32.** The agent's tone is inconsistent: formal with some customers, casual with others. No policy,
money or identity decision is involved.

- A. A `PreToolUse` hook that inspects outgoing messages before they are sent
- B. A validation service that rewrites replies not matching the house style
- C. A forced `tool_choice` on a `format_reply` tool for every response
- D. System prompt guidance on the intended tone, with two to four examples

**33.** Accounts with a pending refund must never have their delivery address changed before the
caller's identity is verified.

- A. A prerequisite gate blocking `update_address` until identity verification has returned
- B. A system prompt rule stating the requirement
- C. Few-shot examples showing verification preceding every address change
- D. A nightly audit that reverses address changes made without verification

**34.** Investigation subagents run one after another, and each one begins by re-establishing case
details the coordinator already holds. **(Select two.)**

- A. Increase `max_tokens` so each subagent can carry more
- B. Issue the Task tool calls within a single assistant response
- C. Include the case facts already gathered in each subagent's prompt
- D. Enable a shared memory flag across the AgentDefinitions

**35.** Which statement about a maximum iteration count in the agentic loop is correct?

- A. It is the correct primary mechanism for terminating the loop
- B. It should replace `stop_reason` checks, which are unreliable in production
- C. It is unnecessary, because `end_turn` always arrives eventually
- D. It is acceptable as a safety limit, but `stop_reason` must drive the loop

**36.** A customer asks a simple balance question. The coordinator invokes all five subagents, and
the reply takes 40 seconds.

- A. The coordinator should select which subagents to invoke based on the complexity of the request
- B. The five subagents should run in parallel to reduce total latency
- C. The five subagents should be merged into one general agent
- D. Responses should be cached so repeated balance questions are faster

**37.** A dispute case produces a correct-looking but useless billing analysis. Coordinator logs
show it passed only the order ID to the billing subagent, omitting the dispute history the customer
had described. The billing subagent's output was correct for the input it received.

- A. The billing subagent's system prompt defines its scope too narrowly
- B. The billing subagent needs access to the dispute lookup tool
- C. The coordinator did not pass the required context in the subagent's prompt
- D. The synthesis step discarded the dispute history when combining results

**38.** Two problems with escalation: human agents receive cases with no usable context, and
customers who ask for a person at the start are escalated only after a full investigation.
**(Select two.)**

- A. Attach the raw untrimmed tool output and the full transcript to every escalation
- B. Escalate whenever message sentiment turns strongly negative
- C. Include a structured summary: customer ID, root cause, amount, recommended action
- D. Escalate immediately when the customer explicitly asks for a human, without completing the
  investigation

**39.** `get_customer` is rejected because the agent's credential lacks the required scope. How
should the tool classify this?

- A. Permission — not retryable; escalate or explain
- B. Transient — retryable once the service recovers
- C. Validation — retryable after the input is corrected
- D. Business — not retryable; explain the policy to the customer

**40.** A subagent hits a network timeout, which succeeds on its own second attempt, and separately
hits an authentication failure it cannot resolve. What should it report to the coordinator?

- A. Both failures, so the coordinator has full visibility
- B. Neither failure; return whatever results it obtained
- C. Only the authentication failure, with what it tried and any partial results
- D. Neither; halt and escalate both to a human

**41.** Which statement about `tool_choice: {"type": "auto"}` is correct?

- A. The model must call exactly one tool per turn
- B. The model may reply with text instead of calling a tool
- C. The model must call the first tool declared in the array
- D. Tool use is disabled for that request

**42.** `analyze_content` and `analyze_document` are still confused after both descriptions were
expanded, because they genuinely overlap: both accept arbitrary text and return arbitrary analysis.

- A. Force `tool_choice` to the correct tool based on the request type
- B. Remove one of the two tools
- C. Add few-shot examples demonstrating the choice between them
- D. Rename and rewrite them so the boundary is explicit, splitting the general one into
  purpose-specific tools

**43.** A customer asks the company to match a competitor's advertised price. The price-match policy
covers only prices on the company's own site, and says nothing about competitors.

- A. Decline, since the policy does not authorise it
- B. Approve, since refusing risks losing the customer
- C. Escalate, because the policy does not cover this case
- D. Ask the customer to submit a written price-match request

**44.** A customer is angry and uses strong language about a duplicate charge. The charge is
straightforward and the agent can refund it immediately.

- A. Acknowledge the frustration, offer to resolve it now, and escalate only if the customer asks
  for a person
- B. Escalate now, because the sentiment score is strongly negative
- C. Escalate, because emotionally charged cases have lower resolution rates
- D. Proceed with the refund without acknowledging the customer's frustration

**45.** An incident report must combine refund figures by month, a narrative summary of the outage,
and technical root-cause findings.

- A. Convert all three into prose, for a consistent reading experience
- B. Tables for the financial data, prose for the narrative, structured lists for the technical
  findings
- C. A single JSON object, so downstream systems can consume it
- D. Bullet points throughout, for scannability

---

## Scenario D — Structured Data Extraction

*A logistics company extracts structured records from dispatch notes, supplier contracts and
remittance advice, validates them against JSON schemas, and submits them to an ERP system.*

**46.** Dispatch notes are machine-generated and always carry a consignment number. In 3% of
extractions the `consignment_number` field is absent from the output, and those records are
rejected.

- A. Keep the field nullable and add a validation rule rejecting nulls
- B. Add a post-processing step that fills the field from the shipping manifest
- C. Add a few-shot example showing the consignment number being extracted
- D. Make the field required in the schema

**47.** Some dispatch notes state quantities informally — "a couple of pallets", "half a container".
Handling of these is inconsistent between runs.

- A. Tighten the schema type on the quantity field
- B. Add two to four few-shot examples aimed at the ambiguous phrasings
- C. Add twenty examples, one for each phrasing observed in the last quarter
- D. Reject documents that do not state quantities numerically

**48.** A regulatory rule states that records above €10,000 must never be auto-approved for ERP
submission.

- A. Few-shot examples demonstrating the threshold being respected
- B. A prominent instruction in the system prompt stating the limit
- C. A programmatic gate that blocks auto-approval above €10,000
- D. A confidence threshold, below which records are held for review

**49.** An engineer argues that moving to tool use with a JSON schema will eliminate extraction
errors. What is the correct response?

- A. It removes syntax errors only; the content can still be wrong, such as a value placed in the
  wrong field
- B. It removes both syntax and semantic errors, which is why it is preferred
- C. It removes semantic errors, but malformed JSON is still possible
- D. It removes neither; schemas are advisory

**50.** A batch of 5,000 documents completes with 4% failures. Some failed because the documents
exceeded the length limit; the rest failed validation on a field the prompt handles poorly.
**(Select two.)**

- A. Resubmit the entire batch once the prompt has been revised
- B. Resubmit only the failures, identified by `custom_id`, splitting the over-long documents first
- C. Test the revised prompt on a small sample before resubmitting
- D. Send the failures through the real-time API instead, to get them back sooner

**51.** Documents arrive throughout the day and are processed in batches. Batch processing may take
up to 24 hours, and the team has committed to a 36-hour SLA from arrival to ERP delivery. What
cadence meets it?

- A. Submit every 8 hours
- B. Submit every 36 hours, matching the commitment
- C. Submit every 18 hours
- D. Submit every 24 hours

**52.** Supplier contracts sometimes name a governing-law jurisdiction and sometimes do not. When
absent, the model produces a plausible one.

- A. Make the field required, so it is never omitted
- B. Add a post-processing check against a list of valid jurisdictions
- C. Constrain the field to an enum of the twelve most common jurisdictions
- D. Make the field optional and nullable

**53.** A review is needed over a known list of 30 modified files, against a fixed set of review
criteria.

- A. Dynamic decomposition, mapping the structure before deciding the steps
- B. A single pass covering all 30 files together, for consistency
- C. Prompt chaining: one pass per file, then one pass across files
- D. One subagent per file, with results concatenated

**54.** Two requirements for the pipeline: three upstream services return dates in different
formats, and records above the approval threshold must never reach the ERP automatically.
**(Select two.)**

- A. A `PostToolUse` hook that normalises the service responses into one format
- B. A system prompt section describing each service's date format
- C. A validation layer after submission that reverses records above the threshold
- D. A tool call interception hook that blocks submission above the threshold

**55.** A single agent asked to review 60 extracted records in one pass produces inconsistent
judgements, better at the start than at the end.

- A. Move to a model with a larger context window
- B. Split it into focused passes covering fewer records each, plus one pass across the full set
- C. Increase `max_tokens` so the output is not truncated
- D. Ask for a summary of the records first, then review the summary

**56.** The pipeline handles invoices, contracts and remittances. The coordinator routes everything
to the invoice subagent, which was built first, and contract-specific fields are missing from the
output. Each subagent extracts correctly from what it receives.

- A. The coordinator's routing and task decomposition
- B. The contract subagent's system prompt
- C. The contract schema's field definitions
- D. The extraction model's handling of long documents

**57.** A response contains two `tool_use` blocks. The second tool raised an error, so the
implementation returns a result for the first only.

- A. Correct — a failed tool has no result to return
- B. Incorrect — the second result should be sent on the following turn
- C. Incorrect — a text note explaining the failure should be sent instead
- D. Incorrect — every `tool_use` needs a matching `tool_result` with the same `tool_use_id`,
  failures included, all in one user message

**58.** The ERP rejects a submission because a date field is malformed. How should the tool classify
this?

- A. Transient — retry the identical call
- B. Business — not retryable; explain the rule
- C. Validation — correct the input, then retry
- D. Permission — escalate to someone with submission rights

**59.** Overall accuracy is 98.5%, and the team proposes reducing human review. **(Select two.)**

- A. Analyse accuracy separately by document type and by field
- B. Increase the review sample uniformly across all extractions
- C. Take a stratified random sample of the high-confidence group, since that is the group review
  would stop covering
- D. Use the model's confidence scores to select which extractions to check

**60.** Two source systems were unreachable during a run. The output report reads as complete.

- A. Retry the unreachable systems until they respond, before releasing the report
- B. Mark which findings are well supported and which topics have gaps because sources were
  unavailable
- C. Omit the affected topics from the report entirely
- D. Note the outage in the pipeline run log

---

*End of Mock 2. Record your finish time, then mark against `mock-02-answers.md`.*
