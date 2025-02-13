import sys
import json

# 標準入力からJSONデータを取得
input_data = json.loads(sys.stdin.read())

# 必要な値を取得
count = input_data["count"]

# フィボナッチ数列生成
if count <= 0:
    result = "Error: Count must be a positive integer."
else:
    fibonacci = [0, 1]
    while len(fibonacci) < count:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    result = f"First {count} Fibonacci numbers: {fibonacci[:count]}"

# 結果を出力
print(result)
