# Mock 5 — Full-length exam simulation, untested-facts paper (60 questions)

**Take this timed and cold. Write down the time you start and the time you finish the first pass,
*before* you open the key.** That number is the one measurement still missing after four mocks
(weak point 45). Budget 75 minutes for the first pass — 75 seconds per question — then a second
pass over flagged questions only.

| | |
|---|---|
| Questions | 60 |
| Time | 120 minutes |
| Format | 4 scenarios × 15 questions, as on the real exam |
| Multiple-response | 10 questions, each marked **(Select two.)** |
| Working pass mark | 43 / 60 (the real exam scales to 720 / 1000) |
| Answer key | `mock-05-answers.md` — with a per-domain score sheet |

Domain spread: D1 16 · D2 11 · D3 12 · D4 12 · D5 9 (the blueprint weighting).

**How this set differs from Mocks 1–4.** Mock 4 was built from the repeat-miss list and cleared it
(58/60). This paper is built from the opposite list — the facts **no repo paper has ever tested**,
which is where the remaining risk sits:

- **The thirteen untested facts** (log, *What is still untested*), each appearing at least once:
  all four `tool_choice` values, both escalation directions, `/compact` as a *correct answer*
  rather than a distractor, severity consistency, plain-text JSON → tool use, batch resubmission
  by `custom_id`, re-review duplicate findings, goal-oriented vs rigid subagent prompts, personal
  command placement, `allowed-tools`, `--resume` in the **positive** direction, multi-issue single
  messages, and the handoff package contents.
- **The two live Domain 2 misses.** Semantic search appears with the words printed in the question
  and no string to search for (6th appearance, missed 5 times). Business-vs-permission appears as
  two adjacent questions — a policy limit with a healthy API and an authorised caller, and a token
  whose scope is too narrow — so the four-category test has to run twice in a row.
- **Three-member sets, deliberately incomplete.** Several questions offer two members of a triad
  and hide the third among the distractors. Name the third before choosing (weak point 44).
- **Repair verbs** appear as distractors in seven questions and as the correct answer in none.
  The halt is what is being tested, not the rejection.
- **Invented features**, four of them: `parallel: true`, `CLAUDE_HEADLESS=true`, `--no-interactive`,
  and a `.claude/config.json` with a `commands` list. Step 2 of the 30-second method deletes each
  on sight.

Scenarios A–D are a pairing not used in Mocks 1–4. Every question is self-contained; the scenario
text is background only.

---

## Scenario A — Claude Code in Continuous Integration

*A payments company runs Claude Code inside its CI pipeline. On every pull request it reviews the
diff, generates missing unit tests, and writes a machine-readable summary that a pipeline gate
reads. The monorepo holds twelve services and three shared packages.*

**1.** The pipeline step hangs until the job timeout kills it, and when it is forced through, the
next step cannot read the result. Which two changes fix this? **(Select two.)**

- A. Run Claude Code with `-p` (`--print`) so it does not wait for interactive input
- B. Set `CLAUDE_HEADLESS=true` in the workflow environment
- C. Add `--output-format json` so the following step can parse the result
- D. Pass `--no-interactive` and scrape the console text with a regular expression

**2.** The gate needs the summary to carry the same fields every time — file, line, severity,
suggested fix — so it can fail the build on any critical finding. What guarantees that shape?

- A. `--output-format json` on its own
- B. A `schema:` key in the workflow file, listing the required fields
- C. `--json-schema`, with the schema the gate expects
- D. Ask for the fields in the prompt, then validate the output with a shell script afterwards

**3.** The generated tests are low value — getters, framework internals — and they ignore the team's
fixture conventions. What fixes this properly?

- A. Append the testing standards to the prompt string inside the pipeline script
- B. Write the testing standards, fixture conventions and review criteria in CLAUDE.md
- C. Add a `.claude/rules/` file with `paths: "**/*.ts"` describing the standards
- D. Reduce the number of tests requested per run, so only the obvious ones are produced

**4.** It also suggests tests for scenarios the suite already covers. What stops that?

