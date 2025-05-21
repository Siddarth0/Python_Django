class car:
    def __init__(self, model, price):
        self.model = model
        self.price = price
        
    def display(self):
        print(f"Car model: {self.model}")
        print(f"Car price: ${self.price}")
    
car_name = input("Enter the car name: ")
car_price = float(input("Enter the car price: "))

car1 = car(car_name, car_price)

car1.display()