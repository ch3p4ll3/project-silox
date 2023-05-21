#include "./pump.h"


Pump::Pump(double silos_height, LevelSensor *level_sensor, int pump_fw_pin, int pump_rw_pin){
    this->silos_height = silos_height;
    this->level_sensor = level_sensor;
    this->is_idle = true;

    this->pump_fw_pin = pump_fw_pin;
    this->pump_rw_pin = pump_rw_pin;
}

void Pump::begin(){
    pinMode(this->pump_fw_pin, OUTPUT);
    pinMode(this->pump_rw_pin, OUTPUT);
}

void Pump::loop(){
    double current_percentage = get_silos_percentage();

    if (!is_idle){
        if ((is_fill && current_percentage < target_percentage) && touchRead(15) >= 11){ //fill
            digitalWrite(pump_fw_pin, HIGH);
            digitalWrite(pump_rw_pin, LOW);
        }
        
        else if(!is_fill && current_percentage > target_percentage) { //empty
            digitalWrite(pump_fw_pin, LOW);
            digitalWrite(pump_rw_pin, HIGH);
        }

        else {  // if ((!is_fill && current_percentage <= target_percentage) || (is_fill && current_percentage >= target_percentage))
            idle();
        }
    }
}

void Pump::fill(double percentage){
    is_idle = false;
    is_fill = true;
    target_percentage = percentage;
}

void Pump::empty(double percentage){
    is_idle = false;
    is_fill = false;
    target_percentage = percentage;
}

void Pump::idle(){
    is_idle = true;
    digitalWrite(pump_fw_pin, LOW);
    digitalWrite(pump_rw_pin, LOW);
}

bool Pump::is_running(){
    return !this->is_idle;
}

double Pump::get_silos_percentage(){  // fix me
    this->raw_reading = this->level_sensor->getValue();

    if (this -> raw_reading == -999.0){
        idle();
    }

    return ((this -> silos_height - this->raw_reading) / this->silos_height) * 100;
}