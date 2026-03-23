def cache(func):
    storage = {}
    
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if args not in storage:
            storage[key] = func(*args, **kwargs)
        return storage[key]
    
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
    print(my_sum(a=1, b=2))
    print(my_sum(1, b=2))
    print(my_sum(42, 42))
    print(my_sum(42, 42))

    print(fib(10))

