# TODO: Complete the tuple exercises

def create_tuple():
    # Create and return a tuple with three elements: 1, 2, 3
    return (1,2,3)

def get_first_last(t):
    # Return a tuple containing (first_element, last_element) from tuple t
    return (t[0],t[-1])

def count_element(t, element):
    # Return how many times element appears in tuple t
    # Use the count() method
    return t.count(element)

def find_index(t, element):
    # Return the index of first occurrence of element in tuple t
    # Use the index() method
    # Return -1 if element not found (handle ValueError)
    try:
        return t.index(element)
    except ValueError:
        return -1

def unpack_coordinates(point):
    # Unpack tuple point into x and y variables
    # Return a tuple (x, y)
    x,y = point
    return (x,y)

def swap_values(a, b):
    # Swap the values of a and b using tuple unpacking
    # Return a tuple (a, b) with swapped values
    return (b,a)

def concatenate_tuples(t1, t2):
    # Concatenate two tuples and return the result
    return (t1+t2)

def repeat_tuple(t, n):
    # Repeat tuple t, n times and return the result
    return t*n

# Test your functions
print("Create tuple:", create_tuple())  # Should be (1, 2, 3)
print("First/Last:", get_first_last((10, 20, 30, 40)))  # Should be (10, 40)
print("Count:", count_element((1, 2, 2, 3, 2), 2))  # Should be 3
print("Index:", find_index((10, 20, 30), 20))  # Should be 1
print("Unpack:", unpack_coordinates((5, 10)))  # Should be (5, 10)
print("Swap:", swap_values(3, 7))  # Should be (7, 3)
print("Concatenate:", concatenate_tuples((1, 2), (3, 4)))  # Should be (1, 2, 3, 4)
print("Repeat:", repeat_tuple((1, 2), 3))  # Should be (1, 2, 1, 2, 1, 2)
