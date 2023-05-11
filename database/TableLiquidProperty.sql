Table liquidProperty {
    id int PRIMARY KEY,
    liquid int NOT NULL REFERENCES liquid(idLiquid),
    property int REFERENCES property(id),
    min float not null,
    max float not null
}