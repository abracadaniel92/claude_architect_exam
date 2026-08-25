# Mock 9 — Full-length exam simulation, heuristic-proof paper (60 questions)

**Take this timed and cold.**

| | |
|---|---|
| Questions | 60 |
| Time | 120 minutes |
| Format | 4 scenarios × 15 questions, as on the real exam |
| Multiple-response | 10 questions, each marked **(Select two.)** |
| Working pass mark | 43 / 60 |
| Answer key | `mock-09-answers.md` |

Domain spread: D1 16 · D2 11 · D3 12 · D4 12 · D5 9 (the blueprint weighting).

**What is different about this paper.**

Mock 8 inverted the length tell — the correct answer was the shortest option on 28 of 50 singles.
That is its own pattern, and a pattern can be learned. **Here neither heuristic is safe.** The
correct answer is the longest option on roughly a third of the singles, the shortest on roughly a
third, and somewhere in the middle on the rest, with no relationship to domain, scenario or
position. Embedded rationale ("…since X degrades Y") appears in right and wrong answers at about
the same rate. Judge the content; option shape carries no information on this paper.

Also, as on Mock 8: written from the blueprint objectives and domain notes, key balanced by letter
(A 12 · B 13 · C 13 · D 12 across the singles, each letter 5× across the ten select-twos), no
positional rotation.

**One deliberate condition.** Somewhere in this paper there is a run of unusually dense stems. It is
not marked. Three consecutive papers have lost a question that was never seen, so:

1. **Take a two-minute break, eyes off the screen, somewhere around the halfway mark.** You will have
   spent perhaps ten minutes by then out of 120. It costs nothing.
2. **Before you check the key, count your answers.** Sixty questions, sixty answers, and two letters
   on each of the ten select-twos. A blank is a guaranteed lost mark; a guess is not.

Every question is self-contained. The scenario paragraph is background only.

---

## Scenario A — Calderwood Rail (Developer Productivity with Claude)

*Calderwood Rail runs a scheduling and signalling platform first written in the 1990s and extended
ever since. Engineers new to it use a Claude Code agent with Read, Write, Edit, Bash, Grep and Glob,
plus MCP servers for the ticket tracker and the internal wiki, to find their way around roughly
4,000 source files.*

**1.** An engineer needs every file in the repository whose path matches the interlocking-test naming
convention, `**/*.interlock.spec.ts`. Which capability?

- A. `Grep`, which accepts a filename pattern as readily as a content pattern
- B. Semantic search, since a naming convention encodes a concept rather than a literal string
- C. `Glob`
- D. `Read` on each test directory in turn, since the convention is confined to a few places

**2.** They also need every place the error constant `SIGNAL_LOCK_TIMEOUT` is referenced anywhere in
the codebase, including comments and test fixtures.

- A. `Grep` for `SIGNAL_LOCK_TIMEOUT`
- B. `Glob` for `**/*signal*`, then read the matches
- C. Semantic search for signal-lock timeout handling
- D. `Bash` running `cat` across the tree and inspecting the output by eye

**3.** A third engineer is looking for whatever decides how a train is re-platformed when its booked
platform is occupied. It may be called re-platforming, reallocation or stand-swap; the team is not
sure, the original authors have retired, and none of those words appears in any file anyone has
opened so far.

- A. `Grep` for `replatform`, then `reallocation`, then `stand-swap`, in that order
- B. `Glob` on `**/*platform*`, widening the pattern until something matches
- C. `Grep` with a case-insensitive alternation of all three candidate terms at once
- D. Semantic search

**4.** The agent attempts an `Edit` on a configuration block and fails: the anchor text it targeted
appears in eleven places in the file, so the unique-match requirement cannot be met. What is the
standard fallback?

- A. Retry the `Edit` with a progressively shorter match string until one of them resolves uniquely
- B. `Read` the file and `Write` it back with the change applied
- C. Delete ten of the eleven occurrences so that the remaining match becomes unique
- D. Switch to `Bash` and apply the change with `sed`, which does not require a unique anchor

**5.** Asked how the timetable-conflict module works, the agent reads forty files up front and
exhausts its context before answering anything. What is the correct exploration strategy?

- A. Read the module's files in alphabetical order and stop when the context limit is reached
- B. Read only the module's README and reason from the documentation it contains
- C. `Grep` to find entry points — key functions, imports, error strings — then `Read` selectively
  along the paths those anchors reveal
