from discord.ext import commands

from main import bot


@bot.event
async def on_ready():
    print('Logged in as: {0} (ID: {0.id})'.format(bot.user))


class Commands:
    def __init__(self, bot):
        self.bot = bot

    @commands.group(name='group')
    async def group(self):
        pass

    @group.command(pass_context=True, no_pm=False)
    async def create(self, ctx):
        pass
