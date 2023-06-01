#include "temp_sensor.h"
#include <Arduino.h>
#include "DHT.h"


TempSensor::TempSensor(String name, String slug, int silosId, DHT* temp_sensor){
    this->slug = slug;
    this->name = name;
    this->silosId = silosId;
    this->temp_sensor = temp_sensor;
    this->value = temp_sensor->readTemperature();
}

String TempSensor::toJson(){
    this->value = temp_sensor->readTemperature();

    return ISensorsInterface::toJson();
}