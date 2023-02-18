import math

import influxdb_client
import os
from statistics import mean

from influxdb_client import WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS


class InfluxDb:
    def __init__(self) -> None:
        self.__org = os.environ.get("INFLUXDB_ORG")
        self.__bucket = os.environ.get("INFLUXDB_BUCKET")
        self.__token = os.environ.get("INFLUXDB_TOKEN")
        # Store the URL of your InfluxDB instance
        self.__url = "http://localhost:8086"

    def write(self, silos_id: str, slung: str, data: dict) -> None:
        write_api = self.client.write_api(write_options=SYNCHRONOUS)

        """
            {
              "name" : "Level Sensor 2",
              "value" : 10,
              "time" : "2023-02-18T17:57:04.488544"
            }
        """

        time = data.pop('time')
        value = data.pop('value')
        name = data.pop('name')

        p = influxdb_client.Point(silos_id)\
            .field(slung, float(value))\
            .tag('sensor_name', name)\
            .time(time)
        write_api.write(bucket=self.__bucket, org=self.__org, record=p)

    def __enter__(self):
        self.client = influxdb_client.InfluxDBClient(
            url=self.__url,
            token=self.__token,
            org=self.__org
        )

        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        self.client.close()
