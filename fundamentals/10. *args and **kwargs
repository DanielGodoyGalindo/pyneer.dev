# TODO: Complete the *args and **kwargs exercises

def sum_all(*args):
    # Sum all numbers passed as positional arguments
    # args is a tuple of all arguments
    result = 0
    for num in args:
        result+=num
    return result

def print_info(**kwargs):
    # Print all key-value pairs from keyword arguments
    # kwargs is a dictionary
    # Format: "key: value" for each pair
    for key, value in kwargs.items():
        print(f"{key}: {value}")

def create_profile(name, *skills, **details):
    # Create a profile dictionary
    # name: required positional argument
    # *skills: variable positional arguments (tuple of skills)
    # **details: variable keyword arguments (dictionary of additional info)
    # Return: {"name": name, "skills": list of skills, **details}
    return {"name": name, "skills": list(skills), **details}

def calculate_total(price, *discounts, tax=0.1, **fees):
    # Calculate total price
    # price: base price
    # *discounts: variable discounts to subtract
    # tax: default 0.1 (10%), can be overridden
    # **fees: additional fees to add
    # Return: price - sum(discounts) + (price * tax) + sum(fees.values())
    return price - sum(list(discounts)) + (price * tax) + sum(fees.values())

def flexible_greet(greeting, *names, **options):
    # Create a greeting message
    # greeting: required (e.g., "Hello")
    # *names: variable names to greet
    # **options: additional options like punctuation, separator
    # If punctuation in options, use it, else use "!"
    # If separator in options, use it, else use ", "
    # Return: greeting + separator.join(names) + punctuation
    return f"Greet: {greeting} {options["separator"].join(names) if options["separator"] else ', '.join(names)}{options["punctuation"] if options["punctuation"] else '!'}"

# Test your functions
print("Greet:", flexible_greet("Hi", "Alice", "Bob", punctuation="?", separator=" and "))
