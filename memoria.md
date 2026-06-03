---
title: "Actualització de continguts de l'assignatura Estructura de computadors (EC) del Grau en Enginyeria Informàtica (GEI); adopció de RISC-V com a arquitectura de referència"
author: "Nom i Cognoms"
date: "18 de juny de 2026"
lang: ca
---

<!-- ============================================================
     NOTA PER A CLAUDE
     Aquest fitxer és la memòria del PFP. Vegeu CLAUDE.md per al
     context complet del projecte i l'estat actual de la feina.
     Els comentaris <!-- TODO: ... --> marquen les seccions pendents.
     ============================================================ -->

# Resum

<!-- TODO: Actualitzar temps verbals i afegir resultats reals un cop
     el cos del document estigui madur. Fer-ho al final. -->

Aquest projecte aborda la necessitat de modernitzar la formació en l'àmbit de l'estructura de computadors mitjançant la incorporació de l'arquitectura RISC-V com a referència. Aquest canvi no és fútil, sinó una aposta decidida per la innovació pedagògica, atès que RISC-V s'ha consolidat com l'arquitectura emergent i de codi obert que està revolucionant la indústria i l'acadèmia. La seva selecció com a eix central per als estudis d'informàtica garanteix que els futurs professionals adquireixin coneixements amb una visió de futur i en línia amb les tendències tecnològiques més actuals.

La rellevància i l'oportunitat temporal d'aquest projecte són inqüestionables. En un context global on la sobirania tecnològica i la seguretat del *hardware* són prioritats estratègiques, la Unió Europea ha identificat RISC-V com una tecnologia *flagship* (tecnologia capdavantera). Aquesta aposta institucional subratlla la importància d'invertir en la formació basada en aquesta arquitectura, la qual fomenta la innovació, redueix la dependència de tecnologies propietàries i obre la porta a la creació d'ecosistemes d'innovació local i col·laborativa.

L'impacte esperat en l'alumnat és significatiu i es centra en l'adquisició i consolidació dels principis fonamentals d'estructura de computadors. RISC-V, gràcies al seu disseny intel·ligent, simplicitat i sistematicitat, ofereix un vehicle pedagògic excepcional. A diferència d'arquitectures més complexes i amb llast històric, la netedat conceptual de RISC-V permet als estudiants entendre de manera clara i profunda com es tradueixen les instruccions en operacions de maquinari. Això no només facilita l'aprenentatge, sinó que també fomenta un pensament més analític i una millor capacitat per a dissenyar i optimitzar sistemes *hardware* i *software*.

**Paraules clau**: RISC-V, estructura de computadors, arquitectura de computadors, llenguatge d'assemblador, STEAM, aprenentatge assistit per intel·ligència artificial.

---

# Abstract

<!-- TODO: Actualitzar temps verbals i afegir resultats reals. Fer-ho al final. -->

This project addresses the need to modernize education in the field of computer organization by incorporating the RISC-V architecture as a reference. This change is not trivial, but a firm commitment to pedagogical innovation, given that RISC-V has established itself as the emergent, open-source architecture that is revolutionizing industry and academia. Its selection as the central pillar for computer science studies ensures that future professionals acquire knowledge with a forward-looking vision and in line with the most current technological trends.

The relevance and timeliness of this project are unquestionable. In a global context where technological sovereignty and hardware security are strategic priorities, the European Union has identified RISC-V as a *flagship* technology. This institutional commitment underscores the importance of investing in training based on this architecture, which promotes innovation, reduces dependence on proprietary technologies, and opens the door to the creation of local and collaborative innovation ecosystems.

The expected impact on students is significant and focuses on the acquisition and consolidation of the fundamental principles of computer organization. RISC-V, thanks to its intelligent design, simplicity, and systematic nature, offers an exceptional pedagogical vehicle. Unlike more complex architectures with historical baggage, the conceptual clarity of RISC-V allows students to understand clearly and profoundly how instructions are translated into hardware operations. This not only facilitates learning but also fosters more analytical thinking and a greater capacity to design and optimize hardware and software systems.

**Keywords**: RISC-V, computer organization, computer architecture, assembly language, STEAM, artificial intelligence assisted learning.

---

# 1. Introducció

## 1.1. Context

### 1.1.1. L'eix d'arquitectura de computadors en el pla d'estudis FIB-GEI

L'assignatura d'Estructura de computadors (EC), de la qual soc coordinador des del segon quadrimestre del curs 2024-25, és una assignatura del segon quadrimestre de la fase inicial (FI) del Grau en enginyeria informàtica (GEI) de la Facultat d'informàtica de Barcelona (FIB) de la Universitat Politècnica de Catalunya (UPC). Pel que fa a l'itinerari de l'estudiantat, tot i que el pla d'estudis del GEI no estableix requisits per a les assignatures de la FI, un gruix significatiu de continguts d'EC tenen els fonaments en continguts de l'assignatura de primer quadrimestre Introducció als computadors (IC). Superada la fase inicial, EC és requisit de Interfícies de Computadors (CI) i Sistemes operatius (SO), totes dues de tercer quadrimestre, i Arquitectura de computadors (AC), de quart quadrimestre.

Arquitectònicament, a IC els estudiants, sense necessitat de cap coneixement previ de circuits digitals, arriben a comprendre en detall el disseny d'un computador (teòric) senzill format per un processador que consta d'unes 3.000 portes lògiques i uns 100 biestables, una memòria principal i un subsistema d'entrada/sortida amb un teclat i una impressora. S'estudien les bases dels circuits digitals combinacionals i seqüencials, es construeixen processadors formats per una unitat de procés i una unitat de control ambdues específiques per a la resolució d'un sol problema i s'arriba al processador de l'ordinador fent generals la unitat de procés i la de control, creant un llenguatge màquina de 25 instruccions que serveix per a executar qualsevol programa que poguéssim escriure en un llenguatge d'alt nivell.

A EC, partint de la base del disseny de computadors senzills après a IC, els estudiants fan el salt cap a l'estudi d'un microprocessador real i d'ús industrial. L'assignatura aprofundeix en l'arquitectura del computador analitzant els conceptes fonamentals d'ISA (*Instruction Set Architecture*) i ABI (*Application Binary Interface*), entenent com es defineix la frontera entre el programari i el maquinari. Al llarg del curs, s'estudia en detall el funcionament d'un subconjunt representatiu del repertori d'instruccions de RISC-V; aquest repertori és reduït precisament per simplificar el disseny del maquinari i permetre que cada instrucció s'executi de manera més ràpida i eficient. Aquest coneixement es posa en pràctica mitjançant la traducció de programes curts i fragments de codi de llenguatge C a llenguatge d'assemblador, permetent que l'estudiant comprengui com les estructures d'alt nivell es converteixen en instruccions reals. A més, s'introdueix la jerarquia de memòria amb l'estudi de la memòria cau, analitzant com la localitat de referència millora el rendiment global del sistema. Finalment, s'aborda la robustesa del sistema mitjançant la gestió d'excepcions i interrupcions, aprenent com el processador reacciona davant d'esdeveniments inesperats o peticions del sistema operatiu per garantir una execució controlada i segura.

