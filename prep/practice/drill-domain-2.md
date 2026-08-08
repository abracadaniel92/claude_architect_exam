# Domain 2 Drill — Tool Design & MCP Integration (15 questions)

**18% of the exam**, about 11 of 60 questions.

You scored 2 out of 2 in Set 1. That is only two questions, which is not enough to know if this
domain is strong. This drill is harder. Several questions ask you to choose between two
techniques that are **both real** and **both in the guide**.

**The questions use exam-level English.** The explanations are in simple English.

Time: 30 minutes. Answers below — cover them while you work.

---

**Q1.** Your research agent has a tool `analyze_document` described as: *"Analyzes a document and
returns useful information."* It is used for three different jobs — pulling specific figures out
of tables, producing an executive summary, and checking whether a claim is supported by a
source. Output quality is erratic and callers can't predict what they'll get back. What is the
most effective structural fix?

A. Expand the description to cover all three use cases with example queries for each.
B. Split it into `extract_data_points`, `summarize_content`, and `verify_claim_against_source`, each with a defined input/output contract.
C. Add an `analysis_type` enum parameter with three values and describe each in the parameter description.
D. Add few-shot examples in the system prompt showing each of the three usage patterns.

---

**Q2.** Two tools exist: `analyze_content` (*"Analyzes content and extracts key information"*) and
`analyze_document` (*"Analyzes documents and extracts key information"*). `analyze_content` is
intended only for web search result pages. Misrouting is frequent. What is the appropriate fix?

A. Merge them into a single `analyze` tool that accepts a `source_type` parameter.
B. Rename `analyze_content` to `extract_web_results` and rewrite its description to be web-specific.
C. Add a system prompt rule: "Use `analyze_content` only for web results."
D. Remove `analyze_content` and route web pages through `analyze_document`.

---

**Q3.** Tool descriptions in your system are detailed and clearly differentiated. Nonetheless the
agent routes nearly every request mentioning the word "report" to `generate_report`, even when
the user is asking to *read* an existing report. Your system prompt contains the line: *"Your
primary purpose is to produce reports for stakeholders."* What should you investigate?

A. Whether `generate_report`'s description needs a stronger "when not to use" section.
B. Whether the system prompt's keyword-sensitive wording is creating an unintended tool association that overrides the descriptions.
C. Whether the agent has too many tools for reliable selection.
D. Whether few-shot examples are needed for read-vs-generate disambiguation.

---

**Q4.** A customer requests a refund on an order that is 95 days old; your policy window is 90
days. The `process_refund` MCP tool must reject this. What should it return?

A. `{"isError": true, "message": "Operation failed"}`
B. `{"isError": true, "errorCategory": "business", "retriable": false, "message": "Refunds are available within 90 days of purchase. This order was placed 95 days ago."}`
C. `{"isError": true, "errorCategory": "validation", "isRetryable": true, "message": "Invalid refund request"}`
D. A successful response with `refund_amount: 0`, letting the agent infer the rejection.

---

**Q5.** Your `search_knowledge_base` MCP tool needs to distinguish two outcomes: the search index
was unreachable, and the search ran successfully but matched nothing. Currently both return an
empty array. Why does this matter? **(Select two.)**

A. The agent cannot decide whether a retry is appropriate.
B. The agent may tell the user no information exists when the index was simply down.
C. Empty arrays consume unnecessary context tokens.
D. The coordinator cannot annotate coverage gaps accurately in the final output.

---

**Q6.** A document-analysis subagent calls an MCP tool that fails with a rate-limit error. The
subagent waits and retries; the second attempt succeeds. Separately, a different call fails
because the requested document requires permissions the subagent does not have, and no retry
will help. What should the subagent report to the coordinator?

A. Both failures, so the coordinator has complete visibility.
B. Neither; the subagent should return only its final analysis.
C. Only the permission failure, including what was attempted and any partial results.
D. Only the rate-limit failure, since permission errors should be escalated to a human directly.

---

**Q7.** Your synthesis agent has 18 tools. Selection has become erratic and it sometimes performs
its own web searches instead of synthesizing. Which statement best explains the mechanism?

A. Tool schemas consume context, leaving less room for the findings it must synthesize.
B. Giving an agent access to too many tools degrades selection reliability by increasing decision complexity, and agents with tools outside their specialization tend to misuse them.
C. The tool descriptions are individually adequate but collectively contradictory.
D. The model's attention dilutes across tool definitions the same way it dilutes across files in a large review.

---

**Q8.** Evaluation shows your synthesis agent needs verification on 40% of its claims: 85% of
those are simple fact-checks (dates, names, statistics) and 15% require multi-source
investigation. Currently every verification round-trips through the coordinator to the web
search agent. Which design best balances overhead against separation of concerns?

A. Give the synthesis agent the full web search tool set so it can verify anything directly.
B. Give the synthesis agent a scoped `verify_fact` tool for simple lookups; route complex verifications through the coordinator as today.
C. Have the synthesis agent batch all verification needs and submit them to the coordinator in one call at the end of its pass.
D. Have the web search agent pre-cache extra context around every source so synthesis rarely needs to verify.

