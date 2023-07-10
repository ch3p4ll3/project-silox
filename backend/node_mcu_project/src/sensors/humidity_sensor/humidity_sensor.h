#include "../ISensorsInterface.h"
#include <Arduino.h>
#include "DHT.h"


class HumiditySensor : public ISensorsInterface{
    private:
        DHT* temp_sensor;

    public:
        HumiditySensor(String name, String slug, int silosId, DHT* temp_sensor);
        String toJson();
};