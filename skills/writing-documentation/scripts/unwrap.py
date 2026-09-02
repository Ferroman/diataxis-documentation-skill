#!/usr/bin/env python3
"""Remove hard line wrapping from Markdown, in place.

Vault documents have no line-length limit: one paragraph is one physical line.
This joins wrapped prose while leaving structure alone — front matter, fenced
code, tables, headings, list markers and callout structure all survive, and a
wrapped list item or callout body is joined onto its own marker rather than the
line above.

Usage:
  unwrap.py FILE.md [FILE.md ...]
  unwrap.py DIR/
"""
import os, re, sys

STARTS_LINE = re.compile(r'^\s*(?:[-*+]\s|\d+\.\s|#{1,6}\s|\||>|```|---\s*$|\*\*\w)')


def unwrap(text):
    lines = text.split('\n')
    out = []
    in_code = in_fm = False

    for i, ln in enumerate(lines):
        s = ln.strip()

        if i == 0 and s == '---':
            in_fm = True
            out.append(ln)
            continue
        if in_fm:
            out.append(ln)
            if s == '---':
                in_fm = False
            continue

        if s.startswith('```'):
            in_code = not in_code
            out.append(ln)
            continue
        if in_code or s == '':
            out.append(ln)
            continue

        prev = out[-1] if out else ''
        prev_s = prev.strip()

        if s.startswith('>'):
            body = s[1:].lstrip()
            joinable = (prev_s.startswith('>') and prev_s != '>'
                        and not re.match(r'^>\s*\[!', prev_s))
            new_line = (body == ''
                        or re.match(r'^\[!', body)
                        or re.match(r'^(?:[-*+]\s|\d+\.\s|#{1,6}\s|\|)', body)
                        or body.startswith('```'))
            if joinable and not new_line:
                out[-1] = prev.rstrip() + ' ' + body
            else:
                out.append(ln)
            continue

        can_join = (prev_s and not prev_s.startswith(('>', '|', '#', '```'))
                    and prev_s != '---')
        if can_join and not STARTS_LINE.match(ln):
            out[-1] = prev.rstrip() + ' ' + s
        else:
            out.append(ln)

    return re.sub(r'\n{3,}', '\n\n', '\n'.join(out))


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    paths = []
    for p in sys.argv[1:]:
        if os.path.isdir(p):
            paths += [os.path.join(p, f) for f in sorted(os.listdir(p)) if f.endswith('.md')]
        elif p.endswith('.md'):
            paths.append(p)

    for p in paths:
        src = open(p, encoding='utf-8').read()
        dst = unwrap(src)
        open(p, 'w', encoding='utf-8').write(dst)
        print(f"  {os.path.basename(p)}: {len(src.splitlines())} -> {len(dst.splitlines())} lines")


if __name__ == '__main__':
    main()
