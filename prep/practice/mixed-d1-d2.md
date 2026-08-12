# Mixed Set — Domains 1 and 2 (15 questions)

**Purpose:** confirm Domains 1 and 2 before moving to Domain 3. Taken 12 August.

Weighted like the blueprint ratio between these two domains: **9 × Domain 1, 6 × Domain 2**.
Three questions ask for **two answers** — about one in five, matching the real exam.

All questions are new. None appear in `drill-domain-1.md` or `drill-domain-2.md`.

Several questions deliberately target the traps you have hit before: a rule that is really a
threshold, stopping at the first correct option on a select-two, and error categories decided by
feel. **The answer key is balanced** — A, B, C and D are each correct three times among the
twelve single-answer questions.

**The questions use exam-level English.** The explanations are in simple English.

Time: 30 minutes. Answers below — cover them while you work.

---

### Scenario: Customer Support Resolution Agent

**Q1.** A response from the API contains one text block ("Let me check both of those for you") and
two `tool_use` blocks; `stop_reason` is `"tool_use"`. Your loop terminates at this point and
returns the text to the customer, leaving both tool calls unexecuted. What is the correct control
flow?

A. Terminate the loop — a text block means the model has produced its final answer.
B. Add a system prompt instruction telling the model never to emit text alongside tool calls.
C. Branch on `stop_reason`: because it is `"tool_use"`, execute both tools and return both `tool_result` blocks to the model in a single user message.
D. Execute the two tools but discard the text block, since narration is not part of the protocol.

---

**Q2.** An MCP tool receives a request for a refund. The parameters are well-formed and the order
is inside the returns window, but the calling service's API key does not carry the `refunds:write`
scope. What should the tool return?

A. `errorCategory: "transient"`, `isRetryable: true` — the call may succeed once the key is refreshed.
B. `errorCategory: "validation"`, `isRetryable: false` — the request was rejected, so the input was not acceptable.
C. `errorCategory: "permission"`, `isRetryable: false`, with a description naming the missing scope.
D. `errorCategory: "business"`, `isRetryable: false` — a rule prevented the operation from completing.

---

**Q3.** Three MCP tools supply event data to your agent: one returns Unix timestamps, one returns
ISO 8601 strings, and one returns numeric status codes with an implicit date convention. The agent
regularly orders events wrongly when reasoning about a case timeline. What is the correct fix?

A. Implement a tool-call interception hook that rejects calls to tools returning non-ISO timestamps.
B. Document each tool's timestamp format in its description, so the model converts as it reasons.
C. Ask the three service owners to standardise on ISO 8601 before the agent ships.
D. Implement a `PostToolUse` hook that converts all three formats to one before the model reads the results.

---

**Q4.** A single `manage_account` MCP tool handles seven operations — address change, contact
update, plan change, suspension, reactivation, credit application, closure — selected through an
`action` enum. Logs show the agent regularly choosing the wrong action for the request. What is
the recommended redesign?

A. Document all seven actions more thoroughly inside the one tool description.
B. Reduce the enum to three actions by merging the closely related operations.
C. Add an eighth action that inspects the request and dispatches to the correct operation.
D. Split it into purpose-specific tools, each with its own defined input and output contract.

---

### Scenario: Multi-Agent Research System

**Q5.** Your multi-agent audit of a twelve-module service returns findings for ten modules. Review
of the run confirms every subagent completed its assigned work correctly and without error.
Separately, the subagent reports repeatedly refer to "the standards document" in ways that show
they never actually had its contents. Which two changes address these? **(Select two.)**

A. Widen the coordinator's task decomposition so every module is assigned — incomplete coverage with correctly-working agents points at the split, not the agents.
B. Increase each subagent's context window so it can examine more modules per invocation.
C. Have whichever subagent finishes first pick up the unassigned modules on its own initiative.
D. Include the standards content directly in each subagent's prompt — subagents inherit nothing from the coordinator automatically.

