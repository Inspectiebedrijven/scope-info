#!/usr/bin/env python3
"""Haalt de verkeerscijfers van de publieke naslag-repo op en bewaart ze in CSV-bestanden.

GitHub bewaart verkeerscijfers 14 dagen. Dit script draait wekelijks en vult de bestanden
naast dit script aan, zodat de reeks compleet blijft:

- per-dag.csv      één regel per dag: weergaven, unieke bezoekers, clones, unieke clones
- verwijzers.csv   momentopname per run: vanaf welke sites bezoekers kwamen (laatste 14 dagen)
- paden.csv        momentopname per run: de meest bekeken pagina's (laatste 14 dagen)

Gebruikt de `gh`-CLI met het account dat op deze computer is ingelogd (schrijfrechten op de
repo zijn nodig). Alleen lezen: het script wijzigt niets op GitHub.
"""
import csv
import datetime
import json
import os
import subprocess
import sys

# De repo en de map voor de CSV-bestanden zijn instelbaar, zodat hetzelfde script lokaal en in een
# GitHub Action kan draaien: `ophalen.py [map]`, met de repo uit GITHUB_REPOSITORY als die is gezet.
REPO = os.environ.get("GITHUB_REPOSITORY") or "Inspectiebedrijven/scope-info"
HERE = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))


def api(path):
    out = subprocess.run(
        ["gh", "api", f"repos/{REPO}/traffic/{path}"], capture_output=True, text=True
    )
    if out.returncode != 0:
        sys.exit(f"FOUT bij traffic/{path}: {out.stderr.strip() or out.stdout.strip()}")
    return json.loads(out.stdout)


def read(name):
    p = os.path.join(HERE, name)
    if not os.path.exists(p):
        return []
    with open(p, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def write(name, fields, rows):
    with open(os.path.join(HERE, name), "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


def main():
    today = datetime.date.today().isoformat()
    views, clones = api("views"), api("clones")

    # Per dag: bestaande regels behouden, en per datum het hoogste cijfer nemen. De lopende dag
    # is bij het ophalen nog niet compleet en wordt bij de volgende run aangevuld.
    fields = ["datum", "weergaven", "unieke_bezoekers", "clones", "unieke_clones"]
    days = {r["datum"]: {k: (r[k] if k == "datum" else int(r[k] or 0)) for k in fields} for r in read("per-dag.csv")}

    def merge(items, total, unique):
        for it in items:
            d = it["timestamp"][:10]
            row = days.setdefault(d, {"datum": d, "weergaven": 0, "unieke_bezoekers": 0, "clones": 0, "unieke_clones": 0})
            row[total] = max(row[total], it["count"])
            row[unique] = max(row[unique], it["uniques"])

    before = len(days)
    merge(views["views"], "weergaven", "unieke_bezoekers")
    merge(clones["clones"], "clones", "unieke_clones")
    write("per-dag.csv", fields, [days[d] for d in sorted(days)])

    # Momentopnames: één set regels per ophaaldatum; opnieuw draaien op dezelfde dag vervangt die set.
    def snapshot(name, fields, rows):
        keep = [r for r in read(name) if r["opgehaald_op"] != today]
        write(name, fields, keep + [dict(opgehaald_op=today, **r) for r in rows])
        return len(rows)

    n_ref = snapshot(
        "verwijzers.csv",
        ["opgehaald_op", "verwijzer", "weergaven", "unieke_bezoekers"],
        [{"verwijzer": r["referrer"], "weergaven": r["count"], "unieke_bezoekers": r["uniques"]} for r in api("popular/referrers")],
    )
    n_paths = snapshot(
        "paden.csv",
        ["opgehaald_op", "pad", "titel", "weergaven", "unieke_bezoekers"],
        [{"pad": r["path"], "titel": r["title"], "weergaven": r["count"], "unieke_bezoekers": r["uniques"]} for r in api("popular/paths")],
    )

    print(f"Opgehaald op {today} voor {REPO}")
    print(f"Laatste 14 dagen: {views['count']} weergaven ({views['uniques']} uniek), {clones['count']} clones ({clones['uniques']} uniek)")
    print(f"per-dag.csv: {len(days)} dagen ({len(days) - before} nieuw); verwijzers: {n_ref}; paden: {n_paths}")
    gaps = []
    ds = sorted(days)
    for a, b in zip(ds, ds[1:]):
        if (datetime.date.fromisoformat(b) - datetime.date.fromisoformat(a)).days > 1:
            gaps.append(f"{a} tot {b}")
    if gaps:
        print("LET OP, gat in de reeks:", "; ".join(gaps))


if __name__ == "__main__":
    main()
