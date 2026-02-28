import discord
from discord.ext import commands

#TODO: 


class KickUser(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="kick")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"User: {member.mention} ah sido expulsado ✅")

async def setup(bot):
    await bot.add_cog(KickUser(bot))