#Question:1913. Maximum Product Difference Between Two Pairs
# The product difference between two pairs (a, b) and (c, d) is defined as (a * b) - (c * d).
# For example, the product difference between (5, 6) and (2, 7) is (5 * 6) - (2 * 7) = 16.
# Given an integer array nums, choose four distinct indices w, x, y, and z such that the product difference between pairs (nums[w], nums[x]) and (nums[y], nums[z]) is maximized.
# Return the maximum such product difference.

#Approach:
# The approach sorts the input array to easily identify the maximum and second-maximum values as well as the minimum and second-minimum values. Then, it calculates the product difference between the largest pair and the smallest pair. 

# Time complexity is O(n log n) due to the sorting step
# Space complexity: O(1)

from typing import List

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:

        nums.sort()
        n=len(nums)

        max1,max2=nums[n-1],nums[n-2]

        min1,min2=nums[0],nums[1]

        return (max1*max2)-(min1*min2)

s=Solution()

# Example 1:
nums = [5,6,2,7,4]
print(s.maxProductDifference(nums))
# Expected Output: 34
# Explanation: We can choose indices 1 and 3 for the first pair (6, 7) and indices 2 and 4 for the second pair (2, 4).
# The product difference is (6 * 7) - (2 * 4) = 34.

# Example 2:
nums = [4,2,5,9,7,4,8]
print(s.maxProductDifference(nums))
# Expected Output: 64
# Explanation: We can choose indices 3 and 6 for the first pair (9, 8) and indices 1 and 5 for the second pair (2, 4).
# The product difference is (9 * 8) - (2 * 4) = 64.