---

**Q6.** You have completed a thorough analysis of a payments module and now want to develop two
competing refactoring strategies independently, each starting from that same completed analysis,
without either exploration contaminating the other. Which mechanism fits?

A. Issue two Task calls in one response, so both strategies are explored in parallel.
B. Use `fork_session` to create two independent branches from the shared analysis baseline.
C. Run both strategies in one session, asking Claude to set aside the first before starting the second.
D. Use `--resume` twice against the same session name, once per strategy.

---

**Q7.** Your finished research reports are coherent and well-cited, but two or three subtopics are
consistently thin. You want the system to detect and repair its own coverage gaps before a report
is finalised. Which orchestration pattern achieves this?

A. Instruct the synthesis agent to write more thoroughly about every subtopic.
B. Run the whole pipeline twice and keep the longer of the two reports.
C. Add a loop counter so the pipeline always performs exactly three research rounds.
D. Have the coordinator evaluate the synthesis for coverage gaps, re-delegate targeted queries to the research subagents, and re-synthesise until coverage criteria are met.

---

**Q8.** Two problems appear in your loop implementation on the same day. The API begins rejecting
requests with an error about a `tool_use_id` that does not correspond to any pending call. And the
model has started re-requesting a tool it already called earlier in the same turn. Which two
corrections apply? **(Select two.)**

A. Increase `max_tokens`, so no tool result is truncated before the model reads it.
B. Return one `tool_result` for every `tool_use` block, each carrying the same `tool_use_id` as the call it answers.
C. Send all results belonging to one assistant message back in a single user message, rather than one message per result.
D. Add a system prompt instruction telling the model not to repeat tool calls it has already made.

---

**Q9.** Your subagents spend a substantial share of their tool calls establishing what data even
exists — listing available document collections, probing for issue summaries, checking which
schemas are present — before any real work starts. Which MCP capability reduces this?

A. Raise the per-subagent tool-call budget so the discovery phase is affordable.
B. Write the current data inventory into each subagent's system prompt.
C. Expose the content catalogues — collection hierarchies, schema listings, issue summaries — as MCP resources.
D. Add a `list_everything` tool that returns the full inventory whenever an agent asks for it.

---

### Scenario: Developer Productivity with Claude

**Q10.** Last week you ran a long session named `perf-audit` that analysed roughly forty files and
reached conclusions your team has since acted on. Since then three configuration files have
changed; the rest of the analysed code is untouched, and the conclusions remain valid. You want to
continue the work. What is the reliable approach?

A. Resume the session and tell it which three files changed, so it re-reads only those.
B. Start a new session seeded with a structured summary of the prior conclusions, since stale tool results make resumption unreliable.
C. Resume the session as-is; Claude re-reads any file whose modification time has changed.
D. Start a new session and re-run the full forty-file exploration from the beginning.

---

**Q11.** You must audit an unfamiliar 900-file service for authorisation flaws. Nobody on the team
can tell you where authorisation is enforced, which modules bypass it, or what depends on what.
Which decomposition approach fits?

A. Run one review pass per file, then a final pass across all files, which is the established pattern for large code reviews.
B. Map the codebase structure first, establish where authentication and authorisation actually live, then build a prioritised plan that adapts as dependencies surface.
C. Fix the sequence in advance: enumerate all 900 files, then process the list in dependency order.
D. Move to a model with a larger context window, so the whole service fits in a single pass.

---

**Q12.** A pull request touches a known, listed set of 22 files in one module, and the review
criteria are the same five aspects your team always checks. Your current single-prompt review
produces detailed findings for the first few files and increasingly thin findings after that.
Which approach is correct?

A. Prompt chaining: one focused pass per file for local issues, plus one additional pass across all files for cross-file data flow.
B. Dynamic decomposition, letting each finding determine which file is reviewed next.
C. A model with a larger context window, so attention is not spread thin across 22 files.
D. Three independent review runs, reporting only the findings that appear in at least two of them.

