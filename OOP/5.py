class Animal:
    def speak(self):
        print("The animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("The dog barks:")

animal1 = Animal()
dog1 = Dog()

animal1.speak()
dog1.speak()