A AC, un cop dominada l'estructura bàsica i el repertori d'instruccions a EC, els estudiants s'endinsen en el disseny de computadors d'alt rendiment mitjançant l'estudi de la segmentació (*pipelining*). Prenent com a referència l'arquitectura x86, s'analitza com dividir l'execució de les instruccions en etapes per augmentar el paral·lelisme a nivell d'instrucció (ILP), identificant i resolent els riscos o *hazards* estructurals, de dades i de control que sorgeixen en el flux de dades. Aquesta anàlisi es complementa amb l'estudi de la jerarquia de memòria avançada, on s'aprofundeix en el disseny i l'impacte de les memòries cau en el rendiment del sistema, així com en la gestió de la memòria virtual per garantir la protecció i l'eficiència en l'accés a les dades.

Així doncs, l'itinerari formatiu compost per IC, EC i AC constitueix el tronc central de l'eix d'arquitectura del GEI de la FIB. Aquesta seqüència representa l'itinerari tradicional i consolidat en els plans d'estudis d'informàtica a nivell internacional, ja que permet una evolució pedagògica natural: després de comprendre la lògica digital amb un processador teòric a IC, el pas per EC utilitzant una arquitectura RISC (*Reduced Instruction Set Computer*) és fonamental; el seu joc d'instruccions reduït i altament regular actua com el pas intermedi ideal, permetent a l'estudiant dominar els conceptes d'execució i traducció sense la complexitat del maquinari real. Finalment, a AC es culmina l'aprenentatge amb el model CISC (*Complex Instruction Set Computer*), on s'estudien arquitectures com x86 que, tot i la seva riquesa i heterogeneïtat d'instruccions, s'aborden amb èxit gràcies a la base sòlida adquirida prèviament.

### 1.1.2. L'assignatura Estructura de computadors (EC)

#### Objectiu general

L'estudiant ha de ser capaç de comprendre i analitzar la frontera entre el programari i el maquinari (*Hardware/Software Interface*), dominant el funcionament intern d'un processador industrial basat en l'arquitectura RISC-V i els mecanismes que regeixen el rendiment i la robustesa del sistema.

#### Resultats d'aprenentatge específics

Per garantir un aprenentatge profund, els resultats d'aprenentatge específics (RA) s'estructuren segons la taxonomia de Bloom, anant des del coneixement fins a l'anàlisi i l'avaluació:

- **RA1. Anàlisi del rendiment i l'arquitectura**
  - Identificar els diferents nivells d'abstracció d'un computador i la seva descripció jeràrquica.
  - Avaluar el rendiment i el consum de potència d'un sistema computacional aplicant mesures estàndard i la Llei d'Amdahl per determinar l'impacte de les millores en el maquinari.

- **RA2. Domini de la frontera Programari-Maquinari (ISA/ABI)**
  - Relacionar la representació de dades bàsiques (naturals, enters i caràcters) i complexes (punters, vectors, matrius i cadenes de caràcters) amb la seva implementació física en memòria.
  - Traduir fragments de codi de llenguatge d'alt nivell (C) a llenguatge d'assemblador RISC-V, fent ús correcte de les estructures de control, les subrutines i les convencions de l'ABI.

- **RA3. Aritmètica del computador**
  - Explicar el funcionament dels algorismes de l'aritmètica d'enters (suma, resta, multiplicació i divisió) i la representació en coma flotant sota l'estàndard IEEE 754.

- **RA4. Optimització de la jerarquia de memòria**
  - Analitzar el comportament de la memòria cau i la memòria virtual per optimitzar el rendiment del sistema basant-se en els principis de localitat espacial i temporal.
  - Dissenyar esquemes bàsics de mapeig i associativitat, i calcular mètriques de fallada de memòria per avaluar-ne l'eficiència.

- **RA5. Robustesa i gestió d'esdeveniments**
  - Comprendre el suport del maquinari per a la gestió d'excepcions i interrupcions, identificant com el processador reacciona davant de fallades de sistema (com les de la TLB) o crides al sistema operatiu (*syscalls*).

#### Seqüenciació temàtica i programació temporal

<!-- TODO: Actualitzar amb la nova estructura T1-T9 RISC-V.
     Afegir nota sobre la reestructuració: T1 antic → T1+T6 nous;
     aritmètica entera T5 antic → T4 nou; T5 nou = coma flotant exclusivament. -->

**Tema 1. Introducció:** Descripció jeràrquica del computador. Codificació de naturals i enters. Setmana 1.

**Tema 2. Instruccions i tipus de dades bàsics:** Introducció a la ISA de RISC-V. Formats d'instrucció. Variables, memòria, operands, punters, vectors i cadenes. Setmanes 2 i 3.

**Tema 3. Traducció de programes:** Operacions lògiques i desplaçaments. Sentències *if* i bucles. Subrutines. Compilació, assemblatge, enllaçat i càrrega. Setmanes 4 i 5.

**Tema 4. Aritmètica entera i matrius:** Suma, resta, multiplicació i divisió d'enters. Sobreeiximent. Matrius i optimitzacions de bucle. Setmana 6.

**Tema 5. Coma flotant:** Representació IEEE 754. Operacions en coma flotant. Coma flotant a RISC-V (RV32F). Setmanes 7 i 8.

**Tema 6. Rendiment i potència:** Mesures de rendiment. Llei d'Amdahl. Potència i escalat de Dennard. Setmana 9.

**Tema 7. Memòria cau:** Jerarquia de memòria. Polítiques d'emplaçament, reemplaçament i escriptura. Rendiment. Tipologia de fallades. Caches multinivell. Setmanes 10 i 11.

**Tema 8. Memòria virtual:** Paginació. Taula de pàgines. Fallada de pàgina. TLB. Setmana 12.

**Tema 9. Excepcions i interrupcions:** Registres CSR de RISC-V. Flux *hardware* en detectar una excepció. Rutina de servei. Crides al sistema. Interrupcions. Fallada de TLB. Setmana 13.

#### Relació entre resultats d'aprenentatge i seqüenciació temàtica

**Temes 1 i 6:** Alimenten el RA1 (Rendiment i arquitectura).

**Temes 2, 3, 4 i 5:** Construeixen el RA2 (Assemblador i traducció) i el RA3 (Aritmètica).

**Temes 7 i 8:** Construeixen el RA4 (Jerarquia de memòria).

**Tema 9:** Finalitza amb el RA5 (Excepcions i interrupcions).

#### Metodologia

Les classes de teoria combinaran la part magistral, on el professor exposarà, explicarà i exemplificarà els conceptes objectiu de l'assignatura, amb la discussió amb l'alumnat sobre les alternatives i avantatges/inconvenients dels aspectes que sigui convenient debatre.

Les classes de problemes es realitzaran de tres maneres: resolució directa del professor amb comentaris dels alumnes; resolució individual per part dels alumnes; i resolució cooperativa. En els dos darrers casos, el professor proporcionarà la retroalimentació necessària per corregir les parts incorrectes.

Les classes de laboratori seguiran una dinàmica similar a la de problemes, però la resolució d'exercicis es farà únicament en parelles i utilitzant eines que permeten la verificació semiautomàtica de les solucions. Els exercicis del laboratori s'avaluaran de forma continuada per estimular el treball regular.

#### Materials docents

