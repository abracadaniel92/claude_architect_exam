# The Recommended Courses — Which to Take, Which to Skip

The Partner Academy recommends seven courses.

- **Two are not tested on this exam at all.**
- **Two are too basic for this exam.**
- **One is only partly useful.**
- **Two are worth your time.**

Choosing correctly saves you several days.

What decides this: Section 6 (Detailed Objectives) and Section 17 (In-Scope and Out-of-Scope
Topics) of the exam guide. Not the course catalogue.

---

## ✅ Take — Claude Code in Action (Level 200)

> *Integrate Claude Code into development workflows — context management, hooks, custom
> commands, and the Agent SDK.*

**This is the most useful course on the list.** Its four topics cover three exam domains:

| Course topic | Domain | Weight |
|---|---|---|
| Custom commands, workflows | 3 — Claude Code Configuration | 20% |
| Hooks, Agent SDK | 1 — Agentic Architecture | 27% |
| Context management | 5 — Context & Reliability | 15% |

That is about **62% of the exam**. Take this one first.

**Pay attention to these** — all are tested:
- `PostToolUse` hooks (change results) vs interception hooks (block calls)
- The Task tool, and `allowedTools` needing `"Task"`
- `.claude/commands/` vs `~/.claude/commands/`
- SKILL.md frontmatter: `context: fork`, `allowed-tools`, `argument-hint`
- `-p` / `--print`, `--output-format json`, `--json-schema`
- `/memory`, `/compact`, `--resume`, `fork_session`, the Explore subagent

**This course replaces:** most of Exercise 2, and the hooks part of Exercise 1.

---

## ✅ Take — Introduction to Model Context Protocol (Level 200)

> *Build MCP servers and clients from scratch using Python. Master tools, resources, and prompts
> to connect Claude with external services.*

This covers Domain 2 (18%).

Note the word **resources** in the description. The exam tests MCP resources specifically: they
show the agent **content catalogues** (issue lists, documentation structures, database schemas)
so it does not need exploratory tool calls. Most people learn MCP tools and ignore resources. Do
not skip that part.

**Pay attention to:**
- The `isError` flag and structured error responses
- How description quality affects tool selection
- Server configuration

**The course probably will not cover these tested items.** Get them from the notes:
- `.mcp.json` (project) vs `~/.claude.json` (user)
- `${VAR}` environment variable expansion
- The four error categories: transient, validation, business, permission
- The "18 tools vs 4–5" guidance

**This course replaces:** the tool-design half of Exercise 1.

---

## ⚠️ Take only parts — Building with the Claude API (Level 100–200)

> *Authentication, prompt engineering, and evaluations through tool use, RAG, agents, and
> production patterns.*

Three of its six topics are **not tested**:

| Topic | Status |
|---|---|
| Authentication | ❌ Out of scope: "Claude API authentication, billing, or account management" |
| RAG | ❌ Not in this exam. It belongs to the Professional exam |
| Evaluations | ❌ Not in this exam. It belongs to the Professional exam |
| Prompt engineering | ✅ Domain 4 (20%) |
| Tool use | ✅ Domains 2 and 4 |
| Agents | ✅ Domain 1 (27%) |
| Production patterns | ~ Depends what it covers |

**Take:** tool use, prompt engineering, agents. **Skip the rest.**

**Pay attention to:**
- `tool_use` with JSON schemas for reliable structured output
- `tool_choice`: `auto`, `any`, forced
- Handling `stop_reason`
- The Message Batches API: `custom_id`, 24-hour window, 50% cheaper, no speed guarantee

---

## ❌ Skip — Claude with Amazon Bedrock (100–200)
## ❌ Skip — Claude on Google Cloud (100–200)

Section 17 of the guide lists as out of scope: **"Specific cloud provider configurations (AWS,
GCP, Azure)."**

Also out of scope, and covered by these courses: rate limits, quotas, API pricing calculations,
and deploying or hosting MCP servers (infrastructure, networking, containers).

These are good courses for your job. They are worth **zero points** on this exam.

---

## ❌ Skip — AI Fluency: Framework & Foundations (100)
## ❌ Skip — Claude 101 (100)

These are Level 100 general-use courses. This exam expects 6+ months of hands-on work with the
Agent SDK, Claude Code, MCP, and the API.

Also, the ethics and safety topics in AI Fluency overlap the out-of-scope list: Constitutional
AI, RLHF, and safety training methods are not tested.

Skim them if you want the vocabulary. Do not plan time for them.

---

## The updated schedule, with courses included

The courses **replace** exercise time. They do not add to it.

| Days | Study | Hands-on |
|---|---|---|
| 1 | Answer patterns, skim notes | Practice Set 1 |
| 2–4 | Domain 1 notes | **Claude Code in Action** — Agent SDK + hooks · Domain 1 drill |
| 5–6 | Domain 2 notes | **Intro to MCP** — tools, resources, errors · Domain 2 drill |
| 7–9 | Domain 3 notes | **Claude Code in Action** — commands, context · Exercise 2 · Domain 3 drill |
| 10 | — | Set 2, then list your weak domains |
| 11–13 | Domain 4 notes | **Building with the Claude API** — tool use + prompt engineering only · Exercise 3 · Domain 4 drill |
| 14–15 | Domain 5 notes | Exercise 4 · Domain 5 drill |
| 16 | Scenarios | Recreate the Sample Q7 coverage failure |
| 17 | Weak domains | — |
| 18 | — | Set 3 (timed) |
| 19 | Review mistakes | — |
| 20 | Blueprint and scope lists | Rest |

---

## When a course and the guide disagree

**Courses teach the product. The exam tests the guide's description of the product.**

- When a course goes **deeper** than the guide (Bedrock model IDs, RAG chunking, evaluation
  design, streaming, prompt caching internals) — that is not tested.
- When the guide states something a course skips — **the guide wins**.

Here are things you will probably not learn from any course, but which are tested:

- `allowedTools` must include `"Task"` before a coordinator can start subagents
- The Batches API has **no speed guarantee** and no multi-turn tool calling
- **Required** schema fields make the model invent values. Make them nullable
- Strict schemas stop **syntax** errors, but not **semantic** ones
- Self-reported confidence is wrong for escalation, but acceptable for routing review work — only
  when calibrated with labelled data
- A bigger context window does **not** fix attention dilution

If you are unsure during a course, check the objective in `notes/domain-N-*.md`. If it is not
listed there as a knowledge or skill statement, it is not on the exam.
