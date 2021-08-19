from discord.ext import commands
import random
import main


def setup(client):
    client.add_cog(Voice_Channel(client))


class Voice_Channel(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.names = ["hallo", "test1", "Dominiks Voice channel", "Jakobs Voices Channel"]

    # create voice channel methode
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if before.channel is not None and before.channel.name != 'Create Channel' and len(
                before.channel.voice_states) == 0:
            await before.channel.delete()

        if after.channel is not None and after.channel.name == 'Create Channel':
            new_channel = await member.guild.create_voice_channel(random.choice(self.names), category=after.channel.category)
            await member.move_to(new_channel)
