def solution(matrix):
    n = len(matrix)
    m = len(matrix[0])

    # Initialize matrices to track the arm lengths for each diagonal
    top_left = [[0] * m for _ in range(n)]
    top_right = [[0] * m for _ in range(n)]
    bottom_left = [[0] * m for _ in range(n)]
    bottom_right = [[0] * m for _ in range(n)]

    # Fill top_left and top_right matrices
    for i in range(n):
        for j in range(m):
            if i > 0 and j > 0 and matrix[i][j] == matrix[i - 1][j - 1]:
                top_left[i][j] = 1 + top_left[i - 1][j - 1]
            if i > 0 and j < m - 1 and matrix[i][j] == matrix[i - 1][j + 1]:
                top_right[i][j] = 1 + top_right[i - 1][j + 1]

    # Fill bottom_left and bottom_right matrices
    for i in range(n - 1, -1, -1):
        for j in range(m):
            if i < n - 1 and j > 0 and matrix[i][j] == matrix[i + 1][j - 1]:
                bottom_left[i][j] = 1 + bottom_left[i + 1][j - 1]
            if i < n - 1 and j < m - 1 and matrix[i][j] == matrix[i + 1][j + 1]:
                bottom_right[i][j] = 1 + bottom_right[i + 1][j + 1]

    max_size = 0
    best_center = None

    # Now find the largest X-shape
    for i in range(n):
        for j in range(m):
            # Find the minimum arm length for this cell (center of the X-shape)
            size = min(top_left[i][j], top_right[i][j], bottom_left[i][j], bottom_right[i][j])
            if size > max_size:
                max_size = size
                best_center = [i, j]
            elif size == max_size:
                # Tie-breaking for minimal row, then column
                if best_center is None or i < best_center[0] or (i == best_center[0] and j < best_center[1]):
                    best_center = [i, j]

    return best_center if best_center else [-1, -1]


# Example usage:
matrix = [
    [0, 0],
    [0, 0],
    [0, 2],
    [0, 0],
    [0, 6],
    [0, 0]
]
print(solution(matrix))  # Output: [-1, -1] because there are no valid X-shapes

