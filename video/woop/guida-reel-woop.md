# Reel animato · «Dal volere al fare, in quattro passi» (Wang, Wang & Gai, 2021)

**File video:** `weself-woop-reel.mp4` (1080×1920, 30 fps, 99 secondi, senza audio). Le scritte sullo schermo coincidono con la voce e fanno da sottotitoli (zona sicura 220–1480 px); nel punto di vista e nel finale non ci sono sottotitoli.

**Grafica:** quattro tessere colorate (Desiderio, Risultato, Ostacolo, Piano), una strada con un sasso, un sole, una nuvoletta, 24 puntini per gli studi, due segnalini verso la bandierina. Nessuna persona. Nessuna parola inglese nel video.

**Come è fatto:** testi in `build_reel.py` (copione approvato nell'editor), grafica in `reel_template.html`. `python3 video/woop/build_reel.py` crea `reel.html`; poi `node tools/render-video.cjs video/woop/reel.html video/woop/weself-woop-reel.mp4 98.6 30`.

## 1. Il copione per la voce (circa 99 secondi)

Leggi con calma, circa 2,5 parole al secondo. Metti ogni frase all'inizio della sua scena.

| Secondi | Scena | Voce |
|---|---|---|
| 0–10 | Quattro tessere che si girano | «Volere non basta. C'è un metodo in quattro passi che aiuta a passare dal volere al fare: desiderio, risultato, ostacolo, piano.» |
| 10–19 | Una linea sale verso una bandierina e si ferma contro un muretto | «Molte persone partono con un buon proposito, immaginano già il traguardo… e poi si fermano al primo ostacolo.» |
| 19–28 | Tessera «Desiderio»; nuvoletta «Camminare 3 volte questa settimana» | «Primo, il desiderio: scegli una cosa che desideri e che puoi davvero ottenere, per esempio camminare tre volte questa settimana.» |
| 28–35 | Tessera «Risultato»; sorge il sole | «Secondo, il risultato: immagina il momento più bello in cui ci sei riuscito.» |
| 35–43 | Tessera «Ostacolo»; cade un sasso sulla strada | «Terzo, l'ostacolo: chiediti che cosa, dentro di te, potrebbe fermarti. La stanchezza, la pigrizia, il telefono.» |
| 43–52 | Tessera «Piano»; una freccia aggira il sasso, «se… allora…» | «Quarto, il piano: "se arriva quell'ostacolo, allora faccio questo". Per esempio: "se torno stanco, allora esco comunque per dieci minuti".» |
| 52–64 | «24 studi su questo metodo»; salute, studio, obiettivi personali | «Una ricerca del 2021 ha messo insieme 24 studi su questo metodo, con studenti, adulti e bambini, per obiettivi di salute, di studio e personali.» |
| 64–70 | Due segnalini: quello corallo («con il metodo») arriva più avanti | «In media, chi ha usato il metodo ha ottenuto risultati migliori!» |
| 70–90 | **Il mio punto di vista** (sfondo lilla, «un'opinione personale, non un risultato dello studio»), senza sottotitoli | «Secondo me, prima ancora del desiderio viene il perché: chiedersi perché lo voglio davvero. Quando un obiettivo è mio, e non un "dovrei", trovo più facilmente la forza di affrontare l'ostacolo. Aggiungere il perché come primo passo, però, la scienza non l'ha ancora messo alla prova.» |
| 90–99 | Finale WeSelf, senza sottotitoli | «Prova adesso: un desiderio, il risultato, l'ostacolo, il piano. Quattro passi, un esercizio breve. Il link è in bio.» |

## 2. Registrazione e montaggio

Una frase alla volta, telefono a 15–20 cm, stanza piccola. In CapCut metti ogni frase all'inizio della sua scena (0; 10; 19; 28; 35; 43; 52; 64; 70; 90 secondi), riduzione del rumore attiva, esporta in 1080p a 30 fps. Non aggiungere sottotitoli automatici nel punto di vista e nel finale. Se una frase è più lunga della sua scena, dimmi i secondi e rigenero il video.

## 3. Pubblicazione

**Didascalia (Instagram e Facebook):**

```
Volere non basta: ecco un metodo in quattro passi per passare dal volere al fare.

1. Il desiderio: una cosa che desideri e che puoi davvero ottenere.
2. Il risultato: immagina il momento più bello in cui ci sei riuscito.
3. L'ostacolo: che cosa, dentro di te, potrebbe fermarti?
4. Il piano: «se arriva quell'ostacolo, allora faccio questo».

Il metodo è conosciuto con la sigla inglese WOOP. Una ricerca del 2021 ha messo insieme 24 studi, con studenti, adulti e bambini, per obiettivi di salute, di studio e personali: in media, chi l'ha usato ha ottenuto risultati migliori di chi non l'ha usato. Un vantaggio piccolo ma reale, per un esercizio breve; ed è risultato più forte quando qualcuno guidava l'esercizio.

Mito o realtà? «Per riuscire basta pensare positivo e immaginare il traguardo.» Mito: in questo metodo il traguardo si guarda insieme all'ostacolo, e all'ostacolo si risponde con un piano.

I limiti: l'effetto potrebbe essere un po' più piccolo, perché mancano probabilmente alcuni studi con risultati deboli; molti risultati sono stati riferiti dalle persone stesse; gli studi erano molto diversi tra loro. E non funziona sempre: in una gara di bici di 40 secondi ha reso lo sforzo più facile, ma non ha fatto vincere di più.

Il punto di vista nel video è un'opinione personale del fondatore di WeSelf, non un risultato della ricerca.

Un'onestà necessaria: la ricerca riguarda questo metodo, non WeSelf. Con WeSelf un obiettivo diventa una settimana di piccole azioni, già in agenda, insieme a chi ha il tuo stesso obiettivo.

Qual è il tuo ostacolo di questa settimana? E il tuo «se… allora…»? 👇

#obiettivi #abitudini #motivazione #crescitapersonale #psicologia #WeSelf
```

**Didascalia breve (TikTok):**

```
Desiderio, risultato, ostacolo, piano: quattro passi per passare dal volere al fare. In 24 studi, chi li ha usati ha ottenuto risultati migliori. Fonte: Wang, Wang & Gai, 2021. #obiettivi #abitudini #WeSelf
```

**Primo commento:**

```
📚 Fonte: Wang G., Wang Y., Gai X. (2021). A Meta-Analysis of the Effects of Mental Contrasting With Implementation Intentions on Goal Attainment. Frontiers in Psychology, 12, 565202. https://doi.org/10.3389/fpsyg.2021.565202 (articolo libero)

Il metodo è noto come WOOP (Wish, Outcome, Obstacle, Plan) o MCII. Come leggere il risultato: l'effetto medio è g = 0,34. Convertito con l'indice U3 di Cohen (U3 = Φ(g)): se metti in fila chi non ha usato il metodo, dal risultato più basso al più alto, chi l'ha usato si colloca in media davanti al 63% di loro (50% = nessun effetto). Con la correzione per i possibili studi mancanti g = 0,24 → 60%. Con una persona che guida l'esercizio g = 0,47 → 68%; da soli, su carta o online, g = 0,28 → 61%. Non è un «63% in più» né un «63% di persone riuscite».

Il limite sulla gara di bici viene da: Riddell H. et al. (2024). Journal of Social Psychology, 164(2), 230–243. https://doi.org/10.1080/00224545.2022.2163610
```

**Testo alternativo:** «Animazione: quattro tessere colorate, desiderio, risultato, ostacolo, piano. Una linea che sale verso una bandierina si ferma contro un muretto; poi i quattro passi uno alla volta: una nuvoletta con l'obiettivo, un sole che sorge, un sasso sulla strada, una freccia che lo aggira con la scritta "se… allora…". Una ricerca su 24 studi; due segnalini verso il traguardo, quello "con il metodo" arriva più avanti. Segue un'opinione personale del fondatore di WeSelf e l'invito a provare i quattro passi.»

## 4. Note di affidabilità

- Numeri verificati sul testo completo (Results, Tabella 2): g = 0,336 complessivo (24 studi da 21 articoli, 15.907 persone); trim-and-fill g = 0,242; con sperimentatore g = 0,465; documento g = 0,277.
- Il totale di 15.907 persone non è citato nel video: per l'87% viene da due grandi studi su corsi online con effetto molto piccolo.
- Il «perché» resta solo nel punto di vista del fondatore, dichiarato come opinione: la ricerca di Wang non lo ha misurato; Riddell et al. (2024) e Koestner et al. (2008) lo hanno studiato, ma nessuno ha messo alla prova il «perché» come passo aggiuntivo del metodo.
- Il limite della gara di bici è un secondo studio, citato solo in didascalia e nel primo commento (Riddell et al., 2024), non nel video.
- Gli esempi (camminare tre volte, «se torno stanco…») sono nostri.
- Tema non clinico: nessun rimando di supporto necessario.
