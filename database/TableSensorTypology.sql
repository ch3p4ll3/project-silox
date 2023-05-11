CREATE TABLE sensorTypology (
    id serial PRIMARY KEY,
    nameSensor text not null,
    type text REFERENCES SensorTypes(id),
    maintenanceInterval int not null,
    measure_unit int REFERENCES MeasureUnits(id),
    minValue decimal not null,
    maxValue decimal not null
);
