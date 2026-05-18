def squares_list(n):
    return [x**2 for x in range(n)]

print(squares_list(5))

def evens_only(arr):
    return [x for x in arr if x%2==0]

print(evens_only([2,4,7,9,10]))

def square_dict(n):
    return {x: x**2 for x in range(n)}

print(square_dict(5))