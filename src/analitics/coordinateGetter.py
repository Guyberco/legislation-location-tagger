from geopy.geocoders import Nominatim

def getCoordinates(location):
    geolocator = Nominatim(user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36")
    location = geolocator.geocode(location)
    if not location == None:
        return [location.longitude, location.latitude]
    else:
        return None