- **Webs:** FIB-GEI3 (guia docent oficial), Racó (campus virtual) i web de l'assignatura (DAC).
- **Apunts de teoria** (T1–T9)
- **Problemes i solucionaris** (PE, PS_T2–T5)
- **Quadern de pràctiques de laboratori** (S1–S6)
- **Compendi de referència RISC-V**

Els materials, originalment en format PDF sense fonts editables, han estat migrats íntegrament a format Quarto Markdown (.qmd) i es troben disponibles en un repositori públic de GitHub, amb sortida en HTML i PDF des d'un únic punt d'entrada.

#### Avaluació

Nota numèrica: 0,20·max{EP,EF} + 0,60·EF + 0,20·(0,85·EL + 0,15·AC)

- EP: nota de l'examen parcial
- EF: nota de l'examen final
- EL: nota de l'examen de laboratori
- AC: nota de l'avaluació continuada de laboratori

Reavaluació: sí, cada quadrimestre.

## 1.2. Descripció de les necessitats, oportunitats o problemàtiques detectades

### 1.2.1. Necessitat: conveniència de l'actualització de l'arquitectura de referència

L'arquitectura MIPS va revolucionar la computació en introduir el concepte de *pipeline* sense bloquejos, una innovació radical que delegava la gestió dels conflictes de dades al compilador en lloc del maquinari. Aquesta simplicitat es traduïa en un cicle d'instrucció únic, instruccions de longitud fixa de 32 bits i una estricta estructura *Load/Store*. En conjunt, MIPS va demostrar que un maquinari simplificat, en mans d'un programari intel·ligent, era la clau per a la potència computacional moderna.

RISC-V és un projecte d'ISA obert i lliure d'ús, sorgit de la Universitat de Califòrnia, Berkeley. Va ser ideat per alguns dels mateixos enginyers que van ser pioners en l'arquitectura MIPS, i es beneficia de més de quaranta anys d'experiència en el disseny d'arquitectures RISC. La naturalesa oberta de RISC-V, amb una llicència permissiva, el distingeix d'altres arquitectures propietàries, permetent a qualsevol empresa o individu dissenyar, fabricar i vendre xips sense pagar drets de llicència. Un aspecte crucial de la seva importància actual és que RISC-V ha estat adoptada com a arquitectura de referència estratègica per diverses institucions i governs, incloent-hi la Unió Europea, que la veu com una eina clau per impulsar la sobirania tecnològica.

Així doncs, la migració de MIPS a RISC-V a EC no és només una actualització de continguts, sinó una decisió estratègica que alinea la formació dels futurs enginyers informàtics amb les tendències actuals i futures de la indústria i l'acadèmia.

### 1.2.2. Oportunitat 1: migració de l'arquitectura de referència

Tècnicament, RISC-V presenta avantatges significatius sobre MIPS que el fan més adequat per a l'ensenyament. En primer lloc, RISC-V és una ISA oberta i lliure de drets d'ús, cosa que fomenta un ecosistema ric i accessible d'eines de desenvolupament, simuladors i implementacions en maquinari. Els estudiants poden descarregar i modificar lliurement compiladors i simuladors, o fins i tot dissenyar els seus propis processadors RISC-V sense les barreres legals o de cost associades a les arquitectures propietàries.

Un altre punt clau és la modularitat i simplicitat del disseny de RISC-V. L'ISA base (RV32I) conté menys de 50 instruccions, la qual cosa facilita enormement la comprensió inicial dels conceptes fonamentals del disseny de processadors. A partir d'aquesta base, es poden afegir extensions estàndard de manera modular (multiplicació i divisió, coma flotant, operacions atòmiques, etc.). Aquest enfocament «a la carta» permet al professorat estructurar el curs de manera progressiva, introduint complexitat a mesura que els estudiants assimilen els conceptes bàsics.

Finalment, RISC-V ha estat dissenyat des de zero tenint en compte les necessitats de la investigació i la docència modernes. Evita certes decisions de disseny heretades de MIPS que generaven confusió als estudiants, com ara el *branch delay slot*, un artefacte de dissenys de *pipeline* antics que ja no és rellevant en processadors moderns. L'eliminació d'aquestes complexitats permet centrar el temps de classe en conceptes fonamentals i actuals.

### 1.2.3. Oportunitat 2: revisió i harmonització dels continguts

S'aprofita l'actualització de l'ISA per dur a terme una revisió exhaustiva de tot el material docent. L'objectiu principal és no només adaptar els exemples i la sintaxi al nou ISA, sinó també harmonitzar i millorar la qualitat general dels recursos. Aquesta revisió inclou els apunts de teoria, les llistes de problemes, els solucionaris, el quadern de laboratori i un nou compendi de referència RISC-V que substitueix completament l'anterior compendi MIPS.

### 1.2.4. Oportunitat 3: format obert, accessibilitat i processament automatitzat

Separar els continguts de les metadades de presentació i estructurar-los jeràrquicament i de manera sistemàtica els fa molt més accessibles tant a les persones com a les màquines. S'aprofita l'actualització per dissociar i curar els continguts, que és on resideix realment el valor.

L'ús sistemàtic d'un llenguatge de marcatge jeràrquic com **Markdown** té, comparat amb el format PDF actual dels materials, dos avantatges clau: l'**accessibilitat universal** (les tecnologies assistives com els lectors de pantalla poden navegar el contingut de manera fluida) i la **integració de la IA** (els models de llenguatge interpreten amb més precisió els documents ben estructurats, facilitant la generació de resums, exercicis personalitzats i anàlisi de dades d'aprenentatge).

**Quarto** és la plataforma de publicació científica i tècnica de codi obert triada per a aquest projecte. Un únic fitxer `.qmd` es pot renderitzar a múltiples formats d'alta qualitat (HTML, PDF, Word) i el sistema compleix els criteris d'accessibilitat de l'estàndard WCAG 2.1 del W3C. La integració amb **GitHub** permet el control de versions i la col·laboració asíncrona entre el professorat, assegurant que tots els materials estiguin sempre harmonitzats.

### 1.2.5. Oportunitat 4: enfortiment de la cohesió de l'equip docent

L'equip docent d'EC és divers tant pel que fa a anys d'experiència docent com pels grups de recerca i les àrees d'interès. Actualment està format per 10 professors, 2 dels quals a temps parcial i 4 professors lectors, dos d'ells incorporats el curs 2025-26.

La diversitat en la trajectòria docent ofereix un espai de transferència de bones pràctiques i d'alineació pedagògica. Els professors novells poden adquirir estratègies i recursos dels docents sènior, mentre que aquests darrers tenen l'oportunitat d'aprendre a aprofitar noves eines (com les basades en IA) i mètodes pedagògics innovadors. La metodologia de treball en grup, que combina sessions de videotrucada puntuals i treball asíncron a través del repositori compartit, enforteix la cohesió de l'equip i potencia la cultura de col·laboració.

## 1.3. Motivació personal i justificació de la temàtica escollida

Des de la perspectiva del professor, la decisió de migrar a RISC-V es fonamenta en diversos arguments de pes.

