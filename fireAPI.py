import requests

API_KEY = "1e0a4116590044779598024a9a205866"
radius = 50
latitude = 37.842447
longitude = -119.518259
response = requests.get(
    "https: // api.breezometer.com/fires/v1/current-conditions?lat={latitude} & lon={longitude} & key=API_KEY & radius={radius}")
