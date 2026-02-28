from discord.ext import commands
import discord

class BanUser(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        try:
            await member.ban(reason=reason)
            await ctx.send(f"User: {member.mention} ah sido baneado ✅")
            
            #~ Manejo de errores - Error handling ~#
            
        except discord.Forbidden:
            await ctx.send("Error: no tengo permisos suficientes ❌")
        except discord.HTTPException:
            await ctx.send("Ocurrio un error al intentar banear al usuario ❌")
        except Exception as E:
            await ctx.send(f"Ocurrio un error inesperado: {E}")        
        
async def setup(bot):
    await bot.add_cog(BanUser(bot))