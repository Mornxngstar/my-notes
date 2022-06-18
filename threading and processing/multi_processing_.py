from multiprocessing import Process, cpu_count
import time
start = time.perf_counter()

def counter(num):
    count = 0
    while count < num:
        count += 1

def run():
    a = Process(target=counter, args=(10000000,))
    a.start()
    a.join()

    print("Finished in: "+ str(round(time.perf_counter() - start, 4)) + " seconds.")


if __name__ == '__main__':
    run()   
