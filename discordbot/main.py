import discord
from discord.ext import commands
from discord import app_commands
import os
import logging
from database import init_db, get_user_data, convert_currency, get_crypto_rate, update_crypto_rate, update_balance, get_balance
from datetime import datetime, timedelta
import asyncio

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

# 最後のアクティビティ時刻を記録
last_active = datetime.now()

async def monitor_activity():
  """10分間アクティビティがなかったらBotを自動停止"""
  global last_active
  while True:
    await asyncio.sleep(60)  # 1分ごとにチェック
    if datetime.now() - last_active > timedelta(minutes=10):
      print("⏳ 10分間アクティビティなし、Botを停止します")
      os._exit(0)  # プロセスを終了（Railway上では停止扱いになる）

@bot.event
async def on_ready():
  """Botが起動したら監視を開始し、スラッシュコマンドを同期"""
  bot.loop.create_task(monitor_activity())
            
  try:
      synced = await bot.tree.sync()
      logger.info(f"✅ スラッシュコマンド {len(synced)} 件を同期しました！")
  except Exception as e:
      logger.error(f"❌ スラッシュコマンドの同期に失敗: {e}")

  logger.info(f"✅ {bot.user} がログインしました！")
@bot.event
async def on_message(message):
  """コマンドやメッセージを受信したらアクティビティを更新"""
  global last_active
  last_active = datetime.now()  # 最後のアクティビティ時刻を更新
  await bot.process_commands(message)  # コマンドの処理を続ける
                                                                    
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

# 🔹 現在の仮想通貨レートを表示
@bot.tree.command(name="crypto_price", description="仮想通貨の現在のレートを表示します")
async def crypto_price(interaction: discord.Interaction):
  rate = get_crypto_rate()
  await interaction.response.send_message(f"📈 現在のレート: 1 YUYUCOIN = {rate} P")

# 🔹 ポイント ↔ 仮想通貨の交換
@bot.tree.command(name="convert", description="ポイントと仮想通貨を交換します")
async def convert(interaction: discord.Interaction, amount: float, to_crypto: bool):
  user_id = str(interaction.user.id)
  success = convert_currency(user_id, amount, to_crypto)

  if not success:
    await interaction.response.send_message("❌ 変換に失敗しました（残高不足の可能性あり）")
    return

  balance, crypto = get_user_data(user_id)
  await interaction.response.send_message(
    f"✅ 変換完了！\n💰 現在のポイント: {balance} P\n🪙 仮想通貨: {crypto:.4f} YUYUCOIN"
    )

# 🔹 仮想通貨レートを変更（管理者のみ）
@bot.tree.command(name="market_update", description="仮想通貨のレートを変更（管理者専用）")
@commands.has_permissions(administrator=True)
async def market_update(interaction: discord.Interaction, new_rate: float):
  update_crypto_rate(new_rate)
  await interaction.response.send_message(f"✅ 仮想通貨レートを {new_rate} P に更新しました！")

  # 🔹 エラーハンドリング
@bot.event
async def on_command_error(ctx, error):
  await ctx.send("⚠️ コマンド実行中にエラーが発生しました！")
  print(error)

# Botの起動
if __name__ == "__main__":
  bot.run(TOKEN)