- D. Ask the engineer who owns the module to explain it before any files are opened

**6.** The team shares a ticket-tracker MCP server that needs an API token, and one engineer runs a
personal experimental server against a scratch database nobody else can reach. Which two
configuration choices are correct? **(Select two.)**

- A. Both servers in `.mcp.json`, with the token written in directly so teammates need not set
  anything up
- B. The shared server in `.mcp.json`, using `${VAR}` expansion so the token is never committed
- C. Both servers in `~/.claude.json`, with setup instructions kept in the team wiki
- D. The personal server in `~/.claude.json`

**7.** Two tasks arrive on the same morning: correcting an off-by-one in a single dwell-time function
with a clear stack trace, and splitting the monolithic scheduling service into three, which touches
around 60 files and has several viable shapes. How should plan mode and direct execution be
assigned?

- A. Direct execution for the dwell-time fix; plan mode for the service split
- B. Plan mode for both, since planning never makes an outcome worse
- C. Plan mode for the dwell-time fix; direct execution for the service split
- D. Direct execution for both, since plan mode is intended for greenfield work rather than changes
  to an existing system

**8.** An engineer cannot understand why a convention about fixture naming is being applied inside a
service where it should not apply. What tells them which memory files the session has loaded?

- A. Reading each CLAUDE.md by hand, working upward from the edited file to the repository root
- B. `--verbose`, which prints configuration resolution alongside the session output
- C. `/context`
- D. `/memory`

**9.** The team wants a `/trace-signal` command that every engineer gets automatically when they clone
the repository. Where does the command file belong?

- A. `~/.claude/commands/trace-signal.md`
- B. `.claude/commands/trace-signal.md`
- C. The root CLAUDE.md, documented under a commands heading
- D. `.claude/rules/trace-signal.md`, with a `paths:` glob covering the signalling folder

**10.** A new engineer's sessions ignore the team's conventions entirely. It turns out the conventions
live in the tech lead's `~/.claude/CLAUDE.md`. What is the correct fix?

- A. Have the new engineer reinstall Claude Code so that configuration is re-resolved from scratch
- B. Send the new engineer the lead's file to copy into their own home directory
- C. Move the conventions into the project-level CLAUDE.md, which is checked in and therefore reaches
  every clone
- D. Paste the conventions at the start of each session until the new engineer has absorbed them

**11.** A programme of work is agreed: "find and remove every remaining use of the deprecated
timetable API." Nobody knows how many call sites there are, where they concentrate, or what depends
on them. Which decomposition approach fits?

- A. Map the codebase first, identify where the uses concentrate, then plan the passes from what the
  map shows, adapting as dependencies surface
- B. Prompt chaining — one pass per file across all 4,000, then one pass across files
- C. A single request containing the deprecated API's definition and a list of every source file
- D. One subagent per top-level directory, each deciding for itself what falls in scope

**12.** After a thorough analysis of the conflict-resolution engine, the team wants to develop two
competing redesigns independently, both starting from that same analysis, without paying to
re-derive it and without either exploration contaminating the other.

- A. Two sessions started fresh, each repeating the analysis before diverging
- B. `/compact` between the first redesign and the second, in one session
- C. One session asked to hold both redesigns apart and report them separately at the end
- D. `fork_session`

**13.** An engineer returns to a session from six weeks ago. Since then the build system has been
replaced, two of the three modules under discussion have been merged, and the ticket has been
rewritten. What should they do?

- A. `--resume` the session and enumerate everything that has changed since it was last open
- B. Start a new session, seeded with a written summary of where the work now stands
- C. `--resume` the session and then `/compact`, so the stale material is dropped from context
- D. `fork_session`, keeping the six-week-old context available for comparison

**14.** In multi-hour exploration sessions the agent has started answering from "the usual pattern for
systems of this age" rather than from the specific classes it found earlier in the same session.
What counteracts this?

- A. Ask the agent to be more specific and to name the classes it is describing
- B. Switch to a model with a larger context window and continue accumulating as before
- C. Record key findings in a scratchpad file as they are discovered, and have the agent read back
  from it
- D. Repeat the important question a second time within the same message

**15.** A three-day migration run ended when the build machine restarted, and the work had to begin
again from the beginning. What prevents a repeat?

