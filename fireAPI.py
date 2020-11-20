import requests
import config

API_KEY = config.fireAPIKey
radius = 50
latitude = 37.842447
longitude = -119.518259
response = requests.get(
    "https: // api.breezometer.com/fires/v1/current-conditions?lat={latitude} & lon={longitude} & key=API_KEY & radius={radius}")

data = response.json()

datetime = data
