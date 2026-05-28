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


def find_missing(arr):
    # Calculate n (length of array)
    # Calculate expected sum: n * (n + 1) // 2 (sum of 0 to n)
    # Calculate actual sum: sum(arr)
    # Return expected - actual (the missing number)
    length = len(arr)
    expected_sum = length * (length + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum


print(find_missing([0, 1, 3]))


def rotate_array(arr, k):
    # Handle edge case: empty array
    # Normalize k: k = k % len(arr) (handles k > len(arr))
    # Use slicing: arr[-k:] gets last k elements, arr[:-k] gets rest
    # Concatenate: return arr[-k:] + arr[:-k]
    # For detailed slicing explanation, see Array/List Slicing in Python Basics
    if not arr:
        return arr
    k = k % len(arr)
    return arr[-k:] + arr[:-k]


print(rotate_array([1, 2, 3, 4, 5], 2))
