import discord
import urllib
import io
import time
import json
from discord.ext import commands
from bs4 import BeautifulSoup as soup
from pathlib import Path
from selenium import webdriver
from core.classes import Cog_Extension
import os

class LOL_HERO(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def h(self, ctx, args):
        print(args)
        # my_header = "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "

        ''' 檢測擺圖片的資料夾是否存在 '''
        pic_path = os.getenv('HERO_PIC_PATH')
        if Path(pic_path).is_dir():
            pass
        else:
            Path(pic_path).mkdir()
        wholepath = pic_path + '\\' + "".join(args) + '.png'
        pic = 1
        if Path(wholepath).exists():
            await ctx.send("有存過囉，給你")
            pic = pic = discord.File(wholepath)
        else:
            await ctx.send("資料庫裡面沒有，等我找一下")
            ''' 如果資料夾沒有就從網路上得到圖片 '''
            url = "https://u.gg/lol/champions/" + "".join(args) + "/build"
            # request = urllib.request.Request(url)
            # request.add_header("User-Agent",my_header)
            # with urllib.request.urlopen(request) as file:
            #     data = file.read().decode('utf-8')
            # data_parsed = soup(data, 'html.parser')
            # print(data_parsed.prettify())
            options = webdriver.ChromeOptions()
            options.add_argument('headless')
            browser = webdriver.Chrome(chrome_options=options)
            browser.set_window_size(1920, 2000)
            browser.get(url)


            # browser.execute_script("""
            # (function () {
            # var y = 0;
            # var step = 500;
            # window.scroll(0, 0);
            # function f() {
            # if (y < document.body.scrollHeight) {
            # y  = step;
            # window.scroll(0, y);
            # setTimeout(f, 50);
            # } else {
            # window.scroll(0, 0);
            # document.title  = "scroll-done";
            # }
            # }
            # setTimeout(f, 1000);
            # })();
            # """)
            # for i in range(300):
            #     if "scroll-done" in browser.title:
            #         break
            # time.sleep(1)
            
            browser.save_screenshot(wholepath)
            browser.close()


            # time.sleep(1)
            
            pic = discord.File(wholepath)
            while pic is None:
                pic = discord.File(wholepath)
        await ctx.send(file = pic)



def setup(bot):
    bot.add_cog(LOL_HERO(bot))