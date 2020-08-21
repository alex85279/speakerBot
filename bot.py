import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='fk')

@bot.event
async def on_ready():
    print(">>Bot is online<<")

@bot.event
async def on_member_join(member):
    print(F'{member}join!')



bot.run('')