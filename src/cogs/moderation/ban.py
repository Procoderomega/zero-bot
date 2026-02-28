from discord.ext import commands
import discord

class BanUser(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"User: {member.mention} ah sido baneado ✅")
        #! Riesgo: puede fallar por que no valida ni verifica los privilegios de el usuario afectado
        #TODO: Anadir validacion y manejo de errores
        
async def setup(bot):
    await bot.add_cog(BanUser(bot))