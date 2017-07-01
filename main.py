from discord.ext import commands

from bot import Commands, run_timer

bot = commands.Bot(command_prefix=commands.when_mentioned_or('='), description='Techraptor Control Bot')


@bot.event
async def on_ready():
    run_timer()
    print('Logged in as: {0} (ID: {0.id})'.format(bot.user))


bot.add_cog(Commands(bot))
bot.run('')