---

**Q13.** You need to find where your service handles rate limiting. There is no agreed name for it
in this codebase — you have seen `throttle`, `backoff` and `quota` used for related things in
different modules, and you do not know which identifier, if any, is the real one. Which search
approach fits?

A. Semantic search — the target is a concept, with no literal string you can spell to match against.
B. `Grep` for "rate limit", widening the pattern until something matches.
C. `Glob` for `**/*rate*limit*`, to locate the responsible files by name.
D. `Bash` running `find` piped to `xargs grep`, to cover both names and contents in one command.

---

**Q14.** An `Edit` call fails on a legacy file: the anchor text the agent targeted occurs five
times, so the unique-match requirement cannot be met. What is the standard fallback?

A. Retry the same `Edit`; the ambiguity usually resolves on a second attempt.
B. `Read` the full file, then `Write` the complete modified content back.
C. Use `Bash` with `sed` and an explicit line-number range to make the change.
D. Remove four of the five occurrences first, so the anchor becomes unique.

---

**Q15.** Two configuration problems surface in review. A live GitHub token is sitting in the
committed `.mcp.json`. And a teammate's experimental MCP server, which he added for his own
testing, is loading in every developer's session. Which two changes are correct? **(Select two.)**

A. Commit both servers to `.mcp.json` and document the required tokens in the team wiki.
B. Keep the shared server in project-scoped `.mcp.json`, but reference the credential with `${VAR}` expansion so no secret is committed.
C. Move both servers to `~/.claude.json`, so nothing sensitive is ever version-controlled.
D. Move the experimental server to user-scoped `~/.claude.json`, where personal servers stay with their owner.

---
---

# Answers

**Q1 — C** · Domain 1

The loop is controlled by `stop_reason`, and nothing else. `"tool_use"` means execute the tools and
return the results. Text and tool requests routinely appear together, so the presence of text
proves nothing about completion.

- **A** — "checking whether the response contains text" is one of the named wrong ways to stop.
- **B** — a prompt instruction papering over a broken mechanism. It also fights normal behaviour.
- **D** — right action, wrong reason, and it loses information. The text is legitimate; the loop
  continues because of `stop_reason`, not because the text was discarded.

**Q2 — C** · Domain 2

Run the four-way test in order. Did the system fail, and might a retry succeed? No. Is the input
malformed? No — the parameters are well-formed. Are the input and system both fine, but a rule
says no? Not a business rule — the *caller* lacks access. That is **permission**, and it is not
retriable.

- **A** — the trap. Nothing here is temporary; the same key will fail identically forever. "A
  refreshed key might work" describes a different request, not a retry of this one.
- **B** — validation means the *input* was malformed. This input was correct.
- **D** — the closest wrong answer. Business means the request is valid and permitted but a policy
  rule blocks the outcome (outside the returns window, over a limit). Here the request would have
  been allowed if the caller had the scope. The distinction: **business = the rule says no;
  permission = the caller may not ask.**

**Q3 — D** · Domain 2 · *(hook mechanics are Domain 1; the error surface is Domain 2)*

`PostToolUse` changes tool **results** before the model reads them. Normalising heterogeneous data
formats is the guide's named use for it — its own example is exactly Unix timestamps, ISO 8601 and
numeric status codes.

- **A** — interception hooks block outgoing **calls**. Wrong hook, and rejecting the calls loses
  the data instead of fixing it.
- **B** — asks the model to do the conversion reliably every time, which is the probabilistic
  approach to a problem with a deterministic fix.
- **C** — may be right long-term, but the agent has to work with the services as they are.

**Q4 — D** · Domain 2

The guide names this fix: replace one general tool driven by a mode or action parameter with
purpose-specific tools, each with a defined input/output contract. A hidden mode decision becomes
a visible tool-selection decision, which is what descriptions are good at guiding.

