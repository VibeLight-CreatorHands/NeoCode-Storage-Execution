import sys
import json

# 標準入力からJSONデータを取得
input_data = json.loads(sys.stdin.read())

# 必要な値を取得
text = input_data["text"]
operation = input_data["operation"]

# 文字列操作
if operation == "reverse":
    result = text[::-1]
elif operation == "uppercase":
    result = text.upper()
elif operation == "lowercase":
    result = text.lower()
else:
    result = "Error: Invalid operation"

# 結果を出力
print(f"Result: {result}")
