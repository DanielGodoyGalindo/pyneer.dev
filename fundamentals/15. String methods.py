def split_and_join(text, separator):
    # Split text by separator, then join with "-"
    # Example: split_and_join("a,b,c", ",") -> "a-b-c"
    splitted=text.split(separator)
    output="-".join(splitted)
    return output
print(split_and_join("a,b,c",","))

def clean_string(text):
    # Remove leading/trailing whitespace and convert to lowercase
    # Example: clean_string("  HELLO  ") -> "hello"
    return text.strip().lower()
print(clean_string("  HELLO  "))

def replace_all(text, old, new):
    # Replace all occurrences of old with new
    # Example: replace_all("hello", "l", "L") -> "heLLo"
    return text.replace(old,new)
print(replace_all("hello", "l", "L"))

def split_into_words(text):
    # Split text into words using default whitespace separator
    # Example: split_into_words("hello world") -> ["hello", "world"]
    return text.split()
print(split_into_words("hello world"))

def join_with_comma(items):
    # Join all items in the list using "," as separator
    # Example: join_with_comma(["a","b","c"]) -> "a,b,c"
    # return items.join(",")
    return ",".join(items)
print(join_with_comma(["a","b","c"]))

def strip_spaces(text):
    # Remove leading and trailing whitespace using strip()
    # Example: strip_spaces("  hello  ") -> "hello"
    return text.strip()
print(strip_spaces("  hello  "))

def replace_vowels(text):
    # Replace all vowels with "*" using replace()
    # Example: replace_vowels("hello") -> "h*ll*"
    for letter in "aeiou":
        text = text.replace(letter, "*")
    return text
print(replace_vowels("hello"))

def to_uppercase(text):
    # Convert text to uppercase using upper()
    # Example: to_uppercase("hello") -> "HELLO"
    return text.upper()
print(to_uppercase("hello"))

def to_lowercase(text):
    # Convert text to lowercase using lower()
    # Example: to_lowercase("HELLO") -> "hello"
    return text.lower()
print(to_uppercase("GOODBYE"))

def starts_with_prefix(text, prefix):
    # Return True if text starts with prefix using startswith()
    # Example: starts_with_prefix("hello", "he") -> True
    return text.startswith(prefix)
print(starts_with_prefix("hello", "he"))

def ends_with_suffix(text, suffix):
    # Return True if text ends with suffix using endswith()
    # Example: ends_with_suffix("hello", "lo") -> True
    return text.endswith(suffix)
print(ends_with_suffix("hello", "lo"))

def find_substring(text, sub):
    # Return the index of the first occurrence of sub using find()
    # Example: find_substring("hello", "l") -> 2
    return text.find(sub)
print(find_substring("hello", "l"))

def count_substring(text, sub):
    # Count how many times sub appears in text using count()
    # Example: count_substring("hello", "l") -> 2
    return text.count(sub)
print(count_substring("hello", "l"))
