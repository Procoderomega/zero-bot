from discord.ext import commands
from discord import app_commands
import discord

class pong(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="ping")
    async def ping(self, ctx):
        await ctx.send("Pong!")
        
    @app_commands.command(name="ping", description="el bot responde 'pong'")
    async def ping_slash(self, interaction: discord.Interaction):
        await interaction.response.send_message("Pong!")
        
async def setup(bot):
    await bot.add_cog(pong(bot))