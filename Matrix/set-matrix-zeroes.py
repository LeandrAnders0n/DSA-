#Question: Set Matrix Zeroes
# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place.

#Approach:
# Set all the rows and columns to 0 in a given m x n  matrix where an element is 0. First, identify the rows and columns containing zeros by iterating through the matrix. Then, iterate through the identified rows and columns and set all elements in those rows and columns to 0.

# Time Complexity: O(m * n), where m is the number of rows and n is the number of columns in the matrix.
# Space Complexity: O(m + n), as we use sets zero_rows and zero_cols to store the row and column indices containing zeros.


def set_zeroes(matrix):
    rows,cols=len(matrix),len(matrix[0])
    zero_cols,zero_rows=set(),set()

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j]==0:
                zero_cols.add(j)
                zero_rows.add(i)

    for row in zero_rows:
        for j in range(cols):
            matrix[row][j]=0
    
    for col in zero_cols:
        for j in range(rows):
            matrix[i][col]=0
    return matrix


matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
print(set_zeroes(matrix))

matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
print(set_zeroes(matrix))
