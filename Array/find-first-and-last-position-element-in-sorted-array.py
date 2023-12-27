#Question:34. Find First and Last Position of Element in Sorted Array
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.


# Approach:
# The code uses a binary search approach to find the first and last occurrences of the target element in a sorted array. Two separate binary searches are performed to find the first and last occurrences, updating the search range accordingly.

# Time Complexity: O(log n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(nums, target, find_first):
            result = -1
            low, high = 0, len(nums) - 1

            while low <= high:
                mid = (low + high) // 2

                if nums[mid] == target:
                    result = mid
                    if find_first:
                        high = mid - 1 
                    else:
                        low = mid + 1  
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

            return result

        first = binary_search(nums, target, True)
        last = binary_search(nums, target, False)

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