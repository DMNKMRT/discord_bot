import discord
from discord.ext import commands

import json

# config aus der json datei holen
config = json.load(open('config.json'))


# client erstellen für die Discord connection
client = discord.ext.commands.Bot(command_prefix="$")








# Das ist damit der Bot startet, wenn das ausgeführt wird
client.run(config["TOKEN"])
