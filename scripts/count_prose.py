#!/usr/bin/env python3
"""
count_prose.py — Compta paraules de prosa en fitxers .qmd
Exclou: YAML front matter, blocs de codi, taules, figures,
        peus de taula Quarto, capçaleres (#), línies en blanc.
"""
import re, sys

def count_file(path):
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()
    in_yaml = False
    in_code = False
    total = 0
    for i, line in enumerate(lines):
        s = line.strip()
        if i == 0 and s == "---":
            in_yaml = True; continue
        if in_yaml:
            if s in ("---", "..."): in_yaml = False
            continue
        if re.match(r"^(`{3,}|~{3,})", s):
            in_code = not in_code; continue
        if in_code: continue
        if s.startswith("|"): continue
        if re.match(r"^#{1,6}\s", s): continue
        if re.match(r"^!\[", s): continue
        if not s: continue
        if re.match(r"^:\s", s) and re.search(r"\{#tbl-", s): continue
        clean = re.sub(r"\{[^}]*\}", "", s)
        clean = re.sub(r"[*_`~]+", "", clean)
        clean = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", clean)
        clean = re.sub(r"@\w[\w:.-]*", "", clean)
        clean = re.sub(r"[^\w\s\-àáèéíïòóúüçÀÁÈÉÍÏÒÓÚÜÇ·]", " ", clean)
        total += len(clean.split())
    return total

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Ús: python3 count_prose.py <fitxer.qmd> [...]"); sys.exit(1)
    grand = 0
    for path in sys.argv[1:]:
        n = count_file(path); grand += n
        print(f"{n:6d}  {path}")
    print(f"{grand:6d}  TOTAL")
