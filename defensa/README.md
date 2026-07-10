# Defensa PFP — mini-projecte

Materials per a l'acte de defensa del Projecte Fi de Postgrau *«De MIPS a RISC-V amb IA supervisada»* (Estructura de Computadors, FIB-UPC).

**Acte:** 14/07/2026, 9:15–9:50, Aula S216 (Omega, soterrani ICE). Format: 15 min d'exposició + 10 min de preguntes.

## Contingut

| Fitxer | Descripció | Sortida |
|---|---|---|
| `defensa_EC.qmd` | Diapositives de l'exposició (13 slides) | reveal.js (HTML) |
| `guio_minutat.qmd` | Guió parlat, minutat, amb punts de control de ritme | HTML |
| `preguntes_tribunal.qmd` | Banc de preguntes previsibles del tribunal + respostes | HTML |
| `custom.scss` | Tema visual del deck (paleta de la memòria) | — |
| `_quarto.yml` | Configuració del mini-projecte | — |

**Figures:** el deck referencia `../figures/*.svg` i `*.png` — la carpeta `figures/` viu a l'arrel del repo (`ICE_PFP/figures/`), compartida amb la memòria, **no** dins de `defensa/`. No dupliquis aquesta carpeta: és la font de veritat per als dos projectes.

## Renderització

Aquest directori és un **projecte Quarto independent** del de la memòria (vegeu «Dos projectes» més avall). Per generar els tres documents de la defensa:

```bash
cd defensa
quarto render
```

Els resultats (`.html`, `.pdf`, i les carpetes `*_files/` amb dependències) es generen **al costat dels fitxers font**, dins de `defensa/` (no hi ha `output-dir`; vegeu la nota tècnica més avall). Per renderitzar un sol fitxer:

```bash
quarto render defensa_EC.qmd        # només el deck
quarto render guio_minutat.qmd      # només el guió
```

- Els documents de preparació (`guio_`, `preguntes_`) surten en **HTML** (TOC lateral, cercador, autocontinguts amb `embed-resources`).
- El deck s'ignora la config HTML del projecte i es genera com a **reveal.js** (ho fixa el seu propi *front matter*).
- Les figures SVG/PNG queden **incrustades** dins l'HTML final (`embed-resources: true`): un cop generat, el fitxer és un únic document portàtil que ja no depèn de `../figures/`. Ideal per presentar des d'un USB o un portàtil aliè. (Per *renderitzar*, en canvi, sí que cal `../figures/` disponible.)

## Dos projectes, dos renders

La memòria (arrel del repo) i la defensa (`defensa/`) són **dos projectes Quarto separats**, cadascun amb el seu `_quarto.yml` i el seu propi `quarto render`:

```bash
cd ~/git/ICE_PFP           && quarto render     # MEMÒRIA  → index.qmd → PDF llarg
cd ~/git/ICE_PFP/defensa   && quarto render     # DEFENSA  → deck + guió + preguntes
```

Això és **deliberat**, no una mancança: tenen `render:`, formats i motors diferents, i no vols regenerar la memòria sencera (lenta, amb LaTeX i portada) cada cop que retoques una diapositiva. Comparteixen només la *configuració comuna* via `metadata-files` (vegeu «DRY»), no el render.

## Com presentar el deck

Obre `defensa_EC.html` amb **Chrome** (recomanat per a la vista de presentador).

### Dreceres de teclat

| Tecla | Acció |
|---|---|
| `S` | Obre la **vista de presentador** en una finestra nova |
| `F` | Pantalla completa |
| `Esc` / `O` | Vista general (totes les slides) |
| `B` / `.` | Pausa (pantalla en negre) |
| `←` `→` | Navegar |

### La vista de presentador (`S`)

Mostra: la slide actual, la **slide següent** ("Upcoming"), les ***speaker notes***, el **rellotge de paret** i el **cronòmetre de la sessió**.

- **Selector "Layout"** (cantonada superior dreta): canvia la disposició del panell — `Default`, `Wide` i altres variants. Prova'l i queda't amb el que et vagi millor; Chrome el recorda per a properes obertures.
- **Zoom del text de les notes:** amb el focus a la finestra de la vista de presentador, `Ctrl` + `-` redueix la mida (un parell de cops sol bastar); `Ctrl` + `0` el torna a la mida per defecte. Chrome recorda el zoom per a aquest fitxer, així que ajustar-ho un cop val per al dia de la defensa.
- **Cronòmetre de ritme ("PACING – Time to finish current slide"):** sota el rellotge "TIME". Indica si vas bé de temps a la slide actual, amb codi de colors:
  - 🟢 **Verd** — vas a temps
  - 🔴 **Vermell** — has d'accelerar
  - 🔵 **Blau** — vas sobrat, pots relaxar el ritme
  - Es basa en el pressupost per slide (`data-timing`) fixat a `defensa_EC.qmd`, ja calibrat amb el guió minutat.