- A. `--resume` on the migration session
- B. A longer context window, so less state is held outside the session
- C. Manifests written as each unit of work completes, loaded when the run resumes
- D. Checkpointing the agent's draft output after every file it touches

---

## Scenario B — Brightwell Financial (Claude Code for Continuous Integration)

*Brightwell Financial runs Claude Code inside its CI pipeline across nineteen services: reviewing
every pull request, generating missing unit tests, and posting a machine-readable summary that a
merge gate consumes. Pull requests average 12 changed files, and the platform team is judged on
whether developers trust the feedback.*

**16.** The review step hangs until the job timeout kills it. What does the invocation need?

- A. `--json-schema`, so the step knows what shape of output to wait for
- B. `--resume`, so the step attaches to an existing session rather than opening a new one
- C. `-p` (`--print`)
- D. A shorter prompt, since the step is timing out on generation rather than on input

**17.** The merge gate needs the review summary to carry the same fields on every run — file, line,
severity, suggested fix — so that it can fail the build on any critical finding. What guarantees
that shape?

- A. `--output-format json` on its own, which is sufficient because JSON is inherently structured
- B. `--output-format json` together with `--json-schema` describing the fields the gate expects
- C. Asking for the fields in the prompt, then validating the result with a shell script afterwards
- D. A `schema:` key in the workflow file, listing the fields the gate requires

**18.** A draft runbook lists four ways of running Claude Code non-interactively. Which two do not
exist? **(Select two.)**

- A. `--no-interactive`
- B. `-p` / `--print`
- C. `CLAUDE_HEADLESS=true` as a workflow environment variable
- D. `--output-format json`

**19.** Generated tests are low-value — exercising getters, asserting framework behaviour — and they
ignore the team's fixture library entirely. What is the configuration-level fix?

- A. Generate three times as many tests, so that enough survive review to be worth having
- B. Lower the temperature on the generation call, so output varies less between runs
- C. Have developers rewrite the generated tests as a standing part of the review workload
- D. Document the testing standards, what makes a test worth having, and the available fixtures in
  CLAUDE.md

**20.** The review re-runs on every new commit and re-posts findings the developer has already read
and acted on. Developers have started muting it. How should re-reviews be designed?

- A. Include the previous review's findings in context and ask for only new issues, plus any earlier
  ones still unaddressed
- B. Review only the most recent commit's diff, in isolation from what came before it
- C. Run the review once per pull request and ignore subsequent commits
- D. Post the findings again in a different format, so they do not read as repetition

**21.** The pipeline also proposes tests for behaviour the existing suite already covers. What stops
that?

- A. Add an instruction to the prompt telling it not to duplicate tests that already exist
- B. Supply the existing test files for the module under review
- C. Run the suite first and pass the resulting coverage percentage into the prompt
- D. Request fewer tests per run and have a reviewer delete whatever duplicates remain

**22.** The review prompt currently says "be conservative and report only findings you are confident
about," and false positives remain high enough that developers skim past them. What does effective
precision engineering look like instead?

- A. Strengthen the wording to "be extremely conservative", so the instruction carries more weight
- B. Report everything but sort the output by the model's own stated confidence, so the strongest
  findings appear first and the weak ones can be ignored in place
- C. Reduce the number of files reviewed per run, so that each one receives more attention
- D. Replace the confidence language with explicit categorical criteria: which issue types to report,
  which to skip, and where the boundary between them falls

**23.** Findings in the "possible resource leak" category are wrong about 70% of the time they fire,
and developers have begun dismissing the SQL-injection findings too, which are accurate. What is the
right operational move?

- A. Ship more resource-leak findings, so developers come to understand the category's importance
- B. Ask developers to tolerate the noise while the category is being tuned over the next quarter
- C. Turn the resource-leak category off, keep the accurate categories running, fix its prompt, and
  re-enable it once it is behaving
- D. Rename the category to something broader, so its findings read as advisory rather than definite

**24.** The reviewer labels near-identical defects "critical" on one run and "minor" on the next, so
the severity-based merge gate cannot be relied on. How is consistent classification achieved?

- A. Define each severity level in the prompt with concrete code examples
- B. Remove severity levels altogether and treat every finding as equally actionable
- C. Let the model assign severity freely, then average the label across five independent runs
- D. Derive severity mechanically from the number of lines the finding touches

