const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const db = require("./database");

const app = express();
const port = 3000;

app.use(cors());


app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.get('/zone', (req, res) => {
    res.json(["idZona1", "idZona2", "idZona3"]);
});

app.get('/zona/:idZona', async (req, res) => {
    let text = 'SELECT * FROM corsi WHERE id = ($1)';
    let values = [req.params.idZona];
    const { rows } = await db.query(text, values);

    res.send(rows[0]);

    //res.json({"silos": [{"idSilos1": {"sensoriMax": 8, "sensoriAttivi": 5, "diametro": 5.45, "liquido": {"nome": "Vino", "densità": 34.43}, "ultimoScarico": "2021", "ultimoRiempimento": "2021"}}, "id2", "..."]})

    //res.status(404).send("Errore")
});

app.get('/zona/:idZona/:idSilos', (req, res) => {
    // info silos
    let idZona = req.params.idZona;
    let idSilos = req.params.idSilos;

    res.json({"silos" : {"sensoriMax": 8, "sensoriAttivi": 5, "diametro": 5.45}});
});

app.post('/aggiungiLiquido', (req, res) => {
    let liquido = req.body;

    console.log(liquido);

    res.send('Liquido aggiunto');
});

app.get("*", function (req, res) {
    res.status(403).send("Forbidden");   
});


app.listen(port, () => console.log(`Hello world app listening on port ${port}!`));