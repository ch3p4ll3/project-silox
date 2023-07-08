import math

import influxdb_client
from os import getenv

from influxdb_client.client.write_api import SYNCHRONOUS


class InfluxDb:
    def __init__(self) -> None:
        self.__org = getenv("INFLUXDB_ORG")
        self.__bucket = getenv("INFLUXDB_BUCKET")
        self.__token = getenv("INFLUXDB_TOKEN")
        # Store the URL of your InfluxDB instance
        self.__url = getenv("INFLUXDB_URL")

    def write(self, silos_id: str, slug: str, data: dict) -> None:
        """Write data to InfluxDB"""
        write_api = self.client.write_api(write_options=SYNCHRONOUS)

        """
            {
              "name" : "Level Sensor 2",
              "value" : 10,
              "time" : "2023-02-18T17:57:04.488544"
            }
        """

        time = data.pop('time')
        value = data.pop('value', 0)
        name = data.pop('name')

        # Write data to InfluxDB using the Point structure
        p = influxdb_client.Point(silos_id)\
            .field(slug, float(value))\
            .tag('sensor_name', name)\
            .time(time)
        write_api.write(bucket=self.__bucket, org=self.__org, record=p)

    def __enter__(self):
        """Instantiate a new InfluxDB client instance."""
        self.client = influxdb_client.InfluxDBClient(
            url=self.__url,
            token=self.__token,
            org=self.__org
        )

        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        """Close the client instance."""
        self.client.close()
