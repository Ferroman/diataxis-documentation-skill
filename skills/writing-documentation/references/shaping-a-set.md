# Shaping a document set

## The structural question — ask it first

Splitting is materially different work from restructuring, so it is one of the
few things worth blocking on. Ask once, with previews showing the resulting file
tree, offering three options:

- **Folder + hub** (usually the right answer). The original document stays at its
  path as a short overview; the mode-split parts go in a sibling folder named
  after it.
- **One restructured document.** Reordered into modes, nothing to relink, but the
  file keeps serving several goals at once.
- **Flat siblings.** Separate documents alongside the original,
  `<Topic> - <part>`.

Ask a second question in the same call when the subject is a *proposal* rather
than something that exists: do the task-oriented how-tos get written now as
target-state, or deferred until the thing is built? Procedures for an unbuilt
system are fiction unless they are labelled.

## Splitting by mode

| Mode | Answers | Typical name |
|---|---|---|
| Overview / hub | "what is this and where do I go?" | the original document |
| Findings / research | "what did we measure?" | `<Topic> audit findings` |
| Explanation | "why is it shaped this way?" | `<Topic> design rationale` |
| Reference | "what is the value for X?" | `<Topic> matrix`, `<Topic> per item` |
| Plan | "what happens next?" | `<Topic> rollout plan` |
| How-to | "how do I do X?" | goes to wherever procedures live |
| Announcement | "what changes for me?" | written for the audience, not the author |

Two of these are commonly missed. **Findings are not explanation** — the audit
data and the argument built on it want separate documents, because one is
re-measured and the other is re-argued. And **a plan is not a how-to** — a
rollout sequence happens once; a procedure happens every time.

## Naming

Give every part a **globally unique, self-describing name**:
`platform access audit findings`, never `Audit findings`. In a wiki or vault,
links resolve by basename across the whole tree, so a generic name is ambiguous
the moment a second one appears, and it reads as noise in backlinks and graph
views. The containing folder does not scope the name.

## The hub

Shortest document in the set. It carries:

- what the thing is, and who asked for it;
- a status callout when the subject is proposed rather than live;
- the one-paragraph result;
- a **which document answers which question** table, one row per part;
- three to five things worth knowing without reading further;
- the related links.

Nothing that belongs in a part. If the hub grows past roughly 120 lines, it has
absorbed content from somewhere.

## Cross-references

Link to the named heading. Never `§4`, never "see section 3 above". Headings are
the addressing scheme, which is why they must not be numbered.

## Per-item reference documents

When the subject applies a pattern across many items — a config file per service,
an owner file per repository, a runbook entry per component — produce **the
specific item, not just the pattern**, in its own document. Two rules:

1. **Generate it from a data table with a script.** Keep the script; a later
   decision will change one field across every entry, and hand-edited entries
   drift. Hand-writing a hundred near-identical blocks guarantees inconsistency.
2. **Give it an index table** at the top: one row per item, the fields somebody
   would scan for, and a link to the entry.

Writing these entries is also the best contradiction detector in the workflow.
The pattern reads fine in the abstract and stops working when applied to a
specific item. That is a finding, and it belongs in the document as a flagged
open question rather than being quietly decided.

## When NOT to split

- The document has one purpose and is long because the subject is large.
- It is a log, a scratchpad, or a meeting record.
- Splitting would produce parts that are only a pointer.

## Audience

A summary aimed at other people is a deliverable, not a chat answer. When asked
to produce something shareable, write it from the reader's side: what changes for
*them*, what they must do, and when they will feel it.

Answer the objection they will actually have, in its own section, rather than as
a defensive aside. For most process changes that objection is "will this slow me
down" — and if the honest answer is "yes, a little, here", say so and say what
you did to bound it.
