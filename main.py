import discord
from discord.ext import commands

import json

# config aus der json datei holen
config = json.load(open('config.json'))


# client erstellen für die Discord connection
client = discord.ext.commands.Bot(command_prefix="$")

# event: Ein event ist wenn etwas passiert
# on_ready event ist, wenn der Bot bereit ist, also quasi "online" ist

@client.event
async def on_ready():
    print("Hello, my name is master_mind and im the master_minddddd")


# ein command hört auf den voreingestelten Prefix ($)
# Wenn man $check in den Discord server schreibt, wird der print und der send befehl ausgeführt.
@client.command()
async def check(ctx):
    print("master_mind is working")
    await ctx.send("master_mind is here")




# Das ist damit der Bot startet, wenn das ausgeführt wird
client.run(config["TOKEN"])
