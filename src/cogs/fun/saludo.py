from discord.ext import commands
from discord import app_commands
import discord

class Saludo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="saludo")
    async def Saludo(self, ctx):
        await ctx.send("Hola, como estas?")
    
    @app_commands.command(name="saludo", description="El bot saluda")
    async def Saludo_Slash(self, interaction: discord.Interaction):
        await interaction.response.send_message("Hola, como estas?")

async def setup(bot):
    await bot.add_cog(Saludo(bot))