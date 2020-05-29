import json
import discord
import requests
from geopy.geocoders import Nominatim

def geocode(client_location):
    geolocator = Nominatim(user_agent="MLH RookieHacks Test Application")
    location = geolocator.geocode(client_location)
    loc = str(location.latitude) + "," + str(location.longitude)
    return loc

def get_gridpoints(location):
    client_location = geocode(location)
    points = requests.get("https://api.weather.gov/points/{0}".format(client_location))
    print(points)