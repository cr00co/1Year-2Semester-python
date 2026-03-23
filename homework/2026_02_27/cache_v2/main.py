import pickle
import os
import functools

def cache_v2(filename, use_kwargs=False):
    def decorator(func):
        cache = {}
        if os.path.exists(filename):
            with open(filename, "rb") as f:
                cache = pickle.load(f)
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = tuple(sorted(kwargs.items())) if use_kwargs else args

            if key not in cache:
                cache[key] = func(*args, **kwargs)
                with open(filename, "wb") as f:
                    pickle.dump(cache, f)
            
            return cache[key]
        
        return wrapper
    return decorator

@cache_v2("2026_02_27/cache_v2/my_cache.pkl")
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

if __name__ == "__main__":
    print("|Fibonacci sequence calc|")
    n = int(input("Enter number of the element: "))
    print(f"Value of the {n} element: {fib(n)}")
    
    print("\nThe data in the cache file:")
    with open("2026_02_27/cache_v2/my_cache.pkl", "rb") as f:
        cache = pickle.load(f)
    
    for key, value in cache.items():
        print(f"{key[0]} - {value}")