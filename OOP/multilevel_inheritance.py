class Organism:

    alive = True

class Animal(Organism):

    def eat(self):
        print("Eats")

class Dog(Animal):
    
    def bark(self):
        print("Bark")

dog = Dog()
print(dog.alive)
