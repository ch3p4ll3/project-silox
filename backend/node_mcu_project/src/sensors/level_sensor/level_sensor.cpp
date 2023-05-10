#include "level_sensor.h"
#include <Arduino.h>
#include <TMP36.h>


LevelSensor::LevelSensor(String name, String slug, int silosId, int sensor_pin){
    this->slug = slug;
    this->name = name;
    this->silosId = silosId;
    this->sensor_pin = sensor_pin;
}

double LevelSensor::getValue(){
    this->value = map(analogRead(sensor_pin), 0, 4095, 0, 100);

    return this->value;
}

String LevelSensor::toJson(){
    this->value = map(analogRead(sensor_pin), 0, 4095, 0, 100);

    return ISensorsInterface::toJson();
}