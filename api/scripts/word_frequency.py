import sys
import json
from collections import Counter

# 標準入力からJSONデータを取得
input_data = json.loads(sys.stdin.read())
text = input_data["text"]

# 単語の頻度を数える
words = text.split()
frequency = Counter(words)

print(f"Word Frequency: {dict(frequency)}")
