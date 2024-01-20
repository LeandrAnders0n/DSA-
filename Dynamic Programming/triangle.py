#Question:120. Triangle
# Given a triangle array, return the minimum path sum from top to bottom.
# For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

#Approach:
# Use dynamic programming to find the minimum path sum in a triangle. Iterate through the triangle from the second-to-last row to the top, updating each element with the minimum path sum from the two possible next elements in the row below. The final result is the minimum path sum stored at the top of the triangle.

# Time Complexity: is O(n^2), where n is the number of rows in the triangle, as each element is visited and updated once.
# Space Complexity: O(1)
  
from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Start from the second to last row and iterate upwards
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                # Update the current element with the minimum path sum
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])

        # The minimum path sum is stored at the top of the triangle
        return triangle[0][0]

s=Solution()
# Example 1:
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(s.minimumTotal(triangle))
# Expected Output: 11
# Explanation: The triangle looks like:
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 

# Example 2:
triangle = [[-10]]
print(s.minimumTotal(triangle))
# Expected Output: -10



