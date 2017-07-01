from discord.ext import commands
from discord import Server, ChannelType, Client, Channel,Role

from discord.utils import get

class GroupInfo:
    def __init__(self):
        self.text = None
        self.voice = None
        self.role = None      

class Commands:
    

    def __init__(self, bot):
        self.bot = bot
        self.groups = []

    @commands.group(name='group')
    async def group(self):
        pass

    @group.command(pass_context=True, no_pm=True)
    async def create(self, ctx, name):
        author = ctx.message.author
        server = author.server
        group = await create_groupinfo(self.bot,server,name)
        self.groups.append(group)
        await self.bot.add_roles(author, group.role)
        await self.bot.move_member(author, group.voice)

async def create_role(client: Client, server: Server, name: str):
    return await client.create_role(server, name = name)


async def create_channel(client: Client, server: Server, name: str, is_voice: bool=False):
    channel_type = ChannelType.text
    if is_voice:
        channel_type = ChannelType.voice
    return await client.create_channel(server, name, type=channel_type)

async def remove_role(client: Client, server:Server, role:Role):
    await client.delete_role(server,get(server.roles,id=role.id))

async def remove_channel(client: Client, server:Server, channel:Channel):
    await client.delete_channel(get(server.channels,id=channel.id))
    
async def create_groupinfo(client:Client,server:Server,name:str):
    info = GroupInfo()
    info.text = await create_channel(client,server,name)
    info.voice = await create_channel(client,server,name,True)
    info.role = await create_role(client,server,name)
    return info

async def remove_groupinfo(client:Client,server:Server,info:GroupInfo):
    await remove_channel(client,server,info.text)
    await remove_channel(client,server,info.voice)
    await remove_role(client,server,info.role)
