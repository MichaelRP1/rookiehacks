import discord
import json
from geocode import geocode

client = discord.Client()

@client.event
async def on_ready():
    print('Logged on as {0.user}!'.format(client))
    print(f'In {len(client.guilds)} guilds!')
    await client.change_presence(activity=discord.Game(name='MLH RookieHacks'))

@client.event    
async def on_message(message):
    print(message.content)
    if message.content.startswith("!location"):
        client_location = message.content[len("!location") +1 :]
        location = get_gridpoints(client_location)
        channel = client.get_channel(message.channel.id)
        await channel.send(location)
    if message.content.startswith("!shutdown"):
        await client.logout()

token = ""
with open('creds.json') as json_file:
    data = json.load(json_file)
    token = data['token']

client.run(token)