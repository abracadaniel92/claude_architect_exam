"""Build printable PDFs from the markdown study material.

Produces two files in the repository root:
  CCAR-F-study-pack.pdf          notes, plan, strategy, scenarios, exercises, drills
  CCAR-F-practice-questions.pdf  questions only - answer keys are deliberately excluded

Run:  python tools/make-study-pdfs.py
"""
import io
import os
import re

import markdown
from xhtml2pdf import pisa

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PREP = os.path.join(ROOT, "prep")

# The built-in Type1 fonts only cover Latin-1. Anything outside it renders as a black
# box, so every such character needs an explicit replacement. run() below asserts that
# none slip through unnoticed.
SUBS = {
    # arrows
    "→": "-&gt;", "←": "&lt;-",
    # box drawing, used in the agentic-loop diagram
    "─": "-", "│": "|", "└": "\\", "├": "|",
    # marks and boxes
    "✓": "[y]", "✗": "[n]", "✅": "[done]", "❌": "[no]",
    "☐": "[ ]", "⚠": "!", "️": "",
    # punctuation and maths
    "—": " - ", "–": "-", "·": "-", "…": "...",
    "≤": "&lt;=", "≥": "&gt;=", "×": "x",
    "“": '"', "”": '"', "‘": "'", "’": "'",
}

CSS = """
@page {
  size: a4 portrait;
  margin: 16mm 14mm 15mm 14mm;
  @frame footer { -pdf-frame-content: footer; bottom: 7mm; height: 8mm; }
}
body { font-family: Helvetica; font-size: 9.3pt; line-height: 1.42; color: #111; }
h1 { font-size: 17pt; margin: 0 0 2px 0; padding-bottom: 3px;
     border-bottom: 1.6pt solid #111; }
h2 { font-size: 12pt; margin: 15px 0 4px 0; color: #111; }
h3 { font-size: 10.2pt; margin: 11px 0 3px 0; color: #222; }
p  { margin: 0 0 6px 0; }
ul, ol { margin: 0 0 7px 0; padding-left: 15px; }
li { margin-bottom: 2.5px; }
table { border: 0.6pt solid #999; margin: 5px 0 9px 0; width: 100%; }
th { background: #E6E6E6; border: 0.5pt solid #999; padding: 3.5px 5px;
     font-size: 8.6pt; text-align: left; }
td { border: 0.5pt solid #BBB; padding: 3.5px 5px; font-size: 8.6pt;
     vertical-align: top; }
code { font-family: Courier; font-size: 8.4pt; background: #F0F0F0; }
pre { background: #F4F4F4; border-left: 2.5pt solid #999; padding: 5px 7px;
      font-family: Courier; font-size: 8pt; margin: 5px 0 8px 0; }
blockquote { border-left: 2.5pt solid #666; padding: 4px 9px; margin: 6px 0;
             background: #F6F6F6; }
hr { border: 0; border-top: 0.5pt solid #CCC; margin: 9px 0; }
strong { font-weight: bold; }
.newdoc { page-break-before: always; }
.cover h1 { border-bottom: none; font-size: 24pt; margin-bottom: 4px; }
.cover .sub { font-size: 11pt; color: #444; margin-bottom: 22px; }
.toc td { font-size: 9.5pt; border: none; border-bottom: 0.4pt solid #DDD;
          padding: 5px 4px; }
.note { border: 1.2pt solid #111; background: #EDEDED; padding: 7px 9px;
        margin: 10px 0; font-size: 9pt; }
"""

FOOTER = ('<div id="footer" style="text-align:center;font-size:7pt;color:#777">'
          'CCAR-F &nbsp;-&nbsp; {title} &nbsp;-&nbsp; page <pdf:pagenumber>'
          '</div>')


def sanitize(text):
    for a, b in SUBS.items():
        text = text.replace(a, b)
    # Safety net: anything still outside Latin-1 would print as a black box.
    # Report it loudly rather than shipping a broken page.
    leftovers = sorted({c for c in text if not _latin1(c)})
    if leftovers:
        print("  WARNING unmapped characters, add them to SUBS: " +
              " ".join("U+%04X" % ord(c) for c in leftovers))
        for c in leftovers:
            text = text.replace(c, "?")
    return text


def _latin1(ch):
    try:
        ch.encode("latin-1")
        return True
    except UnicodeEncodeError:
        return False


def render(md_text):
    """Markdown -> HTML fragment."""
    html = markdown.markdown(md_text, extensions=["tables", "fenced_code", "sane_lists"])
    return sanitize(html)


def read(rel):
    with io.open(os.path.join(PREP, rel), encoding="utf-8") as f:
        return f.read()