**25.** The pipeline sometimes has the same session that generated a change also review it, and defects
that session introduced pass review unremarked. Why, and what follows?

- A. The model is being agreeable, and the review prompt should instruct it to adopt a harsher stance
- B. A session carries the reasoning that produced the code, which biases it against questioning its
  own choices — so reviews should run in an independent instance without the generating context
- C. Review quality depends on model tier, and the review step should be moved to a larger model
- D. Generation and review should be separated in time, so that the review runs against a codebase
  the pipeline has had a chance to settle

**26.** A platform engineer proposes running each review three times and reporting only findings that
appear in at least two of the three runs, to cut false positives. What is wrong with this?

- A. Nothing — majority agreement across runs is the standard way to raise precision
- B. It triples the cost of every review for a marginal gain in the false-positive rate
- C. It requires the three runs to use different prompts, which the pipeline cannot currently express
- D. Voting across runs suppresses real defects, because a genuine bug found on only one run is
  discarded exactly like a false positive

**27.** Brightwell is deciding which CI workloads to move to the Message Batches API. Which two
statements are accurate? **(Select two.)**

- A. Results are returned within a guaranteed window, which is what makes scheduling around them
  possible
- B. Nightly test generation and the weekly dependency audit suit it, since nobody is waiting on the
  result
- C. Pre-merge checks should stay on the synchronous API, because a batch may take up to 24 hours and
  carries no latency guarantee
- D. Multi-turn tool calling within a single request is supported, which is what makes iterative
  review viable in batch

**28.** The team is adding few-shot examples to the review prompt. Which two practices reflect how
few-shot prompting actually works? **(Select two.)**

- A. Use two to four examples, aimed at the cases where the correct call is genuinely unclear
- B. Use fifteen to twenty examples, so that every category in the scheme is represented at least
  twice and the model has seen the full range
- C. Once worked examples are in place, the explicit criteria can be removed, since the examples
  carry the same information in a form the model follows more reliably
- D. Include examples that demonstrate the exact output shape wanted — location, issue, severity,
  suggested fix

**29.** A release branch changes 34 files. The list is known before the work begins and the review
criteria are fixed. Which approach?

- A. Prompt chaining — one pass per file, then one pass across all files for issues that only appear
  between them
- B. Dynamic decomposition — map the branch first, then plan the passes from what the map shows
- C. A single pass over the entire diff, using the largest context window available
- D. One subagent per service touched, each deciding independently what is worth reporting

**30.** One of the nineteen services was unreachable for most of the nightly run, so the morning
quality report rests on eighteen services rather than nineteen. What must the report do?

- A. Retry the unreachable service until it responds, and delay the report until it does
- B. Compress the affected sections, so that the thinner coverage is less conspicuous to readers
- C. Record the outage in the pipeline's own logs and publish the report on its normal schedule
- D. State which findings are well supported and which areas have coverage gaps

---

## Scenario C — Aldergate Policy Institute (Multi-Agent Research System)

*Aldergate Policy Institute produces evidence reviews for government departments. A coordinator plans
each review; subagents search academic databases, read parliamentary records, read statistical
releases and read stakeholder submissions; a synthesis agent writes the final review with full
citation. Reviews run for weeks and draw on thousands of documents.*

**31.** The coordinator's system prompt instructs it to delegate, but at runtime it never spawns a
subagent — it reads everything itself and exhausts its context. Its configuration restricts it to
planning tools. What is the most likely cause?

- A. Subagents must be registered in `.mcp.json` before a coordinator can reach them
- B. The coordinator's `allowedTools` does not include `"Task"`
- C. The coordinator's model tier is too small to represent a delegation strategy reliably
- D. Subagents must be started as separate processes before the coordinator run begins

**32.** The statistical-releases subagent returns work that ignores the review's date range, the
jurisdictions in scope and the department's stated question — all of which the coordinator had.

- A. The coordinator's context was compacted before the subagent had a chance to read it
- B. The subagent should have queried the coordinator for the constraints it was missing
- C. Subagents do not inherit the coordinator's conversation — the constraints must be written into
  the Task prompt
- D. Subagents read the coordinator's context only within the turn that spawned them

**33.** Four subagents currently run one after another and each review takes far longer than it should.
Their tasks do not depend on one another. How are they made to run concurrently?

