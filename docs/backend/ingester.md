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
