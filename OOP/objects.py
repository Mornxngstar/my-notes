class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def bark(self):
        print("Bark")

d = Dog("Bill", 21)
print(d.get_name())
print(d.get_age())
d.bark()