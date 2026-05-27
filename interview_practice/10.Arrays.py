def find_max(arr):
    max_val = arr[0]
    for el in arr:
        if el > max_val:
            max_val = el
    return max_val
    
print(find_max([4,1,10,8,3]))