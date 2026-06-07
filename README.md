# README — Memòria PFP ICE-UPC

## Fitxers principals

| Fitxer | Descripció |
|--------|------------|
| `index.qmd` | Document principal complet (sense límit de paraules) |
| `article.qmd` | Versió ICE reduïda (≤8.000 paraules al cos) |
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

### Versió ICE (`article.qmd`)
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

## Recompte de paraules (juny 2026)

| Secció | Paraules actuals | Màxim ICE | Estat |
|--------|-----------------|-----------|-------|
| Introducció | ~3.873 | 2.000 | cal reduir |
| Metodologia | ~2.384 | 2.000 | acceptable |
| Resultats | ~3.078 | 2.000 | cal reduir |
| Discussió | ~1.939 | 2.000 | ✓ |
| **Total cos** | **~11.274** | **8.000** | cal reduir |
| Annex | ~1.594 | lliure | suprimir |

Suprimir l'Annex elimina ~1.594 paraules. La resta de l'esforç se concentra
a Introducció (−~1.873) i Resultats (−~1.078).

## Arquitectura de fitxers (futura, pendent de decisió)

Opció en estudi: extreure Metodologia i Discussió a fitxers `_metodologia.qmd`
i `_discussio.qmd` i usar `{{< include >}}` tant a `index.qmd` com a `article.qmd`,
de manera que siguin font única de veritat per a les seccions que no canvien.
