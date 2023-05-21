#pragma once

#include "../ISensorsInterface.h"
#include <Arduino.h>
#include "Adafruit_VL53L0X.h"


class LevelSensor : public ISensorsInterface{
    private:
        Adafruit_VL53L0X* lox;
        int max_level;
    public:
        LevelSensor(String name, String slug, int silosId, int max_level, Adafruit_VL53L0X* lox);
        String toJson();
        double getValue();
};