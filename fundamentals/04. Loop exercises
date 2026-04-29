# TODO: Complete the loop exercises

def sum_list(numbers):
    # Use a for loop to sum all numbers in the list
    # Return the total
    sum = 0
    for num in numbers:
        sum+=num
    return sum

def count_evens(numbers):
    # Use a for loop to count how many even numbers are in the list
    # Return the count
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count+=1
    return count

def print_range(start, stop):
    # Use a for loop with range() to print numbers from start to stop-1
    # Don't return anything, just print each number
    for num in range(start, stop):
        print(num)

def find_first_negative(numbers):
    # Use a for loop to find the first negative number
    # Return the number, or None if no negative numbers found
    # Use break when you find it
    for num in numbers:
        if num < 0:
            return num
    return None

def skip_odds(numbers):
    # Use a for loop with continue to skip odd numbers
    # Return a list containing only even numbers
    even_numbers = []
    for num in numbers:
        if num % 2 != 0:
            continue
        even_numbers.append(num)
    return even_numbers

def countdown(n):
    # Use a while loop to countdown from n to 1
    # Print each number, then return "Done!"
    while n>=1:
        print(n)
        n-=1
    return "Done!"

def sum_until_negative(numbers):
    # Use a while loop to sum numbers until you encounter a negative
    # Return the sum
    # Hint: Use an index variable and check if number is negative
    i = 0
    positive_sum = 0
    while i < len(numbers):
        if numbers[i] > -1:
            positive_sum+= numbers[i]
        else:
            break
        i+=1
    return positive_sum

# Test your functions
print("Sum:", sum_list([1, 2, 3, 4, 5]))  # Should be 15
print("Evens:", count_evens([1, 2, 3, 4, 5, 6]))  # Should be 3
print_range(1, 5)  # Should print 1, 2, 3, 4
print("First negative:", find_first_negative([1, 2, -3, 4]))  # Should be -3
print("Skip odds:", skip_odds([1, 2, 3, 4, 5, 6]))  # Should be [2, 4, 6]
countdown(3)  # Should print 3, 2, 1
print("Sum until negative:", sum_until_negative([1, 2, 3, -1, 4]))  # Should be 6
