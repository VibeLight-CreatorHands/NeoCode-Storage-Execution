import sys
import json

# 標準入力からJSONデータを取得
input_data = json.loads(sys.stdin.read())
text = input_data["text"]
shift = input_data["shift"]

# 暗号化処理
encrypted_text = ""
for char in text:
    if char.isalpha():
        shift_base = 65 if char.isupper() else 97
        encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
    else:
        encrypted_text += char

print(f"Encrypted Text: {encrypted_text}")
