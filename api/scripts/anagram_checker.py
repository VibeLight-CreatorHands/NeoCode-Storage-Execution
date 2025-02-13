import sys
import json

# 標準入力からJSONデータを取得
input_data = json.loads(sys.stdin.read())
word1 = input_data["word1"]
word2 = input_data["word2"]

# アナグラム判定
if sorted(word1.lower()) == sorted(word2.lower()):
    result = f'"{word1}" and "{word2}" are anagrams.'
else:
    result = f'"{word1}" and "{word2}" are not anagrams.'

print(result)
