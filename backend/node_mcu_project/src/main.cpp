#include "DHT.h"
#include "Adafruit_VL53L0X.h"
#include <ArduinoJson.h>

#include "EspMQTTClient.h"

#include "sensors/temp_sensor/temp_sensor.h"
#include "sensors/level_sensor/level_sensor.h"
#include "sensors/humidity_sensor/humidity_sensor.h"
#include "sensors/ISensorsInterface.h"
#include "./pump/pump.h"

#define DELAY 1000  // in ms
#define MAX_SENSORS 3

#define SILOS_HEIGHT 250 // in mm
#define MAX_LEVEL 50 // in mm, 30mm = full silos
#define SILOS_ID -1

#define PUMP_FW_PIN 16
#define PUMP_RW_PIN 17

#define DHTTYPE DHT22
#define DHT_SENSOR_PIN 4

IPAddress local_ip(10, 188, 26, 10);
IPAddress gateway(10, 188, 26, 1);
IPAddress subnet(255, 255, 255, 0);
IPAddress primaryDNS(8, 8, 8, 8);
IPAddress secondaryDNS(1, 1, 1, 1);

EspMQTTClient client;          // using the default constructor

DHT dht(DHT_SENSOR_PIN, DHTTYPE);
Adafruit_VL53L0X lox = Adafruit_VL53L0X();

LevelSensor level_sensor("Level Sensor", "level_sensor", SILOS_ID, MAX_LEVEL, &lox);
TempSensor temp_sensor("Temp Sensor", "temp_sensor", SILOS_ID, &dht);
HumiditySensor humidity_sensor("Humidity Sensor", "humidity_sensor", SILOS_ID, &dht);

Pump pump(SILOS_HEIGHT - MAX_LEVEL, &level_sensor, PUMP_FW_PIN, PUMP_RW_PIN);

ISensorsInterface* sensors[MAX_SENSORS] = {
  &temp_sensor,
  &humidity_sensor,
  &level_sensor
};

int cur_millis;
bool to_kill = false;
bool start = true;
int percentage = 0;


typedef struct {
  uint8_t debug;        // Debug on yes/no 1/0
  char nodename[32];    // this node name
  char ssid[32];        // WiFi SSID
  char password[64];    // WiFi Password
  char mqttip[32];      // Mosquitto server IP
  uint16_t mqttport;    // Mosquitto port
  char mqttuser[32];    // Mosquitto Username (if needed, or "")
  char mqttpass[64];    // Moqsuitto Password (if needed, or "")
} configuration_t;


//Declare a default configuration_t to use
configuration_t CONFIGURATION = {
  false,
  "TestClient",
  "5G COVID-19 TEST",
  "30Matvid11!",
  "10.188.26.101",
  1883,
  "",
  ""
};

void setup()
{
  Serial.begin(115200);

  pump.begin();
  dht.begin();
  lox.begin();
  lox.configSensor(lox.VL53L0X_SENSE_HIGH_ACCURACY);

  //lox.setMeasurementTimingBudgetMicroSeconds(200000);

  // enable debug messages if our configuration tells us to
  if (CONFIGURATION.debug)
    client.enableDebuggingMessages();

  client.setWifiCredentials(CONFIGURATION.ssid, CONFIGURATION.password); //, local_ip, gateway, subnet, primaryDNS, secondaryDNS);
  client.enableOTA();
  client.setMqttClientName(CONFIGURATION.nodename);
  client.setMqttServer(CONFIGURATION.mqttip, CONFIGURATION.mqttuser, CONFIGURATION.mqttpass, CONFIGURATION.mqttport);

  lox.startRangeContinuous();
}

// This function is called once everything is connected (Wifi and MQTT)
// WARNING : YOU MUST IMPLEMENT IT IF YOU USE EspMQTTClient
void onConnectionEstablished()
{
  // Subscribe to "mytopic/test" and display received message to Serial
  client.subscribe("t/simulator/silos/" + String(SILOS_ID) + "/command/+", [](const String & topic, const String & payload) {
    if (topic.endsWith("fill")){
      DynamicJsonDocument doc(1024);
      deserializeJson(doc, payload);

      percentage = doc["percentage"];
      pump.fill(percentage);
    }

    else if (topic.endsWith("empty")){
      DynamicJsonDocument doc(1024);
      deserializeJson(doc, payload);

      percentage = doc["percentage"];
      pump.empty(percentage);
    }

    else if (topic.endsWith("idle")){
      pump.idle();
    }

    else if (topic.endsWith("kill")){
      DynamicJsonDocument doc(1024);
      deserializeJson(doc, payload);

      to_kill = doc["kill"];
    }

    else if (topic.endsWith("start")){
      start = true;
    }

    else if (topic.endsWith("stop")){
      start = false;
    }
  });
}

void loop()
{
  client.loop();
  pump.loop();

  if (!to_kill && start && client.isConnected()){
    if (millis() - cur_millis >= DELAY){
      cur_millis = millis();

      for(auto sensor : sensors){
        client.publish(sensor->getTopic(), sensor->toJson());
      }
    }
  }

  if ((to_kill || !start) && pump.is_running()){
    pump.idle();
  }
}