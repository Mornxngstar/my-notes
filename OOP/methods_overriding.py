class Animal:

    def eat(self):
        print("This animal eats")

class Rabbit(Animal):

    def eat(self):
        print("This rabbit eats a carrot")

r = Rabbit()
r.eat()