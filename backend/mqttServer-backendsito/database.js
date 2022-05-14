const { Client } = require('pg');
const token="9fxmHGECaPlFDvh1Eji-NClgUcUthQp4jPOFmYHrv5dQDBWhYbnhXk63xSZ7Ce2zFqiy_43rGXtixFkqBoBMOA==";
const {InfluxDB, Point} = require('@influxdata/influxdb-client')

const url = 'https://eu-central-1-1.aws.cloud2.influxdata.com'
const client = new InfluxDB({url, token})
let org = `mattia.vidoni@stud.itsaltoadriatico.it`
let bucket = `silos`


// client per DB postgres
let pgClient = new Client({
    user: 'amministratore',
    host: 'dbsilos.c9nj1x2p6gk5.eu-west-1.rds.amazonaws.com',
    database: 'postgres',
    password: 'Vmware1!',
    port: 5432,
});


pgClient.connect();

const writeClient = client.getWriteApi(org, bucket, 'ns')
const queryApi = client.getQueryApi(org)


//metodo per aggiungere su influx le misurazioni
function addMeasurement(idZona, idSilos, ph, tempInt, tempEst, umiditaInt, umiditaEst, pressioneInt, volume){
    let point = new Point(idSilos)
    .tag('zona', idZona)
    .floatField('ph', ph)
    .floatField('tempInt', tempInt)
    .floatField('tempEst', tempEst)
    .floatField('umiditaInt', umiditaInt)
    .floatField('umiditaEst', umiditaEst)
    .floatField('pressioneInt', pressioneInt)
    .floatField('volume', volume)

    console.log(point);

    writeClient.writePoint(point)
    writeClient.flush()
}


//funzione per ordinare le query prese da influx
function orderDict(dict, o, last_table){
    if (o.table != last_table){
        last_table = o.table;
    }

    if (dict[o._time] == null){
        dict[o._time] = {};
    }
    dict[o._time][o._field] = o._value;
}


//prendi l'ultima misurazione di un silos
function getLastSilosMeasurements(idSilos, silosInfo, res){
    let last_table = -1;
    let dict = {};
    let fluxQuery = `from(bucket: "silos")
    |> range(start: -42h)
    |> filter(fn: (r) => r._measurement == "${idSilos}")
    |> last(column: "_time")`;


    queryApi.queryRows(fluxQuery, {
        next: (row, tableMeta) => {
            // the following line creates an object for each row
            const o = tableMeta.toObject(row);
            orderDict(dict, o, last_table);
        },
        error: (error) => {
          console.error(error)
          console.log('\nFinished ERROR')
          res.error(403).send("errore");
        },
        complete: () => {
            console.log('\nFinished SUCCESS')
            let rtn = {"lastMeasurement": dict};
            rtn['silosInfo'] = silosInfo;
            res.json(rtn);
        },
      })
}


//prendi tutte le misurazioni delle ultime 12h
function getAllSilosMeasurements(idSilos, silosInfo, res){
    let last_table = -1;
    let dict = {};
    let fluxQuery = `from(bucket: "silos")
    |> range(start: -12h)
    |> filter(fn: (r) => r._measurement == "${idSilos}")`;


    queryApi.queryRows(fluxQuery, {
        next: (row, tableMeta) => {
            // the following line creates an object for each row
            const o = tableMeta.toObject(row);
            orderDict(dict, o, last_table);
        },
        error: (error) => {
          console.error(error)
          console.log('\nFinished ERROR')
          res.error(403).send("errore");
        },
        complete: () => {
            console.log('\nFinished SUCCESS')
            let rtn = {"measurements": []};

            for (const [key, value] of Object.entries(dict)) {
                rtn['measurements'].push({[key] : value});
            };
            rtn['silosInfo'] = silosInfo;
            res.json(rtn);
        },
      })
}


module.exports = {
    getAllSilosMeasurements, getLastSilosMeasurements, 
    addMeasurement, query: (text, params) => pgClient.query(text, params)
}