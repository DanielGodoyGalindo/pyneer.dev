def max_sum_subarray(arr, k):
    # Calculate sum of first k elements
    # Initialize max_sum with this sum
    # Iterate from index k to end:
    #   Subtract arr[i-k] (element leaving window)
    #   Add arr[i] (element entering window)
    #   Update max_sum = max(max_sum, current_sum)
    # Return max_sum
    current_sum = sum(arr[:k])
    max_sum = current_sum
    for idx in range(k, len(arr)):
        current_sum = current_sum - arr[idx-k] + arr[idx]
        max_sum = max(current_sum, max_sum)
    return max_sum