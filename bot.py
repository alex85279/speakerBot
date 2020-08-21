import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='fk')

@bot.event
async def on_ready():
    print(">>Bot is online<<")

bot.run('NzQ1OTEzNDE2MzU0MzY1NDYw.Xz4sAA.3oW83nkSQeMW8UyQzu-I7HcyWT4')