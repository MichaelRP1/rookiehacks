import discord
import json
from geocode import get_gridpoints
from geocode import getForecast

client = discord.Client()

@client.event
async def on_ready():
    print('Logged on as {0.user} '.format(client), end='')
    print(f'in {len(client.guilds)} guilds!')
    await client.change_presence(activity=discord.Activity(name='National Weather Service', type=discord.ActivityType.watching))

@client.event    
async def on_message(message):
    if message.content.startswith("!coords"):
        client_location = message.content[len("!coords") +1 :]
        location = get_gridpoints(client_location)
        channel = client.get_channel(message.channel.id)
        await channel.send(location)
    if message.content.startswith("!forecast"):
        client_location = message.content[len("!forecast") +1 :]
        channel = client.get_channel(message.channel.id)
        wait = await channel.send("Please wait, fetching data")
        forecast = getForecast(client_location)
        await wait.delete()
        if forecast == None:
            await channel.send("Please input a correct location")
        else:    
            i = 0
            for data in forecast:
                if i > 2:
                    break
                await forecastEmbed(channel, client_location, data)
                i = i+1
    if message.content.startswith("!shutdown"):
        await client.logout()

# "Weather: " + data['shortForecast'] + "\nTemperature: " + str(data['temperature']) + " °F\nWind: " + data['windSpeed'] + " " + data['windDirection']
@client.event
async def forecastEmbed(channel, location, data):
    embed = discord.Embed(
        title = data['name'],
        description = "Forecast for " + location,
        colour = 0x4285F4
    )
    embed.set_thumbnail(url=data['icon'])
    embed.set_footer(text="Unofficial National Weather Service")
    embed.add_field(name="Weather", value=data['shortForecast'], inline=False)
    embed.add_field(name="Temperature", value=str(data['temperature']) + " °F", inline=False)
    embed.add_field(name="Wind", value=data['windSpeed'] + " " + data['windDirection'], inline=False)
    await channel.send(embed=embed)

token = ""
with open('creds.json') as json_file:
    data = json.load(json_file)
    token = data['token']

client.run(token)