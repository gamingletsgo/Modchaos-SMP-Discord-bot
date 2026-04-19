import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run('MTQ5NTEzNzM0NTE5NDgxOTY2NA.GEXfOf.hdg7HWZpiXxCOW74BZmiwbKQadSFW83GweAudE')