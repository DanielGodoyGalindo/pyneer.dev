def spiral_order(matrix):
    # Initialize result list
    # Set boundaries: top=0, bottom=len(matrix)-1, left=0, right=len(matrix[0])-1
    # While top <= bottom and left <= right:
    #   Traverse right: top row from left to right
    #   top += 1
    #   Traverse down: right column from top to bottom
    #   right -= 1
    #   If top <= bottom: traverse left (bottom row from right to left)
    #   bottom -= 1
    #   If left <= right: traverse up (left column from bottom to top)
    #   left += 1
    # Return result
    result = []
    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1

    while top <= bottom and left <= right:
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result
