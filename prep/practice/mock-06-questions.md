# Mock 6 — Full-length exam simulation, reading-discipline paper (60 questions)

**Take this timed and cold.** Write down the time you finish the first pass, then **stay in the
room** and run the two sweeps before you open the key:

1. **Every *select two* — count your letters.** Ten questions here are select-two. Say the number
   of letters you owe out loud before you read the options.
2. **Every last sentence containing *never*, *not*, *except*, *instead* — re-read the stem.** Four
   questions here run in the inverse direction (Q25, Q37, Q48, Q57). Two of them look exactly like
   ordinary questions until the last five words.

| | |
|---|---|
| Questions | 60 |
| Time | 120 minutes |
| Format | 4 scenarios × 15 questions, as on the real exam |
| Multiple-response | 10 questions, each marked **(Select two.)** |
| Working pass mark | 43 / 60 |
| Answer key | `mock-06-answers.md` — with a per-domain score sheet |

Domain spread: D1 16 · D2 11 · D3 12 · D4 12 · D5 9 (the blueprint weighting).

**What this paper targets.** Mock 5 (48/60) lost five marks on select-two and six on Domain 3
grouping. So:

- **Domain 3 is one solid block, Q16–Q25**, ten grouping questions in a row with `@import`,
  `.claude/rules/`, a directory CLAUDE.md, the root CLAUDE.md and a skill all live in the same
  scenario. Before each one, say the sentence: *what set of files does this content govern?*
- **Select-two appears in every scenario**, including two questions where the two symptoms are
  **different kinds of thing**, which is where the habit broke on 14 Aug.
- **Both Mock 5 blanks are back**: the handoff package (Q60) and multi-issue handling (Q59).
- **Invented features** appear five times: `CLAUDE_HEADLESS=true`, `--no-interactive`,
  `parallel: true`, `.claude/config.json` with a `commands` list, and a `paths:` key in SKILL.md.
- Every question is self-contained; the scenario text is background only.

---

## Scenario A — Claims intake at a motor insurer

*An insurer processes claim packets that arrive from three carriers as PDFs, emails and scanned
forms. A Claude-based pipeline extracts a structured claim record, checks it against policy rules,
and passes anything unresolved to a human adjuster. Volumes are about 40,000 packets a night.*

**1.** The pipeline prompt asks for the claim record "as JSON in your response". About one response
in twenty cannot be parsed, and the failures have no pattern. What is the correct fix?

- A. Add six more few-shot examples of well-formed JSON to the prompt
- B. Wrap the parser in a lenient mode that repairs trailing commas and unquoted keys
- C. Declare the record as a tool input schema and return it through tool use
- D. Set temperature to 0 so the output format stops varying

**2.** A claim packet contains the loss adjuster liability opinion only when the claimant disputed
fault; most packets have no such section. How should `liability_opinion` be declared?

- A. Nullable, so the model can return null when the section is absent
- B. Required, so the field is never missing from the output
- C. Required, with a validation rule that rejects an empty string
- D. Nullable, with a validation rule that rejects null

**3.** Every carrier acknowledgement is machine-generated and always carries a claim reference in a
fixed position. Extractions are sometimes coming back without one. How should the field be declared?

- A. Nullable, and log the packets where it is missing
- B. Nullable, with a post-processing step that fills it from the filename
- C. Optional, with the reference recovered later from the carrier portal
- D. Required, so the field cannot be omitted from the output

**4.** The three carriers write dates as `14/08/26`, `2026-08-14` and `14 Aug 2026`, and amounts as
`GBP 1,240.00`, `1240.00 GBP` and `1240`. The schema types are already strict. What produces one
consistent record?

- A. A post-processing layer with a branch per carrier format
- B. Format normalisation rules in the prompt, alongside the strict schema
- C. A separate extraction prompt per carrier, selected by sender address
- D. A looser schema that accepts each carrier native format as a string

**5.** Some packets state a settlement total that does not match the sum of the line items, and the
pipeline has been passing them through. What should the schema add?

- A. A `calculated_total` field next to the `stated_total` from the document
- B. A `total_is_correct` boolean the model fills in after checking
- C. A required `line_item_count`, so short extractions are visible
- D. A confidence score on the `stated_total` field

