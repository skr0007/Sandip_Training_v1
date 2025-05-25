def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        raise ValueError("Invalid operator")

if __name__ == "__main__":
    n1 = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /): ")
    n2 = float(input("Enter second number: "))

    try:
        result = calculate(n1, n2, op)
        print(f"Result: {result}")
        with open("result.txt", "w") as f:
            f.write(str(result))
    except Exception as e:
        print("Error:", e)
