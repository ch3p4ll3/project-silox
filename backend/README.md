# Backend #

## mqttClient ##
Client per protocollo mqtt che simula il PLC che manda i dati ad un broker MQTT

### Come funziona ###
selezionare zona/silos quando ci sarà un cambiamento manderà un messaggio al server 
nel topic /zona/silos contenente il numero di sensori attivi.

Se il server manda nel topic info un messaggio es. aggiornamento, scarica, carica il client
simula l'azione richiesta

#TODO: topic info

## mqttServer-backendsito ##
Dentro questa cartella sono presenti i backend del server mqtt e del sito web

### brokermqtt.js ###
applicazione in node che fa da server MQTT, utilizzato per salvare stato sensori e inviare info ai PLC

#TODO: salvataggio stati, invio info

### index.js ###
contiene le rest API per fornire informazioni il sito web, per accedere alle info usare endpoint specificati, altrimenti
il server ritornerà l'errore 403 Forbidden.

#TODO: richieste Db, ulteriori endpoint

### database.js ###
Contiene informazioni per collegarsi al DB usato sia da index.js che da brokermqtt.js