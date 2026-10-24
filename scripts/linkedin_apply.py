#!/usr/bin/env python3
"""Apply the LinkedIn URLs filled in the worksheet made by linkedin_worksheet.py.

    python3 scripts/linkedin_apply.py ~/Desktop/linkedin-worksheet-BSc.xlsx          # dry run
    python3 scripts/linkedin_apply.py ~/Desktop/linkedin-worksheet-BSc.xlsx --write  # apply

Reads the "LinkedIn URL" and "Page" columns (.xlsx -- no extra package needed -- or .csv).  For each
row with a URL it adds `linkedin: "<url>"` to the front matter of the page (after `date`/`date_label`),
checking that the URL looks like https://www.linkedin.com/in/<id> and that the page has no link yet
(an existing one is reported, never overwritten).  Photos are not handled here: put the image in the
page folder, named like the folder (e.g. 2022/hugo-pereira/hugo-pereira.jpg).
"""
import argparse, csv, os, re, sys, zipfile
from xml.etree import ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NS = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}


def read_xlsx(path):
    z = zipfile.ZipFile(path)
    shared = []
    if "xl/sharedStrings.xml" in z.namelist():
        for si in ET.fromstring(z.read("xl/sharedStrings.xml")).findall("m:si", NS):
            shared.append("".join(t.text or "" for t in si.iter("{%s}t" % NS["m"])))
    sheet = ET.fromstring(z.read("xl/worksheets/sheet1.xml"))
    rows = []
    for r in sheet.find("m:sheetData", NS).findall("m:row", NS):
        d = {}
        for c in r.findall("m:c", NS):
            col = re.match(r"[A-Z]+", c.get("r")).group(0)
            v = c.find("m:v", NS)
            if c.get("t") == "s" and v is not None:
                d[col] = shared[int(v.text)]
            elif c.get("t") == "inlineStr":
                d[col] = "".join(t.text or "" for t in c.iter("{%s}t" % NS["m"]))
            elif v is not None:
                d[col] = v.text
        rows.append(d)
    head = rows[0]
    return [{head[k]: v for k, v in r.items() if k in head} for r in rows[1:]]


def read_csv(path):
    return list(csv.DictReader(open(path, encoding="utf-8")))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("sheet")
    ap.add_argument("--write", action="store_true", help="modify the pages (default: only report)")
    a = ap.parse_args()
    rows = read_xlsx(a.sheet) if a.sheet.endswith(".xlsx") else read_csv(a.sheet)
    n_ok = 0
    for r in rows:
        url = (r.get("LinkedIn URL (paste here)") or "").strip()
        page = (r.get("Page") or "").strip()
        if not url:
            continue
        if not re.match(r"^https?://([a-z]{2,3}\.)?linkedin\.com/in/[^/\s]+/?$", url):
            print("SKIP (not a linkedin.com/in/ URL): %s -> %s" % (r.get("Name"), url)); continue
        f = os.path.join(ROOT, page)
        if not os.path.isfile(f):
            print("SKIP (page not found): %s" % page); continue
        t = open(f, encoding="utf-8").read()
        m = re.match(r"---\n(.*?)\n---", t, re.S)
        if not m or re.search(r"^linkedin:", m.group(1), re.M):
            print("SKIP (page already has a linkedin field): %s" % page); continue
        lines = m.group(1).split("\n")
        i = max([k for k, l in enumerate(lines) if re.match(r"(date|date_label):", l)] or [0])
        lines.insert(i + 1, 'linkedin: "%s"' % url)
        print("%s %s: %s" % ("ADD" if a.write else "would add", r.get("Name"), url))
        n_ok += 1
        if a.write:
            open(f, "w", encoding="utf-8").write("---\n" + "\n".join(lines) + t[m.end(1):])
    print("%d page(s) %s." % (n_ok, "updated" if a.write else "would be updated (use --write)"))


if __name__ == "__main__":
    main()
