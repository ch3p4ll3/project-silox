#include "level_sensor.h"
#include <Arduino.h>
#include "Adafruit_VL53L0X.h"


LevelSensor::LevelSensor(String name, String slug, int silosId, int max_level, Adafruit_VL53L0X* lox){
    this->slug = slug;
    this->name = name;
    this->silosId = silosId;
    this->lox = lox;
    this->max_level = max_level;
}

double LevelSensor::getValue(){
    while (!lox -> isRangeComplete()) {
        if (lox -> Status != 0){
            return -999;
        }
    }

    this->value = lox -> readRange() - this->max_level;

    return this->value;
}

String LevelSensor::toJson(){
    this->value = this->getValue();

    return ISensorsInterface::toJson();
}