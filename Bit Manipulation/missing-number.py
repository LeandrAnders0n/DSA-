#Question:268. Missing Number
# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

#Approach:
# Utilize the XOR operation to efficiently identify the missing element by XORing all numbers from 1 to n and all elements in the input list. This bitwise XOR approach cancels out the common elements, leaving only the missing number. 

# Time complexity: O(n) 
# Space Complexity: O(1)

from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1, n + 1):
            ans ^= i
        for num in nums:
            ans ^= num
        return ans

s=Solution()

# Example 1:
nums = [3,0,1]
print(s.missingNumber(nums))
# Expected Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

# Example 2:
nums = [0,1]
print(s.missingNumber(nums))
# Expected Output: 2
# Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

# Example 3:
nums = [9,6,4,2,3,5,7,0,1]
print(s.missingNumber(nums))
# Expected Output: 8
# Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.