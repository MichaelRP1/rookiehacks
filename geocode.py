import json
import discord
import requests
from geopy.geocoders import Nominatim
from noaa_sdk import noaa as nws

noaa = nws.NOAA()

points_headers = {
    'User-Agent': 'MLH RookieHacks Test Application. Used for Discord bot using Discord.py',
    'Accept': 'application/ld+json'
}

def geocode(client_location):
    geolocator = Nominatim(user_agent="MLH RookieHacks Test Application")
    location = geolocator.geocode(client_location)
    loc = [location.latitude, location.longitude]
    return loc

def get_gridpoints(location):
    client_location = geocode(location)
    points = requests.get("https://api.weather.gov/points/{0.lat},{0.lon}".format(client_location), headers=points_headers)
    print(points)

def getForecast(location):
    client_location = geocode(location)
    lat, lon = client_location
    forecast = noaa.points_forecast(lat, lon, hourly=False)
    print(forecast)

