import random
import string

def generate_password(length: int):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    length = int(input("Enter password length: "))
    print(f"Generated password: {generate_password(length)}")
