#Question:34. Find First and Last Position of Element in Sorted Array
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first, last = -1, -1
        for i in range(len(nums)):
            if nums[i] == target:
                if first == -1:
                    first = i
                last = i
        return [first, last]

s=Solution()
# Example 1:
nums = [5,7,7,8,8,10]
target = 8
print(s.searchRange(nums,target))
# Expected Output: [3,4]

# Example 2:
nums = [5,7,7,8,8,10]
target = 6
print(s.searchRange(nums,target))
# Expected Output: [-1,-1]

# Example 3:
nums = []
target = 0
print(s.searchRange(nums,target))
# Expected Output: [-1,-1]