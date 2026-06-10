# README — Memòria PFP ICE-UPC

## Fitxers principals

| Fitxer | Descripció |
|--------|------------|
| `index.qmd` | Document principal complet (sense límit de paraules) |
| `index_article.qmd` | Versió ICE reduïda (≤8.000 paraules al cos) |
| `_quarto.yml` | Configuració Quarto base (HTML + PDF complet) |
| `_quarto-article.yml` | Perfil Quarto per a la versió ICE |
| `portada.tex` | Portada LaTeX (plantilla ICE; s'inclou a totes dues versions) |
| `before-body.tex` | Preàmbul LaTeX (s'inclou a totes dues versions) |
| `CLAUDE.md` | Context del projecte per a Claude |

## Renderització

### Versió completa (`index.qmd`)
```bash
quarto render index.qmd
```
Usa `_quarto.yml` directament. Genera HTML i PDF (KOMA `scrartcl`).

### Versió ICE (`index_article.qmd`)
```bash
quarto render index_article.qmd --profile article
```
Quarto fusiona `_quarto.yml` (base) amb `_quarto-article.yml` (perfil).
Genera PDF amb classe `article` estàndard, sense TOC.

## Com funcionen els profiles de Quarto

Quarto fusiona els YAMLs per *deep merge*:
- **Valors escalars** (`toc: false`, `documentclass: article`): el perfil sobreescriu el base.
- **Llistes** (`include-in-header`, `render`): el perfil **substitueix** la llista sencera.
  - Per tant, `include-in-header: []` al perfil eliminaria `portada.tex`.
  - Per **mantenir** `portada.tex` i `before-body.tex` a la versió article, cal **no declarar** `include-in-header` ni `include-before-body` al perfil (s'hereten del base).
  - Si calgués **afegir** un fitxer addicional, caldria repetir tota la llista al perfil.
- **Claus absents** al perfil: s'hereten del base sense canvis.

## Recompte de paraules — versió completa (`index.qmd`, juny 2026)

Recompte de les seccions del cos (exclou resum, abstract, bibliografia i annex):
```bash
python3 ~/bin/count_prose.py \
  _1_introduccio.qmd \
  _2_metodologia.qmd \
  _3_resultats.qmd \
  _4_discussio.qmd
```

| Secció | Fitxer font | Paraules |
|--------|-------------|---------|
| Introducció | `_1_introduccio.qmd` | 3.670 |
| Metodologia | `_2_metodologia.qmd` | 3.281 |
| Resultats | `_3_resultats.qmd` | 1.577 |
| Discussió | `_4_discussio.qmd` | 1.823 |
| **Total cos** | | **10.351** |

## Recompte de paraules — versió ICE (`index_article.qmd`, juny 2026)

L'script `count_prose.py` compta paraules de prosa excloent taules, figures,
blocs de codi, peus de taula, capçaleres i YAML front matter.

### Instal·lació

Desa l'script en qualsevol ubicació permanent, per exemple:
```bash
cp count_prose.py ~/bin/count_prose.py
```

### Ús

Recompte d'un fitxer:
```bash
python3 ~/bin/count_prose.py _3_resultats.qmd
```

Recompte de totes les seccions del cos de `index_article.qmd`:
```bash
python3 ~/bin/count_prose.py \
  _1_introduccio_article.qmd \
  _2_metodologia_article.qmd \
  _3_resultats.qmd \
  _4_discussio.qmd
```

| Secció | Fitxer font | Paraules | Límit ICE |
|--------|-------------|---------|-----------|
| Introducció | `_1_introduccio_article.qmd` | 1.968 | ~2.000 |
| Metodologia | `_2_metodologia_article.qmd` | 1.953 | ~2.000 |
| Resultats | `_3_resultats.qmd` (compartit) | 1.655 | ~2.000 |
| Discussió | `_4_discussio.qmd` (compartit) | 1.776 | ~2.000 |
| **Total cos** | | **7.352** | **≤8.000** |

Resum, abstract, bibliografia i annex no compten per al límit.

## TODO obert

- **Columna `Solució` de `tbl-reestructuracio-problemes`** (`_3_resultats.qmd`, comentari `<!-- TODO afegir si solució -->`): 23 exercicis nous amb la columna buida. Confirmar si tots tenen solució als `PS_Tx.qmd` i omplir-la o eliminar-la.
