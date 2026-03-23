import functools

def retry(count):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(count):
                try:
                    return func(*args, **kwargs)
                except ValueError:
                    pass
                except OSError:
                    print(f"{func.__name__} raise OsError exception.")
        
        return wrapper
    return decorator