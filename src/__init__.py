from discord.ext.commands import Bot
from os import listdir

class Main(Bot):
    def __init__(self, prefix, intents, color=0x36393e):
        super().__init__(prefix, intents=intents)
        self.prefix = prefix
        self.color = color

    def load_commands(self):
        for cog in listdir("./src/commands"):
            if cog.endswith(".py"):
                name = cog[:-3]
                super().load_extension(f"src.commands.{name}")
                print(f"[LOG] El comando {name.capitalize()} fue cargado")

    def load_events(self):
        for cog in listdir("./src/events"):
            if cog.endswith(".py"):
                name = cog[:-3]
                super().load_extension(f"src.events.{name}")
                print(f"[LOG] El evento {name} fue cargado")
 