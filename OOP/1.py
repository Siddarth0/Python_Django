class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

user_name = input("Enter your name: ")
user_age = input("Enter your age: ")

person1 = person(user_name, user_age)

person1.display()