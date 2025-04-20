

class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")