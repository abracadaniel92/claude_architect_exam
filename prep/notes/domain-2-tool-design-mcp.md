# Domain 2 — Tool Design & MCP Integration (18%)

About 11 of the 60 questions come from here. There are 5 task statements.

Two ideas run through the whole domain:

1. **Tool descriptions are how the model chooses a tool.** Bad descriptions cause wrong choices.
2. **Errors must contain enough detail for the agent to decide what to do next.**

---

## 2.1 Designing tool interfaces

### The most important fact in this domain

Tool descriptions are the main way the model decides which tool to use. If a description is
short, the model cannot tell similar tools apart.

### What a good description contains

- What the tool does
- **Which input formats** it accepts
- **Example queries**
- **Edge cases**
- **When to use it instead of a similar tool**

### The failure to remember

Descriptions that are unclear or overlap cause **misrouting** (the model picks the wrong tool).

The guide's example: `analyze_content` and `analyze_document` have almost the same description.

### Three fixes, from cheapest to most expensive

1. **Make the descriptions longer and clearer.**
   This is the answer when the question asks for the "most effective first step" (Sample Q2).

2. **Rename the tool and rewrite its description**, so the two no longer overlap.
   Guide example: rename `analyze_content` to `extract_web_results`, with a web-specific
   description.

3. **Split one general tool into several specific tools**, each with a defined input and output.
   Guide example: split `analyze_document` into `extract_data_points`, `summarize_content`, and
   `verify_claim_against_source`.

### Also check the system prompt

Words in the system prompt can create unwanted links to tools. This can override good
descriptions. The guide calls this "keyword-sensitive instructions."

Example: if the system prompt says "your main purpose is to produce reports," the model may send
every request containing the word "report" to `generate_report`.

### One thing to be careful about

Combining several tools into one general tool (for example, one `lookup_entity` that accepts any
ID) is a **valid design choice**. But it is the wrong answer when the question asks for a "first
step." It costs more effort than fixing the descriptions.

---

## 2.2 Structured error responses for MCP tools

MCP uses an **`isError` flag** to tell the agent that a tool failed.

### The four error categories

| Category | Example | What the agent should do |
|---|---|---|
| **Transient** | Timeout, service is down | Retry |
| **Validation** | Bad input | Fix the input, then retry |
| **Business** | The action breaks a policy | Explain it to the user. Do not retry |
| **Permission** | Not allowed | Escalate or explain |

### Why one generic error is wrong

A message like `"Operation failed"` gives the agent nothing. It cannot decide whether to retry,
explain, or escalate.

On the exam, any answer offering a single generic error message is wrong.

### What to return instead

```json
{
  "isError": true,
  "errorCategory": "transient",
  "isRetryable": true,
  "message": "A clear sentence a person can read"
}
```

For a business rule violation, include `isRetryable: false` **and a customer-friendly
explanation**, so the agent can explain the policy to the user. (The guide's prose sometimes
spells the field "retriable" — same field, same meaning.)

### Local recovery in subagents

A subagent should fix transient failures itself. It only reports failures it **cannot** fix. When
it reports one, it includes **partial results and what it tried**.

### Access failure is not the same as an empty result

- **Access failure:** the tool could not reach the service. The agent may need to retry.
- **Valid empty result:** the search worked, and found nothing.

Treating these as the same thing is a wrong answer on the exam.

---

## 2.3 Which agent gets which tools, and `tool_choice`

### Too many tools is a real problem

The guide gives a number: **18 tools instead of 4–5** makes tool selection unreliable. More
tools means a harder decision.

Also: an agent with tools outside its job will misuse them. Example: a synthesis agent that
starts doing web searches.

### Scoped cross-role tools

Sometimes an agent needs one small ability from another role. Give it a **narrow tool**, not the
full set.

Sample Q9 in the guide: the synthesis agent needs to check facts. 85% of checks are simple
(dates, names, numbers). Give it a small `verify_fact` tool for those. The other 15% still go
through the coordinator.