- **A** — better documentation of an ambiguous structure. The structure is the problem.
- **B** — fewer wrong choices available, same overloaded design.
- **C** — adds another selection decision to fix a selection problem.

**Q5 — A and D** · Domain 1

The scenario names **two distinct symptoms**, so the two answers map onto them — one each.
Symptom one: coverage is incomplete but every agent worked correctly, which always points at the
**coordinator's decomposition being too narrow**. Symptom two: subagents receive **nothing**
automatically, so the standards content must be in the prompt.

- **B** — no subagent ran out of context; two modules were never assigned to anyone.
- **C** — subagents cannot see the coordinator's plan or each other's work, so none of them knows
  a module is unassigned. All messages go through the coordinator.

*This is the shape you have missed three times: if you answered only A, re-read the symptom list.*

**Q6 — B** · Domain 1

`fork_session` exists for exactly this: independent branches from one shared starting point, so
both strategies inherit the completed analysis without re-paying for it or contaminating each
other.

- **A** — **the mechanism confusion to watch.** Parallel Task calls run *independent* work
  concurrently; they do not branch from a shared conversation state. This was your Set 1 Q8 miss.
- **C** — context cannot be selectively forgotten on request.
- **D** — `--resume` continues one session; it does not create two divergent branches.

**Q7 — D** · Domain 1

The iterative refinement loop: evaluate the output against coverage criteria, re-delegate targeted
follow-up work where gaps exist, re-synthesise, repeat until the criteria are met.

- **A** — "write more thoroughly" is a vague instruction with no gap detection behind it.
- **B** — length is not coverage, and it doubles the cost to pick by the wrong measure.
- **C** — a fixed round count is the loop-counter anti-pattern again: it does not aim the extra
  rounds at anything.

**Q8 — B and C** · Domain 1

Two symptoms, two rules, one each. Every `tool_use` block needs exactly one `tool_result` with
the **matching `tool_use_id`** (**B**) — that is what the API error is reporting. And all results
from one assistant message go back in **one** user message (**C**); splitting them across several
messages is what makes the model treat a call as unanswered and re-request it.

- **A** — `max_tokens` limits output length. It has nothing to do with result identity or
  batching.
- **D** — a prompt instruction for a protocol error. The model is re-requesting because it never
  received a proper answer, not because it forgot.

**Q9 — C** · Domain 2

MCP **resources** are for exposing content catalogues — document hierarchies, issue summaries,
schema listings — so agents start informed instead of probing. Discovery becomes a lookup.

- **A** — pays for the waste rather than removing it.
- **B** — goes stale the moment the data changes, and it is not maintainable across agents.
- **D** — the near-miss. Still a tool call per agent per session, still returns everything
  regardless of relevance. Resources are the named mechanism; a discovery tool is the thing
  resources replace.

**Q10 — A** · Domain 1

The question is **how much** is stale. Three known configuration files inside a forty-file
analysis is a small, identifiable delta, so **resume and name the changed files** — the agent
re-reads only those instead of exploring everything again.

- **B** — **the over-applied rule, and the mark this cost you on 10 August.** Starting fresh with
  a summary is right when *most* of the tool results describe code that no longer exists. Here
  37 of 40 files are unchanged, so discarding the session throws away valid context.
- **C** — no automatic re-verification happens. Stale results sit in context as though true.
- **D** — re-pays for the entire exploration to handle a three-file change.

**Q11 — B** · Domain 1

The task is open-ended, the structure is unknown, and each step depends on what the previous one
found. That is **dynamic decomposition**: map first, prioritise by risk, and let the plan change
as dependencies surface.

- **A** — **the trap, and the second half of your threshold problem.** One pass per file plus one
  across files is correct when you already know the file list and the review is predictable — see
  Q12. Here you do not know where the relevant code is, so a per-file sweep of 900 files spends
  the whole budget before finding the authorisation layer. The real question is: **do I know the
  shape of the work before I start?**
