from discord.ext import commands
from discord.ext.commands import Cog

class HelloCommand(Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hello")

def setup(bot):
    bot.add_cog(HelloCommand(bot))