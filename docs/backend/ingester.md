---
label: Ingester Module
order: 1
---

# Ingester Module
The ingester is a python script that subscribes to the MQTT broker and saves the data in the influxdb database.

## How to start the ingester
To start the ingester you need to have python 3.11 installed on your machine.
Then you need to install the requirements with `pip install -r requirements.txt`
Then you need to enter the `backend/ingester` folder and start the ingester with `python main.py`

## How to start dockerized ingester
To start the ingester in docker you need to have docker and docker-compose installed on your machine.
Then you need to run `docker-compose --env-file .env up --build`
