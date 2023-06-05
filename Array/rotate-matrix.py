# Question:
# Rotate a given 2d array by 90° clockwise or anticlockwise based on the flag(0 or 1) given- 0 for clockwise and 1 for anticlockwise 
#Approach:
# Clockwise rotation, the code reverses the rows of the array and then transposes it. 
# This is done by using zip(*arr[::-1]), which first reverses the order of the rows ([::-1]) and then uses zip to transpose the rows into columns.
# Anticlockwise rotation, the code transposes the array first using zip(*arr) and then reverses the resulting transposed array using [::-1]. 
# This achieves the desired rotation in the opposite direction.
# Time and Space Complexity: O(N*M), where N is the number of rows and M is the number of columns in the input array.


def rotate(matrix,flag):

    if flag==0:
        return list(zip(*matrix[::-1]))
    
    else:
        return list(zip(*matrix))[::-1]



original_matrix = [[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]]

print("Clockwise: ")
print(rotate(original_matrix,0))
print("Anticlockwise: ")
print(rotate(original_matrix,1))