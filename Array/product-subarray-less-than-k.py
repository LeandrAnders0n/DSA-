#Question: 713. Subarray Product Less Than K
# Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

#Approach: Sliding Window
# Use a sliding window approach to count the number of contiguous subarrays where the product of all elements is strictly less than the given threshold `k`. Initialize two pointers, `left` and `right`, and calculate the product of elements within the sliding window. Iterates over the array, adjusting the window boundaries based on the product value until the product becomes less than `k`. At each iteration,  update the count by adding the length of the valid subarray. 

# Time Complexity: O(n) 
# Space Complexity: O(1)

from typing import List
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
    
        left = 0
        product = 1
        count = 0

        for right in range(len(nums)):
            product *= nums[right]

            while product >= k:
                product /= nums[left]
                left += 1

            count += right - left + 1

        return count
    
s=Solution()
# Example 1:
nums = [10,5,2,6]
k = 100
print(s.numSubarrayProductLessThanK(nums,k))
# Expected Output: 8
# Explanation: The 8 subarrays that have product less than 100 are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

# Example 2:
nums = [1,2,3]
k = 0
print(s.numSubarrayProductLessThanK(nums,k))
# Output: 0