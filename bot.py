#Import modules and connect to Discord
import os
import discord
import random
from dotenv import load_dotenv


# Getting motivational quotes ready
with open("motivation.csv") as motivation:
    quotes = []
    for line in motivation:
        line = line.replace("\n", "")
        line = line.replace('"',"")
        line = line.split("—")
        quotes.append([x.strip() for x in line])




#Getting the token and guild name from the .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv('DISCORD_GUILD')

#https://stackoverflow.com/questions/64231025/discord-py-bot-cant-see-members
intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    
    if message.content.lower() == '!motivation':
        random_quote = random.choice(quotes)
        response = f"{random_quote[0]} - {random_quote[1]}"
        await message.channel.send(response)
        
    elif message.content == 'raise-exception':
        raise discord.DiscordException

client.run(TOKEN)





