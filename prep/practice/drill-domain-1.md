# Domain 1 Drill — Agentic Architecture & Orchestration (15 questions)

The biggest domain: **27%** of the exam, about **16 of 60 questions**.

This drill is harder than Set 1 on purpose. Several questions have two answers that both look
correct. The difference is usually one phrase in the question text.

**The questions use exam-level English.** The explanations are in simple English.

Time: 30 minutes. Answers at the bottom — cover them while you work.

---

**Q1.** Your agentic loop is implemented as:

```
for i in range(10):
    response = call_claude(messages)
    if "I have completed" in response_text:
        break
    execute_tools_and_append(response)
```

Production logs show two failure classes: the loop sometimes exits while the agent still has
pending tool calls, and sometimes runs all 10 iterations on tasks that finished at iteration 3.
Which change fixes both?

A. Raise the iteration cap to 25 and add more completion phrases to the text check.
B. Branch on `stop_reason`: continue while it is `"tool_use"`, terminate when it is `"end_turn"`.
C. Have the model call an explicit `task_complete` tool, and break when that tool is called.
D. Check whether the response contains any text content blocks; if so, treat the turn as complete.

---

**Q2.** A coordinator agent spawns a synthesis subagent with the prompt: "Synthesize the
research findings into a report." The synthesis subagent responds asking what findings it
should synthesize. What is the cause?

A. The coordinator's `allowedTools` is missing `"Task"`.
B. Subagents operate with isolated context and do not inherit the coordinator's conversation history; the findings must be included explicitly in the subagent's prompt.
C. The synthesis subagent's AgentDefinition system prompt does not describe its role clearly enough.
D. The coordinator needs to invoke the synthesis subagent with `fork_session` so it inherits the analysis baseline.

---

**Q3.** Your refund policy states that refunds over $500 require manager approval. You add to
the system prompt: "IMPORTANT: You must never process a refund over $500. Always escalate
these to a human." In a 5,000-conversation audit, 11 refunds over $500 were processed. What
is the correct remediation?

A. Strengthen the instruction with explicit examples of over-threshold refunds being escalated.
B. Move the threshold check into the `process_refund` tool's input validation, returning a business error.
C. Implement a tool-call interception hook that blocks the call when the amount exceeds $500 and redirects to the escalation workflow.
D. Lower the effective threshold in the prompt to $400 to create a safety margin.

---

**Q4.** Your research coordinator produces reports on "renewable energy adoption" that cover
solar comprehensively and barely mention wind, hydro, or geothermal. Logs show three subtasks:
"solar panel efficiency trends," "residential solar adoption rates," "solar policy incentives."
Each subagent returned high-quality results. Which two changes address the root cause?
**(Select two.)**

A. Design the coordinator to analyze query requirements and dynamically select subagents rather than always routing through a fixed pipeline.
B. Partition research scope across subagents by assigning distinct subtopics, minimizing duplication and maximizing coverage.
C. Implement an iterative refinement loop where the coordinator evaluates synthesis output for gaps and re-delegates with targeted queries.
D. Instruct the synthesis subagent to flag topic areas that appear underrepresented in the findings it receives.

---

**Q5.** You need to compare two refactoring strategies for the same module, both starting from
an expensive codebase analysis you've already completed in the current session. What mechanism
is designed for this?

A. `--resume <session-name>` twice, once per strategy.
B. `fork_session`, creating independent branches from the shared analysis baseline.
C. Two Task tool calls emitted in a single response, one per strategy.
D. `/compact`, then start each strategy as a fresh session with the compacted summary.

---

**Q6.** Your MCP tools return timestamps in three formats: `order_service` uses Unix epoch
seconds, `billing_service` uses ISO 8601, and `legacy_crm` uses a numeric status code plus a
separate date string. The agent frequently miscalculates date differences across services.
What is the appropriate fix?

A. A `PostToolUse` hook that normalizes the heterogeneous formats before the model processes the results.
B. A system prompt section documenting each service's timestamp format and conversion rules.
C. Few-shot examples demonstrating correct date arithmetic for each format.
D. A tool-call interception hook that rewrites requests to ask each service for ISO 8601.

---

**Q7.** You are automating "add comprehensive test coverage to a legacy billing module." You do
not know the module's structure, which paths are highest-risk, or what the dependency graph
looks like. Which decomposition strategy fits?

A. Prompt chaining: a fixed pipeline that analyzes each file, generates tests, then runs a coverage check.
B. Dynamic adaptive decomposition: map the structure, identify high-impact areas, then build a prioritized plan that adapts as dependencies are discovered.
C. Per-file local passes plus a separate cross-file integration pass.
D. Spawn one subagent per file in parallel, each responsible for that file's tests.

---

**Q8.** A customer message reads: "My order #4471 arrived damaged, and separately I was charged
twice for order #4390 last month." How should a well-designed agent handle this?

A. Address the damaged order first, then ask the customer to open a separate ticket for the billing issue.
B. Decompose into two distinct items, investigate each in parallel using shared context, then synthesize a unified resolution.
C. Escalate to a human, since multi-concern messages exceed the agent's single-issue design.
D. Ask the customer which issue they would like resolved first.

---

**Q9.** You resume a named investigation session two days later with `--resume auth-refactor`.
In the interim, three of the files the agent analyzed have been substantially rewritten by
another developer. What should you do?

A. Resume as normal; the agent will re-read files as needed.
B. Resume, and inform the agent about the specific file changes so it re-analyzes those targets rather than re-exploring everything.
C. Start a fresh session, since any file change invalidates the prior analysis.
D. Run `/compact` first to clear the stale file contents from context.

---

**Q10.** Your coordinator's system prompt reads: "Step 1: call the web search agent. Step 2:
pass results to the document analyzer. Step 3: pass output to synthesis. Step 4: pass to report
generation." Queries that need no document analysis still run the full pipeline, and complex
queries that would benefit from a second search round never get one. What change addresses
this?

A. Add conditional branches to the prompt describing when each step may be skipped.
B. Write the coordinator prompt to specify research goals and quality criteria rather than step-by-step procedures, so it can dynamically select subagents and iterate.
C. Add a routing classifier ahead of the coordinator that determines which pipeline stages to enable per query.
D. Split into four separate coordinators, one per query type.

---

**Q11.** In a code review workflow, a single-pass review of a 22-file PR produces detailed
findings for the first few files, superficial comments for the rest, and flags a pattern as a
bug in one file while approving identical code in another. Which decomposition applies?

A. Dynamic adaptive decomposition based on what each file reveals.
B. Prompt chaining: analyze each file individually for local issues, then run a separate cross-file integration pass.
C. Run the review three times and report only findings that recur.
D. Route each file to a separate subagent and have the coordinator merge results.

---

**Q12.** Your agent escalates a billing dispute to a human. The human agent replies in Slack:
"I have no idea what this is about — what did the customer say, what did you check, and what
do you want me to do?" What was missing?

A. A transcript link so the human can read the conversation.
B. A structured handoff summary containing customer ID, root cause analysis, refund amount, and recommended action.
C. A confidence score indicating how uncertain the agent was.
D. The escalation should not have occurred; the agent should have resolved it autonomously.

---

**Q13.** Which of the following correctly describes the relationship between an agentic loop
iteration and conversation history? **(Select two.)**

A. Tool results are appended to conversation history so the model can incorporate new information into its reasoning on the next iteration.
B. Each `tool_use` block must receive a corresponding `tool_result` with the matching `tool_use_id`.
C. Tool results should be summarized before appending, to prevent context growth.
D. The assistant message containing `tool_use` blocks should be omitted from history once the results are known.

---

**Q14.** A coordinator delegates to four subagents. One subagent's tool fails with a transient
network error, retries locally twice, and succeeds on the third attempt. What should it report
to the coordinator?

A. The successful result. The transient failure was resolved locally and does not require coordinator involvement.
B. The successful result plus a structured error record documenting the transient failures.
C. A partial-failure status, so the coordinator can decide whether to trust the result.
D. Nothing — subagents should propagate all errors upward for centralized handling.

---

**Q15.** Your synthesis subagent has been given the full tool set: `web_search`, `load_document`,
`extract_data_points`, `verify_claim_against_source`, `fetch_url`, `summarize_content`,
`generate_citation`, and 11 others — 18 tools total. It has begun performing its own web
searches instead of synthesizing the findings it was given, and tool selection has become
erratic. Which two changes address this? **(Select two.)**

A. Restrict the synthesis subagent's tool set to those relevant to its role.
B. Provide a scoped `verify_fact` tool for the high-frequency simple verification case, routing complex verifications through the coordinator.
C. Add a system prompt instruction forbidding the synthesis agent from performing web searches.
D. Replace `fetch_url` with a constrained `load_document` tool that validates document URLs.

---
---

# Answers

**Q1 — B.** The loop must be controlled by `stop_reason`. Reading the text (the current bug) and
using a loop counter as the main stop method are both named as wrong in the guide. Both failures
in the question come from these two mistakes.
- **A** — keeps both mistakes and makes them bigger.
- **C** — reasonable engineering, but it makes stopping depend on the model *choosing* to call a
  tool. The API already gives you the signal directly. The guide does not use this pattern.
- **D** — the guide names this as wrong: "checking for assistant text content as a completion
  indicator." Text and tool requests often appear in the same response, so this breaks
  immediately.

**Q2 — B.** Subagents do not receive the coordinator's history, and do not share memory between
calls. The findings must be written into the prompt.
- **A** — `Task` is clearly working. The subagent was started and replied.
- **C** — the subagent understood its job perfectly. It is missing **data**, not instructions.
- **D** — `fork_session` creates branches of a session for exploring different approaches. It is
  not a way to pass context from coordinator to subagent.

**Q3 — C.** A business rule involving money must always work, so it needs programmatic
enforcement. The guide's example is almost the same: intercept the tool call, block it above the
limit, and send it to escalation.
- **A** — prompt-based. 11 failures out of 5,000 is exactly the "non-zero failure rate" the guide
  warns about. Stronger wording does not make it certain.
- **B** — **close, and partly right.** Validation inside the tool does enforce the rule. But it
  returns an error instead of **sending the case to escalation**, so the customer is stuck. The
  guide says to intercept and redirect. If the question had not mentioned escalation, this
  answer would be much stronger.
- **D** — changes a number inside an instruction that still fails sometimes. Now the policy is
  wrong as well.

**Q4 — A and C.** The cause is a coordinator split that is too narrow. **A** fixes the choice of
subagents at the start. **C** finds any remaining gaps afterwards, by checking the synthesis
output and sending new targeted questions. Together they close the gap.
- **B** — **very close.** Scope partitioning reduces **duplication** between subagents. But
  duplication is not the problem here. All three subtasks were different. The problem is that the
  whole split covered only one part of the topic. Dividing a too-small scope more neatly changes
  nothing.
- **D** — asks a later agent to find the gap. But that agent only sees what it was given. It
  cannot know that wind and hydro exist if nothing earlier mentioned them.

**Q5 — B.** `fork_session` exists exactly for this: separate branches from one shared analysis,
used to explore different approaches.
- **A** — `--resume` continues one conversation. It does not create branches.
- **C** — parallel Task calls send out separate subtasks. They do not inherit the coordinator's
  analysis (see Q2).
- **D** — throws away the expensive analysis and rebuilds it, losing detail.

**Q6 — A.** `PostToolUse` changes tool **results** before the model reads them. The guide names
this exact situation: Unix timestamps, ISO 8601, and numeric status codes from different MCP
tools.
- **B** and **C** — both ask the model to do date arithmetic in its head. That is the thing it is
  already failing at.
- **D** — wrong hook type. Interception hooks act on outgoing calls, not results. Also, you
  usually cannot make an old service change its response format.

**Q7 — B.** The task is open-ended, the structure is unknown, and each step depends on what you
find. That is dynamic adaptive decomposition. The guide uses almost the same words.
- **A** — prompt chaining is for **predictable** work.
- **C** — that is the code-review pattern, used when you already know the files.
- **D** — starts one subagent per file before you know which files matter. The question says the
  risky paths are unknown.

**Q8 — B.** Split into separate items, investigate each **in parallel with shared context**, then
give one combined answer.
- **A** — moves work to the customer and reduces first-contact resolution.
- **C** — messages with several problems are clearly in scope. The escalation reasons are:
  the customer asks, a policy gap, or no progress.
- **D** — also moves work to the customer, and there is no reason to handle only one.

**Q9 — B.** Tell the resumed session which specific files changed, so it re-reads only those
instead of exploring everything again.
- **A** — the agent thinks it already knows those files. It has no reason to read them again.
- **C** — **close.** Starting fresh with a summary is correct when **all** the earlier tool
  results are out of date. Here only three files changed out of a wider analysis, so targeted
  re-reading keeps the parts that are still correct. The difference is **how much** is stale.
- **D** — `/compact` reduces context size. It does not correct wrong information.

**Q10 — B.** Coordinator prompts should describe research goals and quality standards, not
step-by-step instructions. That is what lets the coordinator choose subagents and repeat steps
when needed. Both problems in the question come from a rigid procedure.
- **A** — adding conditions is still a procedure, and cannot cover every case.
- **C** — too big a solution. It adds a system to replace judgement the model can already make.
- **D** — more to maintain, and the routing is still fixed.

**Q11 — B.** The file list is known and the review is predictable, so use prompt chaining. One
pass per file gives consistent depth. The separate pass across files finds integration problems.
This directly fixes attention dilution and contradictory findings.
- **A** — the work is not open-ended. You know exactly which files to review.
- **C** — voting across runs **hides real bugs** that are only found sometimes.
- **D** — **reasonable but incomplete.** One subagent per file does give consistent depth. But
  merging separate per-file results is exactly how you **lose** issues that cross files. The
  separate integration pass is the important part, and D leaves it out.

**Q12 — B.** A human who receives an escalation **cannot see the conversation**. So the handoff
must contain the customer ID, the root cause, the amount, and the recommended action.
- **A** — reasonable in a real product, but the guide's stated skill is writing the structured
  summary, exactly because transcript access is not assumed.
- **C** — self-reported confidence is rejected throughout this exam.
- **D** — nothing in the question suggests the escalation was wrong.

**Q13 — A and B.** Both describe how the loop works. Results go into the history so the model can
use them next time. Every `tool_use` needs a matching `tool_result` with the same `tool_use_id`.
- **C** — the guide does not say to summarise tool results. It says to **trim long output to the
  useful fields** (Domain 5). Trimming and summarising are different actions. Watch this
  difference.
- **D** — removing the assistant message breaks the link between `tool_use` and `tool_result`,
  and destroys the reasoning chain.

**Q14 — A.** Subagents fix transient failures themselves and report **only** what they cannot
fix. This one was fixed.
- **B** — harmless, but the design rule is that a fixed transient failure does not need the
  coordinator's attention. If the question had been about logging, this would be arguable.
- **C** — it is not a partial failure. It succeeded.
- **D** — goes against the local recovery rule and fills the coordinator with noise.

**Q15 — A and B.** **A** is the direct fix: 18 tools instead of 4–5 makes selection unreliable,
and an agent with tools outside its job will misuse them. The question shows both symptoms.
**B** is the guide's matching recommendation: a small cross-role tool for the common case, and
the coordinator for the difficult ones.
- **C** — a rule in the prompt placed on top of a structural problem. It also fights against the
  tool descriptions instead of removing the tools.
- **D** — a real technique (replace a general tool with a limited one), but it is about
  **validating input** to `fetch_url`. It does not fix the number of tools or the specialisation
  problem the question describes. Right idea, wrong problem.

---

## Score

___ / 15 · Q4, Q13 and Q15 need two answers each. You need both to get the point.

- **Below 10** — read `notes/domain-1-agentic-architecture.md` again before starting Domain 2.
  This domain is 27% of the exam. You cannot pass without it.
- **10–12** — look at which questions you missed. Are they about enforcement (Q3, Q6) or about
  splitting up work (Q4, Q7, Q10, Q11)? Practise that half.
- **13 or more** — move on. Come back to this on day 17.
