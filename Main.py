import discord
from discord.ext import commands
from botconfig import TOKEN, PREFIX
import asyncio

intents = discord.Intents.default()
intents.message_content = True  # Privileged Intent, activar en portal Discord

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} Sirviendo...")

async def main():
    # Cargar cogs correctamente
    await bot.load_extension("cogs.fun")
    await bot.start(TOKEN)  # token seguro desde .env

if __name__ == "__main__":
    asyncio.run(main())
