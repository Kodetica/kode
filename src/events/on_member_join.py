from discord.ext.commands import Cog

class OnJoin(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_member_join(self, member):
        pass

def setup(bot):
    bot.add_cog(OnJoin(bot))