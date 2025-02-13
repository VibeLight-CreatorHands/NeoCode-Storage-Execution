import random

def generate_welcome_message():
    messages = [
        "ようこそ！今日も素晴らしい一日になりますように。",
        "こんにちは！新しい冒険が待っています。",
        "おかえりなさい！今日も頑張りましょう。",
        "こんにちは！素敵な一日をお過ごしください。",
        "ようこそ！新しい挑戦があなたを待っています。"
    ]
    return random.choice(messages)

if __name__ == "__main__":
    print(generate_welcome_message())