This is **least privilege** applied to tools: give each agent only what it needs.

### Replace general tools with limited ones

Guide example: replace `fetch_url` (which can fetch anything) with `load_document` (which
validates that the URL is a document).

### `tool_choice` values

| Value | What happens |
|---|---|
| `{"type": "auto"}` | The model decides. It **may return text instead of calling a tool** |
| `{"type": "any"}` | The model **must** call a tool, but chooses which one |
| `{"type": "tool", "name": "..."}` | The model must call **that specific** tool |
| `{"type": "none"}` | The model cannot use tools. *Real, but the guide does not test it* |

Short version: **auto may talk · any must act · forced picks the actor.**

**How the exam uses them:**
- `"any"` — you have several extraction schemas and do not know the document type yet. Or the
  model keeps replying with text instead of extracting.
- Forced — you need one specific tool to run first. Example: run `extract_metadata` before any
  enrichment tool. Later steps happen in the next turns.

---

## 2.4 Setting up MCP servers

### Where configuration files go

| Scope | File | Use it for |
|---|---|---|
| **Project** | `.mcp.json` (in the repository) | Shared team tools. Version-controlled |
| **User** | `~/.claude.json` | Personal or experimental servers |

Learn this table. It appears often.

### Keeping secrets out of the repository

Use **environment variable expansion** in `.mcp.json`, like `${GITHUB_TOKEN}`. The file can be
committed. The secret is not in it.

### All servers work at the same time

Tools from every configured server are discovered when the connection opens. Project servers and
personal servers are available together.

### Tools vs resources

- **Tools** = actions the agent can take.
- **Resources** = a way to show the agent **content catalogues**: lists of issues, documentation
  structures, database schemas.

Resources let the agent see what data exists **without making exploratory tool calls** first.

### Two judgement questions the exam likes

1. **Improve MCP tool descriptions** so the agent understands what they can do. Otherwise it
   prefers built-in tools like Grep, even when the MCP tool is better.
2. **Use an existing community MCP server** for standard integrations such as Jira. Build a
   custom server only for workflows specific to your team.

---

## 2.5 The built-in tools

| Tool | What it does | Choose it when |
|---|---|---|
| **Grep** | Searches **inside** files | Finding function callers, error messages, import statements |
| **Glob** | Matches **file paths** | Finding files by name or extension, such as `**/*.test.tsx` |
| **Read** | Loads a whole file | Following imports, tracing how code works |
| **Write** | Writes a whole file | When Edit cannot find unique text |
| **Edit** | Changes part of a file, by matching unique text | Small, precise changes |
| **Bash** | Runs shell commands | — |

**Remember:** Grep looks inside files. Glob looks at file names and paths. This pair is confused
often.

### When Edit fails

If Edit cannot find unique text to match, use **Read + Write** instead. This is a direct exam
fact.

### How to explore a codebase

Do not read every file first. Instead:
1. Use **Grep** to find entry points.
2. Use **Read** to follow imports and trace the flow.
3. Repeat.

### Tracing a function through wrapper modules

First find all the exported names. Then search for each name across the codebase.

---

## Quick review list for Domain 2

1. Tool descriptions decide tool choice. Improve them before anything else.
2. A description needs: inputs, examples, edge cases, and when to use it instead of a similar tool.
3. Errors carry `errorCategory` + `isRetryable` + a readable message.
4. Four categories: transient, validation, business, permission.
5. An access failure is not an empty result.
6. 18 tools is bad. 4–5 is good. Add small cross-role tools for the common case.
7. `auto` may return text · `any` must call something · forced calls a named tool.
8. `.mcp.json` = project and shared. `~/.claude.json` = personal.
9. `${VAR}` keeps secrets out of the repository.
10. MCP **resources** are content catalogues. They reduce exploratory calls.
11. Grep = inside files. Glob = file paths. Edit fails on unclear matches → Read + Write.
