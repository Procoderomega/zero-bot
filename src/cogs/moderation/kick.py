import discord
from discord.ext import commands

class KickUser(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="kick")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        try:
            await member.kick(reason=reason)
            await ctx.send(f"User: {member.mention} ah sido expulsado ✅")
        except discord.Forbidden:
            await ctx.send("No tengo permisos suficientes ❌")
        except discord.HTTPException:
            await ctx.send("Ocurrio un error inesperado ❌")
        except Exception as e:
            await ctx.send(f"Ocurrio un error inesperado: {e}")
        

async def setup(bot):
    await bot.add_cog(KickUser(bot))