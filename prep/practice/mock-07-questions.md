# Mock 7 — All-six-scenarios exam (72 questions)

**Take this timed and cold.** This paper does what the real exam never does: it runs **all six**
scenarios instead of the 4-of-6 the exam draws at random, so every scenario domain-mix gets tested
in one sitting. That pushes the count to 72, past the real exam's 60 — deliberately, per your
request. Because all six are in play (Domain 5 sits inside four of them), the domain split below is
not blueprint-weighted the way Mocks 1–6 were; read it as a coverage paper, not a scaled mock.

| | |
|---|---|
| Questions | 72 |
| Suggested time | 144 minutes (2 min/question, matching exam pace) |
| Format | 6 scenarios × 12 questions |
| Multiple-response | 9 questions, each marked **(Select two.)** |
| Answer key | `mock-07-answers.md` — with a per-domain and per-scenario score sheet |

Domain spread: D1 13 · D2 11 · D3 14 · D4 18 · D5 16.

**What this paper is built to catch, on top of ordinary content:**

- **Domain 3 runs as one nine-question block (Q13–Q21)**, all five grouping mechanisms —
  `@import`, `.claude/rules/`, a directory CLAUDE.md, the root CLAUDE.md, a skill — live in the same
  scenario. Say the sentence before each one: *what set of files does this content govern?*
- **Coverage annotations and partial-results-vs-false-success each appear twice**, in two different
  scenarios (Q35/Q70 and Q36/Q71), each time with a distractor not used in any earlier mock. Three
  repo papers in a row have lost this pair to a "new-looking" wrong answer rather than an
  old one — see if a fourth distractor still gets it.
- **Select-two appears in five of the six scenarios**, nine in total. Say how many letters you owe
  before reading the options.
- **A few questions run in the inverse direction** — watch for *never*, *must never*, *do not
  exist* in the last sentence, and answer the direction actually asked.
- Every question is self-contained. The scenario paragraph is background only.

---

## Scenario A — Meridian Play (Customer Support Resolution Agent)

*Meridian Play, a video-streaming service, runs a Claude-based support agent over four MCP tools:
`get_subscriber`, `lookup_invoice`, `issue_credit`, and `escalate_to_agent`. The agent may issue
account credit up to $250 on its own; anything above that needs a human. The team wants 80%+
first-contact resolution.*

**1.** Mid-diagnosis, a model response comes back with `stop_reason: "refusal"`. What should the
orchestration loop do?

- A. Continue, since `stop_reason` is not `end_turn`
- B. Continue, and ask the model to rephrase the same request
- C. Stop — the loop continues only on `stop_reason: "tool_use"`
- D. Continue, treating `refusal` the same as `max_tokens`

**2.** In one turn the model calls `get_subscriber` and `lookup_invoice`. The next request to the API
is rejected as malformed. What does a correct implementation send back?

- A. Two separate user messages, one per tool result, in call order
- B. One assistant message containing both results
- C. One user message with a single `tool_result` block listing both outputs
- D. One user message containing two `tool_result` blocks, each with its matching `tool_use_id`

**3.** Two rules must hold without exception: no credit above $250 may be issued by the agent, and a
subscriber's identity must be confirmed by `get_subscriber` before `issue_credit` is ever called.
Which two changes guarantee this? **(Select two.)**

- A. A `PreToolUse` hook that blocks `issue_credit` when the amount exceeds $250 and routes the case
  to escalation
- B. A system-prompt rule stating both limits, reinforced with few-shot examples
- C. A prerequisite gate that fails the `issue_credit` call unless `get_subscriber` has already
  returned a confirmed match
- D. A note in the `issue_credit` tool description stating the $250 limit

**4.** A subscriber returns to a chat from nine days ago. The two shows they were asking about are
still under dispute; everything else about the earlier conversation — the promotions discussed, the
retention offer — has since expired or changed. What should the agent do?

- A. `--resume` the old session and name the two shows still in dispute
- B. Start a new session with a written summary of where the case stands
- C. `/compact` the old session and continue as if nothing changed
- D. `fork_session` from the old session to keep both threads live

**5.** The agent needs to check a subscriber's loyalty tier and their open support tickets before
replying. Both lookups are independent of each other. How should this run at the same time rather
than one after another?

- A. Set `parallel: true` on both tool calls
- B. Issue both Task calls in a single response
- C. Issue the two Task calls in consecutive turns
- D. Run two separate sessions and merge the results

