from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
# BOT動作プログラム
@client.event
# async defでコルーチン宣言
# on_messageメッセージがサーバーに送信されたとき呼び出される。
async def on_message(message):
 # messageが「おはよう」で始まるか?
 if message.content.startswith("どすこい"):
  # 送り主がBotだった場合反応しないように条件つける。
  if client.user != message.author:
   # メッセージをmに格納。
   # message.author.nameに送り主の名前が入る。
   m = message.author.name + "うるせえ"
   # awaitはコルーチン内部でコルーチンを宣言する時に。
   # メッセージが送られてきたチャンネルへメッセージを送ります
   await client.send_message(message.channel, m)

bot.run(token)
