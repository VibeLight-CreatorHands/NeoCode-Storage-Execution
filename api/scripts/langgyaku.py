def reverse_word(word: str):
    return word[::-1]

if __name__ == "__main__":
    word = input("Enter a word to reverse: ")
    print(f"Reversed word: {reverse_word(word)}")
