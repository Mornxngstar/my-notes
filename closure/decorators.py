from datetime import datetime

def execution_time(func):

    def wrapper(*args, **kwargs):
        intitial_time = datetime.now()
        func(*args,**kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - intitial_time
        print("It's been", str(time_elapsed.total_seconds()), "seconds")

    return wrapper

@execution_time
def random_func():
    for _ in range(1, 10000000):
        pass

@execution_time
def addition(a:int, b:int) -> int :
    return a + b

people = {
    'name': 'Josh'
}

@execution_time
def add_ages(people):
    people.update({'age':18})

random_func()
addition(10000,555555)
add_ages(people)
