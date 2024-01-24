#Question:63. Unique Paths II
# You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
# An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.
# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
# The testcases are generated so that the answer will be less than or equal to 2 * 109.

#Approach: Dynamic Programming
# Initialize a 2D array to store the number of unique paths for each cell in the grid. Start by handling the top-left cell and initializing the boundaries based on obstacle conditions. Then iterate through the remaining cells, filling in the dynamic programming array by summing values from the top and left cells if the current cell is not an obstacle. Finally, the value in the bottom-right cell of the dynamic programming array is returned as the solution, representing the number of unique paths. 

# Time and Space Complexity: O(m * n)

from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0]:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])

        # Create a 2D array to store the number of unique paths
        dp = [[0] * n for _ in range(m)]

        # Initialize the top-left cell
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0

        # Initialize the first row
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] if obstacleGrid[i][0] == 0 else 0

        # Initialize the first column
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] if obstacleGrid[0][j] == 0 else 0

        # Fill in the DP array based on the possible paths
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]

s=Solution()
# Example 1:
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
print(s.uniquePathsWithObstacles(obstacleGrid))
# Expected Output: 2
# Explanation: There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right

# Example 2:
obstacleGrid = [[0,1],[0,0]]
print(s.uniquePathsWithObstacles(obstacleGrid))
# Expected Output: 1
                