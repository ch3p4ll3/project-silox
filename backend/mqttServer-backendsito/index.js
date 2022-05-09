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

app.get('/zone', async (req, res) => {
    let text = 'SELECT idZona, nome FROM zona';
    const { rows } = await db.query(text, null);

    mqtt.aedes.publish({topic: 'info', payload: 'ergaerg'});

    res.json(rows);
});

app.get('/zona/:idZona', async (req, res) => {
    db.getMeasurment("silos1", res)
    /*let text = 'SELECT idsilo, diametro, liquido.nome, densita, sensoritotali, sensoriattivi, umidità, temperatura, altezza, data FROM zona INNER JOIN silo ON id_zona = idZona INNER JOIN liquido ON id_liquido = idliquido WHERE idZona= $1';
    let values = [req.params.idZona];
    let { rows } = await db.query(text, values);

    rows.forEach(element => {
        if (element['sensoriattivi'] == null){
            element['sensoriattivi'] = 0;
        }

        element['riempimento'] = ((element['altezza']/element['sensoritotali']*element['sensoriattivi'])/element['sensoritotali'])*100;
        element['volume'] = (Math.PI*Math.pow(element['diametro']/2, 2))*(element['altezza']/element['sensoritotali']*element['sensoriattivi']);
        element['peso'] = element['volume']*element['densita'];
    });

    res.json(rows);*/
});

app.get('/zona/:idZona/silos/:idSilos', async (req, res) => {
    let text = 'SELECT idsilo, diametro, liquido.nome, densita, sensoritotali, sensoriattivi, umidità, temperatura, altezza, data FROM zona INNER JOIN silo ON id_zona = idZona INNER JOIN liquido ON id_liquido = idliquido WHERE idZona= $1 AND idsilo= $2';
    let values = [req.params.idZona, req.params.idSilos];
    let { rows } = await db.query(text, values);

    rows.forEach(element => {
        if (element['sensoriattivi'] == null){
            element['sensoriattivi'] = 0;
        }

        element['riempimento'] = ((element['altezza']/element['sensoritotali']*element['sensoriattivi'])/element['sensoritotali'])*100;
        element['volume'] = (Math.PI*Math.pow(element['diametro']/2, 2))*(element['altezza']/element['sensoritotali']*element['sensoriattivi']);
        element['peso'] = element['volume']*element['densita'];
    });

    res.json(rows);
});

app.post('/aggiungiLiquido', (req, res) => {
    let liquido = req.body;

    console.log(liquido);

    res.send('Liquido aggiunto');
});

app.get('/aggiorna', (req, res) => {
    mqtt.aedes.publish({topic: 'info', payload: 'update'});
    res.send("OK");
});

app.get("*", function (req, res) {
    res.status(403).send("Forbidden");
});

mqtt.server.listen(mqtt.port, function () {
    console.log(`MQTT Broker running on port: ${mqtt.port}`);
});

app.listen(port, () => console.log(`Hello world app listening on port ${port}!`));