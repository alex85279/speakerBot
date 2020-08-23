import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import os

class React(Cog_Extension):
    @commands.command()
    async def 我要進去囉(self, ctx):
        pass
        # pic = discord.File(os.getenv('HERO_PIC_PATH'))
        # await ctx.send(file = pic)
        
def setup(bot):
    bot.add_cog(React(bot))