El principal és la **rellevància industrial i la projecció de futur**. MIPS ha perdut pràcticament tota la seva quota de mercat i rellevància en la indústria. En canvi, RISC-V està experimentant una adopció massiva en una àmplia gamma de sectors, des de sistemes encastats i dispositius IoT fins a centres de dades i computació d'alt rendiment (HPC). Empreses capdavanteres com Google, Nvidia, Samsung i Intel estan invertint fortament en l'ecosistema RISC-V. Ensenyar MIPS avui dia és, en certa manera, ensenyar una tecnologia obsoleta, mentre que ensenyar RISC-V és invertir directament en l'ocupabilitat i la capacitat d'innovació dels futurs graduats.

Un altre motiu important és l'**abundància de recursos educatius moderns**. L'ecosistema RISC-V ha crescut exponencialment, amb simuladors avançats (com RARS), plaques de desenvolupament assequibles i llibres de text de referència —com les darreres edicions de *Computer Organization and Design* de Patterson i Hennessy— que ara utilitzen RISC-V com a arquitectura principal.

Finalment, adoptar RISC-V obre la porta a **projectes de recerca i innovació** molt més rellevants. La naturalesa oberta de l'arquitectura permet als estudiants i investigadors experimentar amb noves idees en disseny de processadors, seguretat, compiladors o sistemes operatius sense les restriccions d'un ISA propietari.

## 1.4. Relació amb la pràctica docent i el context institucional

La migració té implicacions directes tant en la praxi docent diària com en el posicionament estratègic de la institució. Des del punt de vista de la pràctica docent, s'abandonen eines de simulació com MARS o SPIM —estancades en el seu desenvolupament— per adoptar simuladors moderns com RARS, en desenvolupament actiu per part d'una comunitat global. Més enllà del programari, el canvi obre la porta a pràctiques de laboratori amb *hardware* real: l'ecosistema RISC-V ofereix plaques de baix cost (com la Raspberry Pi Pico 2 W, amb nucli RP2350 RISC-V) que permeten als estudiants compilar codi assemblador i executar-lo en un dispositiu físic.

En el pla institucional, adoptar RISC-V és una decisió estratègica que transcendeix una sola assignatura. Posiciona el programa acadèmic a l'avantguarda, alineant-lo amb les iniciatives de sobirania tecnològica promogudes per governs i consorcis internacionals (com l'*European Processor Initiative*). A més, l'adopció d'una plataforma oberta fomenta un ecosistema d'innovació dins de la mateixa universitat, facilitant projectes de final de grau, màsters i tesis doctorals sense les barreres de la propietat intel·lectual.

## 1.5. Marc teòric i conceptual: referències actuals i rellevants

<!-- TODO: Ampliar de 6 a ~25 referències. Migrar a APA 7a edició.
     Les referències actuals estan en format IEEE al Google Doc original. -->

El marc teòric principal per a la docència de RISC-V es troba en els llibres de text que han establert l'estàndard de facto en l'ensenyament de l'arquitectura de computadors durant dècades. Les edicions més recents d'aquestes obres han adoptat RISC-V com a eix central, la qual cosa representa l'aval acadèmic més significatiu per a la migració.

Patterson i Hennessy (2021) presenten en la segona edició de *Computer Organization and Design RISC-V Edition* l'obra de referència fonamental per a qualsevol curs introductori d'estructura o arquitectura de computadors. El fet que els seus autors, pioners de MIPS, hagin reescrit completament el llibre al voltant de RISC-V és la declaració més clara del canvi de paradigma. En la mateixa línia, Hennessy i Patterson (2022) consoliden en la sisena edició de *Computer Architecture: A Quantitative Approach* RISC-V com a arquitectura vàlida per a la computació d'altes prestacions.

A nivell d'especificació tècnica, Waterman, Asanović et al. (eds.) mantenen *The RISC-V Instruction Set Manual* com el document fundacional que defineix amb precisió l'ISA base i les extensions estàndard. RISC-V International publica a més un conjunt d'especificacions ratificades que cobreixen l'arquitectura privilegiada, la gestió d'interrupcions i la depuració, essencials per a projectes avançats.

A nivell pràctic, Patterson i Waterman (2017) ofereixen en *The RISC-V Reader* una guia concisa de 180 pàgines que sintetitza conceptes arquitectònics complexos en un manual directe, amb 75 «punts clau de disseny» que expliquen la lògica de RISC-V en contrast amb arquitectures anteriors. Winans (2022) completa el panorama amb *RISC-V assembly language programming*, una introducció de codi obert per a principiants allotjada a GitHub, que prioritza la configuració d'entorns reals i l'aplicació pràctica.

## 1.6. Revisió d'experiències o pràctiques similars

La transició de MIPS a RISC-V en l'àmbit acadèmic ha estat liderada per les mateixes institucions que van originar ambdues arquitectures. La Universitat de Califòrnia, Berkeley, bressol de RISC-V, ha estat la pionera: el seu curs CS 61C (*Great Ideas in Computer Architecture*) ha abandonat completament MIPS per adoptar RISC-V. El fet que Patterson i Hennessy hagin publicat les noves edicions del seu llibre canònic exclusivament amb RISC-V és el principal motor del canvi a escala global.

En l'escena internacional, la Universitat Cornell ha migrat la seva assignatura CS 3410 (*Computer System Organization and Programming*) a RISC-V de 64 bits, contribuint activament a l'ecosistema amb el seu propi intèrpret en línia i fent ús de simuladors visuals i interactius com Venus. A Europa, centres com l'ETH Zürich mostren un compromís profund amb RISC-V, especialment en recerca i cursos avançats on els estudiants aprenen a estendre l'ISA base amb instruccions personalitzades.

## 1.7. Connexió amb el context del sistema educatiu català

<!-- TODO: Completar la frase trencada. El text original deia "La [institució]..."
     Confirmar si es refereix a la FIB, la UPC o una altra institució. -->

A Catalunya, la transició està en marxa i és objecte de debat i planificació activa. La FIB-UPC, un referent en enginyeria informàtica, ha formalitzat propostes d'innovació docent per executar aquesta mateixa migració en assignatures com EC. Les propostes justifiquen el canvi per l'obsolescència industrial de MIPS i l'alineament estratègic amb RISC-V, considerant-lo clau per a la sobirania tecnològica i per dotar els estudiants de competències rellevants. L'experiència a la UPC se centra a substituir els simuladors clàssics de MIPS per eines modernes com RARS, que manté una interfície familiar però adaptada al nou ISA. Aquesta adopció progressiva, recolzada per la creació de la Xarxa-RISC-V a nivell de recerca dins de la mateixa universitat, assegura una transició coherent que permea des de la docència bàsica fins a la investigació de frontera.

## 1.8. Definició de l'objectiu general i dels objectius específics del treball

L'objectiu general d'aquest treball és l'actualització integral dels materials docents escrits de l'assignatura Estructura de Computadors (EC) del GEI a la FIB, substituint l'arquitectura MIPS per RISC-V com a nou referent d'aprenentatge.

Per assolir aquest objectiu general, es defineixen els objectius específics (OE) següents:

