import json

from src.analytics.coordinateGetter import getCoordinates, locactionToCordinated
from src.analytics.locationsCollector import locationsMap

geoJSON = {
    "type": "FeatureCollection",
    "features": []
}


# 
locationToHref = json.load(open('locationToHref.json', 'r', encoding='UTF-8'))

def buildGeoJson():
    with open('locationsMap.json', 'r', encoding='UTF-8') as json_file:
        locationsMapJson = json.load(json_file)
        features = list(map(buildLocationFeature, locationsMapJson.keys()))
        geoJSON.update({"features": list(filter(lambda feature: feature is not None, features))})
        with open('geoJsonResult.json', 'w', encoding='UTF-8') as file:
            json.dump(geoJSON, file)
        with open('locactionToCordinated.json', 'w', encoding='UTF-8') as file:
            json.dump(locactionToCordinated, file)


def buildLocationFeature(location):
    coordinates = getCoordinates(location)
    locationHref = locationToHref.get(location)
    if coordinates is not None:
        laws = locationsMap.get(location)
        lawNames = list(map(lambda law: law["name"], laws))
        properties = {
            "marker-color": "#1c26b5" if location == "ישראל" else getColorByNumer(len(laws)),
            "Location": location,
            "DBpedia Link": locationHref or ""
        }

        if location == "ישראל":
            properties.update({"marker-symbol": "religious-jewish"})

        for i, lawName in enumerate(lawNames):
            properties.update({f" {i + 1}": lawName})
        coordinates = getCoordinates(location)

        return {
            "type": "Feature",
            "properties": properties,
            "geometry": {
                "type": "Point",
                "coordinates": coordinates
            }
        }
    else:
        return None

def getColorByNumer(number):
    if 0 < number <= 1:
        return '#607d8b'
    elif 1 < number <= 3:
        return '#ffe52e'
    elif 3 < number <= 6:
        return '#ffbe5d'
    elif 6 < number <= 10:
        return '#dc8300'
    elif 10 < number <= 30:
        return '#f38080'
    else:
        return '#b71c1c'

# with open('locationsMap.json', 'r', encoding='UTF-8') as json_file:
#     geoJsonResult = json.load(json_file)
#     for key in geoJsonResult.keys():
#         print(len(geoJsonResult.get(key)))

buildGeoJson()
