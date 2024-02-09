#Question: 279. Perfect Squares
# Given an integer n, return the least number of perfect square numbers that sum to n.
# A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

#Approach: Dynamic Programming
# Initialize an array dp where dp[i] represents the minimum number of perfect squares needed to sum up to i. Iterate through numbers from 1 to n, and for each number, explore all possible perfect square combinations by incrementing j. The inner loop calculates the minimum count by considering the previously calculated counts for smaller numbers. The final result is stored in dp[n], representing the least number of perfect squares needed for the given input n. 
# Time Complexity: O(n * sqrt(n))
# Space Complexity: O(n) 

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            min_val = float('inf')
            j = 1
            while j * j <= i:
                min_val = min(min_val, dp[i - j * j] + 1)
                j += 1
            dp[i] = min_val
        return dp[n]
s=Solution()
 

# Example 1:
n = 12
print(s.numSquares(n))
# Expected Output: 3
# Explanation: 12 = 4 + 4 + 4.

# Example 2:
n = 13
print(s.numSquares(n))
# Expected Output: 2
# Explanation: 13 = 4 + 9.