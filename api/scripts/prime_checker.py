import sys
import json

# 標準入力からJSONデータを取得
input_data = json.loads(sys.stdin.read())

# 必要な値を取得
number = input_data["number"]

# 素数判定
if number < 2:
    result = f"{number} is not a prime number."
else:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            result = f"{number} is not a prime number."
            break
    else:
        result = f"{number} is a prime number."

# 結果を出力
print(result)
