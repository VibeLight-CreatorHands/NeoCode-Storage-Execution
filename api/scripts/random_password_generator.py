import sys
import json
import random
import string

# 標準入力からJSONデータを取得
input_data = json.loads(sys.stdin.read())
length = input_data["length"]

# パスワード生成
if length < 4:
    print("Error: Password length must be at least 4.")
else:
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    print(f"Generated Password: {password}")
