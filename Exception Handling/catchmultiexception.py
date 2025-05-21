a = int(input("Enter numerator: "))
b = int(input("Enter denominator: "))


try:
    result = a/b
    print(f"Result: {result}")

except ValueError:
    print("Error: please enter a valid integer")

except ZeroDivisionError:
    print("Error: Division by zero isnot allowed")