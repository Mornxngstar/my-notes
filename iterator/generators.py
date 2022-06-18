
import time

def gen(max_num):
    num1, num2 = 0, 1
    counter = 0

    while counter <= max_num:
        yield num1
        num1, num2 = num2, num1 + num2
        counter += 1

def run():
    try:
        times = int(input("How many numbers do you want this sequence to have? ")) 
    except ValueError:
        run()
    fibo = gen(times)
    for i in fibo:
        print(i)

if __name__ == '__main__':
    run()