def strip_answers(md_text):
    """Cut a drill file at its answer key."""
    return re.split(r"\n#\s+Answers", md_text)[0].rstrip().rstrip("-").rstrip()


def build(outfile, title, subtitle, sections, intro_html=""):
    """sections: list of (heading, markdown_text)."""
    toc_rows = "".join(
        '<tr><td width="7%%">%d</td><td>%s</td></tr>' % (i + 1, h)
        for i, (h, _) in enumerate(sections))

    parts = [
        '<div class="cover"><h1>%s</h1><div class="sub">%s</div>' % (title, subtitle),
        intro_html,
        '<h2>Contents</h2><table class="toc">%s</table></div>' % toc_rows,
    ]
    for heading, md_text in sections:
        parts.append('<div class="newdoc">%s</div>' % render(md_text))

    doc = ("<html><head><meta charset='utf-8'><style>%s</style></head><body>%s%s</body></html>"
           % (CSS, FOOTER.format(title=title), "".join(parts)))

    path = os.path.join(ROOT, outfile)
    with open(path, "wb") as fh:
        result = pisa.CreatePDF(io.StringIO(doc), dest=fh, encoding="utf-8")
    if result.err:
        raise SystemExit("FAILED: %s (%d errors)" % (outfile, result.err))
    print("written: %-34s %6.0f KB" % (outfile, os.path.getsize(path) / 1024.0))


# --------------------------------------------------------------- study pack
STUDY_INTRO = """
<div class="note">
<b>How to use this pack.</b> Follow the calendar in section 1. Each day: 10 minutes of recall
drill, 50 minutes of new material from the domain notes, 45 minutes of practice questions from
the separate questions booklet, then 15 minutes reviewing what you got wrong.<br/><br/>
Read section 2 before anything else. It is worth more than any single fact.<br/><br/>
<b>The answer keys are not in this pack</b>, on purpose. Mark your practice on screen.
</div>
"""

build(
    "CCAR-F-study-pack.pdf",
    "Study Pack",
    "Claude Certified Architect - Foundations &nbsp;|&nbsp; exam Tue 25 August 2026",
    [
        ("The 15-day calendar", read("00-study-plan.md")),
        ("How the exam builds its questions", read("01-answer-patterns.md")),
        ("Domain 1 - Agentic Architecture (27%)", read("notes/domain-1-agentic-architecture.md")),
        ("Domain 2 - Tool Design and MCP (18%)", read("notes/domain-2-tool-design-mcp.md")),
        ("Domain 3 - Claude Code Configuration (20%)", read("notes/domain-3-claude-code-config.md")),
        ("Domain 4 - Prompts and Structured Output (20%)", read("notes/domain-4-prompt-structured-output.md")),
        ("Domain 5 - Context and Reliability (15%)", read("notes/domain-5-context-reliability.md")),
        ("The six exam scenarios", read("notes/scenarios.md")),
        ("Domain 4 daily fact drill", read("practice/daily-facts-domain-4.md")),
        ("Hands-on exercises", read("exercises/README.md")),
        ("Which courses to take and skip", read("02-course-map.md")),
    ],
    STUDY_INTRO,
)

# ----------------------------------------------------------- question booklet
Q_INTRO = """
<div class="note">
<b>No answers in this booklet.</b> That is deliberate. Write your answers on paper, then mark
them on screen against the answer files in <code>prep/practice/</code>.<br/><br/>
<b>The questions use exam-level English</b>, the same long formal style as the real exam.
Reading that style quickly is part of the test, so they are not simplified.<br/><br/>
Take each drill only <b>after</b> you have read that domain's notes. Taking one early wastes the
questions.<br/><br/>
<b>Timing:</b> Set 1 is 40 minutes. Each 15-question drill is 30 minutes. Watch the clock - the
real exam gives you about 2 minutes per question.
</div>
"""

build(
    "CCAR-F-practice-questions.pdf",
    "Practice Questions",
    "Claude Certified Architect - Foundations &nbsp;|&nbsp; no answer keys",
    [
        ("Set 1 - mixed, 20 questions", read("practice/set-01-questions.md")),
        ("Domain 1 drill - 15 questions", strip_answers(read("practice/drill-domain-1.md"))),
        ("Domain 2 drill - 15 questions", strip_answers(read("practice/drill-domain-2.md"))),
        ("Domain 3 drill - 15 questions", strip_answers(read("practice/drill-domain-3.md"))),
        ("Domain 4 drill - 15 questions", strip_answers(read("practice/drill-domain-4.md"))),
    ],
    Q_INTRO,
)
