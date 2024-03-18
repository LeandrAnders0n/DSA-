#Question:452. Minimum Number of Arrows to Burst Balloons
# There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.
# Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.
# Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

#Approach:
# First, check if the input list is empty and return 0 if so. Then,  sort the intervals based on their ending points in ascending order. Iterate through the sorted list, and count the number of disjoint intervals by comparing the starting point of each interval with the ending point of the previous one. If a new interval starts after the previous one ends, increment the arrow count and update the endpoint. Finally,  return the total arrow count

# Time complexity: O(n log n) 
# Space complexity: O(1) 

from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda x: x[1])
        arrows = 1
        end = points[0][1]

        for p in points[1:]:
            if p[0] > end:
                arrows += 1
                end = p[1]

        return arrows
s=Solution()

# Example 1:
points = [[10,16],[2,8],[1,6],[7,12]]
print(s.findMinArrowShots(points))
# Expeceted Output: 2
# Explanation: The balloons can be burst by 2 arrows:
# - Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
# - Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].

# Example 2:
points = [[1,2],[3,4],[5,6],[7,8]]
print(s.findMinArrowShots(points))
# Expected Output: 4
# Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.

# Example 3:
points = [[1,2],[2,3],[3,4],[4,5]]
print(s.findMinArrowShots(points))
# Expected Output: 2
# Explanation: The balloons can be burst by 2 arrows:
# - Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
# - Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].