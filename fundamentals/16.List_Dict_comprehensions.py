def squares_list(n):
    # Return list of squares from 0 to n-1 using list comprehension
    # Example: squares_list(5) -> [0, 1, 4, 9, 16]
    return [x**2 for x in range(n)]
print(squares_list(5))


def evens_only(arr):
    # Return list of even numbers from arr using list comprehension
    # Example: evens_only([1,2,3,4,5]) -> [2, 4]
    return [x for x in arr if x % 2 == 0]
print(evens_only([2, 4, 7, 9, 10]))


def square_dict(n):
    # Return dictionary mapping numbers to their squares using dict comprehension
    # Example: square_dict(5) -> {0:0, 1:1, 2:4, 3:9, 4:16}
    return {x: x**2 for x in range(n)}
print(square_dict(5))
