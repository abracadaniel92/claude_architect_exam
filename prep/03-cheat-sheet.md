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

**Which mechanism holds which content** — this decides several questions:

| The content is | Use | Because |
|---|---|---|
| Universal standards, must always apply | **CLAUDE.md** | Always loaded |
| Shared documents, and each package's **maintainer picks** which apply — no duplication | **`@import`** in each package's CLAUDE.md | Selective inclusion by reference, nothing copied |
| Conventions that follow a **file type across many folders** (`**/*.test.*`) | **`.claude/rules/`** with `paths:` | Loads only when a matching file is edited |
| Conventions for **one folder and nothing outside it** (`services/billing/`) | **a CLAUDE.md inside that folder** | Covers exactly that subtree |
| An on-demand, task-specific **workflow** (quarterly migration, release notes) | **a skill** | Called when needed |

> ⚠️ **16 Aug: three questions, three mechanisms, each answered with a different row of this
> table.** The table is known and is being matched by feel. Choose by **what the content is
> grouped by**, and nothing else:
>
> | The grouping is | Answer |
> |---|---|
> | by **package or component**, maintainer picks which documents | **`@import`** |
> | by **file type**, wherever the file lives (`**/*.test.*`) | **`.claude/rules/` + `paths:`** |
> | by **one folder**, everything in it, nothing outside | **a directory CLAUDE.md** |
> | by **nothing — it always applies** | **the root CLAUDE.md** |
> | by **the moment someone asks for it** | **a skill** |
>
> `.claude/rules/` has become the reflex answer for anything about scoping. It is only correct
> when the grouping is a **file pattern**.
>
> **17 Aug — the table is not the problem. Reading the grouping off the wrong words is.** A question
> that asked for this discriminator in the abstract was answered correctly, in the same sitting as
> two wrong applications of it. Both misses came from the sentence, not the content: *"they exist in
> nine packages"* was read as a package grouping when the content governs `**/*.stories.tsx`, and
> *"each lead decides which apply"* was read as invoking when the documents then govern all work in
> that service.
>
> **Ask one question, and only this one: what set of files does this content govern?**
> A pattern → `.claude/rules/`. One package or service → `@import`. One folder → a directory
> CLAUDE.md. Everything → the root CLAUDE.md. Only when someone asks → a skill.
> Never decide it from which nouns appear in the question, and never from the word "chooses".

**Skills must be invoked.** So a skill can *never* be the answer for something that must always
apply, or must load automatically. If a question says "automatic" or "always", skills are out.

> ⚠️ **`@import` — missed three times, twice by choosing skills.** The trap is the word
> **"chooses"**. These questions always say a maintainer *chooses* or *decides* which documents
> apply, and choosing feels like invoking. It is not.
>
> | | Who chooses | When | Then it loads |
> |---|---|---|---|
> | **`@import`** | the **maintainer**, once, while writing the file | at authoring time | **always** |
> | **a skill** | the **model or developer**, at run time | every single use | **only when invoked** |
>
> Ask: *after the choice is made, does the content apply to everything, or only when someone
> calls it?* Applies to everything → `@import`.

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
- All seven API values: `end_turn`, `max_tokens`, `stop_sequence`, `tool_use`, `pause_turn`,
  `refusal`, `model_context_window_exceeded`. The guide tests only the first pair above.
- Every `tool_use` needs one `tool_result` with the same `tool_use_id`.
- Send all results from one Claude message back in **one** user message.

**Four wrong ways to stop:** reading the text · a loop counter as the main method · checking if
text exists · a `task_complete` tool.

---

## 6. Subagents (Domain 1)

- Started with the **Task tool**.
- The coordinator's **`allowedTools` must include `"Task"`**.
- Subagents receive **nothing** automatically. Put everything in the prompt.
- **Parallel** = several Task calls in **one response**. ⚠️ **Missed twice (16 Aug):** once by
  choosing a `parallel: true` field that **does not exist**, once by not selecting it at all on a
  select-two. Separate turns run sequentially. There is no flag, no setting, no config key.
- **`fork_session`** = branches from one shared analysis, to compare approaches.
- All messages go **through the coordinator**. Subagents never talk to each other.
- Coverage is incomplete but every agent worked → **the coordinator's split was too narrow.**

**Resume or start fresh?** Decided by **how much** is stale. A few known files changed →
`--resume` and name the changed files. Most of the earlier context stale → **new** session with a
written summary.

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
- **`PreToolUse`** (the interception hook) — blocks an outgoing tool **call**. Use for blocking
  refunds over $500 and redirecting to escalation.

**Before answering ANY question:** does it say **select two**? If yes, count the symptoms in the
scenario and check you have one answer per symptom. Mechanical step, every time.

---

**Splitting up work (Domain 1)**

Ask one question first: **do I know the shape of the work before I start?**

| Answer | Pattern |
|---|---|
| **Yes** — the file list is known, the criteria are fixed | **Prompt chaining.** Large review = one pass per file + one pass across files |
| **No** — the structure is unknown, each step depends on the last | **Dynamic decomposition.** Map first, then a plan that adapts |

The words "audit", "large" and "comprehensive" do **not** decide this. A 900-file audit where you
do not know where the relevant code lives is **dynamic**. A 22-file review with a known list is
**chaining**. Same size, opposite answers.

---

## 8. Error handling (Domains 2 and 5)

**Four categories:** transient · validation · business · permission

