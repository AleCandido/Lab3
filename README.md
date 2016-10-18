# Lab3
===
Relazioni di laboratorio

### Istruzioni generali
---
Pushare non è necessario se non è di utilità condividere, perciò:
* Si può non farlo continuamente
* Si può anche non committare continuamente, anche se concludi una 'sessione' di lavoro
* Però se modifichi il python committi (così c'è speranza di sbattersi un po' di meno nel debug...)

## 18 Oct 2016:
Per quanto riguarda le mie idee sul punto 5), V_Early:
* analizzare i 'salti' fra i vari punti sulla base del salto medio (magari i salti si possono pesare in qualche modo con l'errore, almeno un peso relativo)
* provare a fittare i due segmenti ben allineati; è vero che la corrispondenza è solo ad occhio, ma non possiamo sbattercene (siamo fisici o matematici?!)
	* capire se si possono imputare a I_B diversi (la cosa più sensata, dovrebbero avere stessa intercetta)
	* capire se cambiando i parametri del transistor (h_FE) c'è un modo facile per spiegarlo
* giustificare ulteriormente quei 4 punti all'inizio (il salto medio è un tentativo di individuazione, ma non di giustificazione)

Non ti preoccupare Bob, mi sarei scritto comunque queste cose su gedit, se le scrivo su README almeno le leggi anche te ^^

## 7 Oct 2016:
Ho modificato leggermente il tuo analizer: per usare i vari ambienti è meglio avere solo tabular, e non anche table.
Per il momento ho lasciato lo stesso che stampasse la caption, supponendo che ogni volta che verrà incluso tabular verrà incluso in un ambiente adeguato, che quindi possa ricevere caption.
* Senza caption: è più esplicito e eviteremo di perdere tempo a volte per capire che l'errore è in un altro file e non nel tex
* Con caption: probabilmente se la scriviamo lì per lì è meglio
Se non usiamo più di tanto le caption in fit() propongo di toglierle e basta.

Ah, ho scritto un po' di relazione, e ti ho trovato l'ambiente per la gestione d'immagini.
* Un prototipo lo trovi già nella nostra relazione, per ogni cosa che ti venga in mente penso che il seguente pdf possa risolvere.
<br/> http://www.guit.sssup.it/downloads/fig_tut.pdf
<br/> (purtroppo il sito di guit è ospitato dai sant'annini...)

Leggi frequentemente questo Readme quando vai a scrivere la relazione, e leggi le note che lascio dentro la relazione.   
P.S.: ho una cartella con un po' di pdf su alcuni pacchetti di tex, se vuoi te la condivido, ma non è niente di eccezionale
