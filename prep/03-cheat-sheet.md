# The Cheat Sheet — Everything You Must Recall Cold

Every fact you need from memory, in one file.

> ### Screen version or paper version?
>
> **This file is the screen version.** Use it on a phone or laptop, where scrolling is easy and a
> PDF is awkward.
>
> **[`CCAR-F-revision-card.pdf`](../CCAR-F-revision-card.pdf) is the paper version.** Same facts,
> laid out for A4 and printed double-sided on 3 sheets. It also adds the exam-attack strategy
> from [`01-answer-patterns.md`](01-answer-patterns.md) — the strength ladder, the five kinds of
> wrong answer, and the signal-word table — which this file does not contain.
>
> If you are printing something, print the PDF. If you are revising on your phone, use this file.
> To change the PDF, edit [`tools/make-revision-card.py`](../tools/make-revision-card.py) and run
> it. Do not edit the PDF by hand, or the two will drift apart.

## How to use it

1. **Every day**: read one section, cover it, say it back out loud.
2. **On 24 August**, the day before the exam: read the whole thing through, twice.

You cannot take notes into the exam. Everything here must be in your head.

---

## 1. Exam facts

| Item | Value |
|---|---|
| Questions | 60 |
| Time | 120 minutes (2 min per question) |
| Pass mark | 720 out of 1000 |
| Scenarios | 4, chosen from 6 |
| Format | Multiple choice and multiple response. Each question says how many to select |
| Domain weights | D1 27% · D2 18% · D3 20% · D4 20% · D5 15% |

---

## 2. File paths (Domain 3)

| What | Where |
|---|---|
| Personal instructions (**not shared**) | `~/.claude/CLAUDE.md` |
| Project instructions (shared) | `.claude/CLAUDE.md` or `CLAUDE.md` in the root |
| Folder instructions | `CLAUDE.md` inside that folder |
| Rule files by topic | `.claude/rules/` |
| Shared slash commands | `.claude/commands/` |
| Personal slash commands | `~/.claude/commands/` |
| Shared skills | `.claude/skills/` |
| Personal skills | `~/.claude/skills/` |
| Shared MCP servers | `.mcp.json` |
| Personal MCP servers | `~/.claude.json` |

**Rule:** anything starting with `~/` is personal and is **not** shared through version control.

---

## 3. Frontmatter keys — do not mix these up

**SKILL.md** (in `.claude/skills/`):
- `context: fork` — run in a separate context, keeping long output out of the main conversation
- `allowed-tools` — limit which tools the skill can use
- `argument-hint` — ask the developer for a missing parameter

**`.claude/rules/` files:**
- `paths:` — glob patterns. The rule loads only when you edit a matching file

`paths:` is **not** a SKILL.md key. This is the most common mistake in Domain 3.

---

## 4. Commands and flags

| Need | Use |
|---|---|
| See which memory files are loaded | `/memory` |
| Reduce context in a long session | `/compact` |
| Continue a named session | `--resume <name>` |
| Branch from one shared analysis | `fork_session` |
| Non-interactive mode in CI (fixes hanging) | `-p` or `--print` |
| Output a script can read | `--output-format json` |
| Force the output to follow a schema | `--json-schema` |
| Noisy discovery without filling the context | Explore subagent |

**These do not exist.** They appear as wrong answers:
`--batch` · `CLAUDE_HEADLESS=true` · `.claude/config.json` with a `commands` list ·
`--no-interactive`

---

## 5. The agentic loop (Domain 1)

- The loop is controlled by **`stop_reason`**. Nothing else.
- `"tool_use"` → run the tools, add results to history, repeat.
- `"end_turn"` → stop.
- All six values: `end_turn`, `max_tokens`, `stop_sequence`, `tool_use`, `pause_turn`, `refusal`.
- Every `tool_use` needs one `tool_result` with the same `tool_use_id`.
- Send all results from one Claude message back in **one** user message.

**Three wrong ways to stop:** reading the text · a loop counter as the main method · checking if
text exists.

---

## 6. Subagents (Domain 1)

- Started with the **Task tool**.
- The coordinator's **`allowedTools` must include `"Task"`**.
- Subagents receive **nothing** automatically. Put everything in the prompt.
- **Parallel** = several Task calls in **one response**.
- **`fork_session`** = branches from one shared analysis, to compare approaches.
- All messages go **through the coordinator**. Subagents never talk to each other.
- Coverage is incomplete but every agent worked → **the coordinator's split was too narrow.**

---

## 7. Making rules that always work (Domain 1)

| Use programmatic enforcement | Use prompts |
|---|---|
| Money, identity checks, policy limits | Style, preferences, judgement |
| Hooks, prerequisite gates | System prompt, few-shot examples |
| Always works | Fails sometimes |

**Two hook types:**
- `PostToolUse` — changes tool **results** before the model reads them. Use for normalising
  different data formats.
- **Interception hook** — blocks an outgoing tool **call**. Use for blocking refunds over $500 and
  redirecting to escalation.