**6.** The agent regularly calls `lookup_invoice` when the subscriber is actually asking about their
subscription tier, which `get_subscriber` would answer. Both tools work correctly. What should be
tried first?

- A. Remove `lookup_invoice` from the agent's toolset
- B. Force `tool_choice` to `get_subscriber` whenever the message mentions a plan or tier
- C. Improve both tool descriptions — inputs, example queries, and when to use one instead of the
  other
- D. Add a routing classifier ahead of the agent

**7.** `get_subscriber` returns three accounts with the same name and postcode. What should the agent
do?

- A. Proceed with the first match returned
- B. Ask the subscriber for another identifier — account number, email, or date of birth
- C. Merge the three accounts and treat them as one
- D. Escalate immediately, since duplicate accounts are a data problem

**8.** `issue_credit` is refused because the subscriber's plan tier does not include the loyalty
credit being requested — nothing is wrong with the API, the token, or the request format. Which
error category?

- A. `permission`, since the subscriber is not entitled to it
- B. `validation`, since the request does not match the plan rules
- C. `business`, with `isRetryable: false` and a customer-friendly explanation
- D. `transient`, since an upgrade would make the credit possible later

**9.** Human agents keep asking the bot to explore what cancellation reason codes exist before they
can file a save-offer. What removes those exploratory calls?

- A. A tool that lists the codes, called once at the start of every conversation
- B. The cancellation reason codes exposed as an MCP resource
- C. The full code list pasted into the system prompt
- D. Caching the exploratory calls between conversations

**10.** Over a long troubleshooting conversation, the credit amount already discussed and the invoice
number in dispute keep disappearing from the running summary. What is the fix?

- A. Summarise more frequently, so less is lost at each step
- B. Increase the context window and stop summarising
- C. Keep a "case facts" block outside the summary, carried forward verbatim
- D. Ask the model to list what it dropped after each summary

**11.** Which two signals must never, on their own, be the basis for escalating a conversation to a
human? **(Select two.)**

- A. The subscriber directly asking to speak to a person
- B. A sentiment score computed from the subscriber's messages
- C. The model's own uncalibrated confidence in its diagnosis
- D. The agent being unable to make any further progress on the case

**12.** A case is escalated to a human agent working in a separate console, with no view of the chat.
Which two things must the handoff summary carry? **(Select two.)**

- A. The complete message transcript, unedited
- B. The verified subscriber ID and the root cause the agent identified
- C. The amount involved and the recommended next action
- D. The model's confidence that its diagnosis is correct

---

## Scenario B — Aurora Retail (Code Generation with Claude Code)

*Aurora Retail runs an e-commerce monorepo with eight packages — checkout, catalog, search,
pricing, inventory, notifications, admin, and shared-ui — used by about 90 engineers. The platform
team is deciding where different kinds of standards and workflows should live.*

**13.** Formatting helpers for currency and dates live in `packages/shared-ui/` and are used only by
code in that package. Where should the conventions for using them live?

- A. In the root CLAUDE.md
- B. In a `.claude/rules/` file with `paths: "packages/shared-ui/**"`
- C. In a CLAUDE.md inside `packages/shared-ui/`
- D. In a skill invoked when a developer touches formatting code

**14.** The team maintains five cross-cutting standards documents — API versioning, error taxonomy,
telemetry, i18n, and accessibility. Each package's lead decides which two or three apply to their
package; once chosen, they must govern all work in that package, and nothing may be copied between
files. What mechanism does this?

- A. A skill per document, invoked when the lead judges it relevant
- B. `@import` lines in each package's CLAUDE.md, referencing the chosen documents
- C. A `.claude/rules/` file per document, with `paths:` covering that package
- D. All five pasted into the root CLAUDE.md with a note on which packages each covers

**15.** Test-fixture conventions apply to any file matching `**/*.fixture.ts`, regardless of which
package it lives in. Where do they belong?

- A. `@import` in every package CLAUDE.md
- B. A `.claude/rules/` file with `paths: "**/*.fixture.ts"`
- C. The root CLAUDE.md
- D. A directory CLAUDE.md in each package that has fixtures

**16.** Commit message format, the ticket-reference rule, and the "no direct pushes to main" policy
must apply to all 90 engineers, in every package, on every task, with nobody having to invoke
anything. Where do they belong?

