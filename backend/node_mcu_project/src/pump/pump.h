#include <Arduino.h>
#include "../sensors/level_sensor/level_sensor.h"


class Pump{
    private:
        int pump_fw_pin;
        int pump_rw_pin;

        int raw_reading;

        bool is_idle;
        bool is_fill;

        double silos_height;
        double target_percentage;
        LevelSensor *level_sensor;

        double get_silos_percentage();

    public:
        Pump(double silos_height, LevelSensor *level_sensor, int pump_fw_pin, int pump_rw_pin);

        void loop();
        void begin();
        void callback();

        bool is_running();

        void fill(double percentage);
        void empty(double percentage);
        void idle();
};