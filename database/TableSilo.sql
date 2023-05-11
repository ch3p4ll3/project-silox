CREATE TABLE silo (
    idSilo SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    size SERIAL REFERENCES size(idSize)
    liquid SERIAL REFERENCES liquid(idLiquid)
);
