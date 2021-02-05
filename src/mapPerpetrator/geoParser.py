import json

from src.mapPerpetrator.coordinateGetter import getCoordinates
from src.mapPerpetrator.locationsCollector import locationsMap, extractDataFromAllLaws

geoJSON = {
    "type": "FeatureCollection",
    "features": []
}


def buildGeoJson():
    extractDataFromAllLaws()
    features = list(map(buildLocationFeature, locationsMap.keys()))
    geoJSON.update({"features": list(filter(lambda feature: feature is not None, features))})
    with open('result.json', 'w', encoding='UTF-8') as file:
        json.dump(geoJSON, file)


def buildLocationFeature(location):
    coordinates = getCoordinates(location)
    if coordinates is not None:
        laws = locationsMap.get(location)
        lawNames = list(map(lambda law: law["name"], laws))
        properties = {
            "marker-color": getColorByNumer(len(laws)),
            "Location": location
        }
        for i, lawName in enumerate(lawNames):
            properties.update({f"Law {i + 1}": lawName})
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
    elif 20 < number <= 2:
        return '#FF9800'
    elif 40 < number <= 3:
        return '#F44336'
    else:
        return '#b71c1c'


buildGeoJson()
