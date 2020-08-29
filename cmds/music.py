import discord
import asyncio
from discord.ext import commands
from core.classes import Cog_Extension
import json
import nacl
from gtts import gTTS
from async_timeout import timeout

class Music(Cog_Extension):
    @commands.command()
    async def 進來(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("你沒進任何頻道阿傻屌")
            return
        channel = ctx.author.voice.channel
            
            

        voice = ctx.voice_client
        if voice is not None:
            if voice.channel.id == channel.id:
                return
            try:
                await voice.move_to(channel)
            except asyncio.TimeoutError:
                raise commands.CommandError(f'移動到<{channel}> time out')
                
        else:
            try:
                await channel.connect()
            except asyncio.TimeoutError:
                raise commands.CommandError(f'移動到<{channel}> time out')

        await ctx.send("來了幹")


    @commands.command()
    async def 滾(self, ctx):
        await ctx.voice_client.disconnect()
        await ctx.send("掰")

    @commands.command()
    async def 說(self, ctx, args):
        output = gTTS(text=args, lang='zh-tw', slow=False)
        output.save('./audio/temp.mp3')
        # source = discord.PCMVolumeTransformer()
        ctx.voice_client.play(discord.FFmpegPCMAudio(executable='D:/ffmpeg/bin/ffmpeg.exe', source='./audio/temp.mp3'))
        os.remove('./audio/temp.mp3')
    
def setup(bot):
    bot.add_cog(Music(bot))