- A. Add "do not duplicate existing tests" to the prompt
- B. Run the suite first and pass the coverage percentage into the prompt
- C. Ask for fewer tests and have a reviewer delete the duplicates
- D. Give it the existing test files for the module

**5.** The review runs again on every new commit, and it re-posts comments the developer has already
read. What is the correct fix?

- A. Include the earlier findings in the context and ask for only new or still-unfixed issues
- B. Run the review only on the first commit of a pull request
- C. Post-process the comments and drop any that match a comment posted earlier
- D. Narrow the review to the files touched by the most recent commit

**6.** One engineer wants a shortcut command for their own debugging workflow. It must not appear for
the rest of the team. Where does it go?

- A. `.claude/commands/`, with their name in the filename
- B. `~/.claude/commands/`
- C. `.claude/skills/`, restricted with `allowed-tools`
- D. `.claude/config.json`, under a `commands` list

**7.** A shared command needs a service name to work on. Developers keep invoking it without one and
it fails. Which frontmatter key addresses this?

- A. `paths`
- B. `context: fork`
- C. `argument-hint`
- D. `allowed-tools`

**8.** A skill that analyses database migrations must never delete or move files, whatever the
conversation asks it to do. What enforces that?

- A. `allowed-tools` in the SKILL.md frontmatter, listing only the tools the skill needs
- B. A line at the top of the skill body: "never delete or move files"
- C. `context: fork`, so its actions stay out of the main conversation
- D. `paths:` frontmatter restricting the skill to the migrations folder

**9.** A skill that maps the whole codebase produces thousands of lines and leaves no room for the
work that follows it. Which key fixes that?

- A. `/compact` immediately after each run of the skill
- B. An instruction in the skill to summarise its findings in under 50 lines
- C. Move the skill to `~/.claude/skills/` so it loads for one developer only
- D. `context: fork`

**10.** Storybook story files exist in eleven of the twelve services. The conventions for writing
them apply to any file matching `**/*.stories.tsx`, wherever it lives. Where do they belong?

- A. `@import` a shared stories document into each of the eleven service CLAUDE.md files
- B. A `.claude/rules/` file with `paths: "**/*.stories.tsx"`
- C. The root CLAUDE.md, since story files exist nearly everywhere
- D. A skill the developer invokes when starting a new story file

**11.** Six shared compliance documents exist. Each service's maintainer picks the two or three that
apply to their service; once picked, they must govern all work in that service, and nothing may be
copied. Which mechanism?

- A. A skill per document, invoked when the developer judges it relevant
- B. `.claude/rules/` with a `paths:` glob per service folder
- C. `@import` of the chosen documents in each service's CLAUDE.md
- D. Paste the chosen documents into each service's CLAUDE.md

**12.** The billing service has its own error-handling and logging conventions. They apply to
everything under `services/billing/` and to nothing outside it. Which mechanism?

- A. A CLAUDE.md inside `services/billing/`
- B. `.claude/rules/` with `paths: "services/billing/**"`
- C. `@import` of a billing conventions document into the root CLAUDE.md
- D. A skill named `billing-conventions`, invoked when working in that service

**13.** A release branch changes 30 files. The list is known before the work starts and the review
criteria are fixed. Which approach?

- A. Dynamic decomposition — map the branch first, then plan from what the map shows
- B. One subagent per service, each deciding for itself what to review
- C. A single pass over the whole diff, with the largest available context window
- D. Prompt chaining — one pass per file, then one pass across files

**14.** Findings come back labelled critical, major or minor, and the same class of bug is labelled
differently between runs. What makes the labelling consistent?

- A. Ask the model to report a confidence score next to each severity label
- B. Define each severity level in the prompt with concrete code examples
- C. Run the review three times and take the majority severity
- D. Reduce the scheme to two levels, blocking and non-blocking

**15.** The "possible race condition" category is wrong about 70% of the time. Developers now ignore
the SQL-injection findings too, which are accurate. What is the correct action?

- A. Turn off the race-condition category, keep the others running, improve its prompt, then turn it
  back on
- B. Add "be conservative and only report what you are confident about" to the review prompt
- C. Report only findings the model marks as high confidence
- D. Keep every category, but downgrade race-condition findings to the lowest severity

