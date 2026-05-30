def cache(func):
    storage = {}

    def wrapper(*args):
        if args not in storage:
            storage[args] = func(*args)
        return storage[args]
    
    return wrapper

@cache
def my_sum(a, b):
    return a + b

@cache
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

if __name__ == "__main__":
    print(my_sum(40, 27))
    print(my_sum(25, 42))

    print(fib(11))

