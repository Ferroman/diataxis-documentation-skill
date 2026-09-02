# Worked example

One real run, anonymised. Every rule in this skill came from something that
happened here.

## The input

A 499-line internal specification in a personal wiki, proposing a new access
model for a large source-control organisation. It served four purposes at once:

- an audit of the current state, with measurements (**findings**);
- an argument about how the platform's permission primitives actually behave
  (**explanation**);
- tables of teams, grants and config-file contents (**reference**);
- an ordered rollout with open decisions (**a plan**).

Sections were numbered, cross-references were `§n`, prose was hard-wrapped, and
four other notes linked to it.

The request: "create proper documentation", naming Diátaxis and a house
documentation-framework note, with the instruction *use ASD-STE100 for clarity
but prioritise detail preservation*.

## What was done

**Checked inbound links first.** `grep -rl` found four notes pointing at the
original. That settled the hub question before it was asked: the original path
had to survive, so the original file becomes the overview.

**Asked the structural question.** Two questions in one call, with file-tree
previews: folder + hub versus one document versus flat siblings; and — because
the model was a *proposal*, with nothing built — whether to write the how-tos now
as target-state. Both recommendations were taken. Asking cost one turn and
avoided building the wrong deliverable.

**Split into seven documents:** the hub at its original path, then findings,
explanation, two reference documents, a plan, and a procedures document filed
with the organisation's other procedures rather than in the new folder. Each
procedure carried a callout naming the rollout step it depended on, because none
of it existed yet.

**Then three corrections, all arriving mid-turn:**

- *"do not use numbering in sections"* — every `## 1. Foo` lost its number, and
  every `§4` became a link to a named heading.
- *"do not use line length limit for documents"* — all seven files unwrapped.
  `scripts/unwrap.py` exists because of this.
- *"no need for diagram where simple list will suffice"* — all six diagrams
  removed. Every one reduced cleanly to a list or a table, including the one that
  looked most defensible: a three-condition decision tree, which became a
  three-item numbered list and read better.

Three corrections in one session, all about form rather than content, is the
signal that the defaults in [house-style.md](house-style.md) are worth having.

**Generated a per-item document.** The design applied a config-file pattern
across more than a hundred items, and the user asked for the specific file per
item rather than the pattern alone. It was built by a Python script from a data
table, with an index at the top. That mattered twice over: two later decisions
each changed one field across every entry, and both were re-run in seconds.

**Writing those entries exposed two contradictions in the source.** The pattern
read fine in the abstract and stopped working on specific items — one rule, read
carefully, locked a team out of its own repository; another item was assigned to
two different shapes in two different tables. Both were flagged in place as open
questions rather than silently decided.

**Answered a design question with evidence, not deference.** Asked why one item
required two approvals, the honest answer was that the source asserted it with a
one-line rationale that did not survive contact with the roster: the owning group
had three people, so "two approvals" meant "two of three, and both of the others
whenever one of them is the author". That produced a change to the model, not
just to the prose.

**Published for the audience.** A summary page for the teams, written from the
reader's side, then the same content as a wiki note with tables in place of the
page's stat rows and native callouts in place of its HTML ones.

## The numbers

499 lines in, 3 776 lines out across 9 documents. 246 links, none broken. Zero
inline-code tokens, handles or link targets from the original missing from the
new set.

## What would have gone wrong without the skill

- Naming the parts `Audit findings` and `Rollout plan` — ambiguous across the
  whole wiki, and unreadable in backlinks.
- Moving the original into the new folder, breaking four inbound links.
- Keeping section numbers, which cannot survive a split.
- Hand-writing a hundred entries, then hand-editing them twice.
- Hard-wrapping at 92 columns, because a neighbouring convention said to.
- Six diagrams that each restated the table above them.
- Silently picking one side of the two contradictions, shipping a config rule
  that locks a team out of its own repository.
