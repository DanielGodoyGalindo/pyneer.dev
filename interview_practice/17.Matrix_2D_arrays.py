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


def rotate(matrix):
    # Method 1: Transpose then reverse rows
    # Step 1: Transpose (swap matrix[i][j] with matrix[j][i] for i < j)
    # Step 2: Reverse each row

    # Or Method 2: Layer-by-layer rotation
    # For each layer from outer to inner:
    #   Rotate four corners, then move to next position
    
    # Input: [[1,2,3],[4,5,6],[7,8,9]]
    # Output: [[7,4,1],[8,5,2],[9,6,3]]

    n = len(matrix)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i].reverse()
    
    return matrix
        
print(rotate([[1,2,3],[4,5,6],[7,8,9]]))
