class Person:
    number_of_people = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.add_person()
    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people
    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

p1 = Person("Bill", 32)
print(Person.number_of_people)
p2 = Person("Tim", 25)
print(Person.number_of_people)

print(Person.number_of_people_())
Person.add_person()
print(Person.number_of_people_())

