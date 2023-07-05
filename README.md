![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg) ![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg) ![Django 4.2](https://img.shields.io/badge/django-4.2-blue.svg) ![Docker](https://img.shields.io/badge/docker-yes-blue.svg) ![Docker](https://img.shields.io/badge/docker-compose-yes.svg)

# Tantitank

## LICENSE
The project is licensed under the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-nd/4.0/.

## CONTESTO ##
SiouxSilos Itd. è un'azienda che produce sistemi industriali di stoccaggio di materiali sfusi e liquidi. Ci commissiona la progettazione e la realizzazione di una soluzione atta al monitoraggio e gestione del livello dei materiali contenuti nei silos di un impianto industriale realizzato nel Nord Dakota. Ciascun serbatoio è dotato di 8 sensori (S) posizionati sul lato interno della cisterna alla distanza di 1 mt ciascuno. All'esterno, ad un metro dalla base ed alla sommità, sono collocati un sensore di umidità ed uno di temperatura. I serbatoi sono sette in totale, suddivisi in due blocchi di 3 e 4, collocati in due aree dello stabilimento distanti circa 150 metri una dall'altra. 
La soluzione dovrà essere in grado di: 
* acquisire, attraverso un PLC, i dati rilevati dai sensori, calcolando le quantità di materiale presente 
nei silos, visualizzando i dati più rilevanti in un display; 
* fornire un allarme qualora il livello del serbatoio superi le soglie inferiori e superiori di riferimento; 
gestire, sempre tramite PLC, una saracinesca per il caricamento/svuotamento dei silos; inviare i dati su cloud, attraverso un gateway, gestendo situazioni di assenza o perdita di connettività internet, e mostrando l'andamento dei dati in forma grafica con una pagina web. 

## COMPONENTI ##
Viene richiesta l'implementazione di una dashboard web per visualizzare lo stato attuale dell'impianto. Poiché essa sarà attiva all'interno della intranet aziendale; non sono perciò richiesti autenticazione e/o schemi di autorizzazione: né per la raccolta, né per la visualizzazione dei dati. 
Componenti/Output * 
Acquisizione dati: PLC Ipotesi di lavoro lato PLC: 
* Usato 1 PLC che gestisce i 7 silos 
* Indicare attraverso 3 display: l'altezza del liquido/solido dentro il serbatoio, il volume occupato, la massa di materiale (questo per ciascun silos)
  * Bonus >> se due o più silos contengono lo stesso materiale va rilevato anche il totale 
  contenuto nei silos ed indicato in un ulteriore display (per quantità e volume) 
* Calcolare la quantità di materiale in base a quali sensori rilevano la presenza di liquido e in base alla 
dimensione dei silos 
* In base al peso specifico del materiale, calcolare: 
  - Livello (in mt) o Volume 
  - Massa 
  * Rubinetto di aggiunta / svuotamento materiale 
  * Parti bonus: 
    * con pulsante di aumento / diminuzione portata (o in automatico in funzione del livello del materiale) Due rubinetti con acqua a temperatura diversa: derivare temperatura finale del 
    liquido 
* Alert al superamento di soglia superiore / inferiore 
Gateway di connessione PLC e cloud Lettura dati da PLC via Gateway (es. Kepserver) 
* Codice per leggere i dati dal gateway via OPC (bonus: via altro protocollo, es. MQTT) 
Invio dati a cloud: 
* Nuovi alert con altre logiche non presenti sul PLC (o farlo lato cloud su Telegraph) 
* Lettura dati da GW e invio su cloud alle API di influx (bonus: non API di influx ma layer di API 
davanti... da capire con che tecnologia) 
* Gestione buffer messaggi: memorizzazione su db / coda e invio quando c'è di nuovo connettività 
Presentazione dei dati Lato presentazione dati: 
Influxdb e Dashboard su Cronograph (andamenti nel tempo, alert) o un qualsiasi altro tipo di programma per la presentazione dei dati 
Gestione del progetto 
* Nel corso dello sviluppo del progetto potranno presentarsi situazioni impreviste, nonché modifiche 
alle esigenze del committente e di conseguenza delle specifiche di progetto. Tali varianti dovranno essere efficacemente gestite: 
o in via preventiva, con una definizione delle priorità e la descrizione dei rischi O Attraverso l'implementazione di azioni correttive 