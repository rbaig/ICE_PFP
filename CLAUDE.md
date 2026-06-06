# CLAUDE.md — Memòria del PFP (EIC-UPC)

## Projecte

Memòria del **Projecte Fi de Postgrau** del Postgrau en Ensenyament
Universitari STEAM de l'Institut de Ciències de l'Educació (ICE) de la UPC.

**Títol**: *Actualització de continguts de l'assignatura Estructura de
computadors (EC) del GEI; adopció de RISC-V com a arquitectura de
referència.*

**Autor**: Roger Baig
**Tutor**: Agustín Fernández Jiménez
**Col·laborador**: Pedro José Martínez Ferrer
**Data de lliurament**: 18 de juny de 2026

## Recursos relacionats

- **Repo del producte** (material migrat): https://github.com/rbaig/migracio.ec.gitlab.upc.edu
- **Guia ICE**: `ICE_guiaPFP.pdf`

## Fitxers principals

- `index.qmd` — document principal de la memòria (Quarto Markdown)
- `_quarto.yml` — configuració de Quarto (HTML + PDF)
- `portada.tex` / `before-body.tex` — portada i preàmbul LaTeX
- `figures/` — figures SVG (`fig_eix_arquitectura.svg`, `fig_flux_produccio.svg`, `fig_fases_produccio.svg`)

## Estructura del document

`index.qmd` segueix l'estructura de la Guia ICE:

1. Introducció
2. Metodologia
3. Resultats
4. Discussió, conclusions i altres propostes
5. Bibliografia (estil APA 7a edició, ordre alfabètic)
6. Annex: Reflexions sobre l'impacte de la IA generativa en la docència

## Convencions

- Llengua: **català normatiu**
- Bibliografia: **APA 7a edició** (ordre alfabètic)
- Figures: SVG amb `width="680"`, font Source Sans Pro, paleta Bootstrap
- Noms de fases: tractats com a noms propis (majúscula inicial)
- Unitats de producció (F2): un fitxer `.qmd` per tema/sessió/PE/PS
- Unitats de revisió (F4): `{Tx.qmd + PE_Tx.qmd + PS_Tx.qmd}` per tema; cada `Lx.qmd` per separat

## Guia ICE: restriccions que no apliquen

La guia estableix un límit de 8.000 paraules al cos del text. Aquest límit
**no és una restricció operativa** per a aquest projecte: preval la qualitat
i completesa del contingut. El tribunal avaluarà el fons, no el recompte.

## Flux de treball

1. Claude edita `index.qmd` directament a la sessió de treball.
2. L'usuari descarrega, revisa localment amb VS Code i fa `quarto render`.
3. L'usuari fa `git push` quan el resultat és satisfactori.
4. Claude no edita fitxers directament al repositori.

## Context clau

- La memòria és per a l'ICE: la **innovació pedagògica és el centre de la narrativa**.
- El producte és la migració del material docent d'EC de MIPS a RISC-V en format Quarto Markdown.
- El corpus és de **36 fitxers** `.qmd`: T1–T9, L1–L6, PE_T1–T9, PS_T1–T9 i materials transversals.
- El material és al **100%** complet; la **Revisió Externa (F4)** és en curs.
- L'eina principal ha estat **Claude** (prèviament NotebookLM en fase d'exploració).
- La implantació a l'aula és al **Q1 del curs 2026-27** (setembre 2026).
- La data de referència de la memòria és el **18 de juny de 2026**.
- Les tres **Definitions of Done** (DoD-F2, DoD-F3, DoD-F4) són un element diferencial del projecte.

## Estructura de fases del projecte

| Fase | Nom | Unitat de treball |
|------|-----|-------------------|
| F1 | Disseny del sistema de producció | — |
| F2 | Producció del corpus docent | Un fitxer `.qmd` |
| F3 | Revisió de Conjunt | Corpus sencer |
| F4 | Cicle de Revisió Externa | T+PE+PS per tema; Lx per separat |
| F5 | Preparació de la docència | — |
| — | Implementació a l'aula | Q1 2026-27 |

## Estat actual

- [x] Estructura completa del document acordada i implementada
- [x] §1 Introducció complet
- [x] §2 Metodologia complet (incl. DoD-F2, DoD-F3, DoD-F4)
- [x] §3 Resultats complet (incl. taula de característiques diferencials)
- [x] §4 Discussió complet (incl. Enriquiment personal, Propostes, Connexions)
- [x] Annex IA complet
- [x] Bibliografia: APA 7a, ordre alfabètic
- [x] Figures: `fig_eix_arquitectura.svg`, `fig_flux_produccio.svg`, `fig_fases_produccio.svg`
- [x] Revisió profunda de consistència completada
