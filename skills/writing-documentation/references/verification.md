# Verification

Two scripts, in this order, before reporting the work complete. Both live in
`scripts/` and both exit non-zero on failure, so they compose into a pre-commit
hook or a CI step.

## Links

```bash
python3 scripts/linkcheck.py [--root ROOT] PATH [PATH ...]
```

Checks `[[wikilinks]]` against a basename index of `ROOT`, and relative
`[text](path.md)` links against the filesystem, and heading anchors for both.
Reports three failures:

| Result | Meaning |
|---|---|
| `BROKEN` | the target does not exist |
| `AMBIGUOUS` | the basename exists in more than one place, so the link is a coin flip |
| `BAD HEADING` | the document exists but has no heading by that name |

Heading anchors are the silent ones. Reword a heading and every link into it dies
with no visible error in most editors.

The checker skips fenced code blocks. Config samples, YAML and shell snippets are
full of bracket and `@` noise that is not a link.

## Facts

```bash
python3 scripts/factdiff.py ORIGINAL NEW [NEW ...]
```

Extracts the load-bearing tokens from the original — inline-code spans, `@`
handles, numbers, and link targets — and asserts each still appears somewhere in
the new set. This is what proves a restructure lost nothing, and it is the check
that makes an aggressive split safe to do.

Expect a small number of legitimate misses, and account for each one by hand: a
token that moved from inline code into a fenced block, or a phrase you
deliberately rewrote. **A miss you cannot explain is a lost fact.**

## By hand

The scripts cannot see these:

- Read the densest two or three sections aloud, watching for the
  over-compression pathology in [house-style.md](house-style.md).
- Confirm the hub is still short.
- Confirm no section heading gained a number.
- `grep -c` for your diagram syntax across the set. Every hit needs a reason a
  list could not serve.
- If the set describes something proposed rather than built, confirm every
  procedure carries the status callout.
- Re-read the open questions you flagged. Each should name the decision and who
  can make it, not just record unease.
