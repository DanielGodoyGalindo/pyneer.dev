# TODO: Complete the function definitions

def add(a, b):
    # Return the sum of a and b
    return a+b

def multiply(x, y):
    # Return the product of x and y
    return x*y

def greet(name):
    # Return a greeting string: "Hello, {name}!"
    return f"Hello, {name}!"

def calculate_area(length, width):
    # Calculate and return the area of a rectangle
    return length*width

def power(base, exponent=2):
    # Calculate base raised to exponent
    # Default exponent should be 2
    return base**exponent

def get_full_name(first, last, middle=""):
    # Return full name
    # If middle is provided, return "first middle last"
    # Otherwise, return "first last"
    return f"{first} {last}" if middle == "" else f"{first} {middle} {last}"

def min_max(numbers):
    # Return a tuple containing (minimum, maximum) from the numbers list
    return (min(numbers), max(numbers))

def is_even(num):
    # Return True if num is even, False otherwise
    return True if (num % 2 == 0) else False

# Test your functions
print("Add:", add(3, 5))  # Should be 8
print("Multiply:", multiply(4, 7))  # Should be 28
print("Greet:", greet("Alice"))  # Should be "Hello, Alice!"
print("Area:", calculate_area(5, 10))  # Should be 50
print("Power:", power(3))  # Should be 9 (default exponent=2)
print("Power:", power(2, 4))  # Should be 16
print("Full name:", get_full_name("John", "Doe"))  # Should be "John Doe"
print("Full name:", get_full_name("John", "Doe", "Middle"))  # Should be "John Middle Doe"
print("Min/Max:", min_max([3, 1, 4, 1, 5]))  # Should be (1, 5)
print("Is even:", is_even(4))  # Should be True
print("Is even:", is_even(7))  # Should be False
