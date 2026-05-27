def find_max(arr):
    # Initialize max_val with the first element of the array
    # Iterate through the remaining elements
    # Compare each element with max_val
    # Update max_val if current element is larger
    # Return max_val
    max_val = arr[0]
    for el in arr:
        if el > max_val:
            max_val = el
    return max_val


print(find_max([4, 1, 10, 8, 3]))


def remove_duplicates(arr):
    # Create an empty set to track seen elements
    # Create an empty list for the result
    # Iterate through each item in arr:
    #   If item not in seen set:
    #     Add item to seen set
    #     Append item to result list
    # Return result list (preserves order)
    seen = set()
    result = []
    for el in arr:
        if el not in seen:
            seen.add(el)
            result.append(el)
    return result


print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
