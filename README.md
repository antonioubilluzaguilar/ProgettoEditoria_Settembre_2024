# ProgettoEditoria_Settembre_2024
## Introduzione

Il progetto è stato pensato con lo scopo di riprodurre il Menù di un ristorante-pizzeria in un formato moderno e accessibile sui dispositivi mobili, anche per diminuire il bisogno di menù cartacei.

La pizzeria in questione è l'**Antica Pizzeria Santi** di Rivolta d'Adda dove occasionalmente lavoro la sera. Il progetto sarà utile alla pizzeria perché espandibile, facilmente modificabile, accessibile dai propri telefoni e permetterà di vedere un anteprima delle pizze e dei piatti.

## Modalità di Utilizzo

### Fase 1: Ideazione e Creazione

Per aggiungere un nuovo piatto o una nuova pizza al menù, sarà necessario scrivere tutte le informazioni su di un file `Markdown`.

### Fase 2: Trasformazione

Il file appena scritto per poter essere aggiunto all'`EPUB` deve prima essere convertito in `xhtml`.

Per la conversione verrà utilizzato `pandoc`, una tecnologia che permette conversioni dinamiche *tra molti formati a molti formati*.

La conversione può richiedere tempo se fatta su molti file, perciò è stato scritto uno script per aggevolare il processo di conversione. Per avviare lo script però è necessario aver installato `python`.

A questo punto bisogna aprire un `command prompt` e dirigerci nella cartella `Utility`, **spostare il file da convertire** anche essa dentro la cartella e poi eseguire:

```cmd
python converter.py
```

Lo script ci chiederà il nome del file da convertire e se il file è in formato Markdown (con l'estenzione `.md`) allora genererà un file con lo stesso nome ma col formato `.xhtml`.

Lo script continuerà a chiederci di inserire il nome dei prossimi file finché non verrà dato in input la stringa `exit`.

In caso non si voglia far uso dello script, non sarà necessario aver installato `python`, e basterà eseguire il seguente comando:

```cmd
pandoc -s [file_name].md --metadata-file=metadata.txt -o [file_name].xhtml
```

Così avremo generato la pagina e sarà pronta da inserire all'interno dell'`EPUB`.

### Fase 3: Inserimento pagina

Per inserire una nuova pagina si fa uso di un editor per `EPUB` gratuito, ***Sigil***.

Dopo aver aperto *Sigil* bisogna aprire il file `.epub`.

Nell'editor si può notare un **cerchio verde** con un **più** all'interno, una volta cliccato verrà chiesto di indicare il file da aggiungere. Qui basterà selezionare il file appena creato in `.xhtml` e verrà automaticamente aggiunto alla sottocartella `Text`.

Col cursore trasciniamo il nuovo file dove vogliamo all'interno della cartella `Text`, in base a dove viene posizionato, quella sarà la posizione all'interno dell'epub. Il `TOC` (Table Of Contents) non viene aggiornato all'inserimento di una nuova pagina, quindi sarà necessario aprire il file `nav.xhtml` e aggiungere il link alla nuova pagina.