const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const db = require("./database");
const mqtt = require("./brokermqtt")

const app = express();
const port = 3000;

app.use(cors());


app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());


//endpoint che ritorna le zone disponibili
app.get('/zone', async (req, res) => {
    let text = 'SELECT idZona, nome FROM zona';
    const { rows } = await db.query(text, null);

    mqtt.aedes.publish({topic: 'info', payload: 'ergaerg'});

    res.json(rows);
});


//endpoint che data una zona ritorna i silos presenti
app.get('/zona/:idZona', async (req, res) => {
    let text = 'SELECT idsilo, diametro, liquido.nome, densita, altezza FROM zona INNER JOIN silo ON id_zona = idZona INNER JOIN liquido ON id_liquido = idliquido WHERE idZona= $1';
    let values = [req.params.idZona];
    let { rows } = await db.query(text, values);

    res.json(rows);
});


//endpoint che ritorna l'ultima misurazione di un silos
app.get('/silos/:idSilos/last', async (req, res) => {
    let text = 'SELECT id_Zona, idsilo, diametro, liquido.nome AS liquido, densita, altezza FROM silo INNER JOIN liquido ON id_liquido = idliquido WHERE idsilo = $1';
    let values = [req.params.idSilos];
    let { rows } = await db.query(text, values);

    db.getLastSilosMeasurements(req.params.idSilos, rows, res)
});


//endpoint che ritorna tutte le misurazioni di un silos
app.get('/silos/:idSilos/all', async (req, res) => {
    let text = 'SELECT id_Zona, idsilo, diametro, liquido.nome AS liquido, densita, altezza FROM silo INNER JOIN liquido ON id_liquido = idliquido WHERE idsilo = $1';
    let values = [req.params.idSilos];
    let { rows } = await db.query(text, values);

    db.getAllSilosMeasurements(req.params.idSilos, rows, res)
});


//metodo post per aggiungere un liquido al db
app.post('/aggiungiLiquido', (req, res) => {
    let liquido = req.body;

    console.log(liquido);

    res.send('Liquido aggiunto');
});


//metodo post per aggiungere un silos
app.post('/aggiungiSilos', (req, res) => {
    let silo = req.body;

    console.log(silo);

    res.send('Silos aggiunto');
});


//forza l'aggiornamento dei sensori
app.get('/aggiorna', (req, res) => {
    mqtt.aedes.publish({topic: 'info', payload: 'update'});
    res.send("OK");
});


//se la richiesta viene effettuata ad un endpoint non creato ritorna un messaggio di errore
app.get("*", function (req, res) {
    res.status(403).send("Forbidden");
});


//avvia server MQTT
mqtt.server.listen(mqtt.port, function () {
    console.log(`MQTT Broker running on port: ${mqtt.port}`);
});


//avvia webAPI
app.listen(port, () => console.log(`Hello world app listening on port ${port}!`));