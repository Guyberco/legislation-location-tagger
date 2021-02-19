import json

from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

locactionToCordinated = {}

def getCoordinates(location):
    cordintates = locactionToCordinated.get(location)

    if locactionToCordinated.get(location) is None:
        geolocator = Nominatim(user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36")
        googleCordeinated = None
        while True:
            try:
                googleCordeinated = geolocator.geocode(location, timeout=10)
                break
            except GeocoderTimedOut:
                print(f"trying again for {location}")
        if not googleCordeinated == None:
            longitudeLatitude = [googleCordeinated.longitude, googleCordeinated.latitude]
            print(location, longitudeLatitude)
            locactionToCordinated.update({location: longitudeLatitude})
            return longitudeLatitude
        else:
            return None
    else:
        return cordintates

# with open('locationsMap.json', 'r', encoding='UTF-8') as json_file:
#     geoJsonResult = json.load(json_file)
#     for key in geoJsonResult.keys():
#         print(len(geoJsonResult.get(key)))