#include "../ISensorsInterface.h"
#include <Arduino.h>
#include <TMP36.h>


class TempSensor : public ISensorsInterface{
    private:
        TMP36* temp_sensor;

    public:
        TempSensor(String name, String slug, int silosId, TMP36* temp_sensor);
        String toJson();
};