- **OE1. Transició de l'arquitectura de referència (ISA):** Migrar el corpus teòric i pràctic de l'assignatura (apunts, problemes i laboratoris) de l'arquitectura MIPS a RISC-V, assegurant la correcta aplicació de l'especificació de l'ISA i de l'ABI.
- **OE2. Transformació digital i optimització per a IA:** Implementar un canvi de paradigma en el format dels materials, passant de formats tancats (PDF) a formats oberts i lleugers que facilitin el control de versions i siguin «IA-friendly», permetent una millor interacció amb eines d'aprenentatge basades en LLM.
- **OE3. Harmonització, esmenes i control de qualitat:** Realitzar una revisió crítica de tots els continguts per unificar el lèxic tècnic, corregir inconsistències acumulades i alinear el discurs docent amb els estàndards actuals de la indústria i la recerca, tot aprofitant l'expertesa dels professors de l'assignatura vinculats al Barcelona Supercomputing Center (BSC).

---

# 2. Metodologia

## 2.1. Enfocament metodològic i estratègies utilitzades

L'execució del projecte s'ha basat en un enfocament de gestió àgil de projectes (*agile*), adaptant elements del marc Scrum (Schwaber & Sutherland, 2020) a la creació de continguts educatius. Aquesta tria respon a la necessitat de gestionar una migració complexa de materials llegats (*legacy*) en un entorn de col·laboració docent on el temps disponible és fragmentat i variable.

L'estratègia central ha estat la **migració iterativa i incremental**: en lloc d'abordar la totalitat del temari com un bloc monolític, s'ha treballat per unitats temàtiques funcionals, cadascuna seguint un cicle de producció que integra la Intel·ligència Artificial Generativa com a eina d'acceleració. El projecte ha passat per dues fases metodològiques diferenciades:

**Fase 1 — Exploració (NotebookLM):** En una primera fase, es va utilitzar NotebookLM com a eina d'extracció de continguts dels PDF originals i de primera traducció semàntica del codi assemblador de MIPS a RISC-V. Aquesta fase va permetre validar la viabilitat de l'enfocament assistit per IA i identificar les seves limitacions: la necessitat de múltiples *notebooks* temàtics per mantenir la coherència, i una velocitat de producció moderada que requeria una supervisió humana intensiva.

**Fase 2 — Acceleració (Claude):** El punt d'inflexió del projecte va arribar amb l'adopció de Claude com a eina principal de producció. El canvi va ser radical: la capacitat de mantenir el context complet del projecte (convencions d'estil, decisions prèvies, estructura del llibre) en una sola sessió de treball va eliminar la fragmentació de la fase anterior. La velocitat de producció va augmentar de manera espectacular, la qualitat dels materials va millorar i la cobertura va superar amb escreix les previsions inicials, assolint el 95% del material total quan el pla inicial preveia acabar la teoria al lliurament final.

El flux de treball de cada unitat temàtica ha estat: (1) extracció i primera conversió assistida per IA; (2) edició i enriquiment en format Quarto Markdown, aplicant les convencions d'estil documentades; (3) validació tècnica del codi assemblador amb el simulador RARS; i (4) consolidació al repositori GitHub.

## 2.2. Descripció de la innovació docent dissenyada

La innovació dissenyada es vertebra en quatre eixos fonamentals:

### 2.2.1. Innovació en el contingut (RISC-V)

L'adopció de RISC-V no és només un canvi d'arquitectura, sinó una aposta per un estàndard obert i modular. El nou programa se centra en la claredat pedagògica que ofereix aquesta ISA: elimina conceptes heretats de MIPS que generaven confusió (com els *branch delay slots* o els registres de multiplicació especials `HI`/`LO`) i introdueix la modularitat com a principi estructurador del curs, presentant primer la base RV32I i afegint progressivament les extensions M (multiplicació/divisió) i F (coma flotant).

### 2.2.2. Innovació en el format (Quarto Markdown i GitHub)

La transició a Quarto Markdown permet que els materials siguin llegibles tant per humans com per màquines, seguint el paradigma *Docs-as-Code*. L'ús de GitHub com a repositori centralitzat facilita el control de versions i la sincronització entre el professorat. El resultat és un **punt d'entrada únic**: una URL que dona accés a tot el material en HTML (navegable, amb mode fosc/clar, *responsive* i accessible WCAG 2.1) i un únic fitxer PDF descarregable.

### 2.2.3. Reestructuració pedagògica del temari

La migració ha estat l'ocasió per revisar críticament l'estructura temàtica de l'assignatura. La nova organització no és un mapatge 1:1 dels materials originals: s'han pres decisions pedagògiques explícites per millorar la progressió didàctica i la coherència interna.

Els canvis estructurals més rellevants són dos. En primer lloc, el Tema 1 original (Introducció) s'ha dividit en dos: el nou T1 manté la introducció conceptual a l'arquitectura de computadors i la codificació de dades, mentre que el nou T6 agrupa els continguts de rendiment i potència. Aquesta separació permet tractar el rendiment com un tema autònom, amb el context que l'estudiant ja ha adquirit en els temes anteriors sobre ISA i programació. En segon lloc, l'aritmètica entera —que en l'estructura original formava part del Tema 5 (Aritmètica d'enters i coma flotant)— s'ha reallotjat en el nou T4 (Aritmètica entera i matrius), mentre que el nou T5 queda dedicat exclusivament a la coma flotant. Aquesta reorganització clarifica la frontera entre aritmètica entera i en coma flotant, i redueix la càrrega cognitiva de cadascun dels temes.

La Taula 1 mostra la correspondència completa entre els materials originals (MIPS) i els nous (RISC-V).

**Taula 1.** Correspondència entre els materials RISC-V (nous) i MIPS (originals).

