from discord.ext.commands import Cog

class OnReady(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        print(f"¡Conectado!\nTag: {self.bot.user.name}\nPrefijo: {self.bot.prefix}")

def setup(bot):
    bot.add_cog(OnReady(bot))