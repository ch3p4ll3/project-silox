#include "../ISensorsInterface.h"
#include <Arduino.h>
#include "DHT.h"


class TempSensor : public ISensorsInterface{
    private:
        DHT* temp_sensor;

    public:
        TempSensor(String name, String slug, int silosId, DHT* temp_sensor);
        String toJson();
};