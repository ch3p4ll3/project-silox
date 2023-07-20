# Project Silox
![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg) ![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg) ![Django 4.2](https://img.shields.io/badge/django-4.2-blue.svg) ![Docker](https://img.shields.io/badge/docker-yes-blue.svg) ![Docker](https://img.shields.io/badge/docker-compose-yes.svg)

## License
The project is licensed under the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License. 
To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-nd/4.0/.

## Context
SiouxSilos Itd. is a company that manufactures industrial bulk and liquid materials storage systems. 
It commissioned us to design and implement a solution suitable for monitoring and managing the level of 
materials contained in the silos of an industrial plant built in North Dakota. 

Each tank is equipped with 8 sensors (S) positioned on the inner side of the tank at the distance of 1 m each. 
On the outside, one meter from the base and at the top, one humidity sensor and one temperature sensor are placed. 
There are seven tanks in total, divided into two blocks of 3 and 4, 
located in two areas of the plant about 150 meters apart. 

The solution should be able to: 
* acquire, through a PLC, the data detected by the sensors, calculating the quantities of material present in the silos, displaying the most relevant data in a display; 
* provide an alarm if the tank level exceeds the lower and upper reference thresholds;
* manage, again through PLC, a shutter for loading/emptying silos; 
* send data to cloud, through a gateway, handling situations of absence or loss of internet connectivity, and showing data trends in graphical form with a web page.

## What we did
We have developed a solution that consists of three main modules:
* REST API: it is a Django application that allows you to manage the database and run the simulators.
* Simulator: it is a python script that simulates the data sent by the sensors.
* Ingester: it is a python script that subscribes to the MQTT broker and saves the data in the influxdb database.

All the modules work autonomously and communicate with each other through the MQTT protocol. In this way, it is possible to simulate the data and send them to the database without having to use the PLC.

## How to start the project
To start the project you need to have docker and docker-compose installed on your machine.
Then you need to run `docker-compose --env-file .env up --build`