---

## Scenario B — Structured Data Extraction

*An insurance group extracts structured records from claim documents — medical reports, repair
estimates and police reports — arriving as PDFs and scans from thousands of sources. About 40,000
documents are processed overnight, plus a small queue where an assessor is waiting.*

**16.** The prompt asks for the record "as JSON" in the response text. About 6% of responses fail to
parse — trailing commas, unescaped quotes, a sentence before the opening brace. What is the reliable
fix?

- A. Add "return only valid JSON" to the prompt, with three examples of well-formed JSON
- B. Parse leniently and repair the malformed JSON downstream
- C. Declare the schema as a tool input schema and have the model return the record through tool use
- D. Lower the temperature and retry any response that fails to parse

**17.** After that change every output validates against the schema. In about 3% of records the line
items still do not add up to the stated total. What should be done?

- A. Mark the total field required, so the model cannot omit it
- B. Add a step after extraction that recomputes the total and overwrites the extracted value
- C. Nothing — a record that validates against a strict schema cannot contain an invalid total
- D. Add a `calculated_total` field next to `stated_total`, because tool use with a schema removes
  syntax errors and not semantic ones

**18.** Repair estimates from the approved garage network are machine-generated, and every one of
them prints the estimate reference in a fixed header block. In about 4% of extractions the reference
field is absent from the output. What should the schema do?

- A. Mark the field required
- B. Keep it nullable and add a validation rule that rejects null
- C. Make it optional with a default of an empty string, to be filled in later
- D. Keep it nullable and add a step that re-reads the header block when it is missing

**19.** Police reports sometimes contain a witness statement section and most do not. The field is
currently required, and the model produces plausible statements that do not appear in the report.
What should the schema do?

- A. Keep the field required and add "leave it blank if there is no statement" to the prompt
- B. Make the field optional and nullable, so absence can be represented
- C. Keep it required, with an enum whose members include `none`
- D. Keep it required and reject any value that is not present verbatim in the source

**20.** Dates arrive as `03/04/26` and `4 March 2026`; amounts as `1.250,00` and `$1,250.00`. The
schema already declares a date type and a decimal amount, and extractions still return mixed
representations. What is the correct fix?

- A. Change both fields to plain strings and reconcile the variants downstream
- B. Add explicit format normalisation rules to the prompt, alongside the strict schema
- C. Build a normalisation layer after extraction, with a branch per known variant
- D. Route each source to its own source-specific extraction tool

**21.** Documents arrive unsorted. Three schemas exist — medical, repair, police — and the type is
not known until the document is read. Which `tool_choice` setting fits?

- A. `auto`
- B. `none`
- C. `any`
- D. `{"type": "tool", "name": "extract_medical"}`

**22.** `extract_metadata` must run before the enrichment step. With the current setting the model
sometimes replies in prose instead of calling it. What is the correct change?

- A. Keep `auto` and retry the turn whenever the response is text
- B. Set `any`, so the model must call one of the available tools
- C. Add "always extract metadata first" to the system prompt
- D. Set `{"type": "tool", "name": "extract_metadata"}` for that turn, then continue in later turns

**23.** A retry request carries the document, the failed extraction and the specific errors. Which
failure is that retry likely to fix?

- A. Two date fields were returned in the wrong structure
- B. The policy number is not printed anywhere in the document
- C. The appendix holding the value was never supplied to the model
- D. The scan is too degraded for the text to be read at all

**24.** The overnight batch of 40,000 requests completes and 900 of them failed. What is the correct
next step?

- A. Resubmit the whole batch, so the results stay consistent
- B. Move the 900 to the real-time API and accept the higher cost
- C. Resubmit only the failed requests, identified by their `custom_id`
- D. Resubmit the batch with a longer processing window so the failures have more time

**25.** The team adds few-shot examples to the extraction prompt. Which two rules apply?
**(Select two.)**

- A. Use ten to fifteen examples, so every document layout is represented
- B. Use two to four examples
- C. Choose the clearest and most typical documents as the examples
- D. Aim the examples at the unclear cases