**6.** Two problems in the same records. Some packets give a different date of loss in the police
report than in the claim form, and both are being dropped silently. Separately, the injury category
list keeps growing as new product lines launch, and unfamiliar categories are being forced into the
nearest existing value. Which two schema changes address these? **(Select two.)**

- A. Make the date of loss nullable, so a disagreement produces null
- B. Add a `conflict_detected` boolean, recording both values with their sources
- C. Raise the temperature so the model stops collapsing onto familiar categories
- D. Use an enum plus an `"other"` value and a free-text detail string

**7.** The nightly run of 40,000 packets goes through the Message Batches API. On Tuesday, 312
requests came back as errors. What is the correct next step?

- A. Resubmit the whole batch, since partial batches cannot be matched to results
- B. Move the whole workload to the real-time API, where failures surface immediately
- C. Resubmit only the failed requests, matched to their results by `custom_id`
- D. Split the batch into twelve smaller batches and rerun them all

**8.** The orchestration loop sometimes ends a turn while a tool call is still outstanding, and
sometimes keeps going after the model has finished. What must the loop use to decide?

- A. Whether the response contains any `tool_use` blocks
- B. `stop_reason`: continue on `"tool_use"`, stop on `"end_turn"`
- C. Whether the response contains a text block and no tool call
- D. A maximum iteration count, with `stop_reason` as a secondary check

**9.** In one turn the model calls three tools. The next API request is rejected as malformed. What
does a correct implementation send back?

- A. Three separate user messages, one per tool result, in call order
- B. One user message containing the results that succeeded, with failures omitted
- C. One assistant message containing all three results
- D. One user message containing three `tool_result` blocks, each with its matching `tool_use_id`

**10.** A quarterly compliance review covers a known list of 34 policy documents against a fixed
checklist of eleven criteria. How should the work be structured?

- A. Prompt chaining: one pass per document, then one pass across all documents
- B. Dynamic decomposition, since a compliance review is a large open-ended task
- C. A single request containing all 34 documents and the checklist
- D. One subagent per criterion, each reading all 34 documents independently

**11.** Two rules must hold on every claim without exception: no payout above 5,000 may be approved
by the pipeline, and the claimant identity must be verified before any payout is approved. Which two
changes guarantee this? **(Select two.)**

- A. A `PreToolUse` hook that blocks the approval call when the amount exceeds 5,000 and routes it
  to escalation
- B. A stronger system prompt stating that payouts above 5,000 must always be escalated
- C. A prerequisite gate that fails the approval call unless identity verification has completed
- D. A few-shot example showing a 6,200 claim being escalated instead of approved

**12.** The policy engine, the API and the caller credentials are all healthy, but a claim is refused
because the policy lapsed eleven days before the incident. How should the tool report this?

- A. `transient`, with `isRetryable: true`, since the policy may be reinstated
- B. `business`, with `isRetryable: false` and a customer-friendly explanation
- C. `validation`, since the incident date fails the policy date check
- D. `permission`, since the claimant is not entitled to a payout

**13.** One `claim_operations` tool takes a `mode` parameter with nine values — `lookup`, `price`,
`approve`, `escalate` and five more — and the model regularly picks the wrong mode. What is the
right redesign?

- A. Keep one tool and expand the description of each mode with examples
- B. Reduce the nine modes to three broader modes
- C. Split it into purpose-specific tools, each with its own input contract
- D. Add a `mode_hint` parameter the caller sets before the model chooses

**14.** One carrier document service was unavailable for four hours, so part of last night report
rests on two carriers instead of three. What must the report do?

- A. Retry the unavailable carrier until it responds, then publish
- B. Summarise the affected sections more aggressively to hide the thin coverage
- C. Publish the totals and note the outage in the pipeline log
- D. State which findings are well supported and which topics have coverage gaps

**15.** Field accuracy averages 97%, and the team wants to stop reviewing extractions the model
marks high-confidence. Which two checks tell them whether that is safe? **(Select two.)**

- A. A stratified random sample of the high-confidence extractions, reviewed by hand
- B. A review of every extraction the model marked low-confidence
- C. Accuracy broken down by document type and by field, not as one average
- D. A second extraction pass, keeping the record where the two passes agree

---

## Scenario B — A platform team standardising a monorepo

