class calculator:
    def square(self,number):
        return number*number
    
calc = calculator()

num = float(input("Enter a number to square: "))

result = calc.square(num)
print(f"The sqaure of {num} is {result}")