**26.** A claim is submitted 30 days after the incident. The policy allows 14 days. The API is
healthy, the payload is well-formed and the caller is authorised. Which error category?

- A. Transient
- B. Validation
- C. Permission
- D. Business

**27.** The extraction service calls the claims API with a token that carries read scope only. The
write call is rejected. Which error category?

- A. Permission
- B. Business
- C. Validation
- D. Transient

**28.** The team is designing the error object every tool returns. Which two things must every error
carry? **(Select two.)**

- A. An `errorCategory` naming one of transient, validation, business or permission
- B. An `isRetryable` flag, plus a message a person can read
- C. The stack trace of the failing call
- D. A single generic message, so internal details never leak to the caller

**29.** Average extraction accuracy is 97%. Assessors report that one document type is wrong far more
often than that suggests. Which two steps find the problem? **(Select two.)**

- A. Increase the sample size uniformly across all extractions
- B. Review everything the model flagged as low confidence
- C. Analyse accuracy by document type and by field, instead of as one average
- D. Take a stratified random sample of the high-confidence extractions

**30.** A summary report is assembled from five reference sources. Two were unavailable for the whole
run, and the report reads as though every topic was checked. What must the output do?

- A. Retry the two sources until they respond, and delay the report
- B. Annotate which findings are well supported and which topics have gaps
- C. Leave out the topics that could not be checked, so nothing unsupported is stated
- D. Mark the run successful and return an empty result for the missing topics

---

## Scenario C — Customer Support Resolution Agent

*A retailer runs a Claude-based support agent over its order, refund and shipping tools. The agent
may refund up to $500; above that a human must approve. The policy documents cover the retailer's
own site only.*

**31.** Halfway through a diagnosis the customer writes: "stop, I want to talk to a person." What is
the correct behaviour?

- A. Escalate immediately, without finishing the diagnosis
- B. Finish the diagnosis first, so the human receives a complete picture, then escalate
- C. Ask whether they would like the agent to try one more option before handing over
- D. Escalate only if the customer asks a second time

**32.** A customer is angry about a delivery that is four days late. The agent can see the parcel in
the carrier's system and can reship today. What is the correct behaviour?

- A. Escalate, because the sentiment score for the conversation is high
- B. Escalate, because complaints of this kind usually end with a human anyway
- C. Acknowledge the frustration, offer to reship today, and escalate only if the customer asks for a
  human
- D. Offer a refund above the agent's limit, to close the case quickly

**33.** A customer asks the retailer to match a competitor's lower price. The price-match policy
covers price drops on the retailer's own site and says nothing about other retailers. What is the
correct behaviour?

- A. Refuse, because the policy does not permit it
- B. Apply the closest policy rule by analogy and grant the difference
- C. Suggest the customer buys from the competitor instead
- D. Escalate, because the policy does not cover this request

**34.** Which two signals must never be used to decide that a conversation should be escalated?
**(Select two.)**

- A. A sentiment score computed from the customer's messages
- B. The customer asking for a human
- C. The agent being unable to make progress on the case
- D. The model's own uncalibrated confidence score

**35.** A case is handed to a human agent who cannot see the conversation. Which two things must the
handoff summary contain? **(Select two.)**

- A. The full message transcript, unedited
- B. The verified customer ID and the root cause the agent identified
- C. The refund amount and the recommended action
- D. The model's confidence that its diagnosis is correct

**36.** One message contains three problems: a refund that never arrived, a wrong delivery address on
the next order, and a promotion code that was rejected. Which two describe correct handling?
**(Select two.)**

- A. Split the message into separate items and investigate them in parallel over shared context
- B. Return one combined answer that covers all three
- C. Ask the customer which of the three to deal with first
- D. Handle them one at a time in separate turns, closing each before opening the next

**37.** Refunds above $500 must never be issued by the agent, in any conversation. What guarantees
that?

- A. A system-prompt rule with few-shot examples of refusing over-limit refunds
- B. A `PreToolUse` hook that blocks the refund call when the amount exceeds $500 and redirects to
  escalation
- C. A `PostToolUse` hook that reverses any refund over $500 after the call has been made
- D. A sentence in the refund tool's description stating the $500 limit

