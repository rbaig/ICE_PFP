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

Aquest directori és un **projecte Quarto independent** del de la memòria. Per generar-ho tot:

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
- Les figures SVG/PNG queden **incrustades** dins l'HTML (`embed-resources: true`): cada sortida és un únic fitxer portàtil, sense dependència de la carpeta `figures/`. Ideal per presentar des d'un USB o un portàtil aliè.

## Com presentar el deck

Obre `_output/defensa_EC.html` amb **Chrome** (recomanat per a la vista de presentador) i:

| Tecla | Acció |
|---|---|
| `S` | Obre la **vista de presentador** en una finestra nova: slide actual, **slide següent**, les *speaker notes* i un **cronòmetre** (temps transcorregut) + rellotge |
| `F` | Pantalla completa |
| `Esc` / `O` | Vista general (totes les slides) |
| `B` / `.` | Pausa (pantalla en negre) |
| `←` `→` | Navegar |

**Muntatge amb projector (doble pantalla):** estén l'escriptori (no el dupliquis). Posa la presentació a pantalla completa (`F`) a la pantalla del projector, i la vista de presentador (`S`) a la pantalla del portàtil. Reveal.js sincronitza les dues finestres: tu veus notes, cronòmetre i slide següent; el tribunal només veu la slide.

> **Requisits:** cal permetre finestres emergents (*pop-ups*) per a la vista de presentador. **Prova-ho el dia abans** amb el muntatge real de doble pantalla, i tingues el `guio_minutat.html` obert al mòbil com a xarxa de seguretat.

## Notes de manteniment

- **Rutes de les figures:** `figures/` viu a l'arrel del repo (`ICE_PFP/figures/`), no dins de `defensa/`. El deck hi referencia amb `../figures/...`. Si mai apareix `[WARNING] Could not fetch resource`, la primera comprovació és senzillament `ls ../figures/` des de `defensa/` — sol ser un problema de ruta relativa, no un bug de Quarto.
- **PDF dels documents de preparació:** el `_quarto.yml` genera PDF amb `pdf-engine: lualatex`, reaprofitant el format de la memòria (`scrartcl` + geometria). Per als emojis i fletxes (`✂️`, `⟵`, `→`) usa un *fallback* de font, que **requereix la font «Noto Color Emoji» instal·lada al sistema**:
  - Debian/Ubuntu: `sudo apt install fonts-noto-color-emoji`
  - Comprovació ràpida: `fc-list | grep -i "noto color emoji"`
  - Si algun glif encara surt buit, amplia la llista del `fallback` al `_quarto.yml` (p. ex. afegint `"Symbola:;"`), o bé sanitza els caràcters al text.
- **Relació amb la memòria:** projecte separat a propòsit. El `_quarto.yml` de la memòria té una llista de render explícita (`render: [index.qmd]`), de manera que els dos projectes no col·lideixen i aquests materials no arrosseguen la portada ni la configuració `scrartcl` del llibre.
- **DRY (futur):** si es vol eliminar la duplicació de format entre els dos projectes, el patró idiomàtic és extreure els claus compartits a un `_format-common.yml` a l'arrel i incloure'l des dels dos amb `metadata-files`.
