import sys
import json

# 標準入力からJSONデータを取得
input_data = json.loads(sys.stdin.read())
temperature = input_data["temperature"]
unit = input_data["unit"]

# 温度変換処理
if unit.lower() == "celsius":
    converted = (temperature * 9/5) + 32
    result = f"{temperature}°C = {converted:.2f}°F"
elif unit.lower() == "fahrenheit":
    converted = (temperature - 32) * 5/9
    result = f"{temperature}°F = {converted:.2f}°C"
else:
    result = "Error: Invalid unit. Use 'Celsius' or 'Fahrenheit'."

print(result)
