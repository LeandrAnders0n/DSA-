#Question: 300. Longest Increasing Subsequence
# Given an integer array nums, return the length of the longest strictly increasing subsequence.

#Approach: Dynamic Programming
# Use a dynamic programming approach with an array dp to store the length of the longest increasing subsequence ending at each index. Iterate through the array, updating the dp values based on the increasing subsequence condition. The final result is the maximum value in the dp array.

# Time Complexity: O(n^2)
# Space Complexity: O(n)

from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

s=Solution()

# Example 1:
nums = [10,9,2,5,3,7,101,18]
print(s.lengthOfLIS(nums))
# Expected Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

# Example 2:
nums = [0,1,0,3,2,3]
print(s.lengthOfLIS(nums))
# Expected Output: 4

# Example 3:
nums = [7,7,7,7,7,7,7]
print(s.lengthOfLIS(nums))
# Expected Output: 1