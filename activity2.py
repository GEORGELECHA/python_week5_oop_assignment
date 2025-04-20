# Base Animal class
class Animal:
    def move(self):
        print("The animal moves")

# Different animal classes
class Fish(Animal):
    def move(self):
        print("The fish swims")

class Bird(Animal):
    def move(self):
        print("The bird flies")

# Create animals
nemo = Fish()
tweety = Bird()

# Demonstrate polymorphism
nemo.move()   # Output: The fish swims
tweety.move() # Output: The bird flies