**38.** `process_refund` is sometimes called before the customer's identity has been verified. What
prevents it?

- A. A prerequisite gate that blocks `process_refund` until `get_customer` has returned a verified
  customer ID
- B. "Always verify identity before refunding" in the system prompt
- C. `tool_choice` forced to `get_customer` on every turn
- D. Reordering the tool definitions so `get_customer` is listed first

**39.** The shipping API returns a 503 while a subagent is checking a parcel. Which two are correct?
**(Select two.)**

- A. Categorise it as a business error and stop the workflow
- B. Return an empty shipping result and mark the call successful
- C. Categorise it as transient, with `isRetryable: true`
- D. Let the subagent retry it itself, and report upward only what it cannot fix

**40.** A single `manage_ticket` tool takes a `mode` parameter with the values `create`, `update`,
`close`, `merge` and `escalate`. The model frequently picks the wrong mode. What is the fix?

- A. Reduce the parameter to two modes, `create` and `update`
- B. Document each mode more thoroughly inside the one tool description
- C. Split it into purpose-specific tools, each with its own contract
- D. Force `tool_choice` to `manage_ticket` and validate the mode after the call

**41.** The agent calls `search_orders` when the customer has given an exact order ID and `get_order`
is the right tool. Both tools work correctly and their schemas are valid. What should be tried
first?

- A. Force `tool_choice` to `get_order` whenever the message contains an order ID
- B. Remove `search_orders` from the agent's tools
- C. Add a routing classifier in front of the agent
- D. Improve both tool descriptions — inputs, example queries, and when to use each one instead of
  the other

**42.** The agent makes many exploratory calls at the start of a conversation to discover which
ticket categories and refund reason codes exist. What removes those calls?

- A. A tool that lists the categories, called at the start of every conversation
- B. Expose the category and reason-code catalogues as MCP resources
- C. Put the full category list in the system prompt
- D. Cache the results of the exploratory calls between conversations

**43.** The team needs a standard Zendesk integration, and also a server for their own internal
refund-approval workflow. What is correct?

- A. Use a community MCP server for Zendesk and build a custom server for the internal workflow
- B. Build both in-house, so the two behave consistently
- C. Use community servers for both and extend the second one
- D. Put both in `~/.claude.json`, so neither is shared through version control

**44.** Mid-task, a response comes back with `stop_reason: "max_tokens"`. What should the loop do?

- A. Continue, because `stop_reason` is not `end_turn`
- B. Continue, because the task is plainly unfinished
- C. Stop — the loop continues only on `tool_use`
- D. Continue, after asking the model to summarise what it produced so far

**45.** One response contains three `tool_use` blocks. How are the results returned?

- A. Three separate user messages, one per result, in the order the tools were called
- B. One user message containing a text summary of all three results
- C. One user message containing a single `tool_result` block that lists all three outputs
- D. One user message containing three `tool_result` blocks, each carrying the matching `tool_use_id`

---

## Scenario D — Multi-Agent Research System

*A consultancy runs a multi-agent research system. A coordinator plans the work; subagents search the
web, read regulatory filings and read the client's internal documents; a synthesis agent writes the
final report.*

**46.** Six sources are currently searched one after another and the run takes too long. How are the
searches run at the same time?

- A. Set `parallel: true` in the AgentDefinition
- B. Issue several Task calls in a single response
- C. Start six sessions with `fork_session`
- D. Raise the concurrency limit in `.claude/config.json`

**47.** The coordinator cannot start any subagent, although its own tools work normally. What is the
most likely cause?

- A. Its `allowedTools` does not include `"Task"`
- B. The subagent definitions are missing the `parallel` key
- C. The subagents are not registered in `.mcp.json`
- D. The coordinator is running with `--print`

**48.** Subagents return work that ignores the client's stated constraints, and two of them ask the
same source the same question. Which two statements are true? **(Select two.)**

- A. Subagents inherit the coordinator's conversation, so the constraints are already available to
  them
- B. Subagents receive nothing automatically — everything they need goes into the Task prompt
- C. Subagents cannot talk to each other; every message goes through the coordinator
- D. A shared memory file gives each subagent the others' findings automatically

