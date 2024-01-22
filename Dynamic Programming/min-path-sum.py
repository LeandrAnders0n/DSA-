#Question:64. Minimum Path Sum
# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
# Note: You can only move either down or right at any point in time.

#Approach: Dynamic Programming
# Follow a bottom-up dynamic programming approach. Iterate through the given grid, updating each cell by adding the minimum of the values from the cell above and the cell to the left. Start from the top-left corner and progress towards the bottom-right corner, ensuring that each cell's value represents the minimum path sum to reach that cell. The final result is the value in the bottom-right cell, representing the minimum path sum for the entire grid.
# Time Complexity: O(m * n)
#Space Complexity: O(1)

from typing import List 

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        for i in range(m):
            for j in range(n):
                if i==0:
                    if j!=0:
                        grid[i][j]+=grid[i][j-1]
                elif j==0:
                    if i!=0:
                        grid[i][j]+=grid[i-1][j]
                else:
                    grid[i][j]+=min(grid[i-1][j],grid[i][j-1])
        return grid[m-1][n-1]

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