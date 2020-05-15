#==========[ Библиотеки ]===========
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
import os

PREFIX = 'Мафия - '
Bot = commands.Bot(command_prefix = PREFIX)
Bot.remove_command('help')
#===================================

#==============[ БД ]===============
import pymysql
BD = pymysql.connect(host = 'mysql51.1gb.ru', user = 'gb_x_ren_d542', password = '8084021a', db = 'gb_x_ren_d542')

a = BD.cursor()
sql = 'SELECT `id` from `AcMafia`;'
a.execute(sql)
if sql:
    print('BD is already!')

countrow = a.execute(sql)
print(countrow)
data = a.fetchall()
print(data)

if 1 == 1:
    print('Equel')
#===================================

#============[ Команды ]============
# Start
@Bot.event
async def on_ready():
    print('Bot is already!')

# Join
@Bot.command(pass_context = True)
async def join(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(Bot.voice_clients, guild = ctx.guild)
    await ctx.channel.purge(limit = 1)

    if voice and voice.is_connected():
        await voice.move_to('Мафия')
    else:
        voice = await channel.connect()
        await ctx.send(f'Бот присоеденился к голосовому каналу "{channel}".')

# Stop
@Bot.command(pass_context = True)
async def stop(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(Bot.voice_clients, guild = ctx.guild)
    await ctx.channel.purge(limit = 1)

    if voice and voice.is_connected():
        await voice.disconnect()
        await ctx.send(f'Игра окончена.')
        await ctx.send(f'Бот покинул голосовой канал.')


# Help
@Bot.command(pass_context = True)
async def help(ctx):
    emb = discord.Embed(title = 'Навигация по командам')

    emb.add_field(name = '{}join'.format(PREFIX), value = 'Присоединение бота к чату')
    emb.add_field(name = '{}start'.format(PREFIX), value = 'Начало игры')
    emb.add_field(name = '{}clear'.format(PREFIX), value = 'Очистка чата')
    emb.add_field(name = '{}kick'.format(PREFIX), value = 'Кик пользователя')
    emb.add_field(name = '{}ban'.format(PREFIX), value = 'Бан пользователя')

    await ctx.send(embed = emb)

# Clear
@Bot.command(pass_context = True)
async def clear(ctx):
    await ctx.channel.purge()

# Kick
@Bot.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def kick(ctx, member: discord.Member, *, reason = None):
    await member.kick(reason = reason)
    await ctx.channel.purge(limit = 1)
    if reason != None:
        await ctx.send(f'Пользователь {member.mention} был выгнан по причине "{reason}".')

    if reason == None:
        await ctx.send(f'Пользователь {member.mention} был выгнан.')

# Ban
@Bot.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def ban(ctx, member: discord.Member, *, reason = None):
    await member.ban(reason = reason)
    await ctx.channel.purge(limit = 1)
    if reason != None:
        await ctx.send(f'Пользователь {member.mention} был забанен по причине "{reason}".')

    if reason == None:
        await ctx.send(f'Пользователь {member.mention} был забанен.')
#===================================

token = os.environ.get('TOKEN')
Bot.run(str(token))





