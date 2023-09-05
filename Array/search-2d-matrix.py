#Question:Search a 2D Matrix
#You are given an m x n integer matrix matrix with the following two properties:
# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.
# You must write a solution in O(log(m * n)) time complexity.

#Approach:Binary Search
# Perform binary search on a 2D matrix to find a target value. To do this, convert the 2D matrix into a 1D list, to apply binary search. Set up `left` and `right` pointers for the binary search and return `True` if the target is found, `False` otherwise.

# Explanation:
# Instead of searching in the 2D matrix directly, the code flattens it into a 1D list by mapping each 2D index `(i, j)` to a 1D index `i * number_of_columns + j`. This simplifies the search. The binary search then compares the middle element of the 1D list with the target value. 

# Time Complexity: O(log(n*m)) 
# Space Complexity: O(1) 

def search_matrix(matrix,target):
    n, m = len(matrix), len(matrix[0])
    left, right = 0, n * m - 1
    while left <= right:
        mid = (left + right) // 2
        num = matrix[mid // m][mid % m]
        if num == target:
            return True
        if num < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]] 
target = 13
# Output: false
print(search_matrix(matrix,target))

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
# Output: true
print(search_matrix(matrix,target))
