from discord.ext import commands
import discord
import datetime
import random
import main



class Automod(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Das ist die methode für einen willkommenstext,
    # wenn ein member joined, bekommt er eine personalisierte Nachricht per DM
    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'{member.name} joined the server and got a welcome message')
        await member.send(f'Hello {member.name}, whats up?!')
        await main.log_channel.send(f"{member.name} joined the server and got a welcome message from me (me = master_mind)")

    # ein command hört auf den voreingestelten Prefix ($)
    # Wenn man $check in den Discord server schreibt, wird der print und der send befehl ausgeführt.
    @commands.command()
    async def status(self, ctx):
        embed = discord.Embed(title=f"{main.time}", description="master_mind is here bitches")
        await ctx.send(embed=embed)
        print("master_mind is working")
        await main.log(f"User: {ctx.message.author.name} had asked for the status of the bot", 0x000000)

    # command um jemandem eine rolle zu geben
    @commands.command()
    async def add_role(ctx, user: discord.Member, role: discord.Role):
        await user.add_roles(role)
        print(f'User: {user.name}, got the {role.name} role')
        await main.log(f"User: {user.name},got the role {role.name}", 0xff1100)

    # Methode um member zu stummzuschalten im sprachchat
    @commands.command()
    async def mute_member(ctx, user: discord.Member):
        mute_role = ctx.guild.get_role(int(main.config["MUTE_ROLE"]))
        await user.add_roles(mute_role)
        print(f'User: {user.name}, got muted')
        await main.log(f"User: {user.name}, got muted by {ctx.message.author.name}", 0xff1100)

    # Methode um member zu stummzuschalten im sprachchat
    @commands.command()
    async def unmute_member(ctx, user: discord.Member):
        mute_role = ctx.guild.get_role(int(main.config["MUTE_ROLE"]))
        await user.remove_roles(mute_role)
        print(f'User: {user.name}, got unmuted')
        await main.log(f"{user.name}, got unmuted by {ctx.message.author.name}", 0xff1100)

    # Methode um einen User zu kicken
    @commands.command()
    async def kick_member(ctx, user: discord.Member):
        if ctx.message.author.guild_permissions.administrator:
            await user.send("You were kicked from the Server - please dont contact the admin")
            print(f'User: {user.name}, got kicked')
            await main.log(f"{ctx.message.author.name}, have kicked {user.name} ", 0xff1100)
            await user.kick()
        else:
            await ctx.send("you have no permissions for the command")
            # Nachricht in Log channel wird geschrieben
            await main.log(f"{ctx.message.author.name}, had tried to kick {user.name}", 0xff1100)
            print(f"user: {ctx.message.author.name} had tried to kick {user.name}")

    # Methode um einen User zu banen
    @commands.command()
    async def ban_member(ctx, user: discord.Member):
        if ctx.message.author.guild_permissions.administrator:
            await user.send("You were banned from the Server - please dont contact the admin")
            print(f'User: {user.name}, got banned')
            await main.log(f"{user.name}, got banned by {ctx.message.author.name}", 0xff1100)
            await user.ban()
        else:
            await ctx.send("you have no permissions for this command")
            # Nachricht in Log channel wird geschrieben
            await main.log(f"{ctx.message.author.name}, had tried to ban {user.name}", 0xff1100)
            print(f"user: {ctx.message.author.name} had tried to ban {user.name}")

def setup(client):
    client.add_cog(Automod(client))