from discord.ext import commands
from discord import app_commands
from typing import Optional
from Helpers.Checks import validade_Actions
import discord

class UnmuteUser(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def unmute(self, ctx, member: discord.Member, *, reason=None):
        #* Here we validate the input
        #* Aqui validamos la entrada de el usuario
        err = await validade_Actions(ctx.author, member, "mutear")
        if err:
            await ctx.send(err)
        
        #^ Here we search for "Muted role"
        #^ Aqui buscamos el rol llamado "Muted role"
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted role")
        if not muted_role:
            return await ctx.send("No existe un rol llamado 'Muted role', porfavor crealo. 😢")
    
        #~ Small error handling
        #~ Pequeno manejo de errores
        try:
            await member.remove_roles(muted_role, reason=reason)
            await ctx.send(f"{member.mention} ha sido desmuteado correctamente ✅!")
        except discord.Forbidden:
            await ctx.send("No tengo suficientes permisos para mutear ❌")
        except discord.HTTPException:
            await ctx.send("Un error inesperado ocurrio ❌")
    
    @app_commands.command(name="unmute", description="Desmutea a un usuario")
    @app_commands.checks.has_permissions(manage_roles=True)
    async def unmute_Slash(self, interaction: discord.Interaction, member: discord.Member, reason: Optional[str]=None):
        #* Here we validate the input
        #* Aqui validamos la entrada de el usuario
        err = await validade_Actions(interaction.user, member, "mutear")
        if err:
            await interaction.response.send_message(err, ephemeral=True)
        
        #^ Here we search for "Muted role"
        #^ Aqui buscamos el rol llamado "Muted role"
        muted_role = discord.utils.get(interaction.guild.roles, name="Muted role")
        if not muted_role:
            return await interaction.response.send_message("No existe un rol llamado 'Muted role', porfavor crealo. 😢")
    
        #~ Small error handling
        #~ Pequeno manejo de errores
        try:
            await member.remove_roles(muted_role, reason=reason)
            await interaction.response.send_message(f"{member.mention} ha sido desmuteado correctamente ✅!", ephemeral=True)
        except discord.Forbidden:
            await interaction.response.send_message("No tengo suficientes permisos para mutear ❌", ephemeral=True)
        except discord.HTTPException:
            await interaction.response.send_message("Un error inesperado ocurrio ❌", ephemeral=True)
    
async def setup(bot):
    await bot.add_cog(UnmuteUser(bot))