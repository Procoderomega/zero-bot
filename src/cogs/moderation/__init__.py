from .kick import KickUser  
from .clear import clearMessages
from .ban import BanUser

async def setup(bot):
    await bot.add_cog(KickUser(bot))
    await bot.add_cog(clearMessages(bot))
    await bot.add_cog(BanUser(bot))