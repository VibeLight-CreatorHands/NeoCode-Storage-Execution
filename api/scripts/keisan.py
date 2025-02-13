import sys
import json

# コマンドライン引数から入力を取得
input_data = json.loads(sys.stdin.read())

# JSONから値を取得
operation = input_data["operation"]
num1 = input_data["num1"]
num2 = input_data["num2"]

# 計算処理
if operation == "add":
    result = num1 + num2
elif operation == "subtract":
    result = num1 - num2
elif operation == "multiply":
    result = num1 * num2
elif operation == "divide":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero"
else:
    result = "Error: Invalid operation"

print(f"Result: {result}")
