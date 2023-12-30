#Question:136. Single Number
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

#Approach:
# This solution uses bitwise XOR (^) to find the single non-repeating number in the given list. Initializing `result` as 0, it XORs each element in the list, effectively canceling out duplicates (XORing the same number twice results in 0), and leaving only the single unique number. The final result holds the unique element.

from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result=0

        for n in nums:
            result=result^n
        return result
 
s=Solution()
# Example 1:
nums = [2,2,1]
print(s.singleNumber(nums))
# Output: 1

# Example 2:
nums = [4,1,2,1,2]
print(s.singleNumber(nums))
# Output: 4


# Example 3:
nums = [1]
print(s.singleNumber(nums))
# Output: 1