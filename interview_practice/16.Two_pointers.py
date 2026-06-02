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
