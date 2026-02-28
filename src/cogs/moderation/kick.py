import discord
from discord import app_commands
from Helpers.Checks import validade_Actions
from discord.ext import commands
from typing import Optional

class KickUser(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #* Comando de prefijo - Prefix Command
    @commands.command(name="kick")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        err = await validade_Actions(ctx.author, member, "kickear")
        if err:
            await ctx.send(err)
        
        try:
            await member.kick(reason=reason)
            await ctx.send("El usuario fue kickeado correctamente ✅")
        except discord.Forbidden:
            await ctx.send("No tengo permisos suficientes ❌")
        except discord.HTTPException:
            await ctx.send("Ocurrio un error inesperado ❌")
        except Exception as e:
            await ctx.send("Ocurrio un error inesperado ❌")
        
        
    #* Comando slash - Slash command
    @app_commands.command(name="kick", description="Kickea a un usuario en especifico")
    @app_commands.checks.has_permissions(kick_members=True)
    async def kickSlash(self, interaction: discord.Interaction, member: discord.Member, reason: Optional[str]=None):
        err = await validade_Actions(interaction.user, member, "kickear")
        if err:
            return await interaction.response.send_message(err)
    
        try:    
            await member.kick(reason=reason)
            await interaction.response.send_message("El usuario fue kickeado correctamente ✅", ephemeral=True)
        except discord.Forbidden:
            await interaction.response.send_message("No tengo permisos suficientes ❌", ephemeral=True)
        except discord.HTTPException:
            await interaction.response.send_message("Ocurrio un error inesperado ⚠️", ephemeral=True)
        except Exception as E:
            await interaction.response.send_message("Ocurrio un error con el servidor ⚠️", ephemeral=True)

async def setup(bot):
    await bot.add_cog(KickUser(bot))