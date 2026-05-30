import json
import os

def cache(filename, use_named=False):
    def decorator(func):
        storage = {}

        if os.path.exists(filename):
            with open(filename, 'r') as f:
                storage = json.load(f)

        def wrapper(*args, **kwargs):
            if use_named:
                key = str(tuple(sorted(kwargs.items())))
            elif len(args) == 1:
                key = str(args[0])
            else:
                key = str(args)

            if key not in storage:
                storage[key] = func(*args, **kwargs)
                with open(filename, 'w') as f:
                    json.dump(storage, f)

            return storage[key]

        return wrapper
    return decorator


@cache('2026_02_27/cache_v2/cache.json')
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

if __name__ == "__main__":
    print("|Fibonacci sequence calc|")
    n = int(input("Enter number of the element: "))
    print(f"Value of the {n} element: {fib(n)}")