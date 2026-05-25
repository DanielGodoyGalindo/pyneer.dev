def is_valid(s):
    mapping_dict = {")": "(", "}": "{", "]": "["}
    stack = []

    for ch in s:
        if ch in mapping_dict:  # es un cierre
            if not stack:
                return False
            popped = stack.pop()
            if popped != mapping_dict[ch]:
                return False
        else:
            stack.append(ch)

    return len(stack) == 0
