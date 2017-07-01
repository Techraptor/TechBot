from discord.ext import commands

from bot import Commands

bot = commands.Bot(command_prefix=commands.when_mentioned_or('='), description='Techraptor Control Bot')

bot.add_cog(Commands(bot))

bot.run('MjQ5NzcxNTIwODI0NTczOTUz.CxLLCA.2BKWURhKHwZPuClpdBGEq1E0vMs')
