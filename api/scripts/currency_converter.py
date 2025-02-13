import sys
import json

# 標準入力からJSONデータを取得
input_data = json.loads(sys.stdin.read())

# 必要な値を取得
password = input_data["password"]

# パスワード強度チェック
strength = "Weak"
if len(password) >= 8 and any(c.isdigit() for c in password) and any(c.isupper() for c in password) and any(c.islower() for c in password):
    strength = "Strong"
elif len(password) >= 6:
    strength = "Moderate"

result = f"Password strength: {strength}"

# 結果を出力
print(result)
