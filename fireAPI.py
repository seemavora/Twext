import requests
import json
import config
from opencage.geocoder import OpenCageGeocode


geocoder = OpenCageGeocode(config.geoCodeAPIKey)
query = 'Reno, United States'
results = geocoder.geocode(query)
latitude = results[0]['geometry']['lat']
longitude = results[0]['geometry']['lng']

API_KEY = config.fireAPIKey
radius = 100
URL = "https://api.breezometer.com/fires/v1/current-conditions?lat={latitude}&lon={longitude}&radius={radius}&key={API_KEY}".format(
    latitude=latitude, longitude=longitude, radius=radius, API_KEY=API_KEY)
res = requests.get(URL)


data = res.json()
dataArr = res.json()['data']
fires = res.json()['data']['fires']
statusList = []
namesList = []
datesList = []
distanceList = []
percentContainedList = []


def listsManager():
    i = 0
    while(len(fires) > i):
        if(fires[i]['details'] is not None):
            statusList.append((fires[i]['details']['status']))
            namesList.append((fires[i]['details']['fire_name']))
            datesList.append((fires[i]['details']['time_discovered']))
            distanceList.append((fires[i]['position']['distance']['value']))
            percentContainedList.append(
                (fires[i]['details']['percent_contained']))
        i += 1
    return statusList, namesList, datesList, distanceList, percentContainedList


listsManager()

recentdate = datesList[0]
idx = 0
for a in datesList:
    if(a > recentdate):
        recentdate = a
        idx = datesList.index(a)

# print(statusList)
# print(namesList)
# print(datesList)
# print(distanceList)
# print(percentContainedList)

resultList = [statusList[idx], namesList[idx], datesList[idx],
              distanceList[idx], percentContainedList[idx]]

#print(resultList)