*A fintech monorepo holds nine product packages and four shared libraries, and around 120 engineers
use Claude Code in it. The platform team is deciding where each kind of standard should live so that
it loads at the right time and nothing is duplicated.*

**16.** Component story files named `*.stories.tsx` exist in all nine packages. The conventions for
writing them are the same everywhere, and the team wants them in context only when someone edits a
story file. Where do they belong?

- A. In each package CLAUDE.md, so the nine copies stay near the code
- B. In a skill the engineer invokes when starting a new story
- C. In a `.claude/rules/` file with `paths: "**/*.stories.tsx"`
- D. In the root CLAUDE.md, since the conventions are identical across packages

**17.** The team maintains six shared engineering documents — API design, error taxonomy, logging,
migrations, testing, release. Each package maintainer decides which of the six govern work in their
package, and nothing may be copied. What mechanism does this?

- A. A skill per document, invoked when the maintainer needs it
- B. `@import` lines in each package CLAUDE.md, referencing the documents that apply
- C. A `.claude/rules/` file per document, with `paths:` covering that package folder
- D. All six in the root CLAUDE.md, with a note saying which packages each applies to

**18.** The billing service in `services/billing/` has reconciliation rules that apply to every file
inside it and to nothing outside it. Where do they go?

- A. In a `.claude/rules/` file with `paths: "services/billing/**"`
- B. In the root CLAUDE.md, under a "billing" heading
- C. In a skill that engineers invoke when they open a billing ticket
- D. In a CLAUDE.md inside `services/billing/`

**19.** Twice a year the team runs a framework upgrade: a sequence of codemods, a dependency sweep
and a changelog. Nobody needs the procedure in between. What holds it?

- A. A skill in `.claude/skills/`, invoked when the upgrade starts
- B. The root CLAUDE.md, so nobody has to remember it exists
- C. A `.claude/rules/` file with `paths: "package.json"`
- D. An `@import` in each package CLAUDE.md pointing at the procedure

**20.** Commit message format, the ticket-reference rule and the "no direct pushes to main" policy
must apply to every engineer, in every package, on every task, without anyone invoking anything.
Where do they belong?

- A. In `~/.claude/CLAUDE.md`, so each engineer carries them
- B. In the root CLAUDE.md
- C. In a `.claude/rules/` file with `paths: "**/*"`
- D. In a skill listed in the onboarding guide

**21.** One engineer has written a `/scratch-review` command they use daily and that nobody else
wants. Where does it go?

- A. `.claude/commands/scratch-review.md`, with a note that it is personal
- B. `.claude/skills/scratch-review/SKILL.md`
- C. `~/.claude/commands/scratch-review.md`
- D. A `commands` list in `.claude/config.json`

**22.** The same engineer runs a local MCP server for a database only they can reach, and it must
not appear for anyone else. Where is it configured?

- A. `~/.claude.json`
- B. `.mcp.json`, with the server disabled by default
- C. `.claude/mcp/local.json`
- D. `.mcp.json`, with `${VAR}` around the connection string

**23.** A dependency-audit skill has two problems: its output is thousands of lines long and it
crowds out the rest of the session, and last week it edited a lockfile when it was only ever meant
to read. Which two frontmatter changes fix this? **(Select two.)**

- A. `paths:` limited to `package-lock.json`
- B. `context: fork`, so the skill runs in a separate context
- C. `allowed-tools` limited to the read-only tools the audit needs
- D. `argument-hint`, so the engineer states the scope before it runs

**24.** An engineer cannot work out why a rule about test fixtures is being applied in a package
where it should not be. What tells them which memory files are loaded?

- A. `--verbose` on the next command
- B. `/context`
- C. Reading each CLAUDE.md by hand up the folder tree
- D. `/memory`

**25.** A draft CI runbook lists four ways to run Claude Code non-interactively. Which two do not
exist and must be removed? **(Select two.)**

- A. `-p` / `--print`
- B. `CLAUDE_HEADLESS=true` as a workflow environment variable
- C. `--output-format json`
- D. `--no-interactive`

**26.** An engineer returns to a migration session from yesterday. Three files they know by name
have changed since; everything else in the earlier context still holds. What should they do?

