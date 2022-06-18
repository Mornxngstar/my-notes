from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def run(self):
        pass

class Car(Vehicle):

    def go(self):
        print("This car is going")

class Motorcycle(Vehicle):
    
    def go(self):
        print("You ride this motocicle")


car = Car()
moto = Motorcycle()

car.go()
moto.go()
