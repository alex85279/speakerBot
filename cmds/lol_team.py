import discord
from discord.ext import commands
from core.classes import Cog_Extension
import urllib
from bs4 import BeautifulSoup as soup
import io
import time
from selenium import webdriver
class LOL_TEAM(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def 稽查隊友(self, ctx, args):
        print(args)
        # my_header = "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "

        url = "https://matchhistory.tw.leagueoflegends.com/zh/#match-history/TW/68599949?matchType=2&map=1"
        
        # request = urllib.request.Request(url)
    
        # request.add_header("User-Agent",my_header)
        # with urllib.request.urlopen(request) as file:
        #     data = file.read().decode('utf-8')
        # data_parsed = soup(data, 'html.parser')
        # print(data_parsed.prettify())
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        browser = webdriver.Chrome(chrome_options=options)
        browser.set_window_size(1920, 1680)
        browser.get(url)


        browser.execute_script("""
        (function () {
        var y = 0;
        var step = 100;
        window.scroll(0, 0);
        function f() {
        if (y < document.body.scrollHeight) {
        y  = step;
        window.scroll(0, y);
        setTimeout(f, 50);
        } else {
        window.scroll(0, 0);
        document.title  = "scroll-done";
        }
        }
        setTimeout(f, 1000);
        })();
        """)
        for i in range(30):
            if "scroll-done" in browser.title:
                break
        time.sleep(1)
        browser.save_screenshot("history.png")
        browser.close()



def setup(bot):
    bot.add_cog(LOL_TEAM(bot))