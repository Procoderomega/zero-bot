from discord.ext import commands

class Saludo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="saludo")
    async def Saludo(self, ctx):
        await ctx.send("Hola, como estas?")

async def setup(bot):
    await bot.add_cog(Saludo(bot))