CREATE TABLE log (
    idLog SERIAL PRIMARY KEY,
    status TEXT NOT NULL,
    description TEXT NOT NULL,
    time TIMESTAMP,
    silo SERIAL REFERENCES silo(idSilo)
);