---

**Q9.** Your agent has a `fetch_url` tool. It has begun fetching arbitrary URLs it encounters in
document text, including tracking links and unrelated pages. What is the appropriate change?

A. Add a system prompt instruction listing which URL patterns are permitted.
B. Replace `fetch_url` with a constrained `load_document` tool that validates document URLs.
C. Add a `PostToolUse` hook that discards responses from non-document URLs.
D. Remove the fetch capability and require documents to be pre-loaded as resources.

---

**Q10.** Your extraction pipeline must always run `extract_metadata` before any enrichment tool,
because enrichment depends on the document type that metadata determines. What configuration
enforces this?

A. `tool_choice: {"type": "any"}` on the first request.
B. `tool_choice: {"type": "tool", "name": "extract_metadata"}` on the first request, then process subsequent steps in follow-up turns.
C. Order `extract_metadata` first in the `tools` array.
D. A system prompt instruction stating that `extract_metadata` must always be called first.

---

**Q11.** Your team shares a Jira MCP server across the project. Individual developers also want a
personal, experimental Notion server that shouldn't affect teammates. Where does each go?

A. Both in `.mcp.json`, with the Notion one commented out by default.
B. Jira in `.mcp.json`; Notion in `~/.claude.json`.
C. Jira in `~/.claude.json`; Notion in `.mcp.json`.
D. Both in `~/.claude.json`, with the Jira config distributed via the team wiki.

---

**Q12.** Your `.mcp.json` needs a GitHub personal access token to authenticate its MCP server, and
the file is committed to the repository. What is the correct approach?

A. Commit the token and rotate it monthly.
B. Use environment variable expansion — `${GITHUB_TOKEN}` — in `.mcp.json`.
C. Move the server config to `~/.claude.json` so the token isn't committed.
D. Store the token in CLAUDE.md, which is excluded from version control.

---

**Q13.** Your agent repeatedly makes exploratory tool calls to discover what issues exist in your
tracker, what documentation pages are available, and what tables the database has — burning
turns before doing real work. Which MCP capability addresses this?

A. Increasing the tool count so each discovery has a dedicated tool.
B. Exposing content catalogs (issue summaries, documentation hierarchies, database schemas) as MCP **resources**.
C. Caching prior tool results in a scratchpad file the agent reads first.
D. Enhancing each tool's description to explain what data it can return.

---

**Q14.** Your team needs Jira integration for a standard workflow — reading issues, transitioning
status, adding comments. A well-maintained community MCP server exists. Your team also has a
bespoke internal deployment-approval workflow with no equivalent anywhere. What should you do?

A. Build custom servers for both, for consistency and control.
B. Use the community server for Jira; build a custom server for the deployment-approval workflow.
C. Use the community server for Jira and implement deployment approvals as built-in Bash tool calls.
D. Fork the community Jira server and extend it to cover deployment approvals too.

---

**Q15.** You have an MCP tool `search_code_semantically` that returns ranked matches with context,
and the built-in `Grep`. Match each task to the right tool. **(Select two correct pairings.)**

A. "Find every caller of `processPayment`" → Grep
B. "Find all files matching `**/*.integration.test.ts`" → Grep
C. "Find the code responsible for retry behavior in checkout" → `search_code_semantically`
D. "Find the exact string `ERR_TIMEOUT_4471`" → `search_code_semantically`

---
---

# Answers

**Q1 — B.** The guide names this fix: split a general tool into specific tools with **defined
inputs and outputs** — `extract_data_points`, `summarize_content`, `verify_claim_against_source`.
The clue in the question is "callers can't predict what they'll get back." That is a contract
problem, not a description problem.
- **A** — a longer description for a tool that does three different jobs still returns three
  different, unpredictable outputs.
- **C** — **the strongest wrong answer.** A parameter with three values is real engineering. But
  one tool still has one output contract for three kinds of result, and it does not help the
  model choose. The guide's stated skill is splitting.
- **D** — few-shot examples cannot fix a structural problem.

**Q2 — B.** Renaming plus a specific description is the guide's fix for overlapping tools. Its own
example is `analyze_content` → `extract_web_results`, with a web-specific description.
- **A** — combining tools is a valid design, but it is more work than needed here. A
  `source_type` parameter also brings back the same confusion one level down.
- **C** — a system prompt rule on top of unclear descriptions. The guide warns that prompt wording
  creating tool links is itself a problem (see Q3).
- **D** — deletes a tool that has a real, separate purpose.

**Q3 — B.** The guide lists this as a skill: "reviewing system prompts for keyword-sensitive
instructions that might override well-written tool descriptions." The question gives you the
keyword — "reports" appears in both the system prompt and the tool name.
- **A** — the question says the descriptions are already detailed and clearly different.
- **C** — the question does not mention a tool-count problem.
- **D** — covers the prompt problem instead of fixing it.

