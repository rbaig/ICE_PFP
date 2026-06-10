# CLAUDE.md — Memòria del PFP (EIC-UPC)

## Projecte

Memòria del **Projecte Fi de Postgrau** del Postgrau en Ensenyament
Universitari STEAM de l'Institut de Ciències de l'Educació (ICE) de la UPC.

**Títol**: Adopció de RISC-V com a arquitectura de
referència: Una oportunitat per a
l’actualització de continguts de l’assignatura
Estructura de computadors (EC) del Grau
en Enginyeria Informàtica (GEI) de la
Facultat d’informàtica de Barcelona (FIB)

**Autor**: Roger Baig Viñas
**Tutor**: Agustín Fernández Jiménez
**Col·laborador**: Pedro José Martínez Ferrer
**Agraïments**: David López Álvarez
**Data de lliurament**: 18 de juny de 2026

## Recursos relacionats

- **Repo del producte** (material migrat): https://github.com/rbaig/migracio.ec.gitlab.upc.edu
- **Repo de la memòria**: https://github.com/rbaig/EIC_PFP
- **Guia ICE**: `ICE_guiaPFP.pdf`

## Fitxers principals

- `index.qmd` — document principal complet (sense límit de paraules)
- `index_article.qmd` — versió ICE reduïda (≤8.000 paraules al cos)
- `_quarto.yml` — configuració Quarto base (HTML + PDF complet, KOMA `scrartcl`)
- `_quarto-article.yml` — perfil Quarto per a la versió ICE (`article`, sense TOC)
- `portada.tex` / `before-body.tex` — portada i preàmbul LaTeX (plantilla ICE; s'inclou a totes dues versions)
- `figures/` — figures SVG:
  - `eix_arquitectura.svg`
  - `etapa_produccio.svg`
  - `etapa_explotacio.svg`
  - `unitat_produccio.svg`
- `README.md` — documentació tècnica del projecte (renderització, profiles, recompte de paraules)

## Estructura del document (`index.qmd`)

1. Introducció
2. Metodologia
3. Resultats
4. Discussió, conclusions i altres propostes
5. Bibliografia (estil APA 7a edició, ordre alfabètic)
6. Annex: Reflexions sobre l'impacte de la IA generativa en la docència

**Nota**: `index_article.qmd` usa versions reduïdes de la Introducció i la Metodologia.

## Convencions

- Llengua: **català normatiu**
    - No Camel Case
- Bibliografia: **APA 7a edició** (ordre alfabètic)
- Figures: SVG amb `width="680"`, font Source Sans Pro, paleta Bootstrap; **sense versió dark**
- El terme "etapa" es fa servir exclusivament per referir-se a l'Etapa de producció o a l'Etapa d'explotació
- Noms de fases de l'Etapa de producció: tractats com a noms propis (majúscula inicial)
- Les etapes estan formades per "fases" (P1, P2, etc., U1, U2, etc. i E1, E2)
- Unitats de producció (P2): un fitxer `.qmd` per tema/sessió/PE/PS
- Unitats de revisió (P4): `{Tx.qmd + PE_Tx.qmd + PS_Tx.qmd}` per tema; cada `Lx.qmd` per separat
- Nom correcte del fitxer: `figures/eix_arquitectura.svg` (no `fig_eix_arquitectura.svg`)

## Guia ICE: restriccions

La guia estableix un límit de 8.000 paraules al cos del text.
- Per a `index.qmd`: **no és una restricció operativa**; preval la qualitat i completesa.
- Per a `index_article.qmd`: **és una restricció estricta** (versió de lliurament formal a l'ICE).

## Flux de treball

1. Claude edita `index.qmd` i/o `index_article.qmd` a la sessió de treball.
2. L'usuari descarrega, revisa localment amb VS Code i fa `quarto render`.
   - Versió completa: `quarto render index.qmd`
   - Versió ICE: `quarto render index_article.qmd --profile article`
3. L'usuari fa `git push` quan el resultat és satisfactori.
4. Claude no edita fitxers directament al repositori.

## Nomenclatura de fases del projecte

El projecte s'estructura en dues etapes amb nomenclatura pròpia:

### Etapa de producció

| Fase | Nom | Unitat de treball |
|------|-----|-------------------|
| P1 | Disseny del sistema de producció | — |
| P2 | Unitats de producció | Un fitxer `.qmd` |
| P3 | Revisió de Conjunt | Corpus sencer |
| P4 | Cicle de Revisió Externa | `{Tx.qmd + PE_Tx.qmd + PS_Tx.qmd}` per tema; `Lx.qmd` per separat |
| P5 | Preparació de la docència | — |

### Etapa d'explotació (iterativa per quadrimestres)

| Fase | Nom |
|------|-----|
| E1 | Disseny del sistema d'explotació |
| E2 | Preparació docent (`Dx.qmd`) |

### Cicle de producció unitària (dins P2)

| Etapa | Nom |
|-------|-----|
| U1 | Extracció i conversió |
| U2 | Revisió tècnica (RARS + coherència) |
| U3 | Revisió lingüística (lèxic, sintaxi) — itera amb U2 |
| U4 | Figures (`.svg`) |
| U5 | Actualització transversal (`sigles.qmd`, `risc.qmd`) |
| U6 | Refinament protocols (`contrib.qmd`, `CLAUDE.md`) |

### Definitions of Done

- **DoD-UP** (DoD d'Unitat de Producció): criteris per a cada unitat de producció; s'aplica 33 vegades (una per fitxer .qmd)
- **DoD-CC** (DoD de Corpus Complet): criteris per a la Revisió de Conjunt; s'aplica una sola vegada
- **DoD-UR** (DoD d'Unitat de Revisió): criteris per a la Revisió Externa; s'aplica una vegada per unitat de revisió

## Context clau

- La memòria és per a l'ICE: la **innovació pedagògica és el centre de la narrativa**.
- El producte és la migració del material docent d'EC de MIPS a RISC-V en format Quarto Markdown.
- El corpus és de **36 fitxers** `.qmd`: T1–T9, L1–L6, PE_T1–T9, PS_T1–T9 i materials transversals.
- El material és al **100%** complet; la **Revisió Externa (P4)** és en curs.
- L'eina principal ha estat **Claude** (prèviament NotebookLM en fase d'exploració).
- La implantació a l'aula és al **Q1 del curs 2026-27** (setembre 2026).
- La data de referència de la memòria és el **18 de juny de 2026**.

## Estat actual

### `index.qmd` (versió completa)

Revisió profunda completada (sessió 2, juny 2026):
- Costures polides: 2 bullets de reestructuració pedagògica (T1→T1+T6; T4/T5) integrats a `_3_resultats.qmd §Redisseny del contingut`; Innovació 2 a `_2_metodologia.qmd` referencia `@sec-disseny-pedagogic`.
- Errors corregits: RA2 (MIPS→RISC-V), errades tipogràfiques i llegendes de taules.
- Totes les referències creuades (`@sec-`, `@tbl-`, `@fig-`) verificades correctes.
- Escala de supervisió P2–P5 homogeneïtzada (P5: ara "Màxim").

**TODO obert**: columna `Solució` de `tbl-reestructuracio-problemes` (`_3_resultats.qmd`, comentari `<!-- TODO afegir si solució -->`). 23 exercicis nous; caldrà confirmar si tots tenen solució als `PS_Tx.qmd` i omplir-la o eliminar-la.

**Pendent**: actualitzar el recompte de paraules (ha canviat per les edicions d'aquesta sessió).

Recompte post-revisió profunda (juny 2026, sessió 2):

| Secció | Fitxer | Paraules |
|--------|--------|---------|
| Introducció | `_1_introduccio.qmd` | 3.670 |
| Metodologia | `_2_metodologia.qmd` | 3.281 |
| Resultats | `_3_resultats.qmd` | 1.577 |
| Discussió | `_4_discussio.qmd` | 1.823 |
| **Total cos** | | **10.351** |

### `index_article.qmd` (versió ICE, ≤8.000 paraules)

Pendent de consolidar un cop tancada la revisió de `index.qmd`.

Recompte previ a la reestructuració (referència):

| Secció | Fitxer | Paraules |
|--------|--------|---------|
| Introducció | `_1_introduccio_article.qmd` | 1.968 |
| Metodologia | `_2_metodologia_article.qmd` | 1.953 |
| Resultats | `_3_resultats.qmd` (compartit) | 1.655 |
| Discussió | `_4_discussio.qmd` (compartit) | 1.776 |
| **Total cos** | | **7.352** |

Resum, abstract, bibliografia i annex no compten per al límit.

## Propera sessió

### Tancament de `index.qmd` (`scrartcl`)

1. Actualitzar el recompte de paraules a `README.md` i `CLAUDE.md` (fer `quarto render` i executar `count_prose.py`).
2. Resoldre el TODO de la columna `Solució` de `tbl-reestructuracio-problemes` (`_3_resultats.qmd`, comentari `<!-- TODO afegir si solució -->`): confirmar si tots els 23 exercicis nous tenen solució als `PS_Tx.qmd` i omplir-la o eliminar-la.
