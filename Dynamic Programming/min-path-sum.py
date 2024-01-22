#Question:64. Minimum Path Sum
# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
# Note: You can only move either down or right at any point in time.

#Approach: Dynamic Programming
# Initialize a 2D table `dp` to store the minimum path sum at each cell. The top-left cell is set to the grid's value. Iterate through the grid, and update each cell in `dp` by considering the minimum sum from either the cell above or the cell to the left. The result is the value in the bottom-right cell of `dp`, representing the minimum path sum. 
# Time & Space Complexity: O(m * n), where m is the number of rows and n is the number of columns in the grid.

from typing import List 

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])

        dp = [[0] * n for _ in range(m)]

        dp[0][0] = grid[0][0]

        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])

        return dp[m - 1][n - 1]

s=Solution()
# Example 1:
grid = [[1,3,1],[1,5,1],[4,2,1]]
print(s.minPathSum(grid))
# Expected Output: 7
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

# Example 2:
grid = [[1,2,3],[4,5,6]]
print(s.minPathSum(grid))
# Expected Output: 12