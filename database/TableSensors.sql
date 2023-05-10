CREATE TABLE sensorType (
    idSensorType serial PRIMARY KEY,
    nameSensor text not null,
    type text not null,
    maintenanceInterval int not null,
    minValue decimal not null,
    maxValue decimal not null
);
