import datetime
import random

import discord
from discord.ext import commands
import discord.ext
import json

import voice_channel

# config aus der json datei holen
config = json.load(open('config.json'))

# Das ist für die member.send methode
intents = discord.Intents.default()
intents.members = True

# client erstellen für die Discord connection
client = discord.ext.commands.Bot(command_prefix="$", intents=intents)


# event: Ein event ist wenn etwas passiert
# on_ready event ist, wenn der Bot bereit ist, also quasi "online" ist
# zusätzlich wird eine globale variable erstellt mit dem log_channel
@client.event()
async def on_ready():
    print("Hello, my name is master_mind and im the master_minddddd")
    global log_channel
    log_channel = client.get_channel(int(config["LOG_ID"]))
    global time
    time = datetime.datetime.now().strftime("**%H:%M**\n%d-%B-%Y")

async def log(log_text, log_color):
    log_embed = discord.Embed(title=f"{time}", description=log_text, color=log_color)
    await log_channel.send(embed=log_embed)

@client.command()
async def bot_logout(ctx):
    if ctx.message.author.guild_permissions.administrator:
        await log(f"The bot was logouted by {ctx.message.author.name}", 0xff1100)
        await ctx.send("bye, im going home")
        await client.close()
    else:
        await ctx.send("You dont have the rigth permissions")
        await log(f"{ctx.message.author.name} has tried to logout the bot", 0xff1100)


# Das ist damit der Bot startet, wenn das ausgeführt wird
client.run(config["TOKEN"])
