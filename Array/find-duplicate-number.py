#Question: 287. Find the Duplicate Number
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and uses only constant extra space.

# Approach: Floyd's Tortoise and Hare Algorithm
# Implement Floyd's Tortoise and Hare algorithm to find the duplicate number in the given list. Initialize two pointers, tortoise and hare, both starting from the first element of the list. The tortoise moves one step at a time while the hare moves two steps at a time. When they meet, it indicates the presence of a cycle. Then, another pointer is initialized from the beginning of the list, and both pointers move at the same pace until they meet again at the entrance of the cycle, which corresponds to the duplicate number.

# Time complexity: O(n)
# Space complexity: O(1)

from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]

        return tortoise

s=Solution()
 

# Example 1:
nums = [1,3,4,2,2]
print(s.findDuplicate(nums))
# Expected Output: 2

# Example 2:
nums = [3,1,3,4,2]
print(s.findDuplicate(nums))
# Expected Output: 3

# Example 3:
nums = [3,3,3,3,3]
print(s.findDuplicate(nums))
# Expected Output: 3