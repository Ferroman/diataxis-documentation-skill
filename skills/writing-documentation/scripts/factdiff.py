#!/usr/bin/env python3
"""Prove a restructure lost no facts.

Extracts the load-bearing tokens from an original document and asserts each one
still appears somewhere in the new document set:

  inline-code tokens   repo names, team names, flags, file paths
  @logins              GitHub users and @org/team references
  numbers              counts, percentages, dates
  wikilink targets     every [[note]] the original pointed at

Expect a small number of legitimate misses — a token that moved from inline code
into a fenced block, or a phrase deliberately rewritten. Check each by hand. A
miss you cannot explain is a lost fact.

Usage:
  factdiff.py ORIGINAL.md NEW1.md [NEW2.md ...]
  factdiff.py ORIGINAL.md NEWDIR/

Exit 1 if anything is unaccounted for.
"""
import os, re, sys

CODE = re.compile(r'`([^`\n]+)`')
LOGIN = re.compile(r'@[\w\-\.]+')
NUM = re.compile(r'(?<![\w.\-])\d[\d\s]*\d(?![\w%])|(?<![\w.\-])\d+(?![\w%])')
LINK = re.compile(r'\[\[([^\]\|#]+)')


def read_all(paths):
    chunks = []
    for p in paths:
        if os.path.isdir(p):
            for f in sorted(os.listdir(p)):
                if f.endswith('.md'):
                    chunks.append(open(os.path.join(p, f), encoding='utf-8').read())
        elif p.endswith('.md'):
            chunks.append(open(p, encoding='utf-8').read())
    return '\n'.join(chunks)


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    orig = open(sys.argv[1], encoding='utf-8').read()
    new = read_all(sys.argv[2:])

    checks = [
        ("inline-code tokens", set(CODE.findall(orig))),
        ("@logins and teams", set(LOGIN.findall(orig))),
        ("wikilink targets", set(LINK.findall(orig))),
        ("numbers", set(NUM.findall(orig))),
    ]

    total_missing = 0
    for label, found in checks:
        missing = sorted(x for x in found if x not in new)
        total_missing += len(missing)
        print(f"{label}: {len(found)} in original, {len(missing)} not found in the new set")
        for x in missing:
            print(f"    MISSING: {x!r}")

    print(f"\n{total_missing} unaccounted token(s)")
    sys.exit(1 if total_missing else 0)


if __name__ == '__main__':
    main()
