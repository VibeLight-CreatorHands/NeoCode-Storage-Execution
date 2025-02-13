import sys
import json
import random

# 標準入力からJSONデータを取得
input_data = json.loads(sys.stdin.read())

# 必要な値を取得
min_value = input_data["min"]
max_value = input_data["max"]

# ランダム数生成
if min_value > max_value:
    result = "Error: Minimum value cannot be greater than maximum value."
else:
    result = f"Random number: {random.randint(min_value, max_value)}"

# 結果を出力
print(result)
