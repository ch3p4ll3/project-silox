#include "temp_sensor.h"
#include <Arduino.h>
#include <TMP36.h>


TempSensor::TempSensor(String name, String slug, int silosId, TMP36* temp_sensor){
    this->slug = slug;
    this->name = name;
    this->silosId = silosId;
    this->temp_sensor = temp_sensor;
    this->value = temp_sensor->getTempC();
}

String TempSensor::toJson(){
    this->value = temp_sensor->getTempC();

    return ISensorsInterface::toJson();
}