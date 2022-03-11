from discord.ext import commands
from os import getenv
import traceback
import datetime

import discord

bot = commands.Bot(command_prefix='/')

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

client = MyClient()
client.run('my token goes here')

#指定した時間経過すると切断する
@bot.command()
async def for_time(ctx,min: int):
    now = datetime.datetime.now()
    disconnect_time = now + datetime.timedelta(minutes=min)
    await ctx.send(datetime.datetime.now())


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
