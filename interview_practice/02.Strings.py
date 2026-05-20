from collections import Counter


def reverse_string(s):
    # Use string slicing with negative step to reverse
    # Syntax: s[::-1] returns the string in reverse order
    # Return the reversed string
    return s[::-1]


def is_palindrome(s):
    # Compare the string with its reverse
    # Use slicing s[::-1] to get the reversed string
    # Return True if they are equal, False otherwise
    return True if s == s[::-1] else False


def count_vowels(s):
    # Convert string to lowercase for case-insensitive comparison
    # Iterate through each character
    # Check if character is in "aeiou" using the 'in' operator
    # Count and return the total number of vowels
    count_vowels = 0
    s_lower = s.lower()
    for ch in s_lower:
        if ch in "aeiou":
            count_vowels += 1
    return count_vowels


def is_anagram(s1, s2):
    # Sort both strings and compare them
    # sorted() returns a list of characters, so compare the lists
    # Return True if they are equal (same characters), False otherwise
    # Note: This approach has O(n log n) time complexity
    s1_sorted = sorted(s1)
    s2_sorted = sorted(s2)
    return True if s1_sorted == s2_sorted else False


def is_anagram_optimized(s1, s2):
    # Option 1: Use Counter from collections module
    #   from collections import Counter
    #   return Counter(s1) == Counter(s2)
    #
    # Option 2: Manual counting with dictionary
    #   Check if lengths are equal first
    #   Count characters in s1, decrement for s2
    #   If any count goes negative, return False
    #   Return True if all counts are zero
    return Counter(s1) == Counter(s2)
