const { Client } = require('pg');


let client = new Client({
    user: 'mattia',
    host: 'localhost',
    database: 'its',
    password: 'qwerty159',
    port: 5432,
});

client.connect();


module.exports = {
    query: (text, params) => client.query(text, params),
  }