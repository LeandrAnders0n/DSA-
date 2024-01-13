#Question: 322. Coin Change
# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
# You may assume that you have an infinite number of each kind of coin.

#Approach: Dynamic Programming
# Implement a dynamic programming approach to solve the coin change problem. Use a 1D array (dp) to store the minimum number of coins needed to make each amount from 0 to the given amount. Iterate through each amount and each coin denomination, updating the dp array accordingly. The final result is the minimum number of coins needed to make the given amount, or -1 if it's not possible. 

# Time complexity: O(amount * number of coins)
# Space complexity: O(amount).

from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[amount+1]*(amount+1)

        dp[0]=0

        for i in range(1,amount+1):
            for c in coins:
                if i-c>=0:
                    dp[i]=min(dp[i],1+dp[i-c])

        return dp[amount] if dp[amount]!=amount+1 else -1
 
s=Solution()
# Example 1:
coins = [1,2,5]
amount = 11
print(s.coinChange(coins,amount))
# Expected Output: 3
# Explanation: 11 = 5 + 5 + 1

# Example 2:
coins = [2]
amount = 3
print(s.coinChange(coins,amount))
# Expected Output: -1

# Example 3:
coins = [1]
amount = 0
print(s.coinChange(coins,amount))
# Expected Output: 0