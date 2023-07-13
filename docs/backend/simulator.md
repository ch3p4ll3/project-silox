---
title: Simulator Module
order: 2

---

# Simulator Module
The simulator connects to the MQTT broker, when the frontend sends the command that contains the data of the silos
Then a thread is started that begins to send a series of data via MQTT to a broker.

## How to start the simulator
To start the simulator you need to have python 3.11 installed on your machine.
Then you need to install the requirements with `pip install -r requirements.txt`
Then you need to enter the `backend/simulator` folder and start the simulator with `python main.py`

## How to start dockerized simulator
To start the simulator in docker you need to have docker and docker-compose installed on your machine.
Then you need to run `docker-compose --env-file .env up --build`

## How to use the simulator
To use the simulator you need to send a command to the MQTT broker.
The command must be sent to the topic `t/simulator/silos/{silos_id}/command/start` where `{silos_id}` is the id of the silo.
The payload of the command must be a json object that contains the data of the silo.
