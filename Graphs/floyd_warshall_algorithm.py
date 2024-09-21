
def floyd_warshall(matrix):
    n = len(matrix)
    m = len(matrix[0])
    for k in range(0,n):
        for i in range(0,n):
            for j in range(0,n):
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
    return matrix

if __name__ == '__main__':
    matrix = [[0, 1, 43],[1, 0, 6],[float('inf'), float('inf'), 0]]
    print(floyd_warshall(matrix))

