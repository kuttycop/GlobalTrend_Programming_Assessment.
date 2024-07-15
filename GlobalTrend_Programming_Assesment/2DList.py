def transposeMatrix(matrix):
    if not matrix:
        return []
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    transposedMatrix = [[0] * num_rows for _ in range(num_cols)]
    for i in range(num_rows):
        for j in range(num_cols):
            transposedMatrix[j][i] = matrix[i][j]
    return transposedMatrix
# Example 
matrix = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]
transposed = transposeMatrix(matrix)
for row in transposed:
    print(row)