import sys
import json

# 標準入力からJSONデータを取得
input_data = json.loads(sys.stdin.read())

# 必要な値を取得
number = input_data["number"]

# 階乗計算
if number < 0:
    result = "Error: Factorial of a negative number is not defined."
else:
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    result = f"Factorial of {number} is {factorial}."

# 結果を出力
print(result)
