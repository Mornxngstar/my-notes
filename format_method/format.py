
animal = "cow"
item = "moon"
print("The", animal, "jumped over the", item)
print("The {} jumped over the {}".format(animal,item))
print("The {1} jumped over the {0}".format(animal,item))  #positional argument
print("The {animal} jumped over the {animal}".format(animal="cow",item="moon"))  #keyword argument

text = "The {} jumped over the {}"
print(text.format(animal, item))

name = "Josh"
print("Hello, mi name is {:10}. Nice to meet ya".format("Josh"))
print("Hello, mi name is {:<10}. Nice to meet ya".format("Josh"))
print("Hello, mi name is {1:>10}. Nice to meet ya".format(item, name))
print("Hello, mi name is {name:^10}. Nice to meet ya".format(name="Josh"))

number = 3.14159
print("The number of pi is {:.2f}".format(number))
print("The number of pi is {:.4f}".format(number))

number = 123456123123
print("The number is {:,}".format(number))  #places a ',' every 3 characters
print("The number is {:b}".format(number))  #binary
print("The number is {:o}".format(number))  #octal number
print("The number is {:x}".format(number))  #hexadecimal number
print("The number is {:X}".format(number))  #hexadecimal number upper case
print("The number is {:e}".format(number))  #scientific notation 
print("The number is {:E}".format(number))  #scientific notation upper case