- A. Emit all four Task calls in a single coordinator response
- B. Set `parallel: true` in each subagent's AgentDefinition
- C. Emit the four Task calls across four consecutive coordinator turns
- D. Raise the concurrency limit in the project configuration file

**34.** A review commissioned to cover four policy areas comes back strong on three and almost silent
on the fourth. Every subagent completed, none reported an error, and each returned work consistent
with the brief it was given.

- A. The synthesis agent lost the fourth area while compressing material for the final document
- B. The fourth subagent silently truncated when it reached its context limit
- C. The subagents had no shared scratchpad and so could not see one another's coverage
- D. The coordinator divided the work too narrowly, and the fourth area fell outside every brief

**35.** Subagent prompts set out an exact sequence of steps. When a step turns out not to apply — a
jurisdiction with no equivalent statistical release, say — the subagent stops and reports the step as
blocked rather than continuing. How should the prompts be written instead?

- A. Extend the sequence with a documented branch for every jurisdiction the institute covers
- B. State the research goal and what a complete answer looks like, and let the subagent choose how to
  get there
- C. Append a final step instructing the subagent to skip any step that does not apply to its case
- D. Move the sequence into the coordinator, which then issues one step at a time and waits

**36.** Completed reviews read coherently but are thin in places, and the institute wants the system to
find and repair its own coverage gaps before a review is signed off. Which orchestration pattern?

- A. Have the coordinator assess the synthesis for gaps, re-delegate targeted follow-up research where
  it finds them, and re-synthesise until coverage meets the criteria
- B. Run every subagent twice on every review, so thin sections get a second pass regardless
- C. Have the synthesis agent fill thin sections from its own background knowledge of the policy area
- D. Accept the first synthesis, on the basis that a researcher can patch thin sections more cheaply
  than the system can

**37.** Mid-review, a response comes back with `stop_reason: "refusal"`. What should the orchestration
loop do?

- A. Continue, since `stop_reason` is not `end_turn` and the review is plainly unfinished
- B. Continue, rephrasing the same request in case the wording caused the refusal
- C. Stop — the loop continues only on `tool_use`
- D. Continue, treating `refusal` the same way the loop treats `max_tokens`

**38.** In a single turn the coordinator calls four tools. The following request to the API is rejected
as malformed. What does a correct implementation send back?

- A. Four separate user messages, one per result, ordered as the tools were called
- B. One assistant message containing all four results
- C. One user message containing a single `tool_result` block that lists all four outputs in order
- D. One user message containing four `tool_result` blocks, each carrying its matching `tool_use_id`

**39.** Two subagents have independently queried the same statistical release and reached different
readings of it, and neither is aware of the other. Which two statements about the architecture are
true? **(Select two.)**

- A. Subagents cannot communicate with one another; every message passes through the coordinator
- B. Subagents share a working memory by default, so the duplication indicates a configuration fault
- C. Each subagent's AgentDefinition carries its own description, system prompt and tool restrictions
- D. Subagent tool restrictions are advisory, and a subagent may exceed them when its task requires it

**40.** Every subagent currently receives the institute's full catalogue of 22 tools. Logs show the
synthesis agent running database searches and the parliamentary-records agent attempting statistical
analysis, with wrong-tool selections throughout. What is the correct redesign?

- A. Add a further tool whose role is to advise each agent which of the 22 it should be using
- B. Scope each subagent's tool set to its role, giving each one only the handful it needs
- C. Write longer system prompts, naming for each agent the tools it must not touch
- D. Present the catalogue in a fixed order, with each agent's most relevant tools listed first

**41.** An academic database returns a 502 partway through a subagent's query, and the team is
specifying the correct behaviour. Which two are right? **(Select two.)**

- A. Treat it as a business error and halt the review, since the evidence base is now incomplete
- B. Have the subagent retry it itself, and pass upward only what it cannot resolve — with what was
  attempted and any partial results
- C. Return an empty result set marked successful, so that the remainder of the review proceeds
- D. Categorise it as transient, with `isRetryable: true`

**42.** Subagents spend a substantial share of every review's tool budget simply establishing what
exists — which databases are indexed, which record types are held, what fields each one carries —
before any research begins. What removes that?

- A. Expose the catalogues as MCP resources
- B. Provide a tool that enumerates everything available, called once at the start of each review
- C. Describe the corpus in prose in each subagent's system prompt, revised whenever it changes
- D. Cache the discovery calls, so that repeats after the first review are inexpensive

