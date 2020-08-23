import discord
from discord.ext import commands
import json
import os

with open('setting.json', 'r', encoding='utf8') as setting:
    jdata = json.load(setting)

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(">>Bot is online<<")

@bot.event
async def on_member_join(member):
    print(F'{member}join!')
    channel = bot.get_channel(int(jdata["RoomId"]))
    await channel.send(F'{member} 真沒想到你能來到這裡，現在你可以滾了')

@bot.event
async def on_member_remove(member):
    print(F'{member}leave!')
    channel = bot.get_channel(int(jdata["RoomId"]))
    await channel.send('我的天，他真的滾了')

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(F'cmds.{filename[:-3]}')


if __name__ == "__main__":
    bot.run(jdata['TOKEN'])