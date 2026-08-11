# The Six Exam Scenarios

The exam gives you **4 of these 6**, chosen at random. Each one is a short story, followed by
about 15 questions.

> ### Read this once. Do not memorise it.
>
> A candidate who passed CCAR-F describes the scenarios as *"more dressing than anything
> substantive... no different to an exam that just asked me a series of unrelated questions about
> specific topics."*
>
> That matches the twelve sample questions in the official guide: every one of them is
> **self-contained**. You never need to remember a detail from the scenario text to answer a
> question.
>
> So this file has one job: **prediction, not memorisation.** When you recognise the scenario, you
> know which domains the questions will come from and which wrong answers to expect. That is
> worth 20 minutes of reading. It is not worth an hour of study.
>
> If you are short of time, skip this file and spend the time on `03-cheat-sheet.md` instead.

---

## Scenario 1 — Customer Support Resolution Agent

Built with the Claude Agent SDK. It handles difficult requests: returns, billing disputes,
account problems. It uses four MCP tools: `get_customer`, `lookup_order`, `process_refund`,
`escalate_to_human`. The goal is **80%+ first-contact resolution**, while knowing when to pass a
case to a human.

**Domains:** 1 (Agentic Architecture), 2 (Tool Design & MCP), 5 (Context & Reliability)

**Expect questions about:**
- Blocking `process_refund` until identity is verified → programmatic enforcement
- The agent confusing `get_customer` and `lookup_order` → tool descriptions
- Escalating the wrong cases → explicit criteria + few-shot. Never sentiment or confidence
- Refunds above a limit → tool call interception hook ($500)
- Several matching customers → ask for another identifier
- A "case facts" block for amounts, dates, order numbers
- A structured handoff summary for the human agent

**Quick answers:** money → hooks. Wrong tool → descriptions. Escalation → criteria + few-shot.
Long order results → trim the fields.

---

## Scenario 2 — Code Generation with Claude Code

A team uses Claude Code for writing code, refactoring, debugging, and documentation. They need
custom slash commands, CLAUDE.md configuration, and to know when to use plan mode.

**Domains:** 3 (Claude Code Configuration), 5 (Context & Reliability)

**Expect questions about:**
- Where a shared `/review` command lives → `.claude/commands/`
- Why a teammate does not get the instructions → user-level CLAUDE.md
- Conventions for test files spread across folders → `.claude/rules/` with globs
- Plan mode for microservice restructuring or a library migration
- Direct execution for a single-file fix
- `context: fork`, `allowed-tools`, `argument-hint` in SKILL.md
- `/memory`, `/compact`, the Explore subagent, scratchpad files

**Quick answers:** "every developer when they clone" → project scope. "Spread throughout" → glob
rules. "Architectural" or "dozens of files" → plan mode.

---

## Scenario 3 — Multi-Agent Research System

A coordinator gives work to specialised subagents: web search, document analysis, synthesis, and
report generation. The system produces detailed reports **with citations**.

**Domains:** 1 (Agentic Architecture), 2 (Tool Design & MCP), 5 (Context & Reliability)

**Expect questions about:**
- The report misses part of the topic → the coordinator's split was too narrow
- A subagent times out → structured error context, not a generic message
- Synthesis needs to check facts often → a small `verify_fact` tool
- Running subagents in parallel → several Task calls in one response; `allowedTools` includes
  `"Task"`
- Keeping claim-source links through synthesis
- Two sources disagree → record both with their sources
- Publication dates are required, so old and new numbers are not mistaken for a contradiction
- Marking coverage gaps in the final report

**Quick answers:** missing coverage → the coordinator. A failure → structured context + partial
results. A conflict → record both, never choose one.

---

## Scenario 4 — Developer Productivity with Claude

An agent helps engineers explore unfamiliar codebases, understand old systems, generate
boilerplate, and automate repetitive work. It uses the built-in tools (Read, Write, Bash, Grep,
Glob) and MCP servers.