**43.** Final reviews state their findings but cite nothing. Each summarisation step compresses the
attribution away, so by the time synthesis runs, nobody can say which claim came from where.

- A. Have the synthesis agent add citations at the end, matching claims to the most likely source
- B. Reduce the pipeline to a single summarisation step, so less attribution is lost on the way
- C. Require subagents to emit structured claim-source mappings — claim, evidence excerpt, source —
  that every downstream agent preserves and merges
- D. Note in the review that full sourcing is available from the research team on request

**44.** Two statistical releases give different figures for the same population measure, and one
subagent's summary simply reported the larger. Which two practices produce correct handling?
**(Select two.)**

- A. Record both figures, each with its source, and surface the disagreement rather than resolving it
  silently
- B. Adopt the more recent figure and set the older one aside as superseded
- C. Present the mean of the two, with the range noted alongside it
- D. Require publication or collection dates in subagent output, so that figures measuring different
  moments are not mistaken for a contradiction

**45.** A subagent assigned 200 stakeholder submissions could retrieve only 130 before its access
window closed. What should it return?

- A. Nothing, holding the task open until the remaining 70 can be retrieved
- B. The findings from the 130 it did retrieve, explicitly marked as partial
- C. A successful result with an empty finding set, since the assignment was not completed as briefed
- D. A hard error that halts the review, since an incomplete evidence base cannot be synthesised

---

## Scenario D — Oakhill Property (Structured Data Extraction)

*Oakhill Property runs residential conveyancing at volume. A Claude-based pipeline extracts structured
records from title registers, local-authority searches, lease documents and survey reports — arriving
as PDFs, scans and email attachments from several hundred firms. Around 8,000 documents are processed
each night, alongside a small same-day queue where a conveyancer is waiting.*

**46.** The pipeline prompt asks for the property record "as JSON in your reply". Around 5% of responses
cannot be parsed, and the failures follow no discernible pattern.

- A. Declare the record as a tool input schema and return it through tool use
- B. Add further worked examples of well-formed JSON to the prompt, drawn from the layouts that fail
  most often in production
- C. Repair the malformed output downstream with a parser that tolerates fences, trailing commas and
  prose before the opening brace
- D. Set temperature to zero, so that formatting stops varying between otherwise identical requests

**47.** Leases contain a ground-rent review clause only where the lease actually provides for one, and a
clear majority do not. The field is currently required, and the model is producing plausible review
clauses for leases that contain none.

- A. Keep it required and instruct the model to leave the field empty when no clause is present
- B. Keep it required, and reject any clause whose wording does not appear verbatim in the source
- C. Make the field optional and nullable
- D. Keep it required, using an enum whose permitted values include `no_review_clause`

**48.** Two further problems. Defect categories on survey reports keep growing as new construction types
appear, and unfamiliar defects are being forced into the closest existing category. Separately, some
survey reports describe a condition in terms that could reasonably be read two ways, and the model is
picking one reading and discarding the ambiguity.

- A. Raise the temperature, so the model stops collapsing onto the categories it has seen most
- B. An enum with an `"other"` value and a free-text detail field, plus an `"unclear"` value for
  genuinely ambiguous readings
- C. A confidence score on the category field, so ambiguous cases can be filtered downstream
- D. A post-extraction reviewer that re-reads any report whose category was assigned with low certainty

**49.** An extraction fails validation with three named field errors. The team resends the document, the
failed extraction and the specific errors. Which failure will that retry **not** fix?

- A. Two date fields returned in the wrong structure
- B. A tenure value returned as free text where the schema declares an enum
- C. A field populated from the wrong section of an otherwise well-formed document
- D. A completion date that does not appear anywhere in the document supplied

**50.** The overnight run of 8,000 documents completes with 240 failures — mostly oversized lease
bundles that exceeded context limits, plus a handful of transient errors.

- A. Identify the failures by `custom_id` and resubmit only those, chunking the oversized bundles first
- B. Resubmit all 8,000, so that the whole night's output is produced under identical conditions
- C. Write off the 240 as an acceptable loss at this volume and process them by hand
- D. Move the 240 to the synchronous API unchanged, where the context ceiling does not apply

