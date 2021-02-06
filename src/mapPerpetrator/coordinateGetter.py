from geopy.geocoders import Nominatim

def getCoordinates(location):
    geolocator = Nominatim(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36")
    location = geolocator.geocode(location)
    if not location == None:
        return [location.longitude, location.latitude]
    else:
        return None