**Domains:** 2 (Tool Design & MCP), 3 (Claude Code Configuration), 1 (Agentic Architecture),
5 (Context Management — scratchpads, `/compact`, subagents for long sessions)

**Expect questions about:**
- Grep or Glob?
- Edit cannot find unique text → use Read + Write
- Exploring step by step: Grep to find entry points, then Read to follow imports
- MCP scoping: `.mcp.json` or `~/.claude.json`, and `${VAR}` expansion
- The agent prefers built-in Grep over a better MCP tool → improve the MCP tool description
- MCP **resources** as content catalogues, to avoid exploratory calls
- A community MCP server or a custom one? (Jira → use the community server)
- Long sessions losing detail → scratchpad files, subagents, `/compact`
- Crash recovery with manifests

**Quick answers:** inside files → Grep. File paths → Glob. Edit fails → Read + Write. Standard
integration → community server.

---

## Scenario 5 — Claude Code for Continuous Integration

Claude Code runs inside a CI/CD pipeline: automatic code review, test generation, and pull
request feedback. The feedback must be useful, with **few false alarms**.

**Domains:** 3 (Claude Code Configuration), 4 (Prompt Engineering & Structured Output)

**Expect questions about:**
- The pipeline hangs → `-p` / `--print`
- Output a script can read → `--output-format json` + `--json-schema`
- Too many false alarms → specific criteria, not "be conservative"
- Inconsistent depth on a 14-file pull request → one pass per file + one pass across files
- Batch or real-time? (blocking check = real-time; overnight report = batch)
- Duplicate comments after a new commit → include earlier findings, report only new ones
- Duplicate tests → give it the existing test files
- CLAUDE.md holding testing standards and fixture conventions
- Reviewing code the same session wrote → use an independent instance
- A `detected_pattern` field to analyse dismissed findings

**Quick answers:** hangs → `-p`. Inconsistent depth → split the passes. False alarms → specific
criteria. Someone is waiting → real-time.

---

## Scenario 6 — Structured Data Extraction

The system extracts information from unstructured documents, checks it with JSON schemas, keeps
accuracy high, handles edge cases, and sends results to other systems.

**Domains:** 4 (Prompt Engineering & Structured Output), 5 (Context & Reliability)

**Expect questions about:**
- The model invents values for required fields → make the fields optional and nullable
- Unknown document type with several schemas → `tool_choice: "any"`
- Forcing `extract_metadata` to run first → forced tool selection
- Enum with `"other"` + detail; `"unclear"` for ambiguous cases
- Retry with specific errors; and when retry cannot help (information is not in the document)
- Semantic vs syntax errors (`calculated_total` vs `stated_total`, `conflict_detected`)
- A batch of 100 documents, `custom_id`, resubmitting only the failures, splitting long documents
- SLA arithmetic (submit every 4 hours for a 30-hour SLA)
- 97% average accuracy hiding one bad document type
- Stratified sampling of high-confidence extractions
- Field-level confidence, calibrated with labelled data
- Few-shot examples for documents with different structures

**Quick answers:** invented values → nullable. Unknown type → `any`. Missing information → retry
will not help. 97% → analyse by segment.

---

## One pattern across all six

**Domain 5 appears in four of the six scenarios**, even though it is only 15% of the exam.
Reliability ideas connect everything.

So if you are stuck between two answers, ask which one handles reliability better: structured
errors, preserved facts, or calibrated human review. That often decides it.

---

## What this means on exam day

Because the questions are self-contained, **do not spend four minutes reading each scenario
story.** Skim it for the tool names and the goal, then go straight to the questions. If a question
needs a detail from the story, that detail is repeated in the question itself.

A candidate who passed finished the whole exam in **90 of the 120 minutes**. Time is adequate but
not generous. Reading four stories carefully would spend a quarter of it for no gain.
