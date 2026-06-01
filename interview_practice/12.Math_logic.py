def is_power_of_two(n):
    # Edge case: n must be positive
    # Use bit manipulation: n & (n-1) == 0
    # This works because powers of 2 have exactly one '1' bit
    # Return True if condition is met, False otherwise
    if n <= 0:
        return False
    return True if n & (n-1) == 0 else False