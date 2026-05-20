def fizz_buzz(n):
    # Initialize an empty list to store results
    # Loop through numbers from 1 to n (inclusive)
    # Check divisibility using modulo operator (%)
    # Order matters: check 15 first (both 3 and 5), then 3, then 5
    # Append appropriate string or number to the result list
    # Return the result list
    results = list()
    for i in range(1,n+1):
        if i % 15 == 0:
            results.append("FizzBuzz")
        elif i % 3 == 0:
            results.append("Fizz")
        elif i % 5 == 0:
            results.append("Buzz")
        else:
            results.append(i)
    return results