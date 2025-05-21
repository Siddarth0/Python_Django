import importfunc #importing the custom module we made

number = int(input("Enter a number"))

print(f"The square of {number} is: {importfunc.square(number)}")
print(f"The cube of {number} is: {importfunc.cube(number)}")