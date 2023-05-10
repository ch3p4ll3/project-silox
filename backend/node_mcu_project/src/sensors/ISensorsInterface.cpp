#include "Arduino.h"
#include <ArduinoJson.h>
#include "ISensorsInterface.h"


void ISensorsInterface::setSlug(String slug){
    this->slug = slug;
}

void ISensorsInterface::setName(String name){
    this->name = name;
}

void ISensorsInterface::setValue(double value){
    this->value = value;
}

String ISensorsInterface::getSlug(){
    return this->slug;
}

String ISensorsInterface::getName(){
    return this->name;
}

double ISensorsInterface::getValue(){
    return this->value;
}

String ISensorsInterface::toJson(){
    String out_str;

    DynamicJsonDocument doc(1024);

    doc["Name"] = this->name;
    doc["Value"] = this->value;

    serializeJson(doc, out_str);

    return out_str;
}

String ISensorsInterface::getTopic(){
    return "t/simulator/silos/" + String(this->silosId) + "/measurements/" + this->slug;
}