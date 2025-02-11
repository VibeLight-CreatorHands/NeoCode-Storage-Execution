import discord
from discord.ext import commands
from discord import app_commands
import os
import logging
from database import init_db, get_balance, update_balance

# ログの設定
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Intents（必要な権限を設定）
intents = discord.Intents.default()
intents.message_content = True  # メッセージの内容を取得するために必要

# Botの設定
TOKEN = os.getenv("DISCORD_BOT_TOKEN")  # 環境変数からトークンを取得
bot = commands.Bot(command_prefix="y!", intents=intents)

# データベースの設定
init_db()

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

# 🔹 ユーザーのポイントを確認
@bot.tree.command(name="balance", description="現在のポイントを確認します")
async def balance(interaction: discord.Interaction):
    user_id = str(interaction.user.id)
    balance = get_balance(user_id)
    await interaction.response.send_message(f"💰 {interaction.user.name} さんのポイント: {balance} P")

     # 🔹 ユーザーにポイントを付与（管理者限定）
@bot.tree.command(name="give", description="ユーザーにポイントを付与します（管理者のみ）")
@commands.has_permissions(administrator=True)
async def give(interaction: discord.Interaction, member: discord.Member, amount: int):
  update_balance(str(member.id), amount)
  await interaction.response.send_message(f"✅ {member.name} に {amount} P を付与しました！")

 # 🔹 ポイントの送金
@bot.tree.command(name="transfer", description="他のユーザーにポイントを送ります")
async def transfer(interaction: discord.Interaction, member: discord.Member, amount: int):
  sender_id = str(interaction.user.id)
  receiver_id = str(member.id)

  if sender_id == receiver_id:
     await interaction.response.send_message("⚠️ 自分にポイントを送ることはできません！")
     return
  if get_balance(sender_id) < amount:
     await interaction.response.send_message("❌ ポイントが足りません！")
     return
  update_balance(sender_id, -amount)
  update_balance(receiver_id, amount)
  await interaction.response.send_message(f"✅ {interaction.user.name} から {member.name} に {amount} P を送金しました！")
  # 🔹 エラーハンドリング
@bot.event
async def on_command_error(ctx, error):
  await ctx.send("⚠️ コマンド実行中にエラーが発生しました！")
  print(error)

# Botの起動
if __name__ == "__main__":
  bot.run(TOKEN)