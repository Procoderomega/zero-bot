from .kick import KickUser  
from .clear import clearMessages
from .ban import BanUser
from .mute import MuteUser
from .unmute import UnmuteUser

async def setup(bot):
    await bot.add_cog(KickUser(bot))
    await bot.add_cog(clearMessages(bot))
    await bot.add_cog(BanUser(bot))
    await bot.add_cog(MuteUser(bot))
    await bot.add_cog(UnmuteUser(bot))