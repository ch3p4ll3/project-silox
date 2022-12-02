import math

import influxdb_client
import os
from statistics import mean

from influxdb_client import WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS


class InfluxDb:
    def __init__(self) -> None:
        self.__org = "org"
        self.__bucket = "silos"
        self.__token = os.environ.get("INFLUXDB_TOKEN")
        # Store the URL of your InfluxDB instance
        self.__url = "http://influxdb:8086"

        self.client = influxdb_client.InfluxDBClient(
            url=self.__url,
            token=self.__token,
            org=self.__org
        )

    def write(self, data, silos_heigth: float) -> None:
        write_api = self.client.write_api(write_options=SYNCHRONOUS)

        time = data.pop('time')
        silos_id = data.pop('id')

        for key in data:
            if "sensor_" in key:
                data[key] = silos_heigth - data[key]

        for key, value in data.items():
            p = influxdb_client.Point(f"silos#{silos_id}")\
                .field(key, value)\
                .time(time, WritePrecision.NS)
            write_api.write(bucket=self.__bucket, org=self.__org, record=p)

    def read(self, silos, last=False):
        query_api = self.client.query_api()
        query = f"""from (bucket:"{self.__bucket}")
  |> range(start: -7d)
  |> filter(fn: (r) => r["_measurement"] == "silos#{silos.id}")
  |> filter(fn: (r) => r["_field"] == "ext_humidity" or r["_field"] == "ext_temp" or \
  r["_field"] == "sensor_1" or r["_field"] == "sensor_2" or r["_field"] == "sensor_3" or \
  r["_field"] == "temp" or r["_field"] == "ph" or r["_field"] == "int_temp" or \
  r["_field"] == "int_pression" or r["_field"] == "int_humidity")
"""

        if last:
            query += "\n  |> last()"

        else:
            query += """  |> sort(columns: ["_time"], desc: true)
  |> limit(n:10, offset:10)"""

        result = query_api.query(org=self.__org, query=query)
        raw_results = {}
        for table in result:
            for record in table.records:
                time_stamp = str(record.get_time().timestamp())
                if raw_results.get(time_stamp) is None:
                    raw_results[time_stamp] = {}

                raw_results[time_stamp][record.get_field()] = record.get_value()

        results = self.__parse_data(raw_results, silos)

        if last:
            try:
                return results[0]
            except IndexError:
                return ''

        return {"measurements": results}

    def __parse_data(self, raw_results: dict, silos):
        results = []
        for key in raw_results:
            raw_results[key]['time'] = key

            sensors = [raw_results[key][i] for i in raw_results[key] if i.startswith('sensor')]  # calc silos level
            raw_results[key]['level'] = mean(sensors)
            raw_results[key]['level_percentage'] = (mean(sensors) / silos.height) * 100

            volume = math.pi * (silos.diameter / 2) ** 2 * mean(sensors)
            raw_results[key]['volume'] = volume
            raw_results[key]['weight'] = volume * silos.liquid.density

            results.append(raw_results[key])

        return results

    def __exit__(self):
        self.client.close()
