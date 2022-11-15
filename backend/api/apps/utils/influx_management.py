import influxdb_client
import os

from influxdb_client import WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS


class InfluxDb:
    def __init__(self) -> None:
        self.__org = "org"
        self.__bucket = "silos"
        self.__token = os.environ.get("INFLUXDB_TOKEN")
        # Store the URL of your InfluxDB instance
        self.__url = "http://localhost:8086"

        self.client = influxdb_client.InfluxDBClient(
            url=self.__url,
            token=self.__token,
            org=self.__org
        )

    def write(self, data) -> None:
        write_api = self.client.write_api(write_options=SYNCHRONOUS)

        time = data.pop('time')
        silos_id = data.pop('id')

        for key, value in data.items():
            p = influxdb_client.Point(f"silos#{silos_id}")\
                .field(key, value)\
                .time(time, WritePrecision.NS)
            write_api.write(bucket=self.__bucket, org=self.__org, record=p)

    def read(self, silos_id, last=False):
        query_api = self.client.query_api()
        query = f"""from (bucket:"{self.__bucket}")
  |> range(start: -60m)
  |> filter(fn: (r) => r["_measurement"] == "silos#{silos_id}")
  |> filter(fn: (r) => r["_field"] == "ext_humidity" or r["_field"] == "ext_temp" or \
  r["_field"] == "sensor_1" or r["_field"] == "sensor_2" or r["_field"] == "sensor_3" or \
  r["_field"] == "temp" or r["_field"] == "ph" or r["_field"] == "int_temp" or \
  r["_field"] == "int_pression" or r["_field"] == "int_humidity")"""

        if last:
            query += "\n  |> last()"

        result = query_api.query(org=self.__org, query=query)
        results = {}
        for table in result:
            for record in table.records:
                time_stamp = str(record.get_time().timestamp())
                if results.get(time_stamp) is None:
                    results[time_stamp] = {}

                results[time_stamp][record.get_field()] = record.get_value()

        return results

    def __exit__(self):
        self.client.close()
