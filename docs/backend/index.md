# Backend
The Backend was developed in python and consists of 3 main modules: REST API, Simulator, ingester. 
These 3 modules work autonomously and communicate with each other through the MQTT protocol.

## System map
<iframe src="https://embed.kumu.io/f0b00ab5c780b721d67cc7c889ea4d3e" width="940" height="600" frameborder="1"></iframe>

## The modules

### API Module
The API was written in python using Django and the Django Rest Framework library. 
The APIs are used to manage the database and run the Silos simulators.

### Simulator Module
The simulator connects to the MQTT broker, when the frontend sends the command that contains the data of the silos
Then a thread is started that begins to send a series of data via MQTT to a broker.

### Ingestor Module
The ingester is a python script that subscribes to the MQTT broker and saves the data in the influxdb database.
