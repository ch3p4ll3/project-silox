const aedes = require('aedes')();
const server = require('net').createServer(aedes.handle);
const db = require("./database");
const port = 1883;

const token = "24705669ef817555487499e723bb00c11656eec404fcd264c899af337d813bfaea5975ef6544214381c61ccdf49dde61984b2bb3b1c1595b9010906011be6cbc";


// emitted when a client connects to the broker
aedes.on('client', function (client) {
    console.log(`[CLIENT_CONNECTED] Client ${(client ? client.id : client)} connected to broker ${aedes.id}`)
})

// emitted when a client disconnects from the broker
aedes.on('clientDisconnect', function (client) {
    console.log(`[CLIENT_DISCONNECTED] Client ${(client ? client.id : client)} disconnected from the broker ${aedes.id}`)
})

// emitted when a client subscribes to a message topic
aedes.on('subscribe', function (subscriptions, client) {
    console.log(`[TOPIC_SUBSCRIBED] Client ${(client ? client.id : client)} subscribed to topics: ${subscriptions.map(s => s.topic).join(',')} on broker ${aedes.id}`)
})

// emitted when a client unsubscribes from a message topic
aedes.on('unsubscribe', function (subscriptions, client) {
    console.log(`[TOPIC_UNSUBSCRIBED] Client ${(client ? client.id : client)} unsubscribed to topics: ${subscriptions.join(',')} from broker ${aedes.id}`)
})

// emitted when a client publishes a message packet on the topic
aedes.on('publish', async function (packet, client) {
    if (client) {
        console.log(`[MESSAGE_PUBLISHED] Client ${(client ? client.id : 'BROKER_' + aedes.id)} has published message on ${packet.topic} to broker ${aedes.id}`)

        //rendi il testo inviato dal PLC un JSON
        let dict = JSON.parse(packet.payload.toString());

        //se il token è valido prosegui
        if(dict['token'] == token) {

            // salva i livelli dei sensori in un array
            let livelli = [dict['livelloSensore1'], dict['livelloSensore2'], dict['livelloSensore3']];

            //calcola la media
            let altezza = (livelli.reduce((a, b) => a + b, 0))/livelli.length;

                try {
                    const res = await db.query("SELECT id_Zona, densita, altezza, diametro, liquido.nome AS liquido FROM silo INNER JOIN liquido ON id_liquido = idliquido WHERE idsilo = $1", [dict['idSilos']])
                    let rows = res.rows[0];
    
                    //aggiungi su influx i dati
                    db.addMeasurement(rows['id_zona'], dict['idSilos'], dict['ph'], dict['tempInt'], dict['tempEst'], dict['umiditaInt'], dict['umiditaEst'], dict['pressioneInt'], rows['altezza']-altezza, rows['densita'], rows['liquido'], rows['diametro']);
            
        
                    // fai sapere al PLC che i dati sono stati salvati correttamente
                    aedes.publish({topic:"info", payload: 'ACK'});
                  } catch (err) {
                    console.log(err.stack)
                  }
        }
    }
});

module.exports = {aedes, server, port};