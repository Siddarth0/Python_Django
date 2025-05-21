import math

number = float(input("Enter a number to find its square root: "))
base = float(input("Enter the base number for power calculation: "))
exponent = float(input("Enter the exponent for power calculation: "))

square_root = math.sqrt(number)
print(f"The Sqaure root of {number} is: {square_root}")

power = math.pow(base, exponent)
print(f"The result of {base} is raised to the power of {exponent} is: {power}")
