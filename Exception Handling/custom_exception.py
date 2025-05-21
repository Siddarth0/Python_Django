class NegativeNumberError(Exception):
    pass

try:
    number = int(input("Enter a positive number: "))

    if number < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")
    
    print(f"You entered: {number}")

except NegativeNumberError as e:
    print(f"Custom Exception Caught; {e}")

except ValueError:
    print("Error: Please enter a valid integer.")