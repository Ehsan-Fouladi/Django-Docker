from datetime import datetime
from django.http import JsonResponse
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# You can generate an API token from the "API Tokens Tab" in the UI
token = "tdNiKj7JYgPqIQ5QMLuzLCS3twkE0kCwv4c3h5DHFtzGpYlIy3S6p9NlCi6oAbOPIlSJ4NcCozvOjPOWREUCeg=="
org = "Ehsan"
bucket = "Fouladi"

with InfluxDBClient(url="http://localhost:8086", token=token, org=org) as client:
	write_api = client.write_api(write_options=SYNCHRONOUS)
	data = "mem,host=host1 used_percent=129.43234543"
	write_api.write(bucket, org, data)


def get_data(request):
    query_api = client.query_api()
    result = query_api.query_csv('from(bucket:"Fouladi") |> range(start: -10m)')
    return JSONResponse(result)