- **Reiniciar el cronòmetre:** **clic directe sobre el rellotge "TIME"** (no és una tecla). Útil per començar l'assaig o la defensa des de zero.

**Muntatge amb projector (doble pantalla):** estén l'escriptori (no el dupliquis). Posa la presentació a pantalla completa (`F`) a la pantalla del projector, i la vista de presentador (`S`) a la pantalla del portàtil. Reveal.js sincronitza les dues finestres: tu veus notes, cronòmetre i slide següent; el tribunal només veu la slide.

> **Requisits:** cal permetre finestres emergents (*pop-ups*) per a la vista de presentador. **Prova-ho el dia abans** amb el muntatge real de doble pantalla, i tingues el `guio_minutat.html` obert al mòbil com a xarxa de seguretat.
>
> ✅ **Validat el 09/07/2026** amb doble pantalla real: vista de presentador, cronòmetre de ritme (`data-timing` per slide) i notes, tots funcionant.

## Notes de manteniment

- **Rutes de les figures:** `figures/` viu a l'arrel del repo (`ICE_PFP/figures/`), no dins de `defensa/`. El deck hi referencia amb `../figures/...`. Si mai apareix `[WARNING] Could not fetch resource`, la primera comprovació és senzillament `ls ../figures/` des de `defensa/` — sol ser un problema de ruta relativa, no un bug de Quarto.
- **Cronòmetre de ritme (`data-timing` / `defaultTiming`):** Quarto **no reconeix `totalTime`** com a clau YAML del format `revealjs` (queda com a metadata pandoc solta, sense arribar a `Reveal.initialize()`). El cronòmetre s'activa via `include-after-body` a `defensa_EC.qmd`, que injecta `Reveal.configure({ defaultTiming: 65 })` (65 s = mitjana per slide). El pressupost específic de cada slide ve del `data-timing="N"` (segons) a cada capçalera `##`, que sí que es propaga correctament. **Si canvies el minutatge del guió, actualitza els `data-timing` de les capçaleres en conseqüència** — són al `.qmd`, cercables amb `grep data-timing defensa_EC.qmd`.
- **PDF dels documents de preparació:** el `_quarto.yml` genera PDF amb `pdf-engine: lualatex`, reaprofitant el format de la memòria (`scrartcl` + geometria). Per als emojis i fletxes (`✂️`, `⟵`, `→`) usa un *fallback* de font, que **requereix la font «Noto Color Emoji» instal·lada al sistema**:
  - Debian/Ubuntu: `sudo apt install fonts-noto-color-emoji`
  - Comprovació ràpida: `fc-list | grep -i "noto color emoji"`
  - Si algun glif encara surt buit, amplia la llista del `fallback` al `_quarto.yml` (p. ex. afegint `"Symbola:;"`), o bé sanitza els caràcters al text.
- **Relació amb la memòria:** projecte separat a propòsit. El `_quarto.yml` de la memòria té una llista de render explícita (`render: [index.qmd]`), de manera que els dos projectes no col·lideixen i aquests materials no arrosseguen la portada ni la configuració `scrartcl` del llibre.
- **DRY (aplicada):** els claus de configuració compartits amb la memòria (`lang`, `crossref` i els escalars de `format.pdf`: `documentclass`, `classoption`, `papersize`, `fontsize`, `colorlinks`, `urlcolor`, `linkcolor`) viuen a `../_format-common.yml` a l'arrel del repo, i s'inclouen des dels dos `_quarto.yml` amb `metadata-files`. La resta (geometria, `pdf-engine`, `include-in-header`, portada...) es queda local a cada projecte, perquè difereix o perquè conté rutes (`metadata-files` no reresol les rutes internes). Recorda: `format` és l'excepció a la fusió de metadades de Quarto **només** pel que fa a la *llista* de formats a nivell de document; les *opcions* dins d'un format sí que es fusionen entre nivells, que és el que fem servir aquí.
