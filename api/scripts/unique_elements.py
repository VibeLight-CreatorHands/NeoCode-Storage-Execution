import sys
import json

# 標準入力からJSONデータを取得
input_data = json.loads(sys.stdin.read())
elements = input_data["elements"]

# ユニークな要素を取得
unique_elements = list(set(elements))
print(f"Unique Elements: {unique_elements}")
