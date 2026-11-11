# Reel animato · «Dove sentiamo le emozioni» (Volynets et al., 2020)

**File video:** `weself-mappe-emozioni-reel.mp4` (1080×1920, 30 fps, 148 secondi, senza audio). Le scritte sullo schermo coincidono con la voce e fanno da sottotitoli; restano nella zona sicura (220–1480 pixel dall'alto).

**Grafica:** sagome stilizzate (non persone reali) che si colorano come le mappe dello studio: dal rosso al giallo dove una sensazione si accende, dal blu all'azzurro dove si spegne. Sotto ogni scena c'è la fonte; in alto, una barra sottile mostra l'avanzamento.

**Come è fatto:** il testo della voce è in `build_reel.py` (copione approvato nell'editor), la grafica in `reel_template.html`. `python3 video/mappe-emozioni/build_reel.py` crea `reel.html`; poi `node tools/render-video.cjs video/mappe-emozioni/reel.html video/mappe-emozioni/weself-mappe-emozioni-reel.mp4 148.1 30`.

**Nota sulle mappe:** i colori delle sagome riproducono a grandi linee la Figura 1 dell'articolo (zone e direzione delle sensazioni), non i valori esatti pixel per pixel.

## 1. Il copione per la voce (circa 148 secondi)

Leggi con calma, circa 2,5 parole al secondo. Metti ogni frase all'inizio della sua scena.

| Secondi | Scena | Voce |
|---|---|---|
| 0–4 | Una sagoma: il petto batte, si accende la pancia, le gambe diventano blu | «Dove sentiamo le emozioni?» |
| 4–19 | Puntini (101 paesi), pillole «quasi 4.000 persone», «101 paesi»; due sagome si colorano: «si attiva» e «si spegne» | «Un gruppo di ricercatori finlandesi ha chiesto a quasi 4.000 persone, in 101 paesi, di colorare su una sagoma dove sentono un'emozione: in rosso dove qualcosa si attiva, in blu dove si spegne.» |
| 19–29 | Sei piccole sagome, ognuna con la sua mappa | «Il risultato: ogni emozione è stata percepita nel corpo in modo diverso, e queste mappe si sono somigliate in tutto il mondo.» |
| 29–48 | Una grande sagoma cambia mappa con il nome dell'emozione (rabbia, paura, disgusto, tristezza, amore, felicità) | «La rabbia si è accesa in testa, nel petto e nelle mani. La paura nel petto. Il disgusto in gola e nello stomaco. La tristezza ha svuotato braccia e gambe. L'amore e la felicità, invece, hanno acceso tutto il corpo ma con intensità diverse.» |
| 48–59 | Amore e felicità affiancate | «Perfino emozioni vicine, come l'amore e la felicità, hanno avuto mappe distinte: per esempio, cambiano le zone più accese e la loro intensità.» |
| 59–77 | Sagome di paesi diversi si sovrappongono in una sola; pillola grande «l'emozione», pillole piccole cultura, sesso, titolo di studio, dove si vive, altezza e peso | «E queste mappe si sono somigliate moltissimo da un paese all'altro. A fare la differenza è stata l'emozione, molto più della cultura, del sesso o del titolo di studio. E non contava dove si vive, né quanto si è alti o pesanti.» |
| 77–92 | Due sagome quasi uguali, una con pancia e gola più accese | «Qualche piccola differenza c'è stata: nei paesi occidentali le sensazioni sono state segnate un po' più forti; le donne hanno sentito di più la pancia e la gola, per esempio nell'ansia e nella vergogna.» |
| 92–100 | Tre sagome sempre più tenui, freccia «con gli anni» | «L'unica differenza importante è stata l'età: con gli anni, le sensazioni sono diventate più tenui.» |
| 100–113 | Un volto che cambia espressione accanto a un cuore che batte | «Perché? Secondo gli autori, un'espressione del volto si può imparare guardando gli altri, il battito del cuore no. Per questo ciò che sentiamo nel corpo sarebbe meno legato alla cultura.» |
| 113–121 | Mito o realtà? Timbro MITO | «Le emozioni stanno solo nella testa? Secondo la ricerca, no: vengono percepite anche nel corpo.» |
| 121–139 | **Il mio punto di vista** (sfondo lilla, «Il fondatore di WeSelf · Un'opinione personale, non un risultato dello studio») | «Sembra banale: chi di noi non ha percepito sul proprio corpo un'emozione… ma avere maggiore consapevolezza su cosa percepiamo fisiologicamente potrebbe aiutarci anche a migliorare le nostre decisioni senza saltare a conclusioni affrettate. Magari non è fame quella che stai provando...» |
| 139–148 | Finale WeSelf (sfondo pervinca, «Scopri WeSelf · link in bio») | «La prossima volta che provi un'emozione, chiediti dove la senti. È un modo per ascoltarti. Il link è in bio.» |

## 2. Registrazione e montaggio

Come per gli altri Reel: una frase alla volta, telefono a 15–20 cm, stanza piccola. In CapCut metti ogni frase all'inizio della sua scena (0; 4; 19; 29; 48; 59; 77; 92; 100; 113; 121; 139 secondi), riduzione del rumore attiva, esporta in 1080p a 30 fps. Se una frase risulta più lunga della sua scena, dimmi i secondi e rigenero il video con i tempi giusti.

**Durata:** 2 minuti e mezzo vanno bene su Instagram (i Reel arrivano a 3 minuti) e su TikTok. Se vuoi accorciarlo, le prime candidate sono le scene «Piccole differenze» (77–92) e «Vicine ma diverse» (48–59): i limiti restano comunque in didascalia.

## 3. Pubblicazione

**Copertina del Reel:** `weself-mappe-emozioni-copertina.png` (1080×1920, titolo «Ogni emozione ha la sua mappa nel corpo»; il testo resta nella zona visibile anche nella griglia del profilo). In Instagram: Modifica copertina → Aggiungi dal rullino.

**Didascalia (Instagram e Facebook):**

```
Ogni emozione ha la sua mappa nel corpo. E si somiglia in tutto il mondo.

Un gruppo di ricercatori finlandesi ha chiesto a quasi 4.000 persone, in 101 paesi, di colorare su una sagoma dove sentono 13 emozioni: dove qualcosa si attiva e dove si spegne.

Ogni emozione ha avuto la sua mappa: la rabbia in testa, nel petto e nelle mani; il disgusto in gola e nello stomaco; la tristezza ha svuotato braccia e gambe. E le mappe si sono somigliate moltissimo da un paese all'altro: contava l'emozione, molto più della cultura, del sesso o del titolo di studio. L'unica differenza importante è stata l'età: con gli anni, le sensazioni sono diventate più tenui.

I limiti: le persone hanno descritto da sole quello che sentivano, con un questionario online in inglese; hanno partecipato soprattutto donne e persone con un alto titolo di studio. Lo studio mostra come le emozioni vengono percepite, non che cosa succede davvero negli organi.

Il punto di vista nel video è un'opinione personale del fondatore di WeSelf, non un risultato dello studio.

Un'onestà necessaria: la ricerca riguarda le emozioni e il corpo, non WeSelf. Con WeSelf costruisci piccole abitudini, già in agenda, e trovi una comunità dove ci si sostiene.

La prossima volta che provi un'emozione, chiediti dove la senti.

#emozioni #corpo #consapevolezza #psicologia #benessere #WeSelf
```

**Didascalia breve (TikTok):**

```
Dove sentiamo le emozioni? Quasi 4.000 persone in 101 paesi le hanno colorate su una sagoma: ogni emozione ha la sua mappa, e si somiglia in tutto il mondo. Fonte: Volynets et al., 2020, Emotion. #emozioni #psicologia #WeSelf
```

**Primo commento:** `📚 Fonte: Volynets S., Glerean E., Hietanen J.K., Hari R., Nummenmaa L. (2020). Bodily maps of emotions are culturally universal. Emotion, 20(7), 1127–1136. https://doi.org/10.1037/emo0000624 — 3.954 partecipanti da 101 paesi, tra i 18 e i 90 anni, hanno colorato su una sagoma le sensazioni di 13 emozioni (più uno stato neutro). Le mappe si sono somigliate molto tra paesi; a pesare di più è stata l'emozione, molto meno cultura e sesso; non c'è stato legame con il paese di residenza, l'altezza, il peso o l'indice di massa corporea. Con l'età le sensazioni sono risultate più deboli. Nel video non ci sono numeri da convertire: i colori delle sagome riproducono a grandi linee la Figura 1 dell'articolo.`

**Testo alternativo:** «Animazione con sagome stilizzate che si colorano come mappe di calore: in rosso e giallo dove un'emozione si accende, in blu dove si spegne. Quasi 4.000 persone in 101 paesi hanno colorato dove sentono le emozioni: la rabbia in testa, nel petto e nelle mani; la paura nel petto; il disgusto in gola e nello stomaco; la tristezza svuota braccia e gambe; amore e felicità accendono tutto il corpo. Le mappe si somigliano in tutto il mondo; con l'età le sensazioni diventano più tenui. Segue un'opinione personale del fondatore di WeSelf e l'invito a chiedersi dove si sente un'emozione.»

## 4. Note di affidabilità

- Tutto quello che dice la voce è stato controllato sull'articolo completo (versione accettata del 2019, pubblicata su Emotion nel 2020).
- «Quasi 4.000» = 3.954 persone; «101 paesi» come nell'articolo.
- «In tutto il mondo»: le mappe dei diversi paesi e gruppi culturali si sono somigliate molto; gli autori parlano di mappe «culturalmente universali». Restano piccole differenze (paesi occidentali più intensi; donne più pancia e gola), dette nel video.
- «Perché?»: è la spiegazione proposta dagli autori, detta al condizionale («sarebbe»).
- Il punto di vista è dichiarato come opinione personale sia sullo schermo sia in didascalia.
- Tema non clinico: nessun rimando di supporto obbligatorio. Il video nomina ansia e vergogna solo come esempi dello studio.
- Nessuna persona reale nelle immagini: solo sagome stilizzate, come concordato per questo Reel.
