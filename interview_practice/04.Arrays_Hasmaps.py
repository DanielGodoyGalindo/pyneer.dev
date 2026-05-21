def two_sum(nums, target):
    # Create an empty dictionary to store {number: index}
    # Use enumerate() to iterate with both index and value
    # For each number, calculate diff = target - num
    # Check if diff exists in dictionary
    # If found, return [stored_index, current_index]
    # If not found, store current number and index in dictionary
    dictionary = {}
    for idx, num in enumerate(nums):
        diff = target - num
        if diff in dictionary:
            return [dictionary[diff], idx]
        dictionary[num] = idx

print(two_sum([2,7,11,15], 26))