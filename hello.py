# Function to multiply two 2x2 matrices
def multiply_matrices(A, B):
    # Create a 2x2 result matrix filled with zeros
    result = [[0, 0], 
              [0, 0]]
              
    # Loop through rows of A
    for i in range(2):
        # Loop through columns of B
        for j in range(2):
            # Loop to calculate dot product
            for k in range(2):
                result[i][j] += A[i][k] * B[k][j]
                
    return result

# Define two 2x2 matrices (Unit 1 Math Style!)
matrix_A = [[1, 2], 
            [3, 4]]

matrix_B = [[5, 6], 
            [7, 8]]

# Run the multiplication
output = multiply_matrices(matrix_A, matrix_B)

print("Matrix A x Matrix B Result:")
for row in output:
    print(row)
