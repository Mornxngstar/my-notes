from os import system
import time
from typing import List

class FiboIter:

    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self
    
    def __next__(self):

        if self.counter > self.max:
            raise StopIteration
        elif self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        else:
            self.aux = self.n1 + self.n2
            self.n1, self.n2 = self.n2, self.aux
            self.counter += 1
            return self.aux

def run():
    try:
        times = int(input("How many numbers do you want this sequence to have? ")) - 1 
    except ValueError:
        run()

    fibonacci = FiboIter(times)
    for i in fibonacci:
        print(i)
        time.sleep(0.5)

if __name__ == '__main__':
    run()
    

