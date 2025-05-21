class person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        if age>=0:
            self.__age = age
        else:
            print("Age cannot be negative")

person1 = person("alice", 30)

print(person1.get_name())
print(person1.get_age)

person1.set_name("Bob")
person1.set_age(35)

print(person1.get_name())
print(person1.get_age)

person1.set_age(-5)
    