# TODO: Complete the boolean operations

def practice_booleans():
    # 1. Compare: 10 == 10, store in result1
    result1 = (10 == 10)
    # 2. Compare: 5 != 3, store in result2
    result2 = (5 != 3)
    # 3. Compare: 7 < 10, store in result3
    result3 = (7 < 10)
    # 4. Compare: 15 > 12, store in result4
    result4 = 15>12
    # 5. Compare: 8 <= 8, store in result5
    result5 = 8<=8
    # 6. Compare: 20 >= 25, store in result6
    result6 = 20 >=25
    # 7. Logical: True and False, store in result7
    result7 = True and False
    # 8. Logical: True or False, store in result8
    result8 = True or False
    # 9. Logical: not True, store in result9
    result9 = not True
    # 10. Combined: (5 > 3) and (10 < 15), store in result10
    result10 = (5>3) and (10<15)
    # 11. Combined: (5 > 10) or (8 < 12), store in result11
    result11 = (5>10) or (8<12)
    # 12. Complex: not ((5 > 10) and (8 < 12)), store in result12
    result12 = not ((5>10) and (8<12))
    # 13. Check if age (25) is between 18 and 65, store in is_valid_age
    is_valid_age = (25 > 18) and (25 < 65)
    # 14. Check if score (85) is passing (>= 60), store in is_passing
    is_passing = (85 >= 60)
    # Return dictionary with all results
    return {
        "result1":result1, "result2":result2, "result3":result3, "result4": result4,
        "result5": result5, "result6": result6, "result7": result7, "result8": result8,
        "result9": result9, "result10": result10, "result11": result11, "result12": result12,
        "is_valid_age": is_valid_age, "is_passing": is_passing
        }
    

# Test your function
result = practice_booleans()
print(result)
