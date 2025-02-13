def fibonacci(n: int):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

if __name__ == "__main__":
    n = int(input("Enter the length of Fibonacci sequence: "))
    print(f"Fibonacci sequence: {fibonacci(n)}")
