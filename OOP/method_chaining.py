class Car:

    def turn_on(self):
        print("You start the engine")
        return self
    
    def drive(self):
        print("You are driving")
        return self
    
    def breaks(self):
        print("You step on the brakes")
        return self
    
    def turn_off(self):
        print("You turn off the engine")
        return self

car = Car()

# car.turn_on()
# car.drive()

# car.turn_on().drive()

car.turn_on()\
    .drive()\
    .breaks()\
    .turn_off()
