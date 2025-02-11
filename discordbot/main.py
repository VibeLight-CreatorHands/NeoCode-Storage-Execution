import discord
from discord.ext import commands
import logging
import os

# ログの設定
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Intents（必要な権限を設定）
intents = discord.Intents.default()
intents.message_content = True  # メッセージの内容を取得するために必要

# Botの設定
TOKEN = os.getenv("DISCORD_BOT_TOKEN")  # 環境変数からトークンを取得
bot = commands.Bot(command_prefix="!", intents=intents)

# Bot起動時の処理
@bot.event
async def on_ready():
    logger.info(f"✅ {bot.user} がログインしました！")

# シンプルなスラッシュコマンド
@bot.tree.command(name="hello", description="Botが挨拶します")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"こんにちは、{interaction.user.name} さん！")

# ボタンを使ったインタラクション
class TestView(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label="押してみて！", style=discord.ButtonStyle.green)
    async def button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(f"ボタンが押されました！ 🎉")

@bot.tree.command(name="button_test", description="ボタンの動作テスト")
async def button_test(interaction: discord.Interaction):
    await interaction.response.send_message("このボタンを押してみて！", view=TestView())

# エラーハンドリング
@bot.event
async def on_command_error(ctx, error):
    logger.error(f"⚠️ エラー: {error}")
    await ctx.send("⚠️ コマンド実行中にエラーが発生しました！")

# Botの起動
if __name__ == "__main__":
    bot.run(TOKEN)
