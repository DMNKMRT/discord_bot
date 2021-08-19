import datetime
import random

import discord
from discord.ext import commands
import discord.ext
import json

import voice_channel_name

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
@client.event
async def on_ready():
    print("Hello, my name is master_mind and im the master_minddddd")
    global log_channel
    log_channel = client.get_channel(int(config["LOG_ID"]))
    global time
    time = datetime.datetime.now().strftime("**%H:%M**\n%d-%B-%Y")


# Das ist die methode für einen willkommenstext,
# wenn ein member joined, bekommt er eine personalisierte Nachricht per DM
@client.event
async def on_member_join(member):
    print(f'{member.name} joined the server and got a welcome message')
    await member.send(f'Hello {member.name}, whats up?!')
    await log_channel.send(f"{member.name} joined the server and got a welcome message from me (me = master_mind)")


# ein command hört auf den voreingestelten Prefix ($)
# Wenn man $check in den Discord server schreibt, wird der print und der send befehl ausgeführt.
@client.command()
async def bot_status(ctx):
    embed = discord.Embed(title=f"{time}", description="master_mind is here bitches")
    await ctx.send(embed=embed)
    print("master_mind is working")
    await log(f"User: {ctx.message.author.name} had asked for the status of the bot", 0x000000)


# command um jemandem eine rolle zu geben
@client.command()
async def add_role(ctx, user: discord.Member, role: discord.Role):
    await user.add_roles(role)
    print(f'User: {user.name}, got the {role.name} role')
    await log(f"User: {user.name},got the role {role.name}", 0xff1100)


# Methode um member zu stummzuschalten im sprachchat
@client.command()
async def mute_member(ctx, user: discord.Member):
    mute_role = ctx.guild.get_role(int(config["MUTE_ROLE"]))
    await user.add_roles(mute_role)
    print(f'User: {user.name}, got muted')
    await log(f"User: {user.name}, got muted by {ctx.message.author.name}", 0xff1100)


# Methode um member zu stummzuschalten im sprachchat
@client.command()
async def unmute_member(ctx, user: discord.Member):
    mute_role = ctx.guild.get_role(int(config["MUTE_ROLE"]))
    await user.remove_roles(mute_role)
    print(f'User: {user.name}, got unmuted')
    await log(f"{user.name}, got unmuted by {ctx.message.author.name}", 0xff1100)


# Methode um einen User zu kicken
@client.command()
async def kick_member(ctx, user: discord.Member):
    if ctx.message.author.guild_permissions.administrator:
        await user.send("You were kicked from the Server - please dont contact the admin")
        print(f'User: {user.name}, got kicked')
        await log(f"{ctx.message.author.name}, have kicked {user.name} ", 0xff1100)
        await user.kick()
    else:
        await ctx.send("you have no permissions for the command")
        # Nachricht in Log channel wird geschrieben
        await log(f"{ctx.message.author.name}, had tried to kick {user.name}", 0xff1100)
        print(f"user: {ctx.message.author.name} had tried to kick {user.name}")


# Methode um einen User zu banen
@client.command()
async def ban_member(ctx, user: discord.Member):
    if ctx.message.author.guild_permissions.administrator:
        await user.send("You were banned from the Server - please dont contact the admin")
        print(f'User: {user.name}, got banned')
        await log(f"{user.name}, got banned by {ctx.message.author.name}", 0xff1100)
        await user.ban()
    else:
        await ctx.send("you have no permissions for this command")
        # Nachricht in Log channel wird geschrieben
        await log(f"{ctx.message.author.name}, had tried to ban {user.name}", 0xff1100)
        print(f"user: {ctx.message.author.name} had tried to ban {user.name}")


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


# create channel methode
@client.event
async def on_voice_state_update(member, before, after):
    if before.channel is not None and before.channel.name != 'Create Channel' and len(before.channel.voice_states) == 0:
        await before.channel.delete()

    if after.channel is not None and after.channel.name == 'Create Channel':
        new_channel = await member.guild.create_voice_channel(random.choice(voice_channel_name.names), category=after.channel.category)
        await member.move_to(new_channel)



# Das ist damit der Bot startet, wenn das ausgeführt wird
client.run(config["TOKEN"])
