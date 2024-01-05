#Question:172. Factorial Trailing Zeroes
# Given an integer n, return the number of trailing zeroes in n!.
# Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

#Approach:
# Iteratively count the factors of 5 in the prime factorization of n by dividing n by 5 in each iteration until n is less than 5. The count represents the number of trailing zeroes.

class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0

        # Count the number of factors of 5 in the prime factorization of n
        while n >= 5:
            n //= 5
            count += n

        return count
 
s=Solution()
# Example 1:
n = 3
print(s.trailingZeroes(n))
# Expected Output: 0
# Explanation: 3! = 6, no trailing zero.

# Example 2:
n = 5
print(s.trailingZeroes(n))
# Expected Output: 1
# Explanation: 5! = 120, one trailing zero.

# Example 3:
n = 0
print(s.trailingZeroes(n))
# Expected Output: 0
 