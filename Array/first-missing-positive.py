#Question:41. First Missing Positive
# Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.
# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

#Approach: Cyclic Sorting
# Use a cyclic sorting algorithm to rearrange the input array such that each positive integer appears in its correct index (1-based). Iterate through the sorted array to find the smallest missing positive integer. 
from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
    
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]
        
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                swap(nums[i] - 1, i)
        
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1


s=Solution()
# Example 1:
nums = [1,2,0]
print(s.firstMissingPositive(nums))
# Expected Output: 3
# Explanation: The numbers in the range [1,2] are all in the array.

# Example 2:
nums = [3,4,-1,1]
print(s.firstMissingPositive(nums))
# Expected Output: 2
# Explanation: 1 is in the array but 2 is missing.

# Example 3:
nums = [7,8,9,11,12]
print(s.firstMissingPositive(nums))
# Expected Output: 1
# Explanation: The smallest positive integer 1 is missing.