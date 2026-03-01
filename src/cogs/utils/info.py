import discord
from discord.ext import commands
from discord import app_commands
import json
from pathlib import Path

class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # Cargar JSON
        path = Path(__file__).parent.parent / "utils" / "list.json"
        with open(path, "r", encoding="utf-8") as f:
            self.help_data = json.load(f)

    @commands.command(name="ayuda")
    async def help_command(self, ctx):
        embed = discord.Embed(title="📜 Comandos disponibles", color=discord.Color.green())
        for category, commands_dict in self.help_data.items():
            cmd_str = ""
            for cmd, desc in commands_dict.items():
                cmd_str += f"`{cmd}` - {desc}\n"
            embed.add_field(name=category, value=cmd_str, inline=False)
        await ctx.send(embed=embed)

    @app_commands.command(name="ayuda", description="Muestra los comandos del bot")
    async def help_slash(self, interaction: discord.Interaction):
        embed = discord.Embed(title="📜 Comandos disponibles", color=discord.Color.green())
        for category, commands_dict in self.help_data.items():
            cmd_str = ""
            for cmd, desc in commands_dict.items():
                cmd_str += f"`{cmd}` - {desc}\n"
            embed.add_field(name=category, value=cmd_str, inline=False)
        await interaction.response.send_message(embed=embed, ephemeral=False)
print("Check 1 ✅")
async def setup(bot):
    await bot.add_cog(HelpCog(bot))
