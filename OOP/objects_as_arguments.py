class Car:

    color = None

class Motorcycle:

    color = None

def change_color(vehicle,color):

    vehicle.color = color

car1 = Car()
bike = Motorcycle()

change_color(car1,"red")
change_color(bike,"yellow")

print(car1.color)
print(bike.color)
