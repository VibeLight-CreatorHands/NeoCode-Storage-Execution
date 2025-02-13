import sys
import json
from pyfiglet import Figlet

# 標準入力からJSONデータを取得
input_data = json.loads(sys.stdin.read())
text = input_data["text"]

# フォント指定（オプションで変更可能）
fig = Figlet(font="slant")
ascii_art = fig.renderText(text)
print(ascii_art)