- A. `--resume` the session and name the three changed files
- B. Start a new session and re-explain the migration from scratch
- C. `/compact` the old session, then continue without mentioning the changes
- D. `fork_session` from the old session and work in the branch

**27.** A second engineer returns to a session from three weeks ago. The package layout, the
dependency versions and the ticket scope have all changed since. What should they do?

- A. `--resume` the session and list every change
- B. `fork_session`, so the stale context stays available for comparison
- C. Start a new session with a written summary of where the work stands
- D. `--resume` the session and run `/compact` to drop the stale parts

**28.** The team wants three package audits to run at the same time rather than one after another.
How is that expressed?

- A. Set `parallel: true` in the coordinator configuration
- B. Issue three Task calls in a single response
- C. Issue three Task calls in three consecutive turns
- D. Run three Claude Code sessions and merge the output by hand

**29.** An engineer needs the code that decides whether a customer is eligible for the overdraft
buffer. It might be called eligibility, entitlement, buffer-check or something else; nobody is sure,
and the term does not appear in any file they have opened. Which search fits?

- A. `Glob` on `**/*eligib*`, then widen the pattern until something matches
- B. `Grep` for `eligibility`, then for `entitlement`, then for `buffer`
- C. `Grep` with a case-insensitive alternation of all four candidate words
- D. Semantic search for the concept of overdraft eligibility

**30.** `.mcp.json` is committed to the repository and two servers need API tokens. What keeps the
tokens out of version control?

- A. `${VAR}` references in `.mcp.json`, resolved from the environment
- B. Moving both servers to `~/.claude.json` on every machine
- C. A `.env` file committed alongside `.mcp.json` and listed in `.gitignore`
- D. Encrypted token values inside `.mcp.json`

---

## Scenario C — A legal research system built from subagents

*A firm runs a multi-agent research system. A coordinator plans the work, research subagents read
case law and filings across three jurisdictions, and a synthesis agent writes the memo. Matters
often run for days and produce hundreds of documents.*

**31.** The coordinator is supposed to launch research subagents but never does; it does the reading
itself and runs out of context. What is missing?

- A. A `subagents:` list in the coordinator configuration
- B. A higher context limit on the coordinator
- C. `"Task"` in the coordinator `allowedTools`
- D. A separate MCP server exposing the subagents

**32.** A research subagent returns work that ignores the matter jurisdiction, the date range and
the client position, all of which the coordinator knew. Why?

- A. Subagents receive nothing automatically, so all of it has to be in the prompt
- B. The coordinator summary was compacted before the subagent read it
- C. Subagents can read the coordinator context only in the same turn
- D. The subagent should have queried the coordinator for the missing constraints

**33.** The firm wants two competing arguments developed from one shared reading of the same
sixty-document record, so the partner can compare them. What mechanism fits?

- A. Two Task calls in one response, each given the document list
- B. `fork_session`, branching both arguments from the shared analysis
- C. Two separate sessions, each starting from the same prompt
- D. One subagent asked to produce both arguments in one report

**34.** The memo covers two jurisdictions well and the third barely at all. Every subagent finished,
reported no errors, and returned results consistent with its own brief. What went wrong?

- A. The synthesis agent dropped the third jurisdiction while summarising
- B. The third jurisdiction subagent hit a context limit and truncated silently
- C. The subagents needed a shared scratchpad to see each other coverage
- D. The coordinator split was too narrow and left the third jurisdiction uncovered

**35.** A new matter involves 900 documents in an unfamiliar regulatory area. Nobody knows yet which
documents matter or what the argument will turn on. How should the work be structured?

- A. Prompt chaining: one pass per document, then one pass across documents
- B. One subagent per hundred documents, each writing a summary
- C. Map the material first, then plan the passes from what the map shows
- D. A single long session, adding documents as they become relevant

**36.** Subagents are given a numbered procedure and follow it literally: when step three does not
apply to their jurisdiction, they stop and report the step as blocked. How should the prompts change?

- A. State the objective and the success criteria, and let the subagent choose the route
- B. Add a branch to the procedure for every jurisdiction the firm covers
- C. Add a step instructing the subagent to skip steps that do not apply
- D. Move the procedure into the coordinator and have it issue one step at a time

**37.** The team is reviewing how the orchestration loop decides a turn is finished. Which two of
these are never valid ways to make that decision? **(Select two.)**

