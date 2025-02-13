import sys
import json

# 標準入力からJSONデータを取得
input_data = json.loads(sys.stdin.read())

# 必要な値を取得
amount = input_data["amount"]
rate = input_data["rate"]

# 通貨変換
converted_amount = amount * rate
result = f"Converted amount: {converted_amount:.2f}"

# 結果を出力
print(result)
