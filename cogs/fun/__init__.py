from .pong import pong
from .saludo import Saludo
from .estado import Status_Shower
from .diceroll import DiceRoll

async def setup(bot):
    await bot.add_cog(pong(bot))
    await bot.add_cog(Saludo(bot))
    await bot.add_cog(Status_Shower(bot))
    await bot.add_cog(DiceRoll(bot))