# Targets

The craft does not change. These four things do: link syntax, front matter,
placement, and which checker runs. Identify the target before writing.

## Wiki with basename links (Obsidian, Foam, Dendron, many others)

**Links.** `[[Note name]]`, `[[Note name|Alias]]`, `[[Note name#Heading]]`.
Resolved by **basename across the whole tree**, so every document name must be
globally unique and self-describing. Escape the pipe inside a table cell:
`[[note\|Alias]]`.

**Front matter.** YAML. Carry the vault's own keys, plus `diataxis:`
(`overview` / `explanation` / `reference` / `how-to`) — it is the only marker
that survives someone reorganising the folders.

**Placement.** The hub stays at the original path; parts go in a sibling folder
named after it. Procedures go wherever the tree already keeps procedures, and
match the naming of the files already there, prefixes included.

**Callouts.** `> [!info]`, `> [!note]`, `> [!important]`, `> [!warning]`,
`> [!question]`. Use `> [!question]` for open decisions — they stand out on a
re-read, which is when they matter.

**Checker.** `linkcheck.py --root <vault>`.

## A repository: docs/, README, ADRs

**Links.** Relative paths: `[text](../design/overview.md)`,
`[text](./guide.md#a-heading)`. They must resolve on disk from the linking file,
which means the depth changes per folder — the commonest broken-link cause in a
repo.

**Front matter.** Usually none. Follow the neighbouring files.

**Placement.** Follow the repo. If it has `docs/`, `CONTRIBUTING.md` or a
template directory, those decide, and this skill fills the gaps only.

**Line width.** If the repo lints line length, that wins over the no-wrapping
default. Check before writing: a `.markdownlint*`, a `.editorconfig`, or a CI
step that runs a markdown linter.

**Checker.** `linkcheck.py` resolves relative links against the filesystem.
Many repos also run a link checker in CI — read the workflow and match its
strictness rather than discovering it in review.

## Confluence and other hosted wikis

**Links.** Page links are resolved by the platform, not by you. Write them as the
platform expects, and prefer linking by page title over by URL, because URLs
carry page IDs that break when a page moves.

**Placement.** Space and parent page, not folders. Decide the parent before
writing: a page created at the wrong level rarely gets moved.

**Front matter.** None. Anything the platform does not render belongs in the page
body or nowhere.

**Round-tripping.** When a wiki page is mirrored into a local file, that file
usually carries the page ID and URL. Preserve those keys exactly — losing them
breaks the sync, and the page then forks silently.

**Checker.** Neither script can reach a hosted page. Verify facts with
`factdiff.py`, and check links by hand or with the platform's own tooling.

## Anything else

Ask two questions before writing:

1. How does a link to another document resolve here — by name, by path, or by
   platform ID?
2. Where do documents of each kind already live, and what are the neighbours
   named?

The answers give you placement and naming. Everything else in this skill applies
unchanged.
