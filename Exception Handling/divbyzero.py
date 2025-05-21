numerator = float(input("Enter a numerator: "))
denominator = float(input("Enter denominator: "))

try:
    result = numerator / denominator
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")