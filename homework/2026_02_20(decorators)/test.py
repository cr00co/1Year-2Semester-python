import time

def timer(func):
    def wrapper():
        time_1 = time.time()
        func()
        time_2 = time.time()
        result = time_2 - time_1
        print(f"runtime: {result}")
    return wrapper

@timer
def some_func():
    time.sleep(2)
    l = [i for i in range(1000000)]


some_func()