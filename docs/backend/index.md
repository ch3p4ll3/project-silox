# Backend


## API.
Django project that manages the API for the frontend, connection with influxdb, and simulator management

### How it works.
Django provides endpoints that the frontend uses to start or stop a simulator. 
When the frontend sends the command to start a simulation a thread is started that begins
to send a set of data via MQTT to a broker.

### How to start Django
All the project is still in the DEV stage so to start it you just need to go to the `api` folder and start the project with `python manage.py runserver`

This way you will only be able to access it from `http://127.0.0.1:8000`. If you want to start it so that it can be reached from other computers as well
start it with `python manage.py runserver 0.0.0.0:8000`

### System map
<iframe src="https://embed.kumu.io/f0b00ab5c780b721d67cc7c889ea4d3e" width="940" height="600" frameborder="1"></iframe>
