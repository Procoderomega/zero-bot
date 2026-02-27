from discord.ext import commands
import random

class Status_Shower(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=["status"])
    async def estado(self, ctx):
        estado = random.choice(["Feliz 😀","Triste 😢","Neutral 😐"])
        await ctx.send(f'Actualmente estoy {estado}!')

async def setup(bot):
    await bot.add_cog(Status_Shower(bot))
        