from discord.ext import commands
import random

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command() # funcion de comando para saludar al usuario
    async def hola(self, ctx):
        await ctx.send(f'¡Hola {ctx.author.name}! 😎')
        
    @commands.command() # funcion de comando para preguntar como esta el usuario
    async def estado(self, ctx):
        await ctx.send(f'Como estas {ctx.author.name}?')
        
    @commands.command() # funcion de usuario dice ping y el bot responde pong
    async def ping(self, ctx):
        await ctx.send(f'Pong! 🏓 | Extra: latencia del bot: {round(self.bot.latency * 1000)}ms')
        
    @commands.command() # funcion de comando para repetir el mensaje del usuario
    async def repeat(self, ctx, *, message: str):
        await ctx.send(message)
        
    @commands.command() # funcion de comando para lanzar un dado
    async def roll(self, ctx):
        dice = random.randint(1, 6)
        await ctx.send(f'Has sacado un {dice}! 🎲')
        
    @commands.command() # funcion de comando para elegir entre opciones
    async def choose(self, ctx, *options):
        if not options:
            await ctx.send("dame una almenos ahuevonao")
            return
        options_list = random.choice(options)
        await ctx.send(f'He elegido: {options_list}')   

# setup async para 2.x+
async def setup(bot):
    await bot.add_cog(Fun(bot))
