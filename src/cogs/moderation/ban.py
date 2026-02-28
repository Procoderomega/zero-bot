from discord.ext import commands
from discord import app_commands
from Helpers.Checks import validade_Actions
import discord

class BanUser(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    #* 💠 Prefix Command - Comando de prejijo 💠 *#
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        
            #~ Validador y Error handler externo ~#
        error = await validade_Actions(ctx.author, member)
        if error:
            return await ctx.send(error)
        
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
    
    #* 💠 Slash Command - Comando de barra
    @app_commands.command(name="ban", description="Banea a un usuario especifico")
    @app_commands.checks.has_permissions(ban_members=True)
    async def banSlash(self, interaction: discord.Interaction, member: discord.Member, reason: str="Sin razon"):
        error = await validade_Actions(interaction.user, member, "banear") #? Llamamos al validador para que verifique
        if error:
            return await interaction.response.send_message(error, ephemeral=True) #? si hay un error lo mand en efemeral

        try:    
            await member.ban(reason=reason)
            await interaction.response.send_message("El usuario fue baneado correctamente ✅", ephemeral=True)
        except discord.Forbidden:
            await interaction.response.send_message("No tengo permisos suficientes ❌", ephemeral=True)
        except discord.HTTPException:
            await interaction.response.send_message("Ocurrio un error inesperado ⚠️", ephemeral=True)
        except Exception as E:
            await interaction.response.send_message("Ocurrio un error con el servidor ⚠️", ephemeral=True)

async def setup(bot):
    await bot.add_cog(BanUser(bot))