---

## 8. Error handling (Domains 2 and 5)

**Four categories:** transient · validation · business · permission

**Every error returns:** `errorCategory` + `isRetryable` + a readable message.
For business rules, add `retriable: false` and a customer-friendly explanation.

**An access failure is not an empty result.** A timeout may need a retry. Zero matches is a
success.

**Subagent error report contains four things:** failure type · what was tried · partial results ·
possible alternatives.

**Never:** a generic message · hiding the error as success · stopping the whole workflow.

**Subagents fix transient failures themselves.** They only report what they cannot fix.

---

## 9. Tools (Domain 2)

- Tool **descriptions** decide which tool the model picks. Improve them first.
- A description contains: inputs · example queries · edge cases · when to use it instead of a
  similar tool.
- **18 tools is bad. 4–5 is good.**
- An agent with tools outside its job will misuse them.
- Give a small cross-role tool for a common need (example: `verify_fact` for the synthesis agent).
- Replace general tools with limited ones (`fetch_url` → `load_document`).
- Check the system prompt for words that create unwanted tool links.

**`tool_choice`:**

| Value | Meaning |
|---|---|
| `auto` | May reply with **text** instead of calling a tool |
| `any` | Must call a tool, chooses which |
| `{"type":"tool","name":"..."}` | Must call that specific tool |
| `none` | Cannot use tools |

Short version: **auto may talk · any must act · forced picks the actor.**

**Built-in tools:** Grep = inside files · Glob = file paths · Edit fails on unclear text → use
**Read + Write**.

**MCP resources** = content catalogues (issue lists, documentation structures, database schemas).
They stop the agent making exploratory calls.

**`${VAR}`** in `.mcp.json` keeps secrets out of the repository.

Use a **community MCP server** for standard integrations. Build custom only for your team's own
workflows.

---

## 10. Schemas and extraction (Domain 4)

- A **required** field makes the model invent a value. **Make it optional and nullable.**
- Enum + `"other"` + a detail string, for categories that may grow.
- `"unclear"` for ambiguous cases.
- Tool use + schema removes **syntax** errors. It does **not** remove **semantic** errors.
- `calculated_total` next to `stated_total` — to catch totals that do not add up.
- `conflict_detected` — a boolean for contradictory source data.
- `detected_pattern` — to analyse which findings developers dismiss.

**Retries:**

| Works | Does not work |
|---|---|
| Wrong format | The information is not in the document |
| Wrong structure | It is only in a document you did not supply |

A retry request contains: the document + the failed extraction + the **specific** errors.

---

## 11. Message Batches API (Domain 4)

| Property | Value |
|---|---|
| Cost | **50% cheaper** |
| Time | **Up to 24 hours** |
| Speed guarantee | **None** |
| Matching results | **`custom_id`** |
| Multi-turn tool calling | **Not supported** |

**Good for:** overnight reports, weekly audits, nightly test generation.
**Bad for:** anything where a person is waiting.

Resubmit only the failures, found by `custom_id`. Test your prompt on a small sample first.
A 24-hour window and a 30-hour SLA means submitting every **4 hours**.

---

## 12. Prompts and review (Domain 4)

- **Specific categories** work. **"Be conservative"** does not.
- A category with many false alarms damages trust in the good ones → turn it off while you fix it.
- **Few-shot: 2 to 4 examples**, aimed at the **unclear** cases.
- Self-review is weak, because the model remembers its own reasoning → use an **independent
  instance**.
- Large review → **one pass per file + one pass across files**.
- **A bigger context window does not fix attention dilution.**
- **Voting across runs hides real bugs.**

---

## 13. Context and escalation (Domain 5)

**Three problems:** progressive summarization loses details · lost in the middle · tool results
fill the context (40+ fields when 5 matter).

**Fixes:** a "case facts" block outside the summary · key findings at the **beginning** · **trim
tool output before it enters the context**.

**Escalate when:** the customer asks · there is a policy gap · no progress is possible.
**Never escalate based on:** sentiment · the model's own confidence.

- Customer **explicitly asks** for a human → escalate **immediately**.
- Customer is frustrated but you can help → offer to help, escalate only if they ask again.
- Several matching customers → **ask for another identifier**. Never guess.

**Context degradation** sounds like: the model talks about "typical patterns" instead of the
specific classes it found → use **scratchpad files**.

**Crash recovery** = **manifests**, loaded by the coordinator when work resumes.

**97% average accuracy can hide one broken document type** → stratified sampling + analysis by
type and field.

**Confidence is usable only when calibrated with labelled data, and only for routing review work.**

**Conflicting sources** → record both with their sources. Dates are required.

---

## 14. The 30-second method for each question

1. Read the **last sentence** first. That is the real question.
2. Remove any answer with a feature that does not exist.
3. Remove any answer blaming a part the question says is working.
4. Choose the **weakest fix that still meets the requirement**.
5. If money, identity, or "must never" appear → choose programmatic enforcement.
