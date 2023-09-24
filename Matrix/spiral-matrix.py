#Question: Spiral Matrix
# Given an m x n matrix, return all elements of the matrix in spiral order.
#Approach:
# Repeatedly add the first row of the matrix to the result and rotate the remaining matrix counterclockwise until all elements are processed. 
# Time & Space complexity: O(m * n)

def spiral_matrix(matrix):
    res=[]

    while matrix:
        res+=matrix[0]
        matrix=list(zip(*matrix[1:]))[::-1]
    return res

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
print(spiral_matrix(matrix))

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
print(spiral_matrix(matrix))
