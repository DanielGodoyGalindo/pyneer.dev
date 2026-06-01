def first_unique_char(s):
    # Create dictionary to count character frequencies
    # First pass: count all characters in s
    # Second pass: iterate through s with index
    #   If count of character is 1, return index
    # If no unique character found, return -1
    character_frequencies = {}
    for char in s:
        if char not in character_frequencies:
            character_frequencies[char] = 0
        character_frequencies[char] += 1
    for idx, char in enumerate(s):
        if character_frequencies[char] == 1:
            return idx
    return -1

print(first_unique_char("loveleetcode"))