**49.** Subagent prompts list the exact steps to follow. When a source is unavailable the subagent
stops instead of finding another route. What is the fix?

- A. Add error-handling steps for each source to the same prompts
- B. Let subagents call one another when a source fails
- C. Write prompts that state goals and quality standards instead of step-by-step instructions
- D. Have the coordinator reissue the task with a longer list of steps

**50.** The team wants to compare three analytical framings of the same collected evidence, without
collecting it again. Which mechanism?

- A. Three Task calls in one response, each collecting the evidence again
- B. `--resume` three times from the same session name
- C. `/compact`, then three follow-up prompts in the same session
- D. `fork_session`, branching three times from the shared analysis

**51.** A session mapped 40 regulatory filings yesterday. Overnight, two named filings were
re-issued; nothing else changed. What is the best way to continue?

- A. Start a fresh session with a written summary of yesterday's findings
- B. `--resume` the session and name the two filings that changed
- C. `/compact` the session and carry on
- D. Start fresh, because any stale content invalidates the earlier analysis

**52.** A new engagement begins. Nobody knows which of the client's 900 internal documents matter, or
how the repository is organised. Which approach?

- A. Dynamic decomposition — map the repository first, then plan the work from what the map shows
- B. Prompt chaining — one pass per document, then one pass across documents
- C. One subagent per document type, with the types decided now
- D. A single pass with the largest available context window

**53.** Every subagent finished successfully and reported no errors, yet the final report omits an
entire regulatory topic. What is the most likely cause?

- A. The subagents summarised their findings too aggressively
- B. The synthesis agent dropped the topic while writing
- C. The coordinator divided the work too narrowly
- D. The sources were unavailable and the failure was reported as success

**54.** The team needs every place the pricing logic lives. There is no agreed name for it — people
call it the rate engine, the tariff module and the pricing core — and searching for each of those
names returns nothing useful. Which capability fits?

- A. `Grep` for "pricing" and read every match
- B. `Glob` for `**/*pricing*` across the repository
- C. `Grep` for each candidate name in turn, widening the pattern until something matches
- D. Semantic search, because there is no literal string to search for

**55.** They also need the list of every file whose path matches `**/reports/*.tsx`. Which capability
fits?

- A. `Glob`
- B. `Grep`
- C. Semantic search
- D. An MCP resource that lists the repository tree

**56.** The synthesis agent cannot tell a 2021 vendor blog post from a 2026 peer-reviewed study, so it
weights them equally. Which two changes fix this? **(Select two.)**

- A. Subagents record the publication or collection date with every finding
- B. The synthesis agent re-fetches each source at synthesis time to check it
- C. The synthesis agent is instructed to weigh sources by credibility
- D. Subagents record the source location and the methodology behind every finding

**57.** The coordinator crashed after four of nine subagents had finished. When the run resumes, their
work must not be repeated. Which mechanism?

- A. `/compact` at intervals during the run
- B. Scratchpad files holding each subagent's findings
- C. A manifest of completed work, which the coordinator loads when it resumes
- D. `--resume` with the session name

**58.** A single long session has nothing stale in it and nothing has crashed, but the context is
nearly full and every remaining step still needs the findings already in the session. What is the
simplest correct action?

- A. Start a fresh session with a written summary of the findings so far
- B. `/compact`, to reduce the context of the live session
- C. Write a manifest and resume the work tomorrow
- D. Move the remaining work to subagents so the context stops growing

**59.** Finding the relevant documents means reading hundreds of them, and that output would fill the
coordinator's context before the analysis begins. Which mechanism?

- A. `/compact` after every batch of reads
- B. `fork_session` for the discovery work
- C. Progressive summarisation of each document as it is read
- D. An Explore subagent, so the noisy discovery stays out of the main context

**60.** `Edit` keeps failing on a configuration block whose exact text the agent cannot match. What is
the correct fallback?

- A. Retry `Edit` with a shorter match string
- B. `Grep` for the block, then call `Edit` again with the matched line
- C. `Read` the file and `Write` it back with the change applied
- D. Delete the file and recreate it from scratch
