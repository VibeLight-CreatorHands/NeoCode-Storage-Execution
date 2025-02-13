import sys
import json
import random

# 標準入力からJSONデータを取得
input_data = json.loads(sys.stdin.read())

# 必要な値を取得
location = input_data["location"]

# 簡易天気シミュレーション
weather_conditions = ["Sunny", "Cloudy", "Rainy", "Stormy", "Snowy"]
temperature = random.randint(-10, 35)

result = f"Weather in {location}: {random.choice(weather_conditions)}, {temperature}°C"

# 結果を出力
print(result)