**51.** Two rules must hold on every matter without exception: no completion may be registered by the
pipeline where the local-authority search is more than six months old, and the client's identity must
be verified before any funds instruction is generated. Which two changes guarantee this?
**(Select two.)**

- A. A system prompt stating both rules and repeating them at the head of every turn
- B. A `PreToolUse` hook that blocks the registration call when the search date is out of range
- C. A prerequisite gate that fails the funds-instruction call until identity verification has returned
- D. Worked examples showing an out-of-date search being referred rather than registered

**52.** A quarterly compliance exercise checks a known list of 40 completed matters against a fixed
schedule of twelve regulatory criteria.

- A. Dynamic decomposition, since compliance work of this scope cannot be planned reliably in advance
- B. One subagent per criterion, each working through all 40 matters on its own
- C. Prompt chaining — one pass per matter, then one pass across all of them
- D. A single request holding all 40 matters and the full schedule of criteria together

**53.** Four search providers return local-authority results in four different shapes, and the model
misreads them roughly one time in six. The team wants a single consistent shape reaching the model.

- A. A `PostToolUse` hook that normalises each result before the model reads it
- B. A `PreToolUse` hook that rewrites the outgoing call so every provider responds identically
- C. A system-prompt section setting out all four shapes and how each should be interpreted
- D. Four separate tools, one per provider, each documenting the shape that provider returns

**54.** A call to the land-registry API is rejected because the service account it uses holds read scope
only and the pipeline attempted a write. The API is healthy and the request was well formed.

- A. `business`, since write access is restricted by the institute's own policy
- B. `validation`, since the request was missing a credential it required
- C. `transient`, with `isRetryable: true`, since scopes are periodically refreshed
- D. `permission`, with `isRetryable: false`

**55.** A single `matter_operations` tool takes an `action` parameter with eight values — `open`,
`search`, `exchange`, `complete` and four more — and the model routinely selects the wrong one.

- A. Document each action more fully within the single tool description, with an example of each
- B. Split it into purpose-specific tools, each with its own input contract
- C. Consolidate the eight actions into three broader ones, reducing the scope for error
- D. Add an `action_hint` parameter that the calling code sets before the model chooses

**56.** Two things need a home. The firm's universal data-handling standards must shape every session
without exception, and a month-end reconciliation workflow is run a handful of times each period.

- A. Standards in CLAUDE.md, which is always loaded; the reconciliation workflow as a skill, invoked
  when it is needed
- B. Both as skills, so that each is invoked deliberately rather than loaded by default
- C. Both in CLAUDE.md, so that neither can be overlooked at the moment it matters
- D. Standards as a skill; the reconciliation workflow in CLAUDE.md

**57.** A title-analysis skill has two problems: it emits several thousand lines of intermediate
reasoning that crowd out everything after it, and last month it wrote to a matter file when it was
only ever meant to read. Which two frontmatter changes fix this? **(Select two.)**

- A. `paths:`, restricting the skill to the title documents it analyses
- B. `argument-hint`, so the conveyancer states the matter reference before it runs
- C. `allowed-tools`, limited to the read operations the analysis requires
- D. `context: fork`, so the skill runs in its own context

**58.** Extraction accuracy averages 96% across all document types, and the operations director wants to
stop reviewing anything the model marks high-confidence. Which two checks must come first?
**(Select two.)**

- A. A stratified random sample of the high-confidence extractions, reviewed by hand on an ongoing
  basis
- B. Accuracy segmented by document type and by field, rather than reported as one figure
- C. A full manual review of everything the model marked low-confidence
- D. A second extraction pass across the corpus, retaining only records where both passes agree

**59.** Field-level confidence scores have been added, and the team intends to use them to decide which
records reach a human. When is that legitimate?

- A. Immediately, given that the model has read the document and is well placed to judge its own
  certainty field by field
- B. Once the scores have been calibrated against a labelled set
- C. Once the scores are averaged to the document level, per-field values being too volatile to act on
- D. Once the scores have been weighted by document length, which tracks extraction difficulty across
  this corpus

**60.** Each local-authority search result returns 60-odd fields, of which the pipeline uses seven, and
the context fills after a handful of matters. What is the fix?

- A. Instruct the model to disregard the fields that are not relevant to the matter in hand
- B. Summarise the accumulated tool results once the context approaches its limit
- C. Call the search tool less frequently, reasoning further between calls
- D. Trim each result to the seven fields before it enters the context
