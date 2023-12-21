#Question: 1637. Widest Vertical Area Between Two Points Containing No Points
# Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between two points such that no points are inside the area.
# A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The widest vertical area is the one with the maximum width.
# Note that points on the edge of a vertical area are not considered included in the area.

#Approach:
# The code sorts a list of 2D points based on their x-coordinates. It then iterates through the sorted points, calculates the width between consecutive x-coordinates, and updates the maximum width. The final result is the maximum vertical gap between points along the x-axis.

# Time Complexity: O(n log n), due to sorting the points.
# Space Complexity: O(1)

from typing import List

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[0])

        max_width=0

        for i in range(1,len(points)):
            width=points[i][0]-points[i-1][0]
            max_width=max(width,max_width)
            
        return max_width
s=Solution()
# Example 1:
points = [[8,7],[9,9],[7,4],[9,7]]
print(s.maxWidthOfVerticalArea(points))
# Expected Output: 1
# Explanation: Both the red and the blue area are optimal.

# Example 2:
points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
print(s.maxWidthOfVerticalArea(points))
# Expected Output: 3