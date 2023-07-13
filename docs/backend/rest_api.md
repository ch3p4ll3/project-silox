---
label: REST API
order: 3
---

## API Module
The API was written in python using Django and the Django Rest Framework library. 
The APIs are used to manage the database and run the Silos simulators.

### How it works
Django provides endpoints that the frontend uses to start or stop a simulator.

### How to start Django in DEV mode
All the project is still in the DEV stage so to start it you just need to go to the `backend/api` folder and start the project with `python manage.py runserver`

This way you will only be able to access it from `http://127.0.0.1:8000`. If you want to start it so that it can be reached from other computers as well
start it with `python manage.py runserver 0.0.0.0:8000`

### How to start Django dockerized
To start the project in docker you need to have docker and docker-compose installed on your machine.
Then you need to run `docker-compose --env-file .env up --build`

### How to use the API
The API is documented with swagger and can be reached at [https://api.projectsilox.ml/schema/swagger-ui/](https://api.projectsilox.ml/schema/swagger-ui/)
