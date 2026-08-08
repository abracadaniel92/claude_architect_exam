# Hands-On Exercises

These are the four exercises from the exam guide, turned into practical work. Each step has a
**checkpoint** ✅ showing what the exam tests.

The goal is not a finished product. The goal is to turn "I recognise this" into "I remember
this."

---

## How to work through these

You have built things like this before with AI help. For exam preparation, do it the other way
round: **write the configuration and schema by hand first, then let Claude check it.**

The exam is proctored. You get no notes and no assistant. Typing `context: fork` yourself three
times helps more than reading it thirty times.

---

## Exercise 1 — Agent with several tools and escalation (Days 2–6)
**Domains: 1, 2, 5**

Build a small support agent. Suggested folder: `prep/exercises/ex1-agent/`

### Steps

**1. Define 3–4 MCP tools** with detailed descriptions. Include **two tools that do similar
things** (for example `get_customer` and `lookup_order`), and write descriptions that make the
difference clear.

- ✅ Each description says: input formats, example queries, edge cases, and **when to use it
  instead of the similar tool**.
- Then try the opposite. Shorten both descriptions to one line and send unclear requests. Watch
  the agent choose wrongly. That is Sample Q2 happening in front of you.

**2. Build the agentic loop**, controlled by `stop_reason`.

- ✅ Your loop checks `"tool_use"` and `"end_turn"`. It does **not** read the text, and does not
  use a loop counter as the main way to stop.
- ✅ Tool results go into the conversation history. All results from one Claude message go back
  in **one** user message, each with the matching `tool_use_id`.

**3. Add structured error responses:** `errorCategory` (transient, validation, permission,
business), `isRetryable`, and a readable message.

- ✅ Cause each error type on purpose. Check that the agent retries transient errors, explains
  business errors, and does not retry the others.
- ✅ Your tools tell the difference between an **access failure** and a **valid empty result**.

**4. Add a tool call interception hook** that blocks an action above a limit (for example refunds
over $500) and sends it to escalation.

- ✅ Test it while the conversation is actively arguing for the refund. The block must still hold.
  That is the point of programmatic enforcement.

**5. Test a message with two problems in it.**

- ✅ The agent splits it into separate items, handles each one, and gives one combined answer.

### Memory check after finishing

Without looking, say: the four error categories, the two `stop_reason` values your loop uses, and
the two hook types (change results vs block calls).

---

## Exercise 2 — Configure Claude Code for a team (Days 7–9)
**Domains: 3, 2**

Do this in a **real repository**. Use one of your existing project folders.

This exercise gives the most points per hour. Domain 3 is 20% of the exam and is almost entirely
memorisation.

### Steps

**1. A project-level CLAUDE.md** with coding and testing standards.
- ✅ Say out loud why this is not in `~/.claude/CLAUDE.md`.

**2. Two files in `.claude/rules/`** with YAML frontmatter:
```yaml
---
paths: ["src/api/**/*"]
---
```
Make the second one match by **file type across folders**: `paths: ["**/*.test.*"]`.
- ✅ Open a matching file and a non-matching file. Check the rule loads only for the match.
- ✅ Say why the second one could not be a subfolder CLAUDE.md.

**3. A project skill** in `.claude/skills/` using `context: fork` **and** `allowed-tools`.
- ✅ Check the skill's output does not appear in the main conversation.
- Add `argument-hint` and call the skill with no arguments, to see the prompt.

**4. A project slash command** in `.claude/commands/`.
- ✅ Say why not `~/.claude/commands/`.

**5. MCP configuration:** a project server in `.mcp.json` using `${VAR}` for its token, plus a
personal server in `~/.claude.json`.
- ✅ Check that **both** work at the same time.
- ✅ Check that no secret is committed.

**6. Plan mode vs direct execution** on three tasks: a single-file bug fix, a multi-file
migration, and a feature with several possible designs.
- ✅ After each one, write one sentence saying why that mode was correct.

**7. Run `/memory`** and read the output. Run `/compact` in a long session.

### Memory check

Write from memory: the three CLAUDE.md levels and their paths; the four folders under `.claude/`;
the three SKILL.md frontmatter keys; the three CI flags.

---

## Exercise 3 — Structured extraction pipeline (Days 11–13)
**Domains: 4, 5**

### Steps

**1. Define an extraction tool with a JSON schema** containing: required fields,
**optional/nullable** fields, and an **enum with `"other"` plus a detail string**.

- ✅ Process documents that are missing the optional fields. Check the model returns `null`
  instead of inventing a value.
- ✅ Now change one field to required. Watch the model invent a value. Seeing both is the lesson.

**2. Build a validation-retry loop.** On failure, send back the document, the failed extraction,
and the **specific** validation error.

- ✅ Sort your failures into two groups: retryable (format or structure) and not retryable
  (information missing from the document). Count them. This distinction is tested directly.

**3. Add few-shot examples** for documents with different structures (data inline, in a table, in
prose).

- ✅ Use 2 to 4 examples, aimed at the **unclear** cases, not the obvious ones.

**4. Add semantic validation.** Extract `calculated_total` next to `stated_total`. Add a
`conflict_detected` boolean.

- ✅ Create a case where the schema passes but the data is wrong. Now you have felt why "schemas
  do not prevent semantic errors."

**5. Batch processing** with the Message Batches API. Submit a batch, match results by
`custom_id`, and resubmit only the failures (split any document that was too long).

- ✅ Do the SLA arithmetic: with a 24-hour window, how often must you submit to guarantee a
  30-hour SLA?
- ✅ Confirm results are matched by `custom_id`, not by position.

**6. Human review routing.** Add field-level confidence scores. Send low-confidence and
contradictory documents to review. Analyse accuracy **by document type and by field**.

- ✅ Create a case where the average accuracy looks good but one document type is failing badly.

---

## Exercise 4 — Multi-agent research pipeline (Days 14–15)
**Domains: 1, 2, 5**

### Steps

**1. A coordinator plus two subagents** (web search, document analysis).
- ✅ The coordinator's `allowedTools` includes `"Task"`.
- ✅ Each subagent gets its input **in its prompt**. Test this: ask a subagent about something the
  coordinator discussed earlier. It should not know.

**2. Parallel execution:** send several Task calls in **one** response. Compare the time with
running them one after another.
- ✅ You can explain the difference between this and `fork_session`.

**3. Structured subagent output** separating content from metadata: claim, evidence excerpt,
source URL or document name, publication date.
- ✅ The source information survives synthesis.

**4. Error reporting:** simulate a subagent timeout.
- ✅ The coordinator receives: failure type, the query it tried, partial results, and possible
  alternatives. It continues with partial results and marks the coverage gap.

**5. Conflicting sources:** give it two credible sources with different numbers.
- ✅ The synthesis keeps both, with their sources, and separates well-established findings from
  contested ones.

**6. Extra — recreate the Sample Q7 failure on purpose.** Give the coordinator a broad topic and
a prompt that pushes it toward one narrow area. Watch every subagent succeed while the report
still misses most of the topic.

This takes five minutes and teaches more than any reading.

---

## If you only have time for two

Do **Exercise 2** and **Exercise 4**.

- Exercise 2: Domain 3 is 20% of the exam and pure memorisation.
- Exercise 4: Domain 1 is 27% and the hardest to guess your way through.

Exercises 1 and 3 repeat much of the same material on error handling and schema design.
