from discord.ext import commands

class clearMessages(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        if amount <= 0:
            await ctx.send("Numero invalido ❌")
            return
        if amount > 200:
            await ctx.send("Numero mayor a 200 ❌")
            return
        
        delete = await ctx.channel.purge(limit=amount)
        await ctx.send(f"Se eliminaron {len(delete)} mensajes 🧼", delete_after=5)
        
async def setup(bot):
    await bot.add_cog(clearMessages(bot))