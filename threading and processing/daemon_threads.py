import threading
import time

def timer():
    print("\n\n")
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for:", count, "seconds.")

x = threading.Thread(target=timer, daemon=True)
# x.setDaemon(True)
x.start()

y = x.isDaemon()
input("Do you want to exit? \n")
print(y)


