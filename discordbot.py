import discord
import json
from geocode import get_gridpoints
from geocode import getForecast

client = discord.Client()

@client.event
async def on_ready():
    print('Logged on as {0.user}!'.format(client))
    print(f'In {len(client.guilds)} guilds!')
    await client.change_presence(activity=discord.Game(name='MLH RookieHacks'))

@client.event    
async def on_message(message):
    print(message.content)
    if message.content.startswith("!coords"):
        client_location = message.content[len("!coords") +1 :]
        location = get_gridpoints(client_location)
        channel = client.get_channel(message.channel.id)
        await channel.send(location)
    if message.content.startswith("!forecast"):
        client_location = message.content[len("!forecast") +1 :]
        forecast = getForecast(client_location)
        channel = client.get_channel(message.channel.id)
        await channel.send(forecast)
    if message.content.startswith("!shutdown"):
        await client.logout()

token = ""
with open('creds.json') as json_file:
    data = json.load(json_file)
    token = data['token']

client.run(token)