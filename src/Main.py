import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import asyncio

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
PREFIX = os.getenv("PREFIX", "--")
GUILD_ID = int(os.getenv("GUILD_ID"))

intents = discord.Intents.default()
intents.message_content = True

class MyBot(commands.Bot):
    async def setup_hook(self):
        # Cargar cogs
        await self.load_extension("cogs.moderation")
        await self.load_extension("cogs.fun")

        # Sincronización rápida solo en tu servidor de desarrollo
        guild = discord.Object(id=GUILD_ID)
        self.tree.copy_global_to(guild=guild)
        await self.tree.sync(guild=guild)
        print("Slash commands sincronizados en desarrollo ⚡")


bot = MyBot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} Sirviendo...")

if __name__ == "__main__":
    bot.run(TOKEN)
