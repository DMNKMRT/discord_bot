import discord
from discord.ext import commands

import json

# config aus der json datei holen
config = json.load(open('config.json'))

# Das ist für die member.send methode
intents = discord.Intents.default()
intents.members = True

# client erstellen für die Discord connection
client = discord.ext.commands.Bot(command_prefix="$", intents=intents)

# event: Ein event ist wenn etwas passiert
# on_ready event ist, wenn der Bot bereit ist, also quasi "online" ist


@client.event
async def on_ready():
    print("Hello, my name is master_mind and im the master_minddddd")


# Das ist die methode für einen willkommenstext,
# wenn ein member joined, bekommt er eine personalisierte Nachricht per DM
@client.event
async def on_member_join(member):
    print("test member")
    await member.send(f'Hello {member.name}, whats up?!')


# ein command hört auf den voreingestelten Prefix ($)
# Wenn man $check in den Discord server schreibt, wird der print und der send befehl ausgeführt.
@client.command()
async def check(ctx):
    embed = discord.Embed(title="dominiks embed", description= "master_mind is here bitches")
    print("master_mind is working")
    await ctx.send(embed= embed)


# command um jemandem eine rolle zu geben
@client.command()
async def add_role(ctx, user: discord.Member, role: discord.Role):
    await user.add_roles(role)

# Das ist damit der Bot startet, wenn das ausgeführt wird
client.run(config["TOKEN"])
