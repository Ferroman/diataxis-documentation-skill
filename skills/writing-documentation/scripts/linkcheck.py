#!/usr/bin/env python3
"""Link checker for Markdown documentation sets.

Checks both link styles used by documentation tools, plus heading anchors:

  [[Wiki links]]            resolved by basename against --root (Obsidian, Foam,
                            Dendron); also [[Note|Alias]] and [[Note#Heading]]
  [text](relative/path.md)  resolved on disk from the linking file; also
                            (path.md#anchor) and same-file (#anchor)

Three failures are reported:

  BROKEN       the target does not exist
  AMBIGUOUS    a wiki-link basename exists in more than one place
  BAD HEADING  the document exists but has no heading by that name

Heading anchors are the silent ones: reword a heading and every link into it
dies with no visible error in most editors.

Fenced code blocks and inline code spans are skipped — config samples, shell
snippets and documentation-about-documentation are full of bracket noise that is
not a link.

Usage:
  linkcheck.py [--root ROOT] PATH [PATH ...]

  PATH   a Markdown file, or a directory whose .md files are checked
  --root the tree used to resolve [[wiki links]] by basename. Defaults to
         $DOCS_ROOT, else the git top level of the first PATH, else its
         directory.

Exit 1 if anything is broken.
"""
import os
import re
import subprocess
import sys
import urllib.parse

WIKI = re.compile(r'\[\[([^\]\|]+)(?:\|[^\]]*)?\]\]')
MD = re.compile(r'(?<!\!)\[[^\]]*\]\(([^)\s]+)(?:\s+"[^"]*")?\)')
HEAD = re.compile(r'^#{1,6}\s+(.*)$', re.M)
SKIP = ('http://', 'https://', 'mailto:', 'tel:')


def slug(text):
    """GitHub-style heading slug."""
    s = text.strip().lower()
    s = re.sub(r'[`*_~\[\]()]', '', s)
    s = re.sub(r'[^\w\s-]', '', s)
    return re.sub(r'\s+', '-', s).strip('-')


INLINE_CODE = re.compile(r'`[^`\n]*`')


def strip_code(text):
    """Remove fenced blocks and inline code spans.

    Both are samples, not links. Documentation about documentation is full of
    `[[Note name]]` and `[text](path.md)` written as examples inside backticks.
    """
    out, in_code = [], False
    for line in text.split('\n'):
        if line.lstrip().startswith('```'):
            in_code = not in_code
            continue
        if not in_code:
            out.append(INLINE_CODE.sub('', line))
    return '\n'.join(out)


def find_root(first):
    if os.environ.get('DOCS_ROOT'):
        return os.environ['DOCS_ROOT']
    start = first if os.path.isdir(first) else os.path.dirname(os.path.abspath(first))
    try:
        top = subprocess.run(['git', '-C', start, 'rev-parse', '--show-toplevel'],
                             capture_output=True, text=True, check=True)
        return top.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return start


def index_tree(root):
    idx = {}
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if not d.startswith('.') and d != 'node_modules']
        for f in fn:
            if f.endswith('.md'):
                idx.setdefault(f[:-3], []).append(os.path.join(dp, f))
    return idx


def expand(paths):
    for p in paths:
        if os.path.isdir(p):
            for dp, dn, fn in os.walk(p):
                dn[:] = [d for d in dn if not d.startswith('.') and d != 'node_modules']
                for f in sorted(fn):
                    if f.endswith('.md'):
                        yield os.path.join(dp, f)
        elif p.endswith('.md'):
            yield p


class Checker:
    def __init__(self, root):
        self.root = root
        self.index = index_tree(root)
        self.heads = {}
        self.total = 0
        self.bad = 0

    def headings(self, path):
        if path not in self.heads:
            try:
                text = open(path, encoding='utf-8').read()
            except OSError:
                self.heads[path] = []
                return []
            self.heads[path] = [h.strip() for h in HEAD.findall(text)]
        return self.heads[path]

    def fail(self, kind, path, link):
        print(f"{kind:<12}{os.path.relpath(path, self.root)}  ->  {link}")
        self.bad += 1

    def check_wiki(self, path, body):
        for m in WIKI.finditer(body):
            raw = m.group(1).strip()
            self.total += 1
            name, _, anchor = raw.partition('#')
            name = name.strip().replace('\\', '')
            anchor = anchor.strip()
            hits = self.index.get(name)
            if not hits:
                self.fail('BROKEN', path, f'[[{raw}]]')
                continue
            if len(hits) > 1:
                self.fail('AMBIGUOUS', path, f'[[{name}]] ({len(hits)} matches)')
            if anchor and anchor not in self.headings(hits[0]):
                self.fail('BAD HEADING', path, f'[[{raw}]]')

    def check_md(self, path, body):
        base = os.path.dirname(os.path.abspath(path))
        for m in MD.finditer(body):
            target = m.group(1).strip()
            if target.startswith(SKIP):
                continue
            self.total += 1
            file_part, _, anchor = target.partition('#')
            file_part = urllib.parse.unquote(file_part)
            anchor = urllib.parse.unquote(anchor).strip()

            if not file_part:
                if anchor and slug(anchor) not in [slug(h) for h in self.headings(path)]:
                    self.fail('BAD HEADING', path, target)
                continue

            resolved = os.path.normpath(os.path.join(base, file_part))
            if not os.path.exists(resolved):
                self.fail('BROKEN', path, target)
                continue
            if anchor and resolved.endswith('.md'):
                if slug(anchor) not in [slug(h) for h in self.headings(resolved)]:
                    self.fail('BAD HEADING', path, target)

    def run(self, paths):
        for path in expand(paths):
            body = strip_code(open(path, encoding='utf-8').read())
            self.check_wiki(path, body)
            self.check_md(path, body)
        print(f"\n{self.total} links checked, {self.bad} problem(s)")
        return 1 if self.bad else 0


def main():
    args = sys.argv[1:]
    root = None
    if args and args[0] == '--root':
        if len(args) < 2:
            sys.exit(__doc__)
        root, args = args[1], args[2:]
    if not args:
        sys.exit(__doc__)
    sys.exit(Checker(root or find_root(args[0])).run(args))


if __name__ == '__main__':
    main()
