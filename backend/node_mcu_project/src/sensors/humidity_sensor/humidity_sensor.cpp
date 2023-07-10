#include "humidity_sensor.h"
#include <Arduino.h>
#include "DHT.h"


HumiditySensor::HumiditySensor(String name, String slug, int silosId, DHT* temp_sensor){
    this->slug = slug;
    this->name = name;
    this->silosId = silosId;
    this->temp_sensor = temp_sensor;
    this->value = temp_sensor->readHumidity();
}

String HumiditySensor::toJson(){
    this->value = temp_sensor->readHumidity();

    return ISensorsInterface::toJson();
}