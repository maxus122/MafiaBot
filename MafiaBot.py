#==========[ Библиотеки ]===========
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
import os

PREFIX = 'Mafia '
Bot = commands.Bot(command_prefix = PREFIX)
Bot.remove_command('help')
#===================================

#==============[ БД ]===============
import pymysql
BD = pymysql.connect(host = 'mysql51.1gb.ru', user = 'gb_x_ren_d542', password = '8084021a', db = 'gb_x_ren_d542')

a = BD.cursor()
sql = 'SELECT `Login` from `AcMafia`;'
a.execute(sql)
if sql:
    print('BD is already!')

countrow = a.execute(sql)
print(countrow)
data = a.fetchall()
print(data)

if data == (('CatDev',),):
    print('Equel')
#===================================

#============[ Команды ]============
# Start
@Bot.event
async def on_ready():
    print('Bot is already!')

# Clear
@Bot.command(pass_context = True)
async def clear(ctx):
    await ctx.channel.purge()
#===================================

token = os.environ.get('TOKEN')
Bot.run(str(token))





