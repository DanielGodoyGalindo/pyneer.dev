def safe_get(d, key, default):
    # Use get() to safely retrieve value or return default
    # Example: safe_get({"a": 1}, "b", 0) -> 0
    return d.get(key, default)

def get_all_items(d):
    # Return list of all (key, value) pairs using items()
    # Example: get_all_items({"a": 1, "b": 2}) -> [("a", 1), ("b", 2)]
    return list(d.items())

def merge_dicts(d1, d2):
    # Update d1 with all key-value pairs from d2 using update()
    # Return the updated d1
    # Example: merge_dicts({"a": 1}, {"b": 2}) -> {"a": 1, "b": 2}
    d1.update(d2)
    return d1

def dict_to_pairs(d):
    # Convert the dictionary into a list of (key, value) tuples using items()
    # Example: dict_to_pairs({"a": 1, "b": 2}) -> [("a", 1), ("b", 2)]
    return list(d.items())

def has_key(d, key):
    # Return True if the key exists in the dictionary using keys()
    # Example: has_key({"x": 10}, "x") -> True
    keys = d.keys()
    return True if key in keys else False

def pop_or_default(d, key, default):
    # Remove the key from the dictionary and return its value
    # If the key does not exist, return the provided default
    # Example: pop_or_default({"a": 1}, "a", 0) -> 1
    return d.pop(key, default)

def merge_three(d1, d2, d3):
    # Update d1 with all key-value pairs from d2 and d3 using update()
    # Return the updated dictionary
    # Example: merge_three({"a":1}, {"b":2}, {"c":3}) -> {"a":1,"b":2,"c":3}
    d1.update(d2)
    d1.update(d3)
    return d1

def reset_dict(d):
    # Remove all items from the dictionary using clear()
    # Return the now-empty dictionary
    # Example: reset_dict({"a":1}) -> {}
    d.clear()
    return d

def clone_and_add(d, key, value):
    # Create a shallow copy of the dictionary using copy()
    # Add a new key-value pair to the copy
    # Return the modified copy without changing the original
    # Example: clone_and_add({"a":1}, "b", 2) -> {"a":1, "b":2}
    new_dict = d.copy()
    new_dict[key] = value
    return new_dict

def invert_dict(d):
    # Return a new dictionary where keys become values and values become keys
    # Use items() to iterate over the dictionary
    # Example: invert_dict({"a":1, "b":2}) -> {1:"a", 2:"b"}
    return {v: k for k, v in d.items()}
