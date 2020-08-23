import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
with open('C:\\Users\\User\\Documents\\GitHub\\speakerBot\\setting.json', 'r', encoding='utf8') as setting:
    jdata = json.load(setting)

class React(Cog_Extension):
    @commands.command()
    async def 我要進去囉(self, ctx):
        pic = discord.File(jdata['pic_url'])
        await ctx.send(file = pic)
        
def setup(bot):
    bot.add_cog(React(bot))