- A. `stop_reason` is `"end_turn"`
- B. The model calls a `task_complete` tool the team defined for the purpose
- C. `stop_reason` is not `"tool_use"`
- D. The response contains a text block

**38.** Over a long matter, the running summary keeps losing details that turn out to matter — the
client incorporation date, the two disputed clause numbers. What is the fix?

- A. Summarise more often, so less is lost each time
- B. Increase the context window and stop summarising
- C. Keep a "case facts" block outside the summary, carried forward verbatim
- D. Ask the model to list what it dropped after each summary

**39.** Two complaints from reviewers. Findings recorded in the middle of a long session are missing
from the memo, and the memo has started describing "typical patterns in cases like this" instead of
the specific clauses the agents actually found. Which two changes address these? **(Select two.)**

- A. Place the key findings at the beginning of the context, not in the middle
- B. Raise the context window so nothing has to be dropped
- C. Write findings to scratchpad files the agents read back from
- D. Ask the synthesis agent to re-read the full transcript before writing

**40.** A case-law tool returns 46 fields per result — court, docket, judge, parties, procedural
history and more — of which the agents use five. Context fills after a dozen calls. What is the fix?

- A. Ask the agents to ignore the fields they do not need
- B. Trim the tool output to the five fields before it enters the context
- C. Summarise the tool results once the context is nearly full
- D. Call the tool less often and reason more between calls

**41.** The synthesis agent cannot tell whether a finding comes from a 2019 practice note or a 2026
appellate decision, and it treats them alike. What must change?

- A. The synthesis agent should weigh sources by credibility
- B. The synthesis agent should re-fetch each source at synthesis time
- C. The coordinator should re-rank findings by recency before synthesis
- D. Each research subagent must record the date, the source location and the methodology with the
  finding

**42.** A matter that had been running for two days died when the machine rebooted. Work had to
restart from nothing. What prevents that?

- A. Manifests written as work completes, loaded by the coordinator when work resumes
- B. `--resume` on the coordinator session
- C. A longer context window, so less state is held outside the session
- D. Checkpointing the synthesis agent draft after every finding

**43.** Research subagents make dozens of exploratory calls just to learn what is available — which
courts are indexed, which filing types exist, what the schema looks like. What removes that?

- A. A tool that lists everything available, called once at the start of each matter
- B. A longer system prompt describing the corpus in prose
- C. MCP resources exposing the catalogues — court index, filing types, schema
- D. Caching the exploratory calls so repeat calls are cheap

**44.** The synthesis agent occasionally needs to check one factual claim, but giving it the full
research toolset made it start doing its own research instead of synthesising. What is the fix?

- A. Instruct it in the system prompt to use the research tools only for verification
- B. Give it one small cross-role tool, `verify_fact`, and nothing else from that set
- C. Have it route verification requests back through the coordinator
- D. Remove all tools and have it flag unverified claims for a human

**45.** The firm has a `/matter-brief` command that every lawyer on the team should be able to run.
Where does it live?

- A. `~/.claude/commands/matter-brief.md`
- B. `.claude/skills/matter-brief/SKILL.md`
- C. The root CLAUDE.md, as a documented procedure
- D. `.claude/commands/matter-brief.md`

---

## Scenario D — A telecom customer support agent

*A mobile network runs a Claude-based support agent across chat and email. It reads billing and
network systems through tools, resolves what it can, and hands the rest to human agents who work in
a separate console.*

**46.** A tool call fails because the service token it was issued does not carry the billing scope.
The API is healthy and the request was well formed. Which category?

- A. `permission`, with `isRetryable: false`
- B. `transient`, with `isRetryable: true`
- C. `validation`, since the request lacked a required credential
- D. `business`, since billing access is restricted by policy

**47.** A different call fails because the customer plan does not allow international roaming to be
enabled mid-cycle. The caller is authorised and the API is healthy. Which category?

- A. `permission`, since the customer is not permitted to make the change
- B. `validation`, since the request is invalid for this plan
- C. `business`, with `isRetryable: false` and a customer-friendly explanation
- D. `transient`, since the change becomes possible next cycle

**48.** The team is auditing how tools report failures. Which two of these must a tool never do?
**(Select two.)**