**Q4 — B.** A business rule violation needs `retriable: false` **and a customer-friendly
explanation**, so the agent can explain the policy. Both parts are named skills in the guide.
- **A** — the generic error the guide rejects.
- **C** — wrongly labelled as validation **and** marked retryable. The agent will retry forever.
- **D** — hides a failure as a success. The agent cannot explain the policy.

**Q5 — A and B.** Telling access failures apart from empty results is what lets the agent decide
whether to retry (**A**) and stops it telling the user something false (**B**).
- **C** — true of any empty response, and not the point. Token cost is not why this matters.
- **D** — **close, and reasonable in a multi-agent system.** But marking coverage gaps is a
  Domain 5 synthesis topic, one level higher. This question is about a single tool's return
  value, where the direct effects are retry decisions and telling the user the truth.

**Q6 — C.** Subagents fix **transient failures themselves** and report only what they cannot fix
— including **what they tried and any partial results**. The rate limit was fixed locally. The
permission failure was not.
- **A** — fills the coordinator with noise about a problem that was already solved.
- **B** — hides an unsolved failure. The coordinator cannot mark the gap.
- **D** — the wrong way round. Permission errors go to the coordinator.

**Q7 — B.** Two separate reasons, both in the guide. Too many tools (18 instead of 4–5) makes the
decision harder and selection worse. And an agent with tools outside its job will misuse them.
The question shows both symptoms.
- **A** — sounds reasonable, but the guide blames decision complexity, not context space.
- **C** — nothing says the descriptions contradict each other.
- **D** — **attention dilution is a real exam idea, but it belongs to reviewing many files**
  (Domains 1 and 4). Using it here is the wrong reason for the right symptom.

**Q8 — B.** Least privilege applied to tools: give a small tool for the common 85%, and keep
coordination for the 15% that needs it.
- **A** — gives the synthesis agent too much and breaks separation of roles. This is what caused
  the problem in Q7.
- **C** — grouping all checks together creates delays, because later synthesis steps may depend
  on facts checked earlier.
- **D** — guessing in advance what synthesis will need to check does not work reliably.

**Q9 — B.** The guide names this skill: replace general tools with limited ones. Its own example
is exactly `fetch_url` → `load_document`, which validates that the URL is a document.
- **A** — a prompt rule on top of an ability the tool gives structurally.
- **C** — the fetch already happened. Filtering afterwards wastes the call and does not stop the
  behaviour.
- **D** — removes an ability that is needed.

**Q10 — B.** Forced tool selection guarantees one specific tool runs first. Later steps happen in
the following turns. This is the guide's stated use of `tool_choice: {"type": "tool", ...}`.
- **A** — `any` guarantees **some** tool is called, not **that** tool.
- **C** — the order of the `tools` array guarantees nothing.
- **D** — an instruction that fails sometimes, used for a hard requirement.

**Q11 — B.** `.mcp.json` at project level for shared team tools. `~/.claude.json` at user level
for personal or experimental servers. Both are found at connection time and work together.
- **A** — a commented-out server still puts personal configuration in the team's repository.
- **C** — exactly the wrong way round.
- **D** — gives up version control for the shared server, which is the reason `.mcp.json` exists.

**Q12 — B.** Environment variable expansion in `.mcp.json` is the guide's named way to handle
credentials without committing secrets.
- **A** — commits a secret. Never correct.
- **C** — **tempting.** It does avoid committing the token. But it also stops the server being
  shared with the team, which was the whole point. It solves the secret problem by throwing away
  the requirement.
- **D** — CLAUDE.md is normally committed, and it is not a place for credentials.

**Q13 — B.** MCP **resources** show content catalogues. The guide names issue summaries,
documentation structures, and database schemas. They let the agent see what data exists
**without exploratory tool calls**.
- **A** — more tools makes selection worse (Q7).
- **C** — scratchpad files save findings across context limits (Domain 5). They do not show what
  exists in an external system.
- **D** — better descriptions say what a tool **does**, not what data is **there**.

**Q14 — B.** Use existing community MCP servers for standard integrations. Build custom servers
only for workflows specific to your team. The question is written to match that sentence.
- **A** — rebuilds something that already exists.
- **C** — hides an approval workflow inside shell commands, losing the tool interface completely.
- **D** — ties your internal workflow to another project's release schedule and review process.

**Q15 — A and C.** **A** searches inside files for a specific name — that is Grep. **C** is a
conceptual question with no exact text to search for — that is semantic search.
- **B** — this is a **file path pattern**, which is Glob's job, not Grep's. Grep and Glob are the
  most confused pair in Domain 2.
- **D** — an exact text string. Grep is correct and cheaper. Using semantic search for an exact
  error code is the opposite version of the same mistake.

---

## Score

___ / 15 · Q5 and Q15 need two answers each. You need both to get the point.

- **Below 10** — read `notes/domain-2-tool-design-mcp.md` again. Focus on the four error
  categories and the `.mcp.json` vs `~/.claude.json` difference.
- **10–12** — check where your mistakes are. Tool design (Q1–Q3, Q7–Q9) or MCP configuration
  (Q11–Q14)? Practise that half.
- **13 or more** — your Set 1 result was real. Move to Domain 3.