- A. `~/.claude/CLAUDE.md`
- B. The root CLAUDE.md
- C. A `.claude/rules/` file with `paths: "**/*"`
- D. A skill listed in the onboarding guide

**17.** Twice a year the team runs a dependency-upgrade procedure — a sequence of codemods, a
compatibility sweep, and a changelog draft. Nobody needs it in between. What holds it?

- A. A skill in `.claude/skills/`, invoked when the upgrade starts
- B. The root CLAUDE.md
- C. A `.claude/rules/` file with `paths: "package.json"`
- D. An `@import` in every package CLAUDE.md pointing at the procedure

**18.** A shared `/release-notes` command keeps failing because engineers run it without saying which
package the release covers. Which frontmatter key fixes this?

- A. `paths`
- B. `context: fork`
- C. `argument-hint`
- D. `allowed-tools`

**19.** A dependency-mapping skill has two problems: its output is thousands of lines long and
crowds the rest of the session, and last month it edited a lockfile when it was only ever meant to
read the dependency tree. Which two frontmatter changes fix this? **(Select two.)**

- A. `paths:` limited to `package-lock.json`
- B. `context: fork`, so the skill runs in a separate context
- C. `allowed-tools` limited to the read-only tools the mapping needs
- D. `argument-hint`, so the engineer states the scope before it runs

**20.** One engineer has written a `/tidy-imports` command they use daily that nobody else on the
team wants. Where does it go?

- A. `.claude/commands/tidy-imports.md`, with a comment marking it personal
- B. `~/.claude/commands/tidy-imports.md`
- C. `.claude/skills/tidy-imports/SKILL.md`
- D. A `commands` list in `.claude/config.json`

**21.** The checkout team is restructuring module boundaries across 40 files in the `checkout`
package, changing how orders, payments, and fulfilment talk to each other. Which approach fits?

- A. Direct execution, editing files as the restructuring proceeds
- B. Plan mode, so the approach is reviewed before any file changes
- C. A `.claude/rules/` file describing the new boundaries, applied automatically
- D. A skill that performs the restructuring on request

**22.** The dependency-upgrade skill runs overnight against all eight packages. The build machine
restarts partway through, after five packages have been upgraded. What prevents redoing those five?

- A. `--resume` on the skill's session
- B. A manifest of completed packages, written as each finishes and loaded when the run resumes
- C. A longer timeout on the overnight job
- D. `/compact` at intervals during the run

**23.** An engineer returns to a session from three weeks ago. Since then, two of the eight packages
have been renamed, the build tool has changed, and the ticket scope has grown. What should they do?

- A. `--resume` the session and list every change
- B. `fork_session`, so the stale context stays available for comparison
- C. Start a new session with a written summary of where the work stands now
- D. `--resume` the session, then `/compact` to drop the stale parts

**24.** An engineer needs a broad survey of how error handling is done across all eight packages
before proposing a standard. The survey itself will be noisy — many files opened, many false leads —
and none of that detail needs to stay in the main conversation. What fits?

- A. `fork_session`, so the survey branches off
- B. `/compact` immediately after the survey finishes
- C. An Explore subagent, so the noisy discovery stays out of the main context
- D. A `.claude/rules/` file describing what to look for

---

## Scenario C — Northbridge Research (Multi-Agent Research System)

*Northbridge Research runs a multi-agent system to profile competitors for its clients. A
coordinator plans the work; subagents search the web, read patent filings, read financial filings,
and read customer reviews; a synthesis agent writes the final report with citations.*

**25.** The coordinator is meant to launch research subagents but instead does all the reading itself
and runs out of context. What is missing?

- A. A `subagents:` list in the coordinator's configuration
- B. A higher context limit on the coordinator
- C. `"Task"` in the coordinator's `allowedTools`
- D. A dedicated MCP server exposing the subagents

**26.** A patent-filings subagent returns work that ignores the client's target market, currency, and
date range — all of which the coordinator already knew. Why?

- A. Subagents receive nothing automatically; everything needed must be in the Task prompt
- B. The coordinator's summary was compacted before the subagent read it
- C. Subagents can only read the coordinator's context in the same turn
- D. The subagent should have asked the coordinator for the missing constraints

**27.** The team wants the web-search, patent, financial, and review subagents to run at the same
time instead of one after another. How is that done?

- A. Set `parallel: true` in each subagent's definition
- B. Issue four Task calls in a single response
- C. Issue four Task calls across four consecutive turns
- D. Run four separate sessions and merge the output by hand

