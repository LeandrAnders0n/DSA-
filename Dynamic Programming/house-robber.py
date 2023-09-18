#Question: House Robber
#You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

#Approach: Dynamic Programming
# Use dynamic programming to find the maximum amount of money that can be robbed from a street of houses without robbing adjacent ones. Iteratively calculate the maximum money that can be obtained up to each house by choosing whether to rob the current house or skip it, and store the results in an array. The final element of the array represents the maximum money that can be robbed.

# Time & Space Complexity: O(n) 

def rob(nums):
    n=len(nums)

    #base cases
    if n==0:
        return 0
    if n==1:
        return nums[0]

    #dp array
    dp=[0]*(n+1)
    dp[0]=nums[0]
    dp[1]=max(nums[0],nums[1])


    for i in range(2,n):
        dp[i]=max(dp[i-1],dp[i-2]+nums[i])
    return dp[n-1]


nums = [2,7,9,3,1]
print(rob(nums))
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
 
nums = [1,2,3,1]
print(rob(nums))
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
