def group_anagrams(strs):
    # Create an empty dictionary to store groups
    # For each string in strs:
    #   Sort the characters of the string to create a key
    #   Convert sorted list back to string (join)
    #   If key not in dictionary, initialize with empty list
    #   Append original string to dictionary[key]
    # Return list of all dictionary values
    dictionary = {}
    for str in strs:
        key = sorted(str)
        key = ''.join(key)
        if key not in dictionary:
            dictionary[key] = []
        dictionary[key].append(str)
    return list(dictionary.values())

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))