**28.** The client wants two competing pricing-strategy narratives developed from one shared reading
of the same 50 filings, so they can be compared side by side. What mechanism fits?

- A. Two Task calls in one response, each given the same 50 filings again
- B. `fork_session`, branching both narratives from the shared analysis
- C. Two separate sessions, each starting from the same prompt
- D. One subagent asked to produce both narratives in a single report

**29.** The synthesis agent occasionally needs to check one factual claim, but giving it the full
research toolset made it start doing its own research instead of synthesising. What is the fix?

- A. Instruct it in the system prompt to use the research tools only for verification
- B. Give it one small cross-role tool, `verify_fact`, and nothing else from that set
- C. Route verification requests back through the coordinator
- D. Remove all tools and have it flag unverified claims for a human

**30.** Research subagents make dozens of exploratory calls at the start of every matter just to
learn what is available — which regions are indexed, which filing types exist, what the schema looks
like. What removes that?

- A. A tool that lists everything available, called once at the start
- B. MCP resources exposing the catalogues — region index, filing types, schema
- C. A longer system prompt describing the corpus in prose
- D. Caching the exploratory calls so repeat calls are cheap

**31.** The firm needs a standard integration with a well-known patent-filings database vendor that
it has not customised in any way. Build or adopt?

- A. Build a custom MCP server, so the tool surface matches exactly
- B. Use the community MCP server for that vendor
- C. Call the vendor's REST API directly from the system prompt
- D. Build a custom server that wraps the community server

**32.** The client asked for coverage of three regions. The final report covers two well and the
third barely at all. Every subagent finished, reported no errors, and returned results consistent
with its own brief. What went wrong?

- A. The synthesis agent dropped the third region while summarising
- B. The third-region subagent hit a context limit and truncated silently
- C. The coordinator's split was too narrow and left the third region uncovered
- D. The subagents needed a shared scratchpad to see each other's coverage

**33.** The web-search subagent and the financial-filings subagent disagree on a competitor's market
share. Both cite sources. What should the report do?

- A. Keep the figure with the more recent-looking source and drop the other
- B. Average the two figures and present one number
- C. Record both figures with their sources; the dates matter
- D. Ask the coordinator to re-run both subagents until they agree

**34.** The synthesis agent cannot tell whether a finding comes from a 2019 press release or a 2026
regulatory filing, and treats them the same. Which two changes fix this? **(Select two.)**

- A. Each subagent must record the publication or collection date with every finding
- B. The model's own confidence in the finding should be recorded alongside it
- C. Each subagent must record the source location with every finding
- D. The synthesis agent should judge credibility itself, once all findings arrive

**35.** Two customer-review subagents were rate-limited for most of the run and returned far fewer
reviews than expected, but the rest of the pipeline completed normally. The draft report reads as
though review sentiment was fully checked. What must the final report do?

- A. Delay publication and retry the rate-limited subagents before sending anything
- B. State which findings are well supported and which topics have coverage gaps
- C. Leave the review-sentiment section out entirely, since it is incomplete
- D. Note the rate-limiting in the project's internal tracking, and publish as planned

**36.** The financial-filings subagent could only retrieve 60 of the 100 filings it was assigned
before its access window closed. What should it return?

- A. Nothing, until the remaining 40 filings can be retrieved
- B. The 60 filings' findings, clearly labelled as partial
- C. A successful result with an empty finding set, since the assignment was not completed
- D. An error that halts the whole research run

---

## Scenario D — Fathom Logistics (Developer Productivity with Claude)

*Fathom Logistics has a decade-old routing engine. New engineers use a Claude Code agent with Read,
Write, Bash, Grep, and Glob, plus MCP servers for Jira and the internal wiki, to find their way
around it.*

**37.** Nobody currently knows which of the 600 files in the routing engine still reference a
protocol the team is retiring, or how deep the dependencies run. How should this audit be
structured?

- A. Prompt chaining — one pass per file, then one pass across all files
- B. Map the codebase first, then plan the remaining passes from what the map shows
- C. A single request containing summaries of all 600 files
- D. One subagent per top-level folder, each deciding its own scope

**38.** An engineer returns to a session from last week. Two files they know by name have since
changed; everything else discussed still holds. What should they do?

- A. `--resume` the session and name the two changed files
- B. Start a new session and re-explain the routing engine from scratch
- C. `/compact` the old session and continue without mentioning the changes
- D. `fork_session` from the old session and work in the branch

