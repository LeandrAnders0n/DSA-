# Question: Transpose of Matrix
# Suppose there is a 2d matrix. 
# Find the transpose of it and multiply the original and the transposed matrix and output the result. 
#Approach:The given code defines a function transpose_multiply that takes a matrix as input. 
# It first computes the transpose of the input matrix by swapping rows and columns. 
# Then, it performs matrix multiplication by iterating through each row of the original matrix and each column of the transpose matrix, calculating the product.
#Time Complexity: O(N * M^2)
#Space Complexity: O(M * N + N^2), where N is the number of rows and M is the number of columns in the input matrix.

def transpose_multiply(matrix):

    transpose=[[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

    result=[[sum(matrix_row[k]*transpose_col[k] for k in range(len(matrix[0]))) for transpose_col in transpose] for matrix_row in matrix]

    return result


original_matrix = [[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]]

print(transpose_multiply(original_matrix))
