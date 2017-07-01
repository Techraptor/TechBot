from discord.ext import commands
from discord import Server, ChannelType, Client


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
        await self.bot.add_roles(ctx.message.author, [role])  # add role to user
        self.roles += role  # add role to cache

        self.channels['text'] += await create_channel(self.bot, ctx.message.author.server, name)

        vChannel = await create_channel(self.bot, ctx.message.author.server, name, True)
        await self.bot.move_member(ctx.message.author, vChannel)  # move user to channel
        self.channels['voice'] += vChannel  # add role to cache


async def create_role(client: Client, server: Server, name: str):
    uncached = await client.create_role(server, name=name)
    return [r for r in server.roles if r.id == uncached.id][0]  # returns cached role


async def create_channel(client: Client, server: Server, name: str, is_voice: bool = False):
    channel_type = ChannelType.text
    if is_voice:
        channel_type = ChannelType.voice
    uncached = await client.create_channel(server, name, type=channel_type)
    return server.get_channel(uncached.id)  # returns cached channel
