# Test evidence

## Scripts — verified 2026-09-02

Each script was run against real documentation, with a positive and a negative
case.

**`linkcheck.py`**

- Wiki-link mode: 330 links across a real 9-document set, 0 problems, exit 0.
- Relative-link mode: this skill's own reference files, 0 problems, exit 0.
- Negative fixture, both styles in one file — one valid wiki link, one missing
  note, one valid heading anchor, one missing heading anchor, and the same four
  again as relative links, plus an external URL and a fenced block containing
  link-shaped text. Reported exactly the four real failures, skipped the external
  URL and the fenced block, exit 1.
- The relative-link run initially reported 8 failures against this skill's own
  documentation. Every one was link syntax written as an example inside inline
  code spans. That was a checker gap, not a documentation bug: inline code is now
  stripped along with fenced blocks, and the run is clean.

**`factdiff.py`**

- Positive: a 499-line original against the 9-document set built from it — 245
  inline-code tokens, 15 handles, 50 link targets and 46 numbers, all accounted
  for, exit 0.
- Negative: the same original against only the hub document reported 314
  unaccounted tokens, exit 1.

**`unwrap.py`**

- Idempotent on an already-unwrapped file: 93 lines in, 93 lines out, byte
  identical.
- It was the script that unwrapped six documents in the run described in
  `references/worked-example.md`.

## Guidance — not yet rubric-tested

The rules in `SKILL.md` come from one real documentation project, recorded in
`references/worked-example.md`. Every row of the Common Mistakes table is a
mistake that was actually made in that run, or a correction the author issued
while it was in progress.

That is real provenance. It is **not** a scored evaluation: no baseline run was
measured, and no fresh agent has been given this skill and compared against one
without it.

## If you change this skill

Fix a rubric before the run. Candidate checks:

- Does the agent ask the structural question before writing anything?
- Does the original document keep its path?
- Are the parts given globally unique names?
- Do any section headings gain numbers?
- Is prose hard-wrapped?
- How many diagrams survive, and could each be a list?
- Are repeated entries generated or hand-written?
- Are both scripts actually executed, or only described?
- Given a **planted contradiction** in the source, does the agent flag it or
  silently pick a side?

That last check matters most. In the original run, silently resolving one of the
two contradictions would have shipped a config rule that locked a team out of its
own repository.

Then run a fresh agent on a long, mixed-purpose document with and without the
skill, and score both. No change without a failing test first.
