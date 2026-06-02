def max_area(height):
    # Initialize left=0, right=len(height)-1, max_area=0
    # While left < right:
    #   Calculate current area = min(height[left], height[right]) × (right - left)
    #   Update max_area = max(max_area, current_area)
    #   If height[left] < height[right]:
    #     Move left pointer right (left += 1)
    #   Else:
    #     Move right pointer left (right -= 1)
    # Return max_area
    left = 0
    right = len(height) - 1
    max_area = 0
    while left < right:
        current_area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, current_area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area


def three_sum(nums):
    # Sort the array
    # Initialize result list
    # For i from 0 to len(nums)-3:
    #   Skip if i > 0 and nums[i] == nums[i-1] (duplicate)
    #   Set left = i+1, right = len(nums)-1
    #   While left < right:
    #     Calculate sum = nums[i] + nums[left] + nums[right]
    #     If sum == 0:
    #       Add [nums[i], nums[left], nums[right]] to result
    #       Skip duplicates for left and right
    #     Elif sum < 0: move left++
    #     Else: move right--
    # Return result
    nums = sorted(nums)
    result = []
    for i in range(0, len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left = i + 1
        right = len(nums) - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif current_sum < 0:
                left += 1
            else:
                right -= 1
    return result
