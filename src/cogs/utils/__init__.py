from .info import HelpCog

async def setup(bot):
    await bot.add_cog(HelpCog(bot))