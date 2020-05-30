# Unofficial NWS Discord Bot
Gathers information from the National Weather Service in the United States and relays back in Discord using embeds.
This bot was made for the [Major League Hacking (MLH) RookieHacks Event](https://organize.mlh.io/participants/events/3468-rookiehacks) spanning from 05/29/2020 to 05/31/2020

Allows you to quicly and easily view the weather forcast and active alerts for a location. 

**Please Visit https://weather.gov for official information from the National Weather Service**

## Features and Commands
- !alerts (location) - Returns first five alerts for a specified area
- !areas - Returns list of areas for !alerts command
- !coords (location) - Returns coorditates, NWS gridpoint, and NWS office for a specified location
- !forecast (location) - Returns forecast for next ~36 hours for a specified location
- !hourly (forecast) - Returns hourly forecast for next ~4 hours for a specified location
- !info - Returns list of information about bot and dependencies

## How to Install / Use
- Clone the repository using ``git clone https://github.com/MichaelRP1/rookiehacks``
- Create a Discord application [here](https://discord.com/developers/applications)
- Create a ``creds.json`` file using the ``creds_template.json`` file as a template and place your Discord app token in the ``token`` field.
- Run ``python discordbot.py``

## Built With
- Python
- [Discord.py](https://github.com/Rapptz/discord.py)
- [GeoPy Geocoder](https://github.com/DenisCarriere/geocoder)
- [National Weather Service API](https://api.weather.gov/)
- [Nominatim API](https://nominatim.org/)

## GitHub Link and License
[GitHub](https://github.com/MichaelRP1/rookiehacks)
[BSD-3-Clause License](https://github.com/MichaelRP1/rookiehacks/LICENSE)
