from discord.ext import commands
import discord

class UnmuteUser(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def unmute(self, ctx, member: discord.Member, *, reason=None):
        muted__role = discord.utils.get(ctx.guild.roles, name="Muted role")
        if not muted__role:
            return await ctx.send("No existe un rol llamado 'Muted role', porfavor crealo. 😢")
    
        try:
            await member.remove_roles(muted__role, reason=reason)
            await ctx.send(f"{member.mention} ha sido desmuteado correctamente ✅!")
        except discord.Forbidden:
            await ctx.send("No tengo suficientes permisos para mutear ❌")
        except discord.HTTPException:
            await ctx.send("Un error inesperado ocurrio ❌")
            
async def setup(bot):
    await bot.add_cog(UnmuteUser(bot))