| Material RISC-V (nou) | Equivalent MIPS (original) | Observacions |
| :--- | :--- | :--- |
| **TEORIA** | | |
| **T1. Introducció** | | |
| T1.1. La gestió de la complexitat: Capes i interfícies | T1 §1. Descripció jeràrquica | Reorganitzat i ampliat |
| T1.2. El cicle de vida del programa | T1 §1. Descripció jeràrquica | Segregat com a secció independent |
| T1.3. El model de Von Neumann | T1 §1. Descripció jeràrquica | Segregat com a secció independent |
| T1.4. Codificació de naturals en base 2 | T2 §5. Repàs de naturals | Avançat a T1; integrat al flux conceptual |
| T1.5. Codificació d'enters en base 2 | T2 §6. Repàs d'enters | Avançat a T1; integrat al flux conceptual |
| **T2. Instruccions i tipus de dades bàsics** | | |
| T2.1. Introducció a l'ISA de RISC-V | T2 §1. Introducció a la MIPS ISA | Reescrit íntegrament per a RISC-V |
| T2.2. Format de les instruccions RV32I | T2 §8. Format de les instruccions MIPS | Reescrit íntegrament per a RISC-V |
| T2.3. Estructura d'un programa en assemblador | T2 §3. (implícit) | Formalitzat com a secció independent |
| T2.4. Variables escalars | T2 §3. Variables | Reorganitzat |
| T2.5. La memòria | T2 §2. La memòria | — |
| T2.6. Operands i modes d'adreçament | T2 §4. Operands | Ampliat amb modes d'adreçament |
| T2.7. Punters | T2 §11. Punters | — |
| T2.8. Vectors | T2 §9. Vectors | — |
| T2.9. Caràcters i cadenes de caràcters | T2 §10. Cadenes de caràcters | Ampliat amb caràcters |
| **T3. Traducció de programes** | | |
| T3.1. Desplaçaments de bits | T3 §1. Desplaçaments de bits | — |
| T3.2. Operacions lògiques bit a bit | T3 §2. Operacions lògiques bit a bit | — |
| T3.3. Comparacions i operacions booleanes | T3 §3. Comparacions i operacions booleanes | — |
| T3.4. Salts | T3 §4. Salts | Reescrit per a RISC-V (eliminat *branch delay slot*) |
| T3.5. Revisió dels modes d'adreçament | — | Nou: consolidació didàctica sense equivalent MIPS |
| T3.6. Sentències alternatives: if-then-else i switch | T3 §5. Sentències alternatives | — |
| T3.7. Sentències iteratives: while, for i do-while | T3 §6. Sentències iteratives | — |
| T3.8. Estructura de la memòria | T3 §8. Estructura de la memòria | — |
| T3.9. Subrutines | T3 §7. Subrutines | Reescrit per a ABI RISC-V |
| T3.10. Compilació, assemblatge, enllaçat i càrrega | T3 §9. Compilació, muntatge i càrrega | Ampliat amb GCC/Clang toolchain |
| **T4. Aritmètica entera i matrius** | | |
| T4.1. Suma, resta i canvi de signe | T5 §1. Overflow de suma i resta | Avançat de T5 a T4 |
| T4.2. Sobreeiximent en suma i resta d'enters | T5 §1. Overflow de suma i resta | Avançat de T5 a T4 |
| T4.3. Multiplicació entera | T5 §2. Multiplicació entera; T4 §1. mult/mflo/mfhi | Fusionat i reescrit per a RV32IM |
| T4.4. Matrius | T4 §2. Matrius | — |
| T4.5. Optimitzacions de bucle | T4 §3–4. Accés seqüencial i recorreguts | Ampliat i formalitzat |
| T4.6. Divisió entera | T5 §3. Divisió entera | Avançat de T5 a T4 |
| **T5. Coma flotant** | | |
| T5.1. Representació en coma flotant | T5 §4. Representació CF | — |
| T5.2. Operacions en coma flotant | T5 §5–6. Suma i multiplicació CF | — |
| T5.3. Coma flotant a RISC-V (RV32F) | T5 §7. La coma flotant en MIPS | Reescrit íntegrament per a RV32F |
| **T6. Rendiment i potència** | | |
| T6.1. Rendiment | T1 §2. Rendiment i potència | Segregat de T1 com a tema independent |
| T6.2. Llei d'Amdahl | T1 §3. Llei d'Amdahl | Segregat de T1 |
| T6.3. Potència | T1 §4. Mesures de dissipació | Segregat de T1; ampliat amb escalat de Dennard |
| **T7. Memòria cau** | | |
| T7.1. La jerarquia de memòria | T6 §1. Introducció | Ampliat amb context GPU i IA |
| T7.2. La memòria cau | T6 §2. Disseny bàsic | — |
| T7.3. Política d'emplaçament | T6 §3. Correspondència directa | Ampliat amb associativitat |
| T7.4. Política de reemplaçament | T6 §6. Associativitat | Reorganitzat |
| T7.5. Política d'escriptura | T6 §4. Polítiques d'escriptura | — |
| T7.6. Rendiment | T6 §5. Mesures de rendiment | — |
| T7.7. Tipologia de les fallades | T6 §8. Tipologia de les fallades | — |
| T7.8. Memòries cau multinivell | T6 §7. Caches multinivell | — |
| **T8. Memòria virtual** | | |
| T8.1. Introducció | T7 §1. Introducció | — |
| T8.2. Paginació | T7 §2. Funcionament de la MV | Reorganitzat i ampliat |
| T8.3. La taula de pàgines | T7 §2. Funcionament de la MV | Segregat; ampliat amb taules multinivell |
| T8.4. Fallada de pàgina | T7 §3. Fallada de pàgina | — |
| T8.5. Traducció ràpida: el TLB | T7 §4. Traducció ràpida amb TLB | Ampliat amb *TLB shootdown* multicore |
| **T9. Excepcions i interrupcions** | | |
| T9.1. Excepcions i interrupcions | T8 §1–4. Introducció, CP0, accions HW/SW | Reescrit íntegrament per a CSR RISC-V |
| T9.2. Crides al sistema | T8 §6. Crides al sistema | Reescrit per a `ecall` RISC-V |
| T9.3. Entrada/Sortida | T8 §7. Interrupcions | Ampliat |
| **CONTINGUT NOU SENSE EQUIVALENT MIPS** | | |
| T2: RISC-V GNU Compiler Toolchain | — | Nou: eina estàndard de l'ecosistema RISC-V |
| T2: Extensions M i F (modularitat) | — | Nou: modularitat de RISC-V vs. integració de MIPS |
| T7: GPUs i memòria en l'era de la IA | — | Nou: context tecnològic actual |
| T8: Taules de pàgines multinivell | — | Nou: sistemes moderns |
| T9: Modes de privilegi (M/S/U) | — | Nou: arquitectura de privilegis RISC-V |
| **LABORATORI** | | |
| S1. Introducció al simulador RARS | S0. Introducció (MARS) | Eina substituïda: MARS → RARS |
| S2. Assemblador RISC-V i tipus bàsics | S1. Assemblador MIPS i tipus bàsics | Reescrit íntegrament per a RISC-V |
| S3. Traducció de programes | S2. Traducció de programes | Reescrit íntegrament per a RISC-V |
| S4. Matrius i subrutines | S3. Tipus de dades estructurats | Ampliat amb subrutines |
| S5. Coma flotant i compilació separada | S4. Codificació en coma flotant | Ampliat amb compilació separada |
| S6. Memòria cau | S5. Memòria cau | Reescrit; ampliat amb *loop tiling* |
| **PROBLEMES I SOLUCIONARIS** | | |
| PE.qmd — Enunciats (T1–T9) | PDF problemes MIPS | Reescrit íntegrament; 23 exercicis nous (vegeu Annex I) |
| PS_T2.qmd — Solucionari T2 | PDF solucionari MIPS | Reescrit per a RISC-V |
| PS_T3.qmd — Solucionari T3 | PDF solucionari MIPS | Reescrit per a RISC-V |
| PS_T4.qmd — Solucionari T4 | PDF solucionari MIPS | Reescrit per a RISC-V |
| PS_T5.qmd — Solucionari T5 | PDF solucionari MIPS | Reescrit per a RISC-V |
| **MATERIALS TRANSVERSALS** | | |
| riscv.qmd — Compendi de referència RISC-V | — | Nou: no existia equivalent MIPS |
| sigles.qmd — Glossari de sigles | — | Nou: formalitzat durant la migració |
| contrib.qmd — Convencions i normes d'estil | — | Nou: sistema de qualitat del projecte |

### 2.2.4. Recursos d'aprenentatge actiu

