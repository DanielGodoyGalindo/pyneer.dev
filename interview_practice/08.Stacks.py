def is_valid(s):
    
    # Create a mapping dictionary: {')': '(', '}': '{', ']': '['}
    # Initialize an empty list to use as a stack
    # Iterate through each character in the string
    #   If character is a closing bracket (in mapping):
    #     Check if stack is empty, return False if so
    #     Pop from stack and check if it matches the opening bracket
    #     If no match, return False
    #   Else (opening bracket):
    #     Push to stack
    # After loop, return True if stack is empty, False otherwise
    
    mapping_dict = {")": "(", "}": "{", "]": "["}
    stack = []

    for ch in s:
        if ch in mapping_dict:
            if not stack:
                return False
            popped = stack.pop()
            if popped != mapping_dict[ch]:
                return False
        else:
            stack.append(ch)

    return len(stack) == 0