- A. Return `errorCategory`, `isRetryable` and a human-readable message
- B. Return a generic "an error occurred" message with no category
- C. Return the partial results it did obtain, marked as partial
- D. Return success with an empty result set when the lookup failed

**49.** Support engineers need every place the string `RETRY_LIMIT_EXCEEDED` appears in the codebase.
Which tool?

- A. `Grep` for `RETRY_LIMIT_EXCEEDED`
- B. `Glob` for `**/*retry*`
- C. Semantic search for retry-limit handling
- D. `Read` on each service error module in turn

**50.** The agent needs to read and update tickets in a widely used ticketing product the firm has
not customised. Build or adopt?

- A. Build a custom MCP server, so the tool surface matches the agent needs exactly
- B. Use the community MCP server for that product
- C. Call the product REST API directly from the system prompt
- D. Build a custom server that wraps the community server

**51.** A classification prompt handles the clear cases well and is inconsistent on the borderline
ones. How many few-shot examples, and of what?

- A. Ten to twelve examples, spread evenly across all categories
- B. One example per category, taken from the clearest cases
- C. As many as the context allows, since more examples means more accuracy
- D. Two to four examples, chosen from the unclear cases

**52.** A prompt describes in prose how to turn a customer complaint into a structured incident
summary. Results vary run to run. What is the most effective change?

- A. Two or three concrete input/output examples of the transformation
- B. A longer prose description covering more of the variations
- C. An instruction to be consistent and follow the format exactly
- D. A validation step that rejects summaries not matching the description

**53.** One of the agent six issue categories, "possible fraud", is wrong most of the time it fires,
and human agents have started ignoring the other five categories too. What should the team do?

- A. Raise the threshold for "possible fraud" and leave it running
- B. Tell the model to be conservative when applying "possible fraud"
- C. Turn "possible fraud" off while they fix it, keeping the other five
- D. Merge "possible fraud" into a broader "account risk" category

**54.** After drafting a resolution, the agent reviews its own draft for policy breaches and finds
almost none, though QA finds several. What is the right design?

- A. Ask for a second self-review pass with a stricter prompt
- B. Have an independent instance review the draft, without the drafting context
- C. Run three self-reviews and take the majority verdict
- D. Have the agent list its assumptions and review those instead

**55.** For the intent-routing step, the agent must always call one of the routing tools and never
answer the customer directly, though which tool it calls is its own decision. What setting?

- A. `tool_choice: "auto"`
- B. `tool_choice: "none"`
- C. `tool_choice: {"type": "tool", "name": "route_intent"}`
- D. `tool_choice: "any"`

**56.** An engineer wants their own shortcuts and phrasing preferences to apply when they use Claude
Code, on their machine only, and not to reach the rest of the team. Where do they go?

- A. `~/.claude/CLAUDE.md`
- B. `CLAUDE.md` in the repository root, in a "personal" section
- C. `.claude/rules/personal.md`
- D. `.claude/CLAUDE.local.md`

**57.** The team is writing the escalation policy. Which two signals must never on their own trigger
an escalation? **(Select two.)**

- A. The customer asking to speak to a person
- B. A situation the policy does not cover
- C. The tone of the customer messages
- D. The model own confidence score in its diagnosis

**58.** A customer writes: "I do not want to keep going round in circles with a bot, put me through
to someone." The agent has a working fix for the billing error in hand. What should it do?

- A. Offer the fix first, and escalate only if the customer asks a second time
- B. Escalate immediately, with a structured handoff summary
- C. Apply the fix, then tell the customer a human will follow up
- D. Ask the customer to confirm they want a human before escalating

**59.** One email contains three problems: a refund that never arrived, a wrong delivery address on
the next order, and a promotion code that was rejected. What is correct handling?

- A. Answer the refund first and ask the customer to write separately about the others
- B. Ask the customer which of the three to deal with first
- C. Split the message into three items, investigate them in parallel over shared context, and
  return one combined answer
- D. Escalate the whole email, since multi-issue messages exceed the agent scope

**60.** A case is escalated to a human agent who works in a separate console and cannot see the
conversation. Which two things must the handoff carry? **(Select two.)**

- A. The verified customer ID and the root cause the agent identified
- B. The complete message transcript, unedited
- C. The amount involved and the recommended action
- D. The model confidence in its own diagnosis
