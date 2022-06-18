import random

x = random.randint(1, 6)  #generates a random integer between the range given
y = random.random()  #generates a random float between 0 and 1

my_list = ["rock", "paper", "scissors"]
z = random.choice(my_list)

cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
random.shuffle(cards)

print(x)
print(y)
print(z)
print(cards)
