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
        self.roles += create_role(ctx.message.author.server, name)
        self.channels['text'] += create_channel(ctx.message.author.server, name)
        self.channels['voice'] += create_channel(ctx.message.author.server, name, True)


async def create_role(client:Client, server: Server, name: str):
    await client.create_role(server,{'name':name})
    #def get_id():
    #    id = 4
    #    flag = True
    #    while flag:
    #        flag = False
    #        for role in server.roles:
    #            if not flag and role.id == id:
    #                flag = True
    #                id += 1

    #args = {'id': get_id(), 'server': server, 'name': name}

    #return Role(**args)
async def create_channel(server: Server, name: str, is_voice: bool=False):
    
    channel_type = ChannelType.text
    if is_voice:
        channel_type = ChannelType.voice
    await client.create_channel(server,name,type=channel_type)
    #def get_id():
    #    id = 4
    #    flag = True
    #    while flag:
    #        flag = False
    #        for channel in server.channel:
    #            if not flag and channel.id == id:
    #                flag = True
    #                id += 1
                        
    #def create_channel_info():
    #    args = {'id': get_id(), 'server': server}

    #    # todo, fix name (lowercase and underscores)
    #    args['name'] = name
    #    args['topic'] = None
    #    args['position'] = -1
    #    if is_voice:
    #        args['bitrate'] = 64
    #        args['type'] = ChannelType.voice
    #    else:
    #        args['bitrate'] = 0
    #        args['type'] = ChannelType.text
    #    args['user_limit'] = 0

    #    return Channel(**args)

