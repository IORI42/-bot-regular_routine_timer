from discord.ext import commands
from os import getenv
import traceback

bot = commands.Bot(command_prefix='/')


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)



#指定した時間経過すると切断する
@bot.command()
async def for_time(ctx):
    await ctx.send('pong')

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
