#Question:137. Single Number II
# Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

#Approach:
# The code uses two variables, ones and twos, to keep track of the bits that appear once and twice, respectively, in the binary representation of the numbers. The XOR operation updates ones and twos, and the bitwise AND operation ensures that the bits are reset when they appear three times. The final result is stored in the ones variable, representing the single number that appears exactly once in the array.

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def singleNumber(self, nums):
        ones = 0
        twos = 0
        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones
        return ones

s=Solution()
# Example 1:
nums = [2,2,3,2]
print(s.singleNumber(nums))
# Expected Output: 3

# Example 2:
nums = [0,1,0,1,0,1,99]
print(s.singleNumber(nums))
# Expected Output: 99