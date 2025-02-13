import sys
import json

# 標準入力からJSONデータを取得
input_data = json.loads(sys.stdin.read())
r = input_data["r"]
g = input_data["g"]
b = input_data["b"]

# 16進数カラーコードに変換
if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
    hex_color = "#{:02X}{:02X}{:02X}".format(r, g, b)
    print(f"Hex Color Code: {hex_color}")
else:
    print("Error: RGB values must be between 0 and 255.")
