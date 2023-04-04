#include "./pump.h"


Pump::Pump(double silos_height, LevelSensor *level_sensor, int pump_fw_pin, int pump_rw_pin){
    this->silos_height = silos_height;
    this->level_sensor = level_sensor;
    this->is_idle = true;

    this->pump_fw_pin = pump_fw_pin;
    this->pump_rw_pin = pump_rw_pin;
}

void Pump::loop(){
    double current_percentage = get_silos_percentage();

    if (!is_idle){
        if (is_fill && current_percentage < target_percentage){
            digitalWrite(pump_fw_pin, HIGH);
            digitalWrite(pump_rw_pin, LOW);
        }
        
        else if(!is_fill && current_percentage > target_percentage) {
            digitalWrite(pump_fw_pin, LOW);
            digitalWrite(pump_rw_pin, HIGH);
        }

        else if (!is_fill && current_percentage <= target_percentage || is_fill && current_percentage >= target_percentage){
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

double Pump::get_silos_percentage(){
    return (100 * this->level_sensor->getValue()) / this->silos_height;
}