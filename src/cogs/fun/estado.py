from discord.ext import commands
import discord
from discord import app_commands
import random

class Status_Shower(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=["status"])
    async def estado(self, ctx):
        estado = random.choice(["Feliz 😀","Triste 😢","Neutral 😐"])
        await ctx.send(f'Actualmente estoy {estado}!')
        
    @app_commands.command(name="estado", description="Muestra el estado emocional del bot")
    async def mostrar_Estado(self, interaction: discord.Interaction):
        estado = random.choice(["Feliz 😀","Triste 😢","Neutral 😐"])
        await interaction.response.send_message(f"Actualmente me siento {estado}!")

async def setup(bot):
    await bot.add_cog(Status_Shower(bot))        