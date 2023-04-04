#include <TMP36.h>
#include <ArduinoJson.h>

#include "EspMQTTClient.h"

#include "sensors/temp_sensor/temp_sensor.h"
#include "sensors/level_sensor/level_sensor.h"
#include "sensors/ISensorsInterface.h"
#include "./pump/pump.h"

#define DELAY 1000  // in ms
#define MAX_SENSORS 2

#define SILOS_HEIGHT 100 // in mm
#define SILOS_ID 1

#define PUMP_FW_PIN 16
#define PUMP_RW_PIN 17

IPAddress local_ip(10, 188, 26, 10);
IPAddress gateway(10, 188, 26, 1);
IPAddress subnet(255, 255, 255, 0);
IPAddress primaryDNS(8, 8, 8, 8);
IPAddress secondaryDNS(8, 8, 8, 8);

EspMQTTClient client;          // using the default constructor

TMP36 myTMP36(36, 3.3);

LevelSensor level_sensor("Level Sensor", "level_sensor", SILOS_ID, 34);
TempSensor temp_sensor("Temp Sensor", "temp_sensor", SILOS_ID, &myTMP36);

Pump pump(SILOS_HEIGHT, &level_sensor, PUMP_FW_PIN, PUMP_RW_PIN);

ISensorsInterface* sensors[MAX_SENSORS] = {
  &temp_sensor,
  &level_sensor
};

int cur_millis;
bool to_kill = false;
bool start = true;
int percentage = 50;


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
  true,
  "TestClient",
  "WiFi SSID",
  "WiFi Password",
  "Broker IP",
  1883,  // broker port
  "MQTT User",
  "MQTT Password"
};

void setup()
{
  Serial.begin(115200);

  pinMode(PUMP_FW_PIN, OUTPUT);
  pinMode(PUMP_RW_PIN, OUTPUT);

  // enable debug messages if our configuration tells us to
  if (CONFIGURATION.debug)
    client.enableDebuggingMessages();


  client.setWifiCredentials(CONFIGURATION.ssid, CONFIGURATION.password, local_ip, gateway, subnet, primaryDNS, secondaryDNS);
  client.setMqttClientName(CONFIGURATION.nodename);
  client.setMqttServer(CONFIGURATION.mqttip, CONFIGURATION.mqttuser, CONFIGURATION.mqttpass, CONFIGURATION.mqttport);
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

  if (!to_kill && start){
    if (millis() - cur_millis >= DELAY){
      cur_millis = millis();

      for(auto sensor : sensors){
        client.publish(sensor->getTopic(), sensor->toJson());
      }
    }
  }
}