import jaconv

def kanji_to_hiragana(kanji: str):
    return jaconv.kanji2hira(kanji)

if __name__ == "__main__":
    kanji = input("Enter kanji text: ")
    print(f"Converted hiragana: {kanji_to_hiragana(kanji)}")
