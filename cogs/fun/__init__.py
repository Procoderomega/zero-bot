from .pong import pong
from .saludo import Saludo

async def setup(bot):
    await bot.add_cog(pong(bot))
    await bot.add_cog(Saludo(bot))