import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='fk')

@bot.event
async def on_ready():
    print(">>Bot is online<<")

@bot.event
async def on_member_join(member):
    print(F'{member}join!')

@bot.event
async def one_member_leave(member):
    print(F'{member}leave!')

bot.run('')