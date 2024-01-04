#Question: 66. Plus One
# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nums=0
        for d in digits:
            nums=(nums*10)+d
        nums+=1
        res = [int(x) for x in str(nums)]
        return res

s=Solution()

# Example 1:
digits = [1,2,3]
print(s.plusOne(digits))
# Expected Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].

# Example 2:
digits = [4,3,2,1]
print(s.plusOne(digits))
# Expected Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].

# Example 3:
digits = [9]
print(s.plusOne(digits))
# Expected Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].
 