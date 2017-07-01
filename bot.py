from discord.ext import commands
from discord import Server, Role, ChannelType, Channel, Client


class Commands:
    def __init__(self, bot):
        self.bot = bot
        self.roles = []
        self.channels = {'text': [], 'voice': []}

    @commands.group(name='group')
    async def group(self):
        pass

    @group.command(pass_context=True, no_pm=False)
    async def create(self, ctx, name):
        self.roles += await create_role(self.bot, ctx.message.author.server, name)
        self.channels['text'] += await create_channel(self.bot, ctx.message.author.server, name)
        self.channels['voice'] += await create_channel(self.bot, ctx.message.author.server, name, True)


async def create_role(client:Client, server: Server, name: str):
    uncached = await client.create_role(server,{'name':name})
    return server.roles.get(uncached.id)#returns cached role

async def create_channel(server: Server, name: str, is_voice: bool=False):
    
    channel_type = ChannelType.text
    if is_voice:
        channel_type = ChannelType.voice
    uncached = await client.create_channel(server,name,type=channel_type)
    return server.get_channel(uncached.id)#returns cached channel

