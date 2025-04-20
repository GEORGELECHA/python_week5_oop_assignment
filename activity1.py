# Superhero class
class Superhero:
    def __init__(self, name, power):
        self.name = name
        self.power = power
    
    def use_power(self):
        print(f"{self.name} uses {self.power}!")

# Flying superhero inherits from Superhero
class FlyingSuperhero(Superhero):
    def fly(self):
        print(f"{self.name} flies high in the sky!")

# Create superheroes
spiderman = Superhero("Spiderman", "web shooting")
superman = FlyingSuperhero("Superman", "super strength")

# Test the classes
spiderman.use_power()  # Output: Spiderman uses web shooting!
superman.use_power()   # Output: Superman uses super strength!
superman.fly()         # Output: Superman flies high in the sky!