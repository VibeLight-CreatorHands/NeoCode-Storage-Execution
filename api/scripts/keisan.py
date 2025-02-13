def calculator(operation: str, num1: float, num2: float):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Invalid operation."

# メイン部分で入力を受け取る
if __name__ == "__main__":
    operation = input("Enter operation (add, subtract, multiply, divide): ").lower()
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"Result: {calculator(operation, num1, num2)}")
