#Question:Jump Game II
# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:
# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

#Approach:Dynamic Programming
# Calculate the minimum number of jumps needed to traverse an array nums, where each element indicates the maximum steps that can be taken from that position. Use dynamic programming to populate an array dp with the minimum jumps required to reach each index. 
# Time complexity: O(n^2) 
# Space complexity: O(n) 

def jump(nums):
    n=len(nums)
    dp=[float('inf') for _ in range(n)]
    dp[0]=0
    for i in range(n):
        for j in range(1,nums[i]+1):
            if i+j<n:
                dp[i+j]=min(dp[i+j],dp[i]+1)
    return dp[n-1]

nums = [2,3,0,1,4]
# Output: 2
print(jump(nums))

nums = [2,3,0,1,4]
# Output: 2
print(jump(nums))
 
