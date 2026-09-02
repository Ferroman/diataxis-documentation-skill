---
name: writing-documentation
description: >-
  Write or restructure technical documentation of any kind, anywhere — a wiki or
  Obsidian note, a repository's docs/ or README, a Confluence page, a design doc.
  Use WHENEVER the user asks to "create proper documentation", "document this",
  "restructure this", "make this a real doc", "split this up", "write a
  guide/SOP/runbook/reference for X", or names diataxis.fr or ASD-STE100.
  Covers splitting a mixed-purpose document into a Diátaxis set, house writing
  style, generating per-item reference documents, surfacing contradictions in the
  source, and the verification that proves no fact was lost.
---

# Writing documentation

## Overview

Documents rot in one specific way. A document starts as a spec, absorbs findings,
grows a rollout plan, and ends up serving four purposes at once. Nobody can
maintain it, because any edit serves one purpose and damages another.

So the job is usually not "write a new document". It is **splitting one document
by purpose, without losing a fact and without breaking a single inbound link**.

The craft below is the same everywhere. Four things change with the target — link
syntax, front matter, where each kind of document lives, and which checker runs.
Those live in [references/targets.md](references/targets.md). Identify the target
before writing, and read its section.

The model is [Diátaxis](https://diataxis.fr/): tutorial, how-to, reference and
explanation are four different documents, not four sections of one.

## When to use

- Any request to document, restructure, split or rewrite something.
- Writing a new guide, SOP, runbook, reference or design document.
- Producing a summary of technical work for an audience.

If the project has its own documentation conventions — a `CONTRIBUTING.md`, a
template directory, a house style guide, a skill of its own — those win. This
skill fills the gaps and never overrides them.

## Ground rules

1. **Identify the target first**, then read its section of
   [references/targets.md](references/targets.md). Link syntax and placement are
   not guessable, and getting them wrong breaks links silently.
2. **Ask the structural question before writing anything.** Splitting into a set,
   restructuring one document, or flat siblings are materially different
   deliverables, and the user is the only one who can choose.
   [references/shaping-a-set.md](references/shaping-a-set.md).
3. **The original document keeps its path and becomes the hub.** Inbound links
   point at it. Find them (`grep -rl`) before touching anything, and never `mv`
   the file you were pointed at.
4. **Never number sections.** No `## 1. Foo`, no `§4` cross-references. Link to
   the named heading instead. Numbers cannot survive a split, and renumbering on
   every insertion is churn nobody reviews.
5. **No hard line wrapping**, unless the target's own tooling enforces a width.
   One paragraph is one physical line: it keeps diffs readable, because an edit
   touches one line rather than reflowing a paragraph.
6. **No diagram where a list will do.** A sequence, a hierarchy, a mapping and a
   set of conditions are all lists or tables. Reserve diagrams for structure a
   list genuinely cannot express — expect that to be rare.
7. **Surface contradictions in the source; never resolve them silently.** A long
   document usually disagrees with itself in two or three places. Write the entry
   that works, and flag the choice in place as unresolved.
8. **Verify before reporting.** Links and facts, every time:
   [references/verification.md](references/verification.md).

## Workflow

1. Read the target document in full, plus every guideline the user named.
2. Identify the output target and read its section of `targets.md`.
3. Classify each section by Diátaxis mode. Note where the source contradicts
   itself — that list is a deliverable in its own right.
4. Ask the structural question (ground rule 2).
5. Shape the set and place each part
   ([references/shaping-a-set.md](references/shaping-a-set.md)).
6. Draft in house style
   ([references/house-style.md](references/house-style.md)). Generate any
   per-item reference document from a data table with a script, never by hand.
7. Verify: `scripts/linkcheck.py`, then `scripts/factdiff.py`. Fix, re-run.
8. If the work has an audience, publish it — see `shaping-a-set.md`, Audience.

A full run is in [references/worked-example.md](references/worked-example.md).

## Common mistakes

| Rationalization | Reality |
|---|---|
| "I'll name the parts `Audit findings.md` — the folder gives context" | In a wiki, links resolve by basename across the whole tree, so a generic name is ambiguous the moment a second one appears. It also reads as noise in backlinks. Prefix every part. |
| "Moving the document into the new folder is tidier" | It breaks every inbound link. The original path is the hub. `grep -rl` for inbound links before touching anything. |
| "Section numbers help the reader navigate" | Numbers cannot survive a split: `§4` means nothing once §4 is a different file. Link to named headings. |
| "Show, don't tell — add a diagram" | In the worked example, six diagrams were written and all six were removed as redundant with the list above them. Write the list first; reach for a diagram only when it fails. |
| "The style guide says compress" | Readability outranks rule compliance, and detail preservation outranks both. A rule that costs the reader a fact has been misapplied. |
| "The design says X, so I'll write X" | Writing the per-item entries is what exposes a self-contradicting source. Flag it, don't paper over it. |
| "It's a proposal, so I'll write the how-tos as if it were live" | Mark target-state procedures with a callout naming the step they depend on. Never imply an unbuilt system works. |
| "The links look fine" | Run the checker. Heading anchors break silently when you reword a heading. |

## Red flags — stop

- You do not know which target the output is for.
- You are about to write a second document without having asked the structural
  question.
- You are about to hand-write more than about five near-identical entries.
  Generate them from a data table instead.
- You are about to report the work complete without having run both scripts.
- You are about to `mv` or rename the document you were pointed at.
