from discord.ext import commands
from os import getenv
import traceback
import datetime

bot = commands.Bot(command_prefix='/')

#指定した時間経過すると切断する
@bot.command()
async def for_time(ctx,min: int):
    time = datetime.datetime.now()
    await ctx.send(time)
    time = time + datetime.timedelta(minutes=min)
    await ctx.send(time)

#毎日のアラームを設定する
@bot.command()
async def set(ctx):
    await ctx.send('pong')

#今日だけ有効なアラームを設定する
@bot.command()
async def today(ctx):
    await ctx.send('pong')

#設定しているアラームの一覧を表示する
@bot.command()
async def show(ctx):
    await ctx.send('pong')

#設定しているアラームを削除する
@bot.command()
async def delete(ctx):
    await ctx.send('pong')

token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
