def count_word_occurrences(text: str, word: str):
    return text.lower().split().count(word.lower())

if __name__ == "__main__":
    text = input("Enter a sentence: ")
    word = input("Enter a word to count: ")
    print(f"The word '{word}' appeared {count_word_occurrences(text, word)} times.")