- **C** — a fixed sequence decided before anything is known about the codebase.
- **D** — bigger context does not improve attention quality. Permanent wrong answer.

**Q12 — A** · Domain 1

The contrast with Q11. Here the file list **is** known and the criteria are fixed, so prompt
chaining applies: one focused pass per file for local issues, plus one pass across all files for
what spans them. This is the fix for attention dilution.

- **B** — adaptivity overhead on work with no uncertainty in it.
- **C** — larger windows do not fix attention dilution. Permanent wrong answer.
- **D** — consensus voting suppresses real findings that are only caught intermittently. Also on
  the permanent wrong-answer list.

**Q13 — A** · Domain 2

The triad: **Glob** = file paths. **Grep** = text you can spell exactly. **Semantic** = a concept
with no literal to search for. Here the concept is rate limiting and you explicitly do not know
what it is called, so there is no string to match.

- **B** — `Grep` needs a literal you can spell. "Widening the pattern until something matches" is
  a description of not having one.
- **C** — `Glob` matches paths, and this codebase does not name the files after the concept.
- **D** — a brute-force pipeline standing in for both purpose-built tools, and it still needs a
  literal string to grep for.

**Q14 — B** · Domain 2

`Edit` requires a unique text match. When a file's repetition defeats that, `Read` the whole file
and `Write` the complete modified content — the documented fallback for this exact failure.

- **A** — a deterministic failure. Five matches will still be five matches.
- **C** — swaps a controlled file operation for fragile stream editing.
- **D** — modifies the code to suit the tool.

**Q15 — B and D** · Domain 2

Two symptoms, two fixes. The committed token: keep the shared server project-scoped in
`.mcp.json` but reference the credential through **`${VAR}` expansion**, so the repository holds
the variable name and never the secret (**B**). The imposed personal server: move it to
user-scoped **`~/.claude.json`**, which is not shared through version control (**D**).

- **A** — leaves the secret committed and adds a manual wiki step that drifts.
- **C** — the plausible over-correction. Moving the *shared* server to user scope un-shares team
  infrastructure, so every developer configures it by hand. Scope follows audience: shared tools
  project-scoped, personal tools user-scoped.

---

## Score

___ / 15 · Q5, Q8 and Q15 need two answers each. You need both for the point.

**By domain:** Domain 1 ___ / 9 (Q1, Q5, Q6, Q7, Q8, Q10, Q11, Q12 — and Q3's hook mechanism)
· Domain 2 ___ / 6 (Q2, Q3, Q4, Q9, Q13, Q14, Q15)

### The traps this set was built to test

| Weak point | Question | What a miss means |
|---|---|---|
| Rule stored where the guide has a **threshold** | **Q10** (resume) and **Q11 vs Q12** (decomposition) | The rule is memorised, the qualifier is not. Ask "how much?" and "do I know the shape?" |
| Stopping at the first correct option on select-two | **Q5**, **Q8**, **Q15** | Two named symptoms means two answers. Count the symptoms before you answer |
| Error categories by feel | **Q2** | Run the four-way test in order. Business = the rule says no; permission = the caller may not ask |
| Mechanism confusion | **Q6** | `fork_session` branches shared state; parallel Task calls run independent work |
| Grep / Glob / semantic | **Q13** | If the question prints the string, it is Grep. If there is no string, it is semantic |

### What to do next

- **13 or more, with both Q11 and Q12 right** — Domains 1 and 2 are confirmed. Move to Domain 3.
- **10–12** — check whether the misses are threshold questions (Q10, Q11, Q12) or flat facts. If
  threshold: re-read those three explanations and move on, they are the same lesson three times.
  If flat facts: put each on the cheat sheet before starting Domain 3.
- **Below 10** — do not move on yet. Re-read the quick review lists at the end of
  `notes/domain-1-agentic-architecture.md` and `notes/domain-2-tool-design-mcp.md`, then retake.
