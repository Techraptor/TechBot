from discord.ext import commands
from discord import Server, ChannelType, Client
from discord.utils import get


class Commands:
    def __init__(self, bot):
        self.bot = bot
        self.roles = []
        self.channels = {'text': [], 'voice': []}

    @commands.group(name='group')
    async def group(self):
        pass

    @group.command(pass_context=True, no_pm=True)
    async def create(self, ctx, name):
        role = await create_role(self.bot, ctx.message.author.server, name)
        await self.bot.add_roles(ctx.message.author, role)  # add role to user
        self.roles.append(role)  # add role to cache

        self.channels['text'].append(await create_channel(self.bot, ctx.message.author.server, name))

        v_channel = await create_channel(self.bot, ctx.message.author.server, name, True)
        await self.bot.move_member(ctx.message.author, v_channel)  # move user to channel
        self.channels['voice'].append(v_channel)  # add role to cache


async def create_role(client: Client, server: Server, name: str):
    uncached = await client.create_role(server, name=name)
    return get(server.roles, id=uncached.id)


async def create_channel(client: Client, server: Server, name: str, is_voice: bool = False):
    channel_type = ChannelType.text
    if is_voice:
        channel_type = ChannelType.voice
    uncached = await client.create_channel(server, name, type=channel_type)
    return server.get_channel(uncached.id)  # returns cached channel
