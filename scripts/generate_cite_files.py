#!/usr/bin/env python3
"""
Generates a cite.bib file next to each content/publications/<slug>/index.md,
containing the single matching BibTeX entry from data/jml-all.bib.

The wowchemy theme automatically shows a "Cite" button on any publication
page that has a cite.bib resource file (see themes/.../page_links.html),
so no template changes are needed -- this script just needs to be re-run
whenever data/jml-all.bib is updated (copy the latest version over first).

Usage: python3 scripts/generate_cite_files.py
"""
import re
import glob
import difflib
import sys
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# NOTE: kept outside Hugo's data/ directory deliberately -- Hugo tries to
# auto-parse every file under data/ as JSON/YAML/TOML/etc, and a .bib file
# there hard-fails the entire site build.
BIB_PATHS = [
    os.path.join(ROOT, "bibliography-source", "jml-all.bib"),
    os.path.join(ROOT, "bibliography-source", "education.bib"),
]
PUB_GLOB = os.path.join(ROOT, "content", "publications", "*", "index.md")

MATCH_CUTOFF = 0.88


def norm(t):
    if not t:
        return ""
    t = t.lower()
    t = re.sub(r"\\[a-zA-Z]+\{|\{|\}|\\", "", t)
    t = re.sub(r"[^a-z0-9à-öø-ÿ]+", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def parse_bib_entries(path):
    content = open(path, encoding="utf-8").read()
    if not content.startswith("\n"):
        content = "\n" + content
    parts = re.split(r"(\n@\w+\{[^,]+,)", content)
    entries = []
    for i in range(1, len(parts), 2):
        header = parts[i]
        body = parts[i + 1]
        key_m = re.match(r"\n@(\w+)\{([^,]+),", header)
        if not key_m:
            continue
        etype, key = key_m.groups()
        title_m = re.search(r"^\s*title\s*=\s*\{+(.*?)\}+,?\s*$", body, re.MULTILINE | re.DOTALL)
        title = title_m.group(1).strip() if title_m else None
        full_text = (header + body).lstrip("\n")
        # trim to just this one entry (up to its closing brace at column 0)
        end = full_text.find("\n}")
        full_text = full_text[: end + 2] + "\n" if end != -1 else full_text
        entries.append({"key": key, "type": etype, "title": title, "text": full_text})
    return entries


def main():
    entries = []
    for path in BIB_PATHS:
        entries.extend(parse_bib_entries(path))
    by_norm = {}
    for e in entries:
        if e["title"]:
            by_norm.setdefault(norm(e["title"]), []).append(e)

    files = sorted(glob.glob(PUB_GLOB))
    matched, unmatched = 0, []
    for f in files:
        text = open(f, encoding="utf-8").read()
        m = re.search(r'^title:\s*"(.*)"\s*$', text, re.MULTILINE)
        if not m:
            unmatched.append((f, None))
            continue
        title = m.group(1)
        tn = norm(title)
        cands = by_norm.get(tn)
        if not cands:
            close = difflib.get_close_matches(tn, by_norm.keys(), n=1, cutoff=MATCH_CUTOFF)
            cands = by_norm[close[0]] if close else None
        if not cands:
            unmatched.append((f, title))
            continue
        entry = cands[0]
        cite_path = os.path.join(os.path.dirname(f), "cite.bib")
        with open(cite_path, "w", encoding="utf-8") as out:
            out.write(entry["text"])
        matched += 1

    print(f"wrote cite.bib for {matched} / {len(files)} publications")
    if unmatched:
        print(f"\n{len(unmatched)} publication(s) with no matching bib entry:")
        for f, title in unmatched:
            print(f"  {f}  {'(' + title + ')' if title else '(no title found)'}")


if __name__ == "__main__":
    main()
