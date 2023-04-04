#pragma once

#include "../ISensorsInterface.h"
#include <Arduino.h>
#include <TMP36.h>


class LevelSensor : public ISensorsInterface{
    private:
        int sensor_pin;
    public:
        LevelSensor(String name, String slug, int silosId, int lambda);
        String toJson();
        double getValue();
};