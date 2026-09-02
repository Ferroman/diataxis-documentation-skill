# House style

## Three defaults worth keeping

These are opinionated. They are defaults, not laws — if the project states
otherwise, the project wins. Each has a reason.

**No line-length limit.** One paragraph is one physical line. An edit then
touches one line instead of reflowing a paragraph, so diffs stay readable and
review comments land on the sentence that changed. Wrapping is worth it only when
the project's own tooling checks it.

**No numbered sections.** No `## 1. Foo`, no `§4` cross-references. Numbers
cannot survive a split, they churn on every insertion, and a link to
`Doc#Named heading` keeps working when the section moves. Ordered *content* is
fine — a rollout is genuinely a sequence, and its steps can be a numbered list.

**No diagram where a simple list will do.** A sequence, a hierarchy, a
question-to-mechanism mapping and a set of conditions are all lists or tables.
"Show, don't tell" is not a licence to open every section with a flowchart. Write
the list; reach for a diagram only when the list genuinely fails.

## ASD-STE100, as applied here

Simplified Technical English is worth borrowing from, in this order of
precedence: **detail preservation, then readability, then rule compliance.** STE
is a means to clarity, not a reason to lose content.

- One idea per sentence. Descriptive sentences ≤ 25 words, instructions ≤ 20.
- Active voice, present tense. "The parser ignores an unresolvable name", not
  "an unresolvable name is ignored".
- One approved term per concept, everywhere. Pick "repository" or "repo" and do
  not alternate.
- `must` = requirement, `can` = possibility, `does not` = negation. Avoid
  "should", which readers split between advice and obligation.
- Articles are mandatory. No noun cluster longer than three words.
- Paragraphs ≤ 6 sentences.

Claim it accurately. "Follows ASD-STE100 writing rules" is true. "STE-100
conformant" is not, without the licensed dictionary.

### The over-compression pathology

STE pressure produces sentences whose subject and predicate are both
abstractions, so the reader must already hold the whole model to parse them.
Rewrite on sight when you see:

- "X stops being <adjective>"
- inverted attribution: "Drivers 1 and 2 are what the mask answers"
- a consequence left implicit: "Both pin kinds must resolve." (So what?)
- staccato verb chains: "It adds the rollups. It rounds the values, it ranks."

The fix is a concrete actor and a spelled-out consequence. Two plain sentences
beat one that satisfies a rule.

## Writing

- Say what is true, including when the source was wrong. "An earlier version set
  two approvals here. That was wrong, because …" beats a silent correction.
- Prefer the number to the adjective. "Three people" beats "a small team".
- Put the reader's objection in a heading, not a footnote.
- Every claim that came from a measurement carries the measurement.
- Duplication between documents is correct when it saves a reader a jump. DRY is
  a code principle; a reader who lands mid-set should not have to reconstruct
  context from three other files.
- Mark anything not yet true. A status callout at the top of a proposal costs one
  line and prevents someone acting on a design that was never built.
