from discord.ext import commands
from discord import Server, ChannelType, Client, Channel, Role, HTTPException

from discord.utils import get
from asyncio import sleep

from checks import get_content_from_ctx, group_exists_check


class GroupInfo:
    def __init__(self):
        self.text = None
        self.voice = None
        self.role = None
        self.server = None
        self.can_delete = False


class Commands:
    def __init__(self, bot):
        self.bot = bot
        self.groups = []
        self.bot.loop.create_task(self.updateTask())

    async def updateTask(self):
        while not self.bot.is_closed:
            for group in self.groups:
                remove = False
                try:
                    channel = get(group.server.channels, id=group.voice.id)
                    remove = len(channel.voice_members) == 0
                except:
                    pass
                if remove:
                    self.groups.remove(group)
                    await remove_groupinfo(self.bot, group)
            await sleep(5)

    @commands.group(name='group')
    async def group(self):
        pass

    @group.command(pass_context=True, no_pm=True)
    @group_exists_check()
    async def create(self, ctx):
        name = get_content_from_ctx(ctx)
        author = ctx.message.author
        server = author.server
        group = await create_groupinfo(self.bot, server, name)
        self.groups.append(group)
        await self.bot.add_roles(author, group.role)
        channel = get(group.server.channels, id=group.voice.id)
        await self.bot.move_member(author, channel)
        group.can_delete = True


async def create_role(client: Client, server: Server, name: str):
    return await client.create_role(server, name=name)


async def create_channel(client: Client, server: Server, name: str, is_voice: bool = False):
    channel_type = ChannelType.text
    if is_voice:
        channel_type = ChannelType.voice
    else:
        name = name.replace(' ', '_')
    return await client.create_channel(server, name, type=channel_type)


async def remove_role(client: Client, server: Server, role: Role):
    await client.delete_role(server, get(server.roles, id=role.id))


async def remove_channel(client: Client, server: Server, channel: Channel):
    await client.delete_channel(get(server.channels, id=channel.id))


# Creates a group, if an error occurs preventing
async def create_groupinfo(client: Client, server: Server, name: str):
    info = GroupInfo()
    info.server = server
    name = name.strip()
    try:
        info.text = await create_channel(client, server, name)
        info.voice = await create_channel(client, server, name, True)
        info.role = await create_role(client, server, name)
    except HTTPException as e:
        try:
            remove_groupinfo(client, info)
        except Exception as ie:
            print(repr(ie))
            pass
        raise e
    return info


# Removes text, voice and role from the group info
async def remove_groupinfo(client: Client, info: GroupInfo):
    if info.text:
        await remove_channel(client, info.server, info.text)
    if info.voice:
        await remove_channel(client, info.server, info.voice)
    if info.role:
        await remove_role(client, info.server, info.role)