**Every error returns:** `errorCategory` + `isRetryable` + a readable message.
For business rules, add `isRetryable: false` and a customer-friendly explanation.
(The guide's prose sometimes spells the field "retriable" — same field, same meaning.)

**An access failure is not an empty result.** A timeout may need a retry. Zero matches is a
success.

**Subagent error report contains four things:** failure type · what was tried · partial results ·
possible alternatives.

**Never:** a generic message · hiding the error as success · stopping the whole workflow.

**Coverage annotations.** When a source or tool was unavailable, the output must say **which
findings are well supported and which topics have gaps.** A report that reads as complete when two
sources never answered is the same failure as hiding an error.

> ⚠️ **Missed twice in one paper (16 Aug), and it was on the revision card but not here.** The two
> wrong answers were *"retry until the sources respond"* and *"summarise more aggressively"* —
> both treat a coverage gap as something to remove rather than something to **declare**.

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
- **One tool with a `mode` / `action` enum → split into purpose-specific tools**, each with its
  own contract. **Merging the modes into fewer modes is the wrong answer** — it keeps the
  overloaded design and only reduces how many wrong choices exist.

**Grep · Glob · semantic:**

| Need | Tool |
|---|---|
| File **paths** by pattern | `Glob` |
| Text you **can spell exactly** | `Grep` |
| A **concept** with no literal to search for | Semantic search |

If the question prints the string → `Grep`. If the question says **you do not know what it is
called** (several candidate names, none confirmed) → **semantic**. "Widen the pattern until
something matches" is a description of not having a string.

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

**Required or nullable? Ask: does the source always contain this value?**

| The source | Use | Because |
|---|---|---|
| **May not** contain it (open-ended contract, optional clause) | **nullable / optional** | A required field forces the model to produce something, so it **invents** a value |
| **Always** contains it (machine-generated confirmation, fixed layout) | **required** | It guarantees the field cannot be **omitted** from the output |

> ⚠️ **Missed 14 Aug by choosing "nullable, plus a validation rule rejecting null".** That is the
> worst of both: it does not stop fabrication, and it now **fails** documents that would have
> extracted fine. Both directions are correct answers on this exam, in different scenarios —
> decide it from the *source*, never from which failure you saw last.

- Enum + `"other"` + a detail string, for categories that may grow.
- `"unclear"` for ambiguous cases.
- Tool use + schema removes **syntax** errors. It does **not** remove **semantic** errors.
- `calculated_total` next to `stated_total` — to catch totals that do not add up.
- `conflict_detected` — a boolean for contradictory source data.
- `detected_pattern` — to analyse which findings developers dismiss.
- Inconsistent dates and currency in the source → **format normalisation rules in the prompt**,
  next to the strict schema. The schema fixes the **type**; the prompt fixes the **format**. A
  post-processing layer is the wrong answer — it needs a branch per variant and breaks on the
  first layout you did not anticipate.

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
- Large review **with a known file list** → one pass per file + one pass across files. (Unknown
  structure → map first instead. See "Splitting up work" above.)
- **A bigger context window does not fix attention dilution.**
- **Voting across runs hides real bugs.**
- **Prose description giving inconsistent results → 2–3 concrete input/output examples.** The
  guide calls this the most effective way to show an expected transformation.
- **Unfamiliar domain, and you are not sure what to specify → the interview pattern.** Let Claude
  ask you questions first, so it raises what you did not think of (cache invalidation, failure
  modes). Not plan mode — plan mode designs against a specification you do not yet have.
- **Problems that affect each other → one detailed message.** Independent problems → one at a time.
- **In CI, CLAUDE.md is how Claude Code learns the project:** testing standards, fixture
  conventions, review criteria. Writing them there is what stops low-value test suggestions —
  not appending them to the prompt in the pipeline script. To stop duplicate tests, **supply the
  existing test files.**

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

> ⚠️ **The sampling half has now been missed twice (16 Aug), both times as the second answer on a
> select-two.** "Analyse by document type and field" is being found; **"stratified random sample
> of the HIGH-CONFIDENCE extractions"** is not. Why that group: it is the group you are about to
> **stop reviewing**, so its true error rate is the only number that matters. Sampling uniformly,
> or sampling what the model already flagged as low confidence, tells you nothing about it.

**Confidence is usable only when calibrated with labelled data, and only for routing review work.**

**Conflicting sources** → record both with their sources. Dates are required.

**Metadata the subagent must record, because nobody downstream can recover it:** publication or
collection **dates** · **source location** · the **methodology** behind the finding. Missing this,
the synthesis agent cannot tell a 2021 survey from a 2026 one, or a peer-reviewed study from a
vendor page.

> ⚠️ **Missed 14 Aug.** Both wrong answers tried to repair it downstream — *"have the synthesis
> agent weigh sources by credibility"* (it cannot see what it needs to weigh) and *"re-fetch each
> source at synthesis time"* (what you find later is not reliably where the claim came from).
> **Provenance travels as structure from the agent that held the source.** It is never restored by
> instruction and never reconstructed afterwards.

---

## 14. The 30-second method for each question

1. Read the **last sentence** first. That is the real question.
2. Remove any answer with a feature that does not exist.
3. Remove any answer blaming a part the question says is working.
4. Choose the **weakest fix that still meets the requirement**.
5. If money, identity, or "must never" appear → choose programmatic enforcement.
6. **Ask where the information should have been produced, not where the failure showed up.**

**Step 6 is your one cross-domain weakness** — every miss on 14 Aug was the same shape, in three
different domains. The failure appears late; the fix belongs early.

| Where the failure shows up | The tempting late fix | The correct early fix |
|---|---|---|
| Extraction omits a field the source always has (D4) | nullable + a rule rejecting null | **required** in the schema |
| Dates and currency arrive inconsistent (D4) | a post-processing normalisation layer | **normalisation rules in the prompt** |
| Synthesis cannot judge a source (D5) | re-fetch the sources, or tell it to weigh credibility | **subagents record dates, location, methodology** |

The late fix is usually *defensible engineering*, which is why it is the distractor. Ask: which
component was holding the information at the moment it was lost? That component is the answer.
