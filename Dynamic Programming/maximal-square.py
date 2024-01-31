#Question: 221. Maximal Square
# Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

#Approach:Dynamic Programming
# Initialize a 2D array `dp` to store the maximum size square ending at each position. Iterate through the matrix, updating `dp` based on the neighboring cells. The variable `max_size` keeps track of the maximum square size encountered during the iteration. The final result is the area of the largest square, calculated as `max_size * max_size`. 

# Time & Space complexity: O(m * n)

from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])        
        dp = [[0] * n for _ in range(m)]
        max_size = 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    
                    max_size = max(max_size, dp[i][j])
        return max_size * max_size
s=Solution()
# Example 1:
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(s.maximalSquare(matrix))
# Expected Output: 4

# Example 2:
matrix = [["0","1"],["1","0"]]
print(s.maximalSquare(matrix))
# Expected Output: 1

# Example 3:
matrix = [["0"]]
print(s.maximalSquare(matrix))
# Expected Output: 0