from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def kick(self, ctx, member: commands.MemberConverter, *, reason=None):
        #// Expulsa a un usuario del servidor
        await member.kick(reason=reason)
        await ctx.send(f"{member.name} ha sido expulsado. 🔨")

    @commands.command()
    async def ban(self, ctx, member: commands.MemberConverter, *, reason=None):
        #// Banea a un usuario del servidor
        await member.ban(reason=reason)
        await ctx.send(f"{member.name} ha sido baneado. 🚫")

async def setup(bot):
    await bot.add_cog(Moderation(bot))
