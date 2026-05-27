def transpose_matrix(matrix):
    # Initialize an empty 2x2 grid
    transposed = [[0, 0], [0, 0]]
    
    for i in range(2):
        for j in range(2):
            # Swap rows and columns
            transposed[j][i] = matrix[i][j]
            
    return transposed

# Our test matrix
original_matrix = [[1, 2], [3, 4]]

print("Original Matrix:")
for row in original_matrix:
    print(row)

print("\nTransposed Matrix:")
output = transpose_matrix(original_matrix)
for row in output:
    print(row)
