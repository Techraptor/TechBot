from discord.ext import commands

from main import bot
from discord import Server, Role


@bot.event
async def on_ready():
    print('Logged in as: {0} (ID: {0.id})'.format(bot.user))


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


def create_role(server: Server, name: str):
    def get_id():
        id = 4
        flag = True
        while flag:
            flag = False
            for role in server.roles:
                if not flag and role.id == id:
                    flag = True
                    id += 1

    args = {'id': get_id(), 'server': server, 'name': name}

    return Role(**args)


def create_channel(server: Server, name: str, isVoice: bool):
    return None
