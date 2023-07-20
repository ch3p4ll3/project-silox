---
label: REST API Module
order: 3
---

## API Module
The API was written in python using Django and the Django Rest Framework library. 
The APIs are used to manage the database and run the Silos simulators.

### How it works
Django provides a series of endpoints that can be used to manage the database and run the simulators.

When the frontend sends a request to the API, the API will process the request and send the data to the MQTT broker.

The MQTT broker will then send the data to the simulator, which will start sending the data. The ingester will then save the data in influxDB.

### How to start Django in DEV mode
All the project is still in the DEV stage so to start it you just need to go to the `backend/api` folder and start the project with `python manage.py runserver`

This way you will only be able to access it from `http://127.0.0.1:8000`. If you want to start it so that it can be reached from other computers as well
start it with `python manage.py runserver 0.0.0.0:8000`

### Docker entrypoint
The docker entrypoint is a script that starts the Django server. It also creates the database tables and the admin user and create the migrations.

### How to use the API
The API is documented with swagger and can be reached at [https://api.projectsilox.ml/schema/swagger-ui/](https://api.projectsilox.ml/schema/swagger-ui/)
