#Question:69. Sqrt(x)
# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
# You must not use any built-in exponent function or operator.
# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

#Approach: Binary Search
# The code implements the square root calculation for a non-negative integer 'x' using binary search. It defines a search space between 1 and the given number 'x'. The algorithm iteratively narrows down this range, checking the middle point's square against 'x' and adjusting the search boundaries accordingly.
    
class Solution(object):
    def mySqrt(self, x):
        if x == 0:
            return 0

        left, right = 1, x

        while left <= right:
            mid = left + (right - left) // 2

            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1

        return right  # return the rounded down square root

s=Solution()
# Example 1:
x = 4
print(s.mySqrt(x))
# Expected Output: 2
# Explanation: The square root of 4 is 2, so we return 2.

# Example 2:
x = 8
print(s.mySqrt(x))
# Expected Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.