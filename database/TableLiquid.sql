CREATE TABLE liquid (
    idLiquid SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    density FLOAT NOT NULL,
    pHMin FLOAT,
    pHMax FLOAT,
    cO2Min FLOAT,
    cO2Max FLOAT,
    temperatureMin FLOAT,
    temperatureMax FLOAT,
    pressureMax FLOAT,
    pressureMin FLOAT DEFAULT 1
);