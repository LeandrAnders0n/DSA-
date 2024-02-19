#Question: 231. Power of Two
# Given an integer n, return true if it is a power of two. Otherwise, return false.
# An integer n is a power of two, if there exists an integer x such that n == 2x.

# Follow up: Could you solve it without loops/recursion?

#Approach: Bit Manipulation
# Check whether a given integer n is a power of two. The function returns True if n is a positive integer and the bitwise AND operation between n and n - 1 results in 0, indicating that n has only one bit set to 1, a characteristic of powers of two. 

# Time & Space Complexity: O(n)

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and (n & (n-1))==0

s=Solution()

# Example 1:
n = 1
print(s.isPowerOfTwo(n))
# Expected Output: true
# Explanation: 2^0 = 1

# Example 2:
n = 16
print(s.isPowerOfTwo(n))
# Expected Output: true
# Explanation: 2^4 = 16

# Example 3:
n = 3
print(s.isPowerOfTwo(n))
# Expected Output: false