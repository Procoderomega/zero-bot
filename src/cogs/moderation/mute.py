from discord.ext import commands
from discord import app_commands
from Helpers.Checks import validade_Actions
from typing import Optional
import discord



class MuteUser(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    #* Comando prefijo - Prefix command
    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        err = await validade_Actions(ctx.author, member, "mutear")
        if err:
            return await ctx.send(err)
        
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted role")
        if not muted_role:
            return await ctx.send("No existe un rol llamado 'Muted role', porfavor crealo. 😢")

        try:
            await member.add_roles(muted_role, reason=reason)
            await ctx.send(f'{member.mention} ah sido muteado ✅')
        except discord.Forbidden:
            await ctx.send("No tengo suficientes permisos para mutear ❌")
        except discord.HTTPException:
            await ctx.send("Un error inesperado ocurrio ❌")
    
    #* Comando slash - Slash command
    @app_commands.command(name="mute", description="mutea a un usuario")
    @app_commands.checks.has_permissions(mute_members=True)
    async def mute_slash(self, interaction: discord.Interaction, member: discord.Member, reason: Optional[str]=None):
        err = await validade_Actions(interaction.user, member, "mutear")
        if err:
            return await interaction.response.send_message(err)
        
        muted_role = discord.utils.get(interaction.guild.roles, name="Muted role")
        if not muted_role:
            return await interaction.response.send_message("No existe un rol llamado 'Muted role', porfavor crealo. 😢")
        try:
            await member.add_roles(muted_role, reason=reason)
            await interaction.response.send_message(f'{member.mention} ah sido muteado ✅')
        except discord.Forbidden:
            await interaction.response.send_message("No tengo suficientes permisos para mutear ❌")
        except discord.HTTPException:
            await interaction.response.send_message("Un error inesperado ocurrio ❌")

async def setup(bot):
    await bot.add_cog(MuteUser(bot))