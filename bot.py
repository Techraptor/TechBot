from discord.ext import commands

from main import bot
from discord import Server, Role, Channel

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
    
    def createRole(server:Server,name:str):
        def getId():
            id = 4;
            flag = True;
            while flag:
                flag = False;
                for role in server.roles:
                    if(not flag and role.id == id):
                        flag = True
                        id += 1
                    
        args = {}
        args['id'] = getId()
        args['server']  = server
        args['name'] = name

        return Role(args);

    def createChannel(server:Server,name:str,isVoice:bool):
        return None
