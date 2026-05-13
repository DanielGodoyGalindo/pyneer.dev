# TODO: Complete the module exercises
# You'll need to import: math, random, datetime
import math, random, datetime

def calculate_circle_area(radius):
    # Use math module to calculate circle area
    # Area = π * r²
    # Import math and use math.pi
    return math.pi * (radius**2)
    

def get_random_number(min_val, max_val):
    # Use random module to generate random integer between min_val and max_val
    # Import random and use random.randint()
    return random.randint(min_val, max_val)

def get_current_date():
    # Use datetime module to get current date
    # Import datetime and use datetime.date.today()
    # Return the date object
    return datetime.date.today()

def calculate_square_root(number):
    # Use math module to calculate square root
    # Import math and use math.sqrt()
    return math.sqrt(number)

def pick_random_item(items):
    # Use random module to pick random item from list
    # Import random and use random.choice()
    return random.choice(items)

def get_pi():
    # Use math module to get the value of π (pi)
    # Import math and return math.pi
    return math.pi

# Test your functions
print("Circle area (radius=5):", calculate_circle_area(5))
print("Random number (1-10):", get_random_number(1, 10))
print("Current date:", get_current_date())
print("Square root of 16:", calculate_square_root(16))
print("Random item:", pick_random_item(['apple', 'banana', 'cherry']))
print("Pi value:", get_pi())
