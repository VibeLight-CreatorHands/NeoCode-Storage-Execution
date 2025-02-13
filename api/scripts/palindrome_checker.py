import sys
import json

# 標準入力からJSONデータを取得
input_data = json.loads(sys.stdin.read())

# 必要な値を取得
text = input_data["text"]

# 回文チェック
if text == text[::-1]:
    result = f'"{text}" is a palindrome.'
else:
    result = f'"{text}" is not a palindrome.'

# 結果を出力
print(result)
