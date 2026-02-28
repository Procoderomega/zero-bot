from discord.ext import commands
import random

class DiceRoll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="dice")
    async def roll(self, ctx, arg1: int = 6):
        if arg1 == 0:
            await ctx.send("No puede haber un dado de 0 caras... 😅")
            return
        if arg1 > 9999:
            await ctx.send("Ingrese un valor menor a 9999 😢")
            return
        
        dice_face = random.randint(1, arg1)
        await ctx.send(f'Te ha tocado la cara {dice_face}! 🎲') 

async def setup(bot):
    await bot.add_cog(DiceRoll(bot))