- **Simulació avançada (RARS):** Substitueix MARS com a entorn de referència, mantenint una interfície familiar però adaptada al nou ISA.
- ***Hardware* real (Raspberry Pi Pico 2 W):** Proposta de pràctica voluntària amb plaques RP2350 (nucli RISC-V) i *Debug Probes*. Permet als estudiants compilar codi assemblador i executar-lo en un dispositiu físic d'última generació.
- **Entorn de desenvolupament professional (Docker):** Contenidor Docker amb la RISC-V GNU Compiler Toolchain oficial, que garanteix la reproductibilitat dels experiments i familiaritza l'estudiantat amb les tecnologies estàndard de la indústria.

## 2.3. Recollida de dades: instruments i població d'estudi

Atès que el projecte es troba en fase d'implementació de materials, la recollida de dades s'ha centrat en la validació experta i el control de qualitat del procés, més que en l'avaluació directa de l'estudiantat en aquesta etapa inicial.

**Població d'estudi:** El grup de treball està format pel professorat de l'assignatura d'EC i membres de l'eix d'arquitectura del Departament d'Arquitectura de Computadors (DAC), incloent-hi investigadors vinculats al Barcelona Supercomputing Center (BSC).

**Instruments de recollida:**

- ***Definition of Done* (DoD):** Llista de verificació per assegurar que cada tema compleix els estàndards de qualitat: format Quarto Markdown consistent, codi validat en RARS i lèxic unificat (vegeu Annex I).
- **Sessions de coordinació:** Videotrucades puntuals i treball asíncron a través del repositori GitHub, on les *pull requests* i els *commits* documenten les decisions de contingut.
- **Registres de traçabilitat (logs de IA):** Documentació del procés de conversió assistida per IA per avaluar l'eficiència de l'eina i la necessitat de supervisió humana.

## 2.4. Consideracions ètiques

Tot i que en aquesta fase el treball no inclou experimentació directa amb dades personals dels estudiants, s'han tingut en compte les dimensions ètiques següents:

1. **Ús responsable de la IA:** La utilització de la IA en l'elaboració dels materials s'ha regit pel principi de la supervisió humana crítica. S'ha vetllat per evitar l'acceptació d'«al·lucinacions» tècniques que poguessin perjudicar la qualitat de l'aprenentatge.
2. **Accessibilitat i sostenibilitat:** L'elecció del format Markdown respon a un compromís ètic amb l'accessibilitat digital i el manteniment futur per part de la comunitat docent.
3. **Transparència:** Els estudiants seran informats de l'ús d'eines d'IA en la creació del material i rebran pautes per a un ús ètic i pedagògic d'aquestes eines en el seu procés d'estudi.

---

# 3. Resultats

## 3.1. Volum i abast dels materials produïts

<!-- TODO: Completar amb dades quantitatives finals quan la validació RARS estigui completa. -->

La migració ha assolit el **95% del material total** de l'assignatura. La Taula 2 en detalla el volum per categoria.

**Taula 2.** Volum de materials produïts.

| Categoria | Fitxers .qmd | Estat |
| :--- | :---: | :--- |
| Teoria (T1–T9) | 9 | Preparat per a revisió externa |
| Laboratori (L1–L6) | 6 | Preparat per a revisió externa (L1 pendent §Pseudoinstruccions) |
| Enunciats de problemes (PE) | 1 | Preparat per a revisió externa |
| Solucionaris (PS_T2–T5) | 4 | En procés |
| Materials transversals (riscv, sigles, contrib) | 3 | Actius |
| **Total** | **23** | |

A aquests fitxers s'afegeixen aproximadament **50-60 figures SVG** (cadascuna en versió *light* i *dark*, ~100-120 fitxers en total), amb una previsió de superar les 100 figures úniques al tancament del projecte. Les figures han estat generades íntegrament en SVG (abandonant Mermaid per limitacions de qualitat), seguint una paleta de colors i convencions documentades a `contrib.qmd`.

Pel que fa als problemes, a més de la migració i revisió dels exercicis existents, s'han afegit 23 exercicis nous que cobreixen continguts sense equivalent en el material MIPS original (vegeu Annex I per al llistat complet).

## 3.2. Qualitat i harmonització

Un dels resultats més significatius del projecte, i que supera l'abast estrictament tècnic de la migració, és l'establiment d'un **sistema de qualitat documentat** per als materials de l'assignatura. Aquest sistema es concreta en tres artefactes:

- **`contrib.qmd`:** Document de convencions i normes d'estil que recull el sistema de *callouts* i prefixos d'etiquetes, les normes d'estil (veu, puntuació, negretes, anglicismes, sigles), els criteris de format (taules, figures SVG, blocs de codi), les substitucions terminològiques obligatòries, la paleta de colors SVG i les decisions específiques per tema.
- **`sigles.qmd`:** Glossari de sigles de l'assignatura, actualitzat incrementalment durant la migració de cada tema.
- ***Definition of Done* (DoD):** Un tema es considera «acabat» quan: (1) el contingut textual és complet i correctament formatat en Quarto Markdown; (2) tots els exemples de codi s'executen sense errors a RARS; (3) s'han eliminat totes les referències a l'arquitectura MIPS i el lèxic està harmonitzat; i (4) el document és funcional dins de l'estructura del repositori GitHub.

## 3.3. Integració i accessibilitat

El resultat final del projecte no és un conjunt de fitxers dispersos, sinó un **ecosistema de materials cohesionat** amb les característiques següents:

- **Punt d'entrada únic:** Una URL dona accés a tots els materials en HTML, i un botó permet descarregar el PDF complet de tot el llibre.
- **Accessibilitat WCAG 2.1:** Marcatge HTML5 semàntic, mode fosc/clar respectant la configuració del sistema de l'usuari, disseny *responsive* i codi amb ressaltat accessible (*a11y*).
- **Repositori públic:** Tot el material font és accessible i reutilitzable per la comunitat docent.
- **Reproductibilitat:** Un contenidor Docker permet renderitzar el llibre complet en qualsevol sistema operatiu.

## 3.4. Comparativa pla→realitat

La Taula 3 contrasta la planificació prevista al lliurament intermedi (març 2026) amb el que s'ha assolit efectivament.

**Taula 3.** Comparativa entre la planificació inicial i els resultats assolits.

| Fita | Previst (lliurament intermedi) | Assolit (lliurament final) |
| :--- | :--- | :--- |
| M1 (Març) | T1, T2; setup del repositori | T1, T2 + estructura completa del projecte i sistema de convencions |
| M2 (Abril) | T3, T4, T5 | T3, T4, T5 + solucionaris PS_T2–T5 |
| M3 (Maig) | T8 (Excepcions) + laboratoris (RARS) | T6, T7, T8, T9 + L1–L6 complets |
| M4 (Juny) | Tancament i memòria | PE complet + 23 exercicis nous + materials transversals + memòria |

La diferència entre el previst i l'assolit és directament atribuïble al **pivot metodològic de la Fase 1 a la Fase 2** descrit a §2.1: l'adopció de Claude com a eina principal va multiplicar la capacitat de producció i va permetre cobrir en els terminis previstos un volum de material molt superior al planificat.

---

# 4. Discussió, conclusions i altres propostes

## 4.1. Contrast dels resultats amb el marc teòric i estudis previs

<!-- TODO: Desenvolupar. Connectar els resultats amb les referències clau,
     especialment la decisió de Patterson i Hennessy d'adoptar RISC-V. -->

## 4.2. Valoració crítica del procés, obstacles i aprenentatges

