import json
import discord
import requests

def geocode(client_location):
    location = requests.get("https://nominatim.openstreetmap.org/search/{0}?format=json&accept-language=en-US&countrycodes=us&limit=1".format(client_location))