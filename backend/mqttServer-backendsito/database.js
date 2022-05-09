/*const { Client } = require('pg');


let client = new Client({
    user: 'amministratore',
    host: 'dbsilos.c9nj1x2p6gk5.eu-west-1.rds.amazonaws.com',
    database: 'postgres',
    password: 'Vmware1!',
    port: 5432,
});


client.connect();*/ 

const token="9fxmHGECaPlFDvh1Eji-NClgUcUthQp4jPOFmYHrv5dQDBWhYbnhXk63xSZ7Ce2zFqiy_43rGXtixFkqBoBMOA==";

const {InfluxDB, Point, FluxTableMetaData} = require('@influxdata/influxdb-client')

const url = 'https://eu-central-1-1.aws.cloud2.influxdata.com'

const client = new InfluxDB({url, token})



let org = `mattia.vidoni@stud.itsaltoadriatico.it`
let bucket = `silos`

const writeClient = client.getWriteApi(org, bucket, 'ns')
const queryApi = client.getQueryApi(org)


function addMeasurement(idSilos, ph, tempInt, tempEst, umiditaInt, umiditaEst, pressioneInt, volume){
    let point = new Point(idSilos)
    .tag('tagname1', 'tagvalue1')
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

function getMeasurment(idSilos, res){
    let last_table = -1;
    let dict = {}
    let fluxQuery = `from(bucket: "silos")
    |> range(start: -20h)
    |> filter(fn: (r) => r._measurement == "${idSilos}")`;


    queryApi.queryRows(fluxQuery, {
        next: (row, tableMeta) => {
            // the following line creates an object for each row
            const o = tableMeta.toObject(row);

            if (o.table != last_table){
                last_table = o.table;
            }

            if (dict[o._time] == null){
                dict[o._time] = {"silos": o._measurement};
            }
            dict[o._time][o._field] = o._value;
        },
        error: (error) => {
          console.error(error)
          console.log('\nFinished ERROR')
          res.error(403).send("errore");
        },
        complete: () => {
          console.log('\nFinished SUCCESS')
          console.log(dict);
          //res.json(ser);
        },
      })
}


module.exports = {
    getMeasurment, addMeasurement
}
//addMeasurement("silos1", 256, 23, 24, 25, 2, 2, 23);

getMeasurment("silos1", null)
//addMeasurement("silos1", 2, 23, 2, 2, 2, 25, 24);

//console.log(getMeasurment("silos1"));

/*

module.exports = {
    query: (text, params) => client.query(text, params),
  }*/