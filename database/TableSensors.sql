CREATE TABLE sensor (
    idSensor serial PRIMARY KEY,
    silo serial REFERENCES silo(idSilo),
    sensor serial REFERENCES sensorTypology(id),
    lastMaintenance TIMESTAMP,
    positionOnSilo text
);
