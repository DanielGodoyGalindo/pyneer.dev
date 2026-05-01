def print_before_after(func):
    # Create a decorator that prints "Before" before function call
    # and "After" after function call
    # Then return the result
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, *kwargs)
        print("After")
        return result
    return wrapper

@print_before_after
def greet(name):
    return f"Hello, {name}!"

# Test the decorator
result = greet("Alice")
# Should print:
# Before
# After
# result = "Hello, Alice!"
