def cache(func):
    storage = {}
    
    def wrapper(*args):
        if args not in storage:
            storage[args] = func(*args)
            print("added:", args, storage[args])
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
    print(my_sum(1, 2))
    print(my_sum(1, 2))
    print(my_sum(42, 42))
    print(my_sum(42, 42))

    print(fib(10))