<!-- TODO: Desenvolupar. Incloure:
     - Obstacles reals: PDF sense fonts, validació tècnica del codi,
       gestió de la coherència entre temes.
     - Narrativa completa del pivot NotebookLM → Claude.
     - Aprenentatges sobre supervisió humana i rol del professor com a validador tècnic.
     - Reflexió sobre l'ús de la IA en la producció de materials docents. -->

## 4.3. Propostes de millora o línies de continuïtat del projecte

<!-- TODO: Desenvolupar. Incloure:
     - Implantació Q1 2025-26 (setembre): 2 grups teoria + 3-4 pràctiques.
     - Recollida de feedback dels estudiants durant el primer quadrimestre.
     - Extensió a IC i AC (coherència de l'eix d'arquitectura).
     - Contribució oberta al repositori per part de la comunitat docent. -->

## 4.4. Possibles connexions amb altres àmbits o temàtiques educatives

<!-- TODO: Desenvolupar. Incloure:
     - El model (àgil + IA + Markdown + GitHub) com a pràctica exportable
       a altres assignatures STEM.
     - Connexió amb el paradigma Docs-as-Code en l'àmbit educatiu.
     - Implicacions per a la formació del professorat en IA. -->

---

# 5. Bibliografia

<!-- TODO: Migrar a APA 7a edició (ordre alfabètic). Ampliar a ~25 referències.
     Les referències actuals estan en format IEEE. -->

Hennessy, J. L., & Patterson, D. A. (2022). *Computer architecture: A quantitative approach* (6th ed.). Morgan Kaufmann.

Patterson, D. A., & Hennessy, J. L. (2021). *Computer organization and design RISC-V edition: The hardware software interface* (2nd ed.). Morgan Kaufmann.

Patterson, D., & Waterman, A. (2017). *The RISC-V reader: An open architecture atlas*. Strawberry Canyon LLC. <http://riscvbook.com/>

RISC-V International. (2020–present). *Official RISC-V specifications*. <https://riscv.org/specifications/ratified/>

Schwaber, K., & Sutherland, J. (2020). *The Scrum guide: The definitive guide to Scrum: The rules of the game*. Scrum.org. <https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-US.pdf>

Waterman, A., Asanović, K., et al. (Eds.). (2019–present). *The RISC-V instruction set manual, volume I: Unprivileged ISA*. RISC-V International. <https://docs.riscv.org/reference/isa/unpriv/unpriv-index.html>

Winans, J. (2022). *RISC-V assembly language programming*. Northern Illinois University. <https://github.com/Hsins/rvalp>

---

# Annex I: Productes del projecte

## A1.1. Llistat de fitxers produïts i estat de revisió

| Fitxer | Descripció | Estat |
| :--- | :--- | :--- |
| `T1.qmd` | Tema 1: Introducció | Preparat per a revisió externa |
| `T2.qmd` | Tema 2: Instruccions i tipus de dades bàsics | Preparat per a revisió externa |
| `T3.qmd` | Tema 3: Traducció de programes | Preparat per a revisió externa |
| `T4.qmd` | Tema 4: Aritmètica entera i matrius | Preparat per a revisió externa |
| `T5.qmd` | Tema 5: Coma flotant | Preparat per a revisió externa |
| `T6.qmd` | Tema 6: Rendiment i potència | Preparat per a revisió externa |
| `T7.qmd` | Tema 7: Memòria cau | Preparat per a revisió externa |
| `T8.qmd` | Tema 8: Memòria virtual | Preparat per a revisió externa |
| `T9.qmd` | Tema 9: Excepcions i interrupcions | Preparat per a revisió externa |
| `L1.qmd` | S1: Introducció al simulador RARS | Preparat (pendent §Pseudoinstruccions) |
| `L2.qmd` | S2: Assemblador RISC-V i tipus bàsics | Preparat per a revisió externa |
| `L3.qmd` | S3: Traducció de programes | Preparat per a revisió externa |
| `L4.qmd` | S4: Matrius i subrutines | Preparat per a revisió externa |
| `L5.qmd` | S5: Coma flotant i compilació separada | Preparat per a revisió externa |
| `L6.qmd` | S6: Memòria cau | Preparat per a revisió externa |
| `PE.qmd` | Enunciats de problemes (T1–T9) | Preparat per a revisió externa |
| `PS_T2.qmd` | Solucionari T2 | En procés |
| `PS_T3.qmd` | Solucionari T3 | En procés |
| `PS_T4.qmd` | Solucionari T4 | En procés |
| `PS_T5.qmd` | Solucionari T5 | En procés |
| `riscv.qmd` | Compendi de referència RISC-V | Actiu |
| `sigles.qmd` | Glossari de sigles | Actiu |
| `contrib.qmd` | Convencions i normes d'estil | Actiu |

## A1.2. *Definition of Done* (DoD)

Un tema o sessió de laboratori es considera «acabat» quan compleix tots els criteris següents:

1. El contingut textual és complet i correctament formatat en Quarto Markdown.
2. Tots els exemples de codi i exercicis s'executen sense errors al simulador RARS.
3. S'han eliminat totes les referències a l'arquitectura MIPS i el lèxic està harmonitzat segons les convencions de `contrib.qmd`.
4. El document és accessible i funcional dins de l'estructura del repositori GitHub (renderitza correctament en HTML i PDF).
5. Les figures SVG estan generades en versió *light* i *dark* i integrades correctament al `.qmd`.
6. El glossari de sigles (`sigles.qmd`) ha estat actualitzat amb les sigles noves del tema.

## A1.3. Exercicis nous sense equivalent en el material MIPS original

**Taula A1.** Exercicis afegits durant la migració.

| Tema | Cobertura |
| :--- | :--- |
| T2 | *Little-endian*, ordre de bytes |
| T2 | Bucles sobre vectors (init, suma, còpia inversa) |
| T2 | Cerca en vector, retorn −1 |
| T2 | Aritmètica de punters sobre `short` |
| T2 | Funció `longitud` amb `'\0'` |
| T2 | Còpia de string |
| T3 | `switch` amb salts encadenats i *jump table* |
| T3 | Compilació separada, símbols externs, `auipc` |
| T4 | Optimització #2: condició al final |
| T4 | Optimització #3: eliminació variable d'inducció |
| T5 | `flw`/`fsw`, `flt.s` |
| T5 | `fcvt.w.s`, `fcvt.s.w`, truncament vs. arrodoniment |
| T6 | Amdahl bàsic, límit teòric |
| T6 | Amdahl amb tres components simultanis |
| T6 | Amdahl invers: quin % de CF cal per a speedup 10× |
| T7 | *Cold-start*, conflicte, capacitat amb seqüències concretes |
| T7 | Conflictes entre dos vectors, efecte de l'adreça base |
| T8 | Taula de pàgines de dos nivells, mida, avantatge |
| T8 | Bit de protecció W, excepcions de protecció |
| T8 | Integració TLB+cau, VIPT, condició antialiàsing |
| T9 | `mepc`, `mtvec` direct/vectored, ajust +4 per `ecall` |
| T9 | Fallada de TLB com a excepció, gestió RSE |
| T9 | Interrupcions E/S, `MIE`/`MEIE`, RSE de teclat |

