import uuid

def generate_unique_id(prefix: str):
    return f"{prefix}-{uuid.uuid4()}"

if __name__ == "__main__":
    prefix = input("Enter a prefix for your unique ID: ")
    print(f"Generated unique ID: {generate_unique_id(prefix)}")
