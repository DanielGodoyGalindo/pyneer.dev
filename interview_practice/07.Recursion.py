def factorial(n):
    # Base case: if n <= 1, return 1 (0! = 1, 1! = 1)
    # Recursive case: return n * factorial(n - 1)
    # This will build up the result: n * (n-1) * (n-2) * ... * 1
    if n <= 1:
        return 1
    return n * factorial(n - 1)
