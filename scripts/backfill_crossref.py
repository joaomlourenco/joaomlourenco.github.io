"""One-off backfill: enrich already-saved publication entries (written before
Crossref cross-checking existed) with journal/volume/issue/doi where missing.
Safe to re-run; only rewrites entries that still have gaps to fill.
"""
import glob
import re
import sys
import time

from utilities import enrich_with_crossref

PUB_RE = re.compile(r'^title:\s*"(.*)"$', re.MULTILINE)
DATE_RE = re.compile(r'^date:\s*(\d{4})', re.MULTILINE)
PUBLICATION_RE = re.compile(r'^publication:\s*"(.*)"$', re.MULTILINE)
URL_RE = re.compile(r"url:\s*'([^']*)'")


def build_publication_entry(journal, year, volume, issue):
    entry = f"{journal} "
    if year:
        entry += f"{year} "
    if volume and 'N/A' not in volume:
        entry += f"{volume} "
    if issue and 'N/A' not in issue:
        entry += f"({issue})"
    return entry


def main(path="content/publications/"):
    files = sorted(glob.glob(path.rstrip('/') + '/*/index.md'))
    print(f"Scanning {len(files)} saved publications for gaps to fill...", flush=True)
    updated = 0
    for i, filepath in enumerate(files):
        with open(filepath, encoding='utf-8') as f:
            content = f.read()

        pub_match = PUBLICATION_RE.search(content)
        if not pub_match or 'Unknown Journal' not in pub_match.group(1):
            continue

        title_match = PUB_RE.search(content)
        date_match = DATE_RE.search(content)
        url_match = URL_RE.search(content)
        if not title_match:
            continue

        title = title_match.group(1)
        year = date_match.group(1) if date_match else ''
        url = url_match.group(1) if url_match else 'N/A'

        print(f"[{i+1}/{len(files)}] {title[:50]}...", flush=True)

        pub = {'title': title, 'journal': 'Unknown Journal', 'volume': 'N/A', 'issue': 'N/A', 'doi': 'N/A', 'url': url}
        enriched = enrich_with_crossref(pub, verbose=True)
        time.sleep(1.5)

        if enriched['journal'] == 'Unknown Journal':
            continue

        new_entry = build_publication_entry(enriched['journal'], year, enriched['volume'], enriched['issue'])
        new_content = PUBLICATION_RE.sub(f'publication: "{new_entry}"', content, count=1)

        if enriched.get('doi', 'N/A') not in ('N/A', '') and url == 'N/A':
            new_content = URL_RE.sub(f"url: 'https://doi.org/{enriched['doi']}'", new_content, count=1)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        updated += 1

    print(f"\nUpdated {updated}/{len(files)} entries.", flush=True)


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "content/publications/"
    main(path)
