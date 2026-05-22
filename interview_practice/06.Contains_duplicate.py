def contains_duplicate(nums):
    # Create an empty set to track seen elements
    # Iterate through each number in nums
    # If number is already in set, return True (duplicate found)
    # Otherwise, add number to set
    # If loop completes, return False (no duplicates)
    seen_elements = {}
    for num in nums:
        if num in seen_elements:
            return True
        seen_elements[num] = True
    return False

print(contains_duplicate([1,2,3,4,2]))