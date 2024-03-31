#Question: 2444. Count Subarrays With Fixed Bounds
# You are given an integer array nums and two integers minK and maxK.
# A fixed-bound subarray of nums is a subarray that satisfies the following conditions:
# The minimum value in the subarray is equal to minK.
# The maximum value in the subarray is equal to maxK.
# Return the number of fixed-bound subarrays.
# A subarray is a contiguous part of an array.

#Approach:
# Maintain indices for the leftmost and rightmost occurrences of `minK` and `maxK`, along with the index of the last invalid element outside the range `[minK, maxK]`. During each iteration, update these indices and compute the count of valid subarrays when both left and right indices are valid.

# Time Complexity: O(N)
# Space Complexity: O(1)

from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count = 0
        last_invalid_idx = -1
        left_idx = right_idx = -1

        for i, num in enumerate(nums):
            if not minK <= num <= maxK:
                last_invalid_idx = i
                left_idx = right_idx = -1 

            if num == minK:
                left_idx = i

            if num == maxK:
                right_idx = i

            if left_idx != -1 and right_idx != -1:
                count += min(left_idx, right_idx) - last_invalid_idx

        return count

s=Solution()

# Example 1:
nums = [1,3,5,2,7,5]
minK = 1
maxK = 5
print(s.countSubarrays(nums,minK,maxK))
# Expected Output: 2
# Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].

# Example 2:
nums = [1,1,1,1]
minK = 1
maxK = 1
print(s.countSubarrays(nums,minK,maxK))
# Expected Output: 10
# Explanation: Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays.