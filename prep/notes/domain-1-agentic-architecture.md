# Domain 1 — Agentic Architecture & Orchestration (27%)

This is the biggest domain. About 16 of the 60 questions come from here.

It has 7 task statements. They are all about the same thing: **how work is split up, given to
other agents, controlled, and continued later.**

---

## 1.1 The agentic loop

An **agentic loop** is the cycle where Claude asks for a tool, you run it, and you send the
result back.

Only one thing controls the loop: **`stop_reason`**.

```
send request → look at stop_reason
  ├── "tool_use"  → run the tools Claude asked for
  │                 → add Claude's message (with the tool_use blocks) to the history
  │                 → add the tool results as a user message
  │                 → repeat
  └── "end_turn"  → stop. Show the final answer.
```

### `stop_reason` values

The exam tests two: `"tool_use"` and `"end_turn"`.

The real API has seven: `end_turn`, `max_tokens`, `stop_sequence`, `tool_use`, `pause_turn`,
`refusal`, `model_context_window_exceeded`. The guide names only the two above — answer with
those.

### Rules for tool results

- Add tool results to the conversation history. This lets the model use the new information in
  the next step.
- Every `tool_use` block needs one matching `tool_result`, with the same `tool_use_id`.
- Send **all** results from one Claude message back together, in **one** user message.

### Four wrong ways to stop the loop

The exam will offer these as answers. They are always wrong.

1. Reading Claude's text to see if it says something like "I am finished."
2. Using a maximum number of loops as the **main** way to stop. (Using it as a safety limit is
   fine. Using it as the mechanism is not.)
3. Checking if the response contains text. Text and tool requests often appear together.
4. Adding an explicit `task_complete` tool the model must call to end. `stop_reason: "end_turn"`
   already signals completion — the extra tool is redundant and the model may forget to call it.

### Model-driven vs pre-configured

- **Model-driven:** Claude decides which tool to call next, based on the situation.
- **Pre-configured:** you write a fixed decision tree or a fixed order of tools.

Choose model-driven — **unless** section 1.4 applies (when a rule must always work).

---

## 1.2 Coordinator and subagent design

A **coordinator** is the main agent. A **subagent** is a helper agent that does one job.

### Hub-and-spoke

All messages go through the coordinator. Subagents never talk to each other.

Why: you get better visibility, one place for error handling, and control over what information
moves where.

### Subagents start empty

A subagent does **not** receive the coordinator's conversation history. It does not share memory
between calls. Anything it needs must be written in its prompt.

### What the coordinator does

- Splits the task into parts (**task decomposition**)
- Gives parts to subagents
- Collects the results
- Decides **which** subagents to call, based on how complex the request is

That last point matters. A good coordinator does not always run every subagent. It chooses.

### The main failure to remember

**Task decomposition that is too narrow.**

This is Sample Q7 in the guide. The topic was "impact of AI on creative industries." The
coordinator split it into three subtasks, and all three were about visual art. Music, writing and
film were never researched.

Every subagent did its job correctly. The **split** was wrong.

**Exam rule:** if the question says coverage is incomplete but each agent worked correctly, the
answer is the coordinator's task decomposition.

### Two more coordinator skills

- **Scope partitioning:** give each subagent a different subtopic, or a different type of source.
  This stops two agents doing the same work.
- **Iterative refinement loop:** the coordinator reads the synthesis output, looks for gaps,
  sends new targeted questions to the search and analysis subagents, then runs synthesis again.
  It repeats until coverage is good enough.

---

## 1.3 Starting subagents and passing context

- Subagents are started with the **Task tool**.
- The coordinator's **`allowedTools` must include `"Task"`**. Without it, the coordinator cannot
  start any subagent. This is a common exam question.
- **AgentDefinition** is the configuration for each subagent type. It holds the description, the
  system prompt, and which tools that subagent may use.
- **To run subagents in parallel:** send several Task tool calls **in one single response**. If
  you send them in separate turns, they run one after another.
- Put the earlier findings **directly in the subagent's prompt**. For example, give the synthesis
  subagent the actual web search results and document analysis output.
- Use a **structured format that separates content from metadata** (source URLs, document names,
  page numbers). This keeps the source information attached to each finding.
- Write coordinator prompts that describe **goals and quality standards**, not step-by-step
  instructions. Step-by-step prompts stop subagents from adapting.
- **`fork_session`** creates separate branches from one shared analysis. Use it to compare
  different approaches.

---

## 1.4 Making rules that always work

This is the most important idea in Domain 1.

| Programmatic enforcement | Prompt-based guidance |
|---|---|
| Hooks, prerequisite gates | System prompt text, few-shot examples |
| Always works | Fails sometimes |
| Use for: identity checks before money operations, policy limits, compliance | Use for: style, preferences, judgement |

The guide's exact reasoning: prompt instructions have a "non-zero failure rate." That means they
fail sometimes. That is not acceptable when money is involved.

**The standard example:** block `process_refund` until `get_customer` has returned a verified
customer ID.

If the question involves money, any answer using prompts or examples is wrong.

### Requests with several problems in one message

Correct handling:
1. Split the message into separate items.
2. Investigate each one **in parallel**, using shared context.
3. Combine the results into **one** answer for the customer.

Wrong: handle them one at a time, or ask the customer to choose which one to fix first.

### Handoff to a human

The human agent **cannot see the conversation**. So the handoff summary must include:
- Customer ID
- Root cause analysis
- Refund amount
- Recommended action

---

## 1.5 Hooks

A **hook** is code that runs automatically at a certain point. The model cannot skip it.

Two types are tested:

**`PostToolUse`** — runs after a tool returns, before the model sees the result.
Main use: **normalise different data formats**. Example from the guide: one service returns Unix
timestamps, another returns ISO 8601, another returns a numeric status code. The hook converts
them all to one format first.

**Tool call interception** (the real event name is **`PreToolUse`**) — runs before a tool is
called, and can block it.
Main use: **stop actions that break a policy**. Example from the guide: block refunds above $500
and send them to human escalation instead.

Choose a hook whenever a business rule must always be followed.

---

## 1.6 How to split up complex work

| Pattern | Use it when | Example |
|---|---|---|
| **Prompt chaining** (fixed steps, always the same) | The work is predictable | Review each file, then run one extra pass across all files |
| **Dynamic decomposition** (steps depend on findings) | The work is open-ended | "Add tests to a legacy codebase": first map the structure, then find the risky areas, then build a plan that changes as you discover dependencies |

### Large code reviews

The correct pattern is: **one pass per file, plus one separate pass across files.**

This fixes **attention dilution** — when a model reviews too much at once, quality drops and it
gives inconsistent answers.

**A bigger context window does not fix this.** The guide is clear: larger context does not
improve attention quality. Any answer suggesting a bigger model or bigger window is wrong.

---

## 1.7 Sessions: continue, branch, or restart

- **`--resume <session-name>`** continues one specific earlier conversation.
- **`fork_session`** creates separate branches from one shared starting point. Example: compare
  two refactoring approaches using the same codebase analysis.
- **Tell a resumed session what changed.** If files were edited since last time, say which files.
  Then the agent re-reads only those, instead of exploring everything again.

### Resume or start fresh?

| Situation | Do this |
|---|---|
| Earlier context is mostly still correct, a few known files changed | **Resume** and name the changed files |
| Earlier tool results are **mostly stale** (out of date) | Start a **new** session and give it a written summary |

The guide states this directly: starting fresh with a structured summary is more reliable than
resuming with stale tool results. But the question is **how much** is stale — when only a few
named files changed inside a wider analysis, resume and say which files changed.

---

## Quick review list for Domain 1

1. The loop is controlled by `stop_reason`. `tool_use` = continue. `end_turn` = stop.
2. `allowedTools` must include `"Task"` to start subagents.
3. Subagents receive nothing automatically. Put context in the prompt.
4. Parallel = several Task calls in **one** response.
5. Coverage is incomplete but every agent worked = the coordinator's split was too narrow.
6. Money, identity, or policy limits = hooks or gates. Never prompts.
7. `PostToolUse` changes results. `PreToolUse` (the interception hook) blocks calls.
8. Big review = one pass per file + one pass across files.
9. Resume or fresh is decided by **how much** is stale. A few known files changed = resume and
   name them. Most of the context stale = new session with a written summary.