**39.** In one turn the model calls `Bash` and `Grep`. The next request to the API is rejected as
malformed. What does a correct implementation send back?

- A. One assistant message containing both results
- B. Two separate user messages, one per result
- C. One user message with two `tool_result` blocks, each carrying its matching `tool_use_id`
- D. One user message with a single `tool_result` block listing both outputs

**40.** The team wants to compare two different ways of restructuring the routing engine's core
module, both starting from the same reading of its current structure, without reading it twice.
What fits?

- A. Two Task calls in one response, each re-reading the module
- B. `fork_session`, branching both restructuring approaches from the shared reading
- C. Two separate sessions, each starting cold
- D. `--resume` twice from the same session name

**41.** An engineer needs every file with a `.proto` extension in the repository. Which tool?

- A. `Glob`
- B. `Grep`
- C. Semantic search
- D. `Read` on each top-level folder in turn

**42.** An engineer is looking for the code that decides how a shipment gets re-routed after a
failed delivery attempt. It might be called re-routing, redelivery, or fallback-dispatch; nobody
currently on the team is sure, and none of those words appear in any file they have opened. Which
search fits?

- A. `Grep` for "re-routing", then "redelivery", then "fallback"
- B. `Glob` on `**/*rout*`, widening the pattern until something matches
- C. `Grep` with a case-insensitive alternation of all three candidate words
- D. Semantic search for the concept of re-routing after a failed delivery

**43.** `Edit` keeps failing on a configuration block because the agent cannot match its exact text
uniquely. What is the correct fallback?

- A. Retry `Edit` with a shorter match string
- B. `Grep` for the block, then call `Edit` again with the matched line
- C. `Read` the file and `Write` it back with the change applied
- D. Delete the file and recreate it from scratch

**44.** The agent keeps reaching for the built-in `Grep` tool instead of a custom MCP tool that
indexes the routing engine semantically and would answer the same question better. What should be
tried first?

- A. Remove `Grep` from the agent's toolset
- B. Force `tool_choice` to the MCP tool whenever a code question is asked
- C. Improve the MCP tool's description — what it does, example queries, when to prefer it
- D. Add a routing classifier ahead of the agent

**45.** `.mcp.json` is committed to the repository, and the Jira and wiki servers both need API
tokens. What keeps the tokens out of version control?

- A. `${VAR}` references in `.mcp.json`, resolved from the environment
- B. Moving both servers to `~/.claude.json` on every machine
- C. A `.env` file committed alongside `.mcp.json`, listed in `.gitignore`
- D. Encrypted token values written directly into `.mcp.json`

**46.** One engineer runs a personal MCP server against a staging database only they can reach, and
it must not appear for anyone else on the team. Where is it configured?

- A. `~/.claude.json`
- B. `.mcp.json`, with the server disabled by default
- C. `.claude/mcp/local.json`
- D. `.mcp.json`, with `${VAR}` around the connection string

**47.** An engineer cannot work out why a rule about test fixtures is applying in a package where it
should not be. What tells them which memory files are actually loaded?

- A. `--verbose` on the next command
- B. `/context`
- C. `/memory`
- D. Reading each CLAUDE.md by hand up the folder tree

**48.** Engineers exploring the routing engine for the first time report two problems: findings from
early in a long session are getting lost by the time they write their summary, and the summary has
started describing "typical routing logic" instead of the specific functions actually found. Which
two changes address this? **(Select two.)**

- A. Write findings to scratchpad files as they are found, and read them back when writing the
  summary
- B. Increase the context window so nothing has to be dropped
- C. Move key findings to the beginning of the context, not the middle
- D. Ask the model to be more concise in its own exploration notes

---

## Scenario E — MedPath Health (Claude Code for Continuous Integration)

*MedPath Health runs Claude Code inside its CI pipeline across a dozen services: reviewing every
pull request, generating missing tests, and posting a machine-readable summary that a pipeline gate
reads. Pull requests average 15–20 changed files.*

**49.** A pipeline step hangs until the job timeout kills it. What should the step use instead?

- A. `--json-schema`
- B. `-p` (`--print`), so it does not wait for interactive input
- C. `--resume`
- D. `/compact` before the step starts

**50.** A draft CI runbook lists four ways to run Claude Code non-interactively. Which two do not
exist and must be removed? **(Select two.)**

