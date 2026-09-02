# writing-documentation

A [Claude Code](https://claude.com/claude-code) skill for writing and
restructuring technical documentation.

Documents rot in one specific way. A document starts as a spec, absorbs findings,
grows a rollout plan, and ends up serving four purposes at once. Nobody can
maintain it, because any edit serves one purpose and damages another.

This skill handles the job that follows: **splitting one document by purpose,
without losing a fact and without breaking a single inbound link.** The model is
[Diátaxis](https://diataxis.fr/).

## What it does

- **Asks the structural question first.** Splitting into a set, restructuring one
  document, or flat siblings are materially different deliverables, and the
  choice belongs to you rather than to the agent.
- **Keeps the original document at its path** as the hub, so inbound links
  survive.
- **Writes in a disciplined style** — ASD-STE100 writing rules, with detail
  preservation and readability ranked above rule compliance.
- **Generates per-item reference documents** from a data table with a script,
  instead of hand-writing a hundred near-identical entries that immediately
  drift.
- **Surfaces contradictions in the source** rather than silently resolving them.
  A long document usually disagrees with itself, and applying its pattern to
  specific items is what exposes it.
- **Verifies.** Two scripts prove the links resolve and that no fact was dropped.

It works against wikis with basename links (Obsidian, Foam, Dendron), repository
`docs/` trees with relative links, and hosted wikis such as Confluence.

## Three opinionated defaults

They are defaults, not laws — if your project states otherwise, your project
wins. Each has a reason:

| Default | Why |
|---|---|
| No hard line wrapping | An edit touches one line instead of reflowing a paragraph, so diffs stay readable and review comments land on the sentence that changed. |
| No numbered sections | Numbers cannot survive a split, and they churn on every insertion. A link to a named heading keeps working when the section moves. |
| No diagram where a list will do | A sequence, a hierarchy and a set of conditions are lists. "Show, don't tell" is not a licence to open every section with a flowchart. |

## Install

As a plugin, from this repository:

```
/plugin marketplace add Ferroman/diataxis-documentation-skill
/plugin install writing-documentation
```

Or copy the skill directly:

```bash
git clone https://github.com/Ferroman/diataxis-documentation-skill
cp -r diataxis-documentation-skill/skills/writing-documentation ~/.claude/skills/
```

The skill then loads whenever you ask Claude to document, restructure or split
something — you do not need to name it.

## The scripts

Both exit non-zero on failure, so they compose into a pre-commit hook or a CI
step. Neither needs anything beyond Python 3.

```bash
# Links: [[wiki links]] by basename, [text](relative.md) on disk, plus anchors
python3 scripts/linkcheck.py --root . docs/

# Facts: every inline-code token, @handle, number and link target from the
# original must still appear somewhere in the new set
python3 scripts/factdiff.py ORIGINAL.md docs/

# Remove hard line wrapping, in place, leaving structure alone
python3 scripts/unwrap.py docs/
```

`linkcheck.py` reports three failures: `BROKEN`, `AMBIGUOUS` (a basename that
exists in more than one place, so the link is a coin flip), and `BAD HEADING`.
The last is the one worth having — reword a heading and every link into it dies
with no visible error in most editors.

## Layout

```
skills/writing-documentation/
├── SKILL.md                      ground rules, workflow, common mistakes
├── references/
│   ├── shaping-a-set.md          how to split, name and place the parts
│   ├── house-style.md            STE writing rules and the three defaults
│   ├── targets.md                per-target link syntax, placement, front matter
│   ├── verification.md           what the scripts check, and what they cannot
│   └── worked-example.md         one real run, anonymised
└── scripts/                      linkcheck.py, factdiff.py, unwrap.py
```

## Status

Version 0.1.0. The scripts are tested (see `TESTING.md`). The guidance comes from
one real documentation project rather than from a scored evaluation — the rubric
a proper test would use is in `TESTING.md`, and contributions that run it are
welcome.

## Licence

MIT.
