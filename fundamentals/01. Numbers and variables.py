# TODO: Complete the following operations

# 1. Create variables: age (integer 25), height (float 5.9), count (integer 0)

# 2. Calculate: 15 + 7 and store in result1

# 3. Calculate: 20 - 8 and store in result2

# 4. Calculate: 6 * 7 and store in result3

# 5. Calculate: 15 / 4 (division) and store in result4

# 6. Calculate: 15 // 4 (floor division) and store in result5

# 7. Calculate: 15 % 4 (modulo) and store in result6

# 8. Calculate: 2 ** 8 (exponentiation) and store in result7

# 9. Convert float 3.7 to integer and store in converted_int

# 10. Convert integer 42 to float and store in converted_float

# Return a dictionary with all results:
# {
#   'age': age,
#   'height': height,
#   'count': count,
#   'result1': result1,
#   'result2': result2,
#   'result3': result3,
#   'result4': result4,
#   'result5': result5,
#   'result6': result6,
#   'result7': result7,
#   'converted_int': converted_int,
#   'converted_float': converted_float
# }

def practice_numbers_and_variables():
    # Your code here
    age: int = 25
    height: float = 5.9
    count: int = 0

    result1 = 15 + 7
    result2 = 20-8
    result3 = 6*7
    result4 = 15/4
    result5 = 15//4
    result6 = 15 % 4
    result7 = 2 ** 8
    converted_int = int(3.7)
    converted_float = float(42)

    return {
        'age':age, 'height':height, 'count':count,
        'result1': result1, 
        'result2':result2,
        'result3': result3,
        'result4': result4,
        'result5': result5,
        'result6': result6,
        'result7': result7,
        'converted_int': converted_int,
        'converted_float': converted_float
        }
    pass

# Test your function
result = practice_numbers_and_variables()
print(result)
