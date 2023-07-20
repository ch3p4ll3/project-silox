# Database

Considering the data we are going to save will be temporal data, we used two databases:
- **Postgresql**: for static data such as silo, liquids, sensors, etc.
- **Influxdb**: for data that comes to us directly from sensors in real time and that we will use to make graphs and statistics.
