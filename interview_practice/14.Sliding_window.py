def length_of_longest_substring(s):
    # Initialize left pointer, max_length, and char_map dictionary
    # Iterate with right pointer through string
    # If character at right is in char_map and within window:
    #   Move left pointer to max(left, char_map[char] + 1)
    # Update char_map with current character's position
    # Update max_length = max(max_length, right - left + 1)
    # Return max_length
    left_pointer = 0
    max_length = 0
    char_map = {}
    for idx, char in enumerate(s):
        if char in char_map and char_map[char] >= left_pointer:
            left_pointer = char_map[char] + 1
        char_map[char] = idx
        max_length = max(max_length, idx - left_pointer + 1)
    return max_length