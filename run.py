import os
import discord
from dotenv import load_dotenv
from src import Main

if __name__ == "__main__":
    load_dotenv() # Carga el archivo dotenv
    intents = discord.Intents(guilds=True,
    messages=True, presences=True, members=True)
    bot = Main(os.environ.get("PREFIX"), intents) # Instancia la clase Main, recibe una string a modo de prefix
    bot.load_commands() # Carga los comandos
    bot.load_events() # Carga los eventos
    bot.run(os.environ.get("TOKEN")) # Conecta el bot