- A. `-p` / `--print`
- B. `CLAUDE_HEADLESS=true` as a workflow environment variable
- C. `--output-format json`
- D. `--no-interactive`

**51.** The pipeline gate needs the review summary to carry the same fields every time — file, line,
severity, suggested fix — so it can fail the build on any critical finding. What guarantees that
shape?

- A. `--output-format json` on its own
- B. Asking for the fields in the prompt, then validating with a shell script afterwards
- C. `--output-format json` together with `--json-schema` describing the fields the gate expects
- D. A `schema:` key in the workflow file listing the required fields

**52.** Generated tests are low-value — getters, framework internals — and ignore the team's fixture
conventions. What fixes this properly?

- A. Append the testing standards to the prompt string inside the pipeline script
- B. Write the testing standards, fixture conventions, and review criteria into CLAUDE.md
- C. Add a `.claude/rules/` file with `paths: "**/*.ts"` describing the standards
- D. Reduce the number of tests requested per run

**53.** The pipeline also suggests tests for scenarios the suite already covers. What stops that?

- A. Add "do not duplicate existing tests" to the prompt
- B. Run the suite first and pass the coverage percentage into the prompt
- C. Give it the existing test files for the module
- D. Ask for fewer tests and have a reviewer delete duplicates

**54.** The review runs again on every new commit and re-posts comments the developer already read
and addressed. What is the correct fix?

- A. Include the earlier findings in the context and ask for only new or still-unfixed issues
- B. Run the review only on the first commit of a pull request
- C. Post-process the comments and drop any that match an earlier one
- D. Narrow the review to files touched by the most recent commit

**55.** A 20-file pull request gets a thorough review on the first five files and a shallow one on
the rest. What structure fixes this?

- A. A single pass over the whole diff, with the largest available context window
- B. One pass per file, then one pass across all files for cross-file issues
- C. One subagent per file, working independently with no final pass
- D. Reduce the review to a sample of files per run

**56.** Findings come back labelled critical, major, or minor, and the same class of bug gets a
different label between runs. What makes the labelling consistent?

- A. Ask the model to report a confidence score next to each severity label
- B. Define each severity level in the prompt with concrete code examples
- C. Run the review three times and take the majority severity
- D. Reduce the scheme to two levels, blocking and non-blocking

**57.** The "possible race condition" category is wrong about 70% of the time it fires. Developers
have started ignoring the accurate SQL-injection findings too. What is the correct action?

- A. Turn off the race-condition category, keep the others running, fix its prompt, then turn it back
  on
- B. Add "be conservative and only report what you are confident about" to the review prompt
- C. Report only findings the model marks as high confidence
- D. Keep every category, but downgrade race-condition findings to the lowest severity

**58.** The pipeline sometimes has the model review code from the same session that wrote it, and
defects it clearly introduced pass review. What is the right design?

- A. Ask for a second self-review pass with a stricter prompt
- B. Have an independent instance review the draft, without the drafting context
- C. Run three self-reviews and take the majority verdict
- D. Have the model list its own assumptions and review those instead

**59.** The security team wants a full-repository dependency audit across all twelve services, run
once a week, with no one waiting on the result. Which API fits, and why?

- A. The real-time Messages API, because audits should run as soon as triggered
- B. The Message Batches API, because nobody is waiting and it is roughly half the cost
- C. The real-time API with a low `max_tokens`, to keep it fast
- D. The Message Batches API, because it supports multi-turn tool calling that a weekly audit needs

**60.** A classification step for pull-request risk level handles the obvious cases well and is
inconsistent on the borderline ones. How many few-shot examples, and of what kind?

- A. Ten to twelve examples, spread evenly across all risk levels
- B. One example per risk level, taken from the clearest cases
- C. Two to four examples, chosen from the unclear, borderline cases
- D. As many as the context allows

---

## Scenario F — Harborline Customs (Structured Data Extraction)

*Harborline Customs extracts structured shipment manifests from freight-forwarder documents —
PDFs, scanned forms, and emails — arriving from dozens of sources. About 25,000 documents move
through overnight, alongside a small queue of urgent shipments an agent is waiting on.*

**61.** The extraction prompt asks for the manifest "as JSON" in the response text. About one
response in twenty fails to parse, with no consistent pattern to the failures. What is the reliable
fix?

- A. Add more few-shot examples of well-formed JSON to the prompt
- B. Parse leniently and repair the malformed JSON downstream
- C. Declare the manifest as a tool input schema and return it through tool use
- D. Lower the temperature and retry any response that fails to parse

**62.** Every customs declaration in this flow is machine-generated and always carries a
`declaration_number` in a fixed field. Extractions are sometimes coming back without one. How
should the field be declared?

- A. Nullable, and log the documents where it is missing
- B. Nullable, with a validation rule that rejects null
- C. Required, so the field cannot be omitted from the output
- D. Optional, with the number recovered later from the sender's email

**63.** A `hazard_class` field is present only when the shipment contains dangerous goods — most
manifests have no such section. The field is currently required, and the model is producing
plausible hazard classes for shipments that have none. What should the schema do?

- A. Keep it required and add "leave blank if absent" to the prompt
- B. Make it optional and nullable, so absence can be represented
- C. Keep it required, with an enum whose members include `none`
- D. Keep it required and reject any value not present verbatim in the source

**64.** The forwarders write dates as `14/08/26`, `2026-08-14`, and `14 Aug 2026`, and weights as
`1,240 kg`, `1240kg`, and `1.24t`. The schema already types these fields strictly. What produces one
consistent record?

- A. A post-processing layer with a branch per forwarder's format
- B. Format normalisation rules in the prompt, alongside the strict schema
- C. A separate extraction prompt per forwarder, selected by sender address
- D. A looser schema that accepts each forwarder's native format as a string

**65.** Manifests arrive unsorted, and four schemas exist — air, sea, rail, and road freight. The
type is not known until the document is read. Which `tool_choice` setting fits?

- A. `auto`
- B. `none`
- C. `any`
- D. `{"type": "tool", "name": "extract_air_freight"}`

**66.** The overnight run of 25,000 documents completes and 400 come back as errors. What is the
correct next step?

- A. Resubmit the whole batch, since partial batches cannot be matched to results
- B. Move the 400 to the real-time API and accept the higher cost
- C. Resubmit only the failed requests, matched to their results by `custom_id`
- D. Resubmit the batch with a longer processing window

**67.** The Message Batches API may take up to 24 hours to return results, and Harborline has
committed to a 30-hour turnaround for every urgent-queue document that goes through it. How often
must the urgent queue be submitted to guarantee this?

- A. Every 4 hours
- B. Every 8 hours
- C. Every 16 hours
- D. Every 24 hours

**68.** Some manifests state a total shipment weight that does not match the sum of the line-item
weights, and separately a few list two different countries of origin for the same shipment without
either being marked wrong. Which two schema additions catch these? **(Select two.)**

- A. A `calculated_total` field next to the `stated_total` from the document
- B. A `total_is_correct` boolean the model fills in after checking
- C. A `conflict_detected` boolean, recording both values with their sources
- D. A confidence score on the `stated_total` field

**69.** Field accuracy averages 97% across all manifests, but hazardous-goods manifests are
suspected of a much higher error rate hidden inside that average. Which two checks find out?
**(Select two.)**

- A. Increase the review sample size uniformly across all manifests
- B. A stratified random sample of the high-confidence extractions, reviewed by hand
- C. Accuracy broken down by document type and by field, not as one average
- D. A second extraction pass, keeping the record only where the two passes agree

**70.** One freight forwarder's document portal was unreachable for six hours overnight, so part of
the morning report rests on fewer sources than usual for that stretch. What must the report do?

- A. Retry the portal until it responds, then publish on schedule
- B. Summarise the affected section more heavily so the gap is less visible
- C. State which findings are well supported and which sections have coverage gaps
- D. Publish as normal and record the outage in the pipeline's internal log

**71.** A batch job could only reach 3,000 of the 4,000 documents assigned to it before its
processing window closed. Which of these is never acceptable in that situation?

- A. Returning the 3,000 extracted records, clearly labelled as a partial result
- B. Returning a successful result with an empty record set, since the batch did not finish
- C. Reporting how many documents were and were not processed
- D. Resubmitting only the missing 1,000 in the next batch window

**72.** The team adds a field-level confidence score to each extraction, meant to decide which
fields go to human review. When is that confidence score actually usable for that purpose?

- A. As soon as the model produces it, since the model has seen the full document
- B. Only once it is calibrated against labelled data — checked confidence against actual accuracy
- C. Only when averaged across the whole document, not per field
- D. Only for documents below the 97% accuracy average
