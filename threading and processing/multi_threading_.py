import threading
import time

def eat_breakfast():
    time.sleep(3)
    print("Breakfast finished")

def drink(*drink):
    time.sleep(4)
    print(f"{drink[0]} time is done")

def study():
    time.sleep(5)
    print("Study time is done")

x = threading.Thread(target=eat_breakfast)
y = threading.Thread(target=drink, args=('Coffee',))
z = threading.Thread(target=study)
x.start()
y.start()
z.start()

y.join()

print(threading.active_count())
print(threading.enumerate())