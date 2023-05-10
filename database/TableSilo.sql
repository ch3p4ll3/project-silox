CREATE TABLE silo (
    idSilo SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    height FLOAT NOT NULL,
    diameter FLOAT NOT NULL,
    liquid SERIAL REFERENCES liquid(idLiquid)
);
