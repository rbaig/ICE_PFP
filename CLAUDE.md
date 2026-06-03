# CLAUDE.md — Memòria del PFP (EIC-UPC)

## Projecte

Memòria del **Projecte Fi de Postgrau** del Postgrau en Ensenyament
Universitari STEAM de l'Institut de Ciències de l'Educació (ICE) de la UPC.

**Títol**: *Actualització de continguts de l'assignatura Estructura de
computadors (EC) del GEI; adopció de RISC-V com a arquitectura de
referència.*

**Autor**: [Nom i Cognoms]
**Tutor**: Agustín Fernández Jiménez
**Col·laborador**: Pedro José Martínez Ferrer
**Data de lliurament**: 18 de juny de 2026

## Recursos relacionats

- **Repo del producte** (material migrat): https://github.com/rbaig/migracio.ec.gitlab.upc.edu
- **Memòria de treball** (Google Doc): https://docs.google.com/document/d/1HtpZh0ttS7QQrrJrVNihTAMCkIOcU9t_Qj0_z-P399o
- **Guia ICE**: `Guia_Projecte_Postgrau_2025-2026.pdf`

## Estructura del document

`memoria.md` és el fitxer principal. Segueix l'estructura obligatòria de la
Guia ICE:

1. Introducció (~2.000 paraules)
2. Metodologia (~2.000 paraules)
3. Resultats (~2.000 paraules)
4. Discussió, conclusions i altres propostes (~2.000 paraules)
5. Bibliografia (estil APA 7a edició, ~25 referències)
6. Annexos

## Convencions

- Llengua: **català**
- Bibliografia: **APA 7a edició** (ordre alfabètic)
- Tot el contingut generat ha de ser en blocs de codi markdown
- No editar fitxers directament: l'usuari fa el commit/push
- En cas de dubte: atura't i pregunta

## Flux de treball

1. Claude escriu/edita `memoria.md` directament al repo.
2. L'usuari fa `git pull`, revisa amb VS Code i fa `git push` quan és llest.

## Context clau per a Claude

- La memòria és per a l'ICE: la **innovació pedagògica és el centre de la narrativa**.
- El producte del projecte és la migració del material docent d'EC de MIPS a RISC-V en format Quarto Markdown, allotjat al repo de producte.
- La migració ha assolit el **95% del material**: T1–T9, L1–L6, PE, PS_T2–T5.
- L'eina principal ha estat **Claude** (prèviament NotebookLM en fase inicial).
- La implantació a l'aula està prevista per al **Q1 del curs 2025-26** (setembre).
- La memòria ha de servir també com a base per a la **proposta del concurs d'estabilització** de plaça a la UPC.
- Límit de paraules de la guia (8.000): no és una restricció operativa; preval la qualitat i completesa.

## Estat actual

- [x] Revisió completa del Google Doc
- [x] Nova estructura del document acordada
- [x] §1 complet (incl. nota reestructuració §1.1.2; TODO §1.7 eliminat)
- [x] §2 complet (incl. §2.2.3 amb taula de mapping MIPS→RISC-V)
- [x] §3 complet (les 4 subseccions)
- [x] §4 complet (les 4 subseccions: contrast teòric, valoració crítica, continuïtat, connexions)
- [x] Annex I complet
- [x] Bibliografia: 8 refs APA 7a (corregit Waterman, URL Winans, afegit WCAG 2.1)
- [x] §2.1/§2.2/§2.3: Addenda inexistent al doc; contingut ja integrat
- [x] Resum/Abstract: reescrits amb resultats reals
