import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import asyncio

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
PREFIX = os.getenv("PREFIX", "--")

intents = discord.Intents.default()
intents.message_content = True  #* Privileged Intent, activar en portal Discord

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} Sirviendo...")

async def main():
    await bot.load_extension("cogs.moderation")
    await bot.load_extension("cogs.fun")    
    await bot.start(TOKEN)

if __name__ == "__main__":
    asyncio.run(main())