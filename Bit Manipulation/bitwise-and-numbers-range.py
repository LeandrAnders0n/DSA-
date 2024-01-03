#Question:201. Bitwise AND of Numbers Range
# Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.

#Approach:
# Consider the binary representations of the two numbers in the given range. By shifting both numbers to the right until they align (i.e., their common prefix), we identify the common bits shared by all numbers in the range. Then, by shifting one of them back to the left by the number of shifts, we effectively isolate this common prefix, revealing the bitwise AND result of all numbers in the range.

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
    
        return left << shift


s=Solution()

# Example 1:
left = 5
right = 7
# Expected Output: 4
print(s.rangeBitwiseAnd(left,right))

# Example 2:
left = 0
right = 0
# Expected Output: 0
print(s.rangeBitwiseAnd(left,right))

# Example 3:
left = 1
right = 2147483647
# Expected Output: 0
print(s.rangeBitwiseAnd(left,right))
