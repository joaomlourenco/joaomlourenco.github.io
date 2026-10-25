#!/usr/bin/env python3
"""Put photos you saved into the right advisee page folders.

    python3 scripts/advisee_photos.py ~/Downloads/advisees            # dry run: only report
    python3 scripts/advisee_photos.py ~/Downloads/advisees --write    # do it
    python3 scripts/advisee_photos.py ~/Downloads/advisees --write --move   # and delete the originals

Name each photo after the student: "Hugo Pereira.jpeg", "Manuel Pinto.jpg".  The first and last name
are matched (accent- and case-insensitive) against the titles of the pages in content/advisees/.
When the same name appears on several pages (e.g. "Diogo Sousa"), add the year of the page to the
file name -- "Diogo Sousa 2021.jpeg" -- or the photo is reported as ambiguous and skipped.

For each photo that matches exactly one page: cropped to a square at the centre, scaled down to at
most 800x800 (never enlarged), saved as <page folder>/<page folder name>.jpg, which is where the site
looks for it.  A page that already has a photo is skipped unless --force.  One second (--pause) between
students, as asked.  Photos are never fetched from anywhere: this script only reads your files.
"""
import argparse, glob, os, re, shutil, sys, time, unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ADV = os.path.join(ROOT, "content", "advisees")
EXT = (".jpg", ".jpeg", ".png", ".webp", ".heic")
IMG = (".jpg", ".jpeg", ".png", ".webp", ".gif")


def norm(s):
    s = unicodedata.normalize("NFKD", s)
    return re.sub(r"[^a-z0-9 ]", "", "".join(c for c in s if not unicodedata.combining(c)).lower())


def pages(adv):
    out = []
    for f in sorted(glob.glob(os.path.join(adv, "*", "*", "index.md"))):
        t = open(f, encoding="utf-8").read()
        m = re.search(r'^title:\s*"?(.*?)"?\s*$', t, re.M)
        if m:
            d = os.path.dirname(f)
            out.append(dict(dir=d, year=os.path.basename(os.path.dirname(d)), title=m.group(1),
                            tokens=norm(m.group(1)).split()))
    return out


def parse_name(stem):
    year = None
    m = re.search(r"[\s_(-]*((?:19|20)\d\d)\)?\s*$", stem)
    if m:
        year = m.group(1); stem = stem[:m.start()]
    toks = norm(stem).split()
    return toks, year


def match(toks, year, allp):
    if len(toks) < 2:
        return []
    first, last = toks[0], toks[-1]
    found = [p for p in allp if first in p["tokens"] and last in p["tokens"]
             and p["tokens"][0] == first and p["tokens"][-1] == last]
    if not found:  # lenient: first/last token anywhere in the title ("Manuel Pinto" -> "Manuel de Sousa ... Pinto")
        found = [p for p in allp if p["tokens"][0] == first and last in p["tokens"]]
    if year:
        found = [p for p in found if p["year"] == year]
    return found


def make_square(src, dst, maxside=800):
    from PIL import Image, ImageOps
    im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
    w, h = im.size
    s = min(w, h)
    im = im.crop(((w - s) // 2, (h - s) // 2, (w - s) // 2 + s, (h - s) // 2 + s))
    if s > maxside:
        im = im.resize((maxside, maxside), Image.LANCZOS)
    im.save(dst, "JPEG", quality=90, optimize=True)
    return im.size


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("folder")
    ap.add_argument("--write", action="store_true", help="do it (default: only report)")
    ap.add_argument("--move", action="store_true", help="delete each original after it was placed")
    ap.add_argument("--force", action="store_true", help="replace a photo the page already has")
    ap.add_argument("--pause", type=float, default=1.0, help="seconds between students (default 1)")
    ap.add_argument("--advisees", default=ADV, help="content/advisees folder (default: this site's)")
    a = ap.parse_args()
    allp = pages(a.advisees)
    files = sorted(f for f in glob.glob(os.path.join(os.path.expanduser(a.folder), "*")) if f.lower().endswith(EXT))
    if not files:
        sys.exit("no photos (%s) in %s" % ("/".join(EXT), a.folder))
    done = 0
    for n, f in enumerate(files):
        stem = os.path.splitext(os.path.basename(f))[0]
        toks, year = parse_name(stem)
        found = match(toks, year, allp)
        label = os.path.basename(f)
        if len(found) == 0:
            print("NO MATCH   %-34s (no advisee page with that first and last name)" % label); continue
        if len(found) > 1:
            print("AMBIGUOUS  %-34s -> %s  (add the year to the file name)" % (label, ", ".join("%s %s" % (p["year"], p["title"]) for p in found))); continue
        p = found[0]
        existing = [x for x in os.listdir(p["dir"]) if x.lower().endswith(IMG)]
        if existing and not a.force:
            print("SKIP       %-34s -> %s/%s already has %s (use --force)" % (label, p["year"], os.path.basename(p["dir"]), existing[0])); continue
        dst = os.path.join(p["dir"], os.path.basename(p["dir"]) + ".jpg")
        if not a.write:
            print("would put  %-34s -> %s" % (label, os.path.relpath(dst, os.path.dirname(a.advisees.rstrip("/")))))
            continue
        for x in existing:
            os.remove(os.path.join(p["dir"], x))
        size = make_square(f, dst)
        if a.move:
            os.remove(f)
        print("PUT        %-34s -> %s (%dx%d)" % (label, os.path.relpath(dst, os.path.dirname(a.advisees.rstrip("/"))), *size))
        done += 1
        if n < len(files) - 1:
            time.sleep(a.pause)
    print("%d photo(s) %s." % (done, "placed" if a.write else "would be placed (use --write)"))


if __name__ == "__main__":
    main()
