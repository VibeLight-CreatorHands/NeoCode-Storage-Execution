import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

# .envから環境変数をロード
load_dotenv()

# Discord Botのトークンを取得
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

# Botが起動した時に呼ばれるイベント
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# サンプルコマンド
@bot.command()
async def hello(ctx):
    await ctx.send("Hello, world!")

# Botを実行
bot.run(TOKEN)
