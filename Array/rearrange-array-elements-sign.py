#Question: 2149. Rearrange Array Elements by Sign
# You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.
# You should rearrange the elements of nums such that the modified array follows the given conditions:
# Every consecutive pair of integers have opposite signs.
# For all integers with the same sign, the order in which they were present in nums is preserved.
# The rearranged array begins with a positive integer.
# Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

#Approach:
#Divide array into positive and negative numbers. 
# Loop through either subarray and append the elements with the required condiitions, ie retaining the order, but alternating signs and starting with a positive integer. 
# This can be done, as the negative and positive subararrays are to be of equal length.

#Time and Space Complexity: O(n)

from typing import List
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res=[]
        negative = [n for n in nums if n < 0]
        positive = [n for n in nums if n >= 0]

        for i in range(len(negative)):
            res.append(positive[i])
            res.append(negative[i])

        return res

        
s=Solution() 
# Example 1:
nums = [3,1,-2,-5,2,-4]
print(s.rearrangeArray(nums))
# Expected Output: [3,-2,1,-5,2,-4]
# Explanation:
# The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4].
# The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].
# Other ways such as [1,-2,2,-5,3,-4], [3,1,2,-2,-5,-4], [-2,3,-5,1,-4,2] are incorrect because they do not satisfy one or more conditions.  

# Example 2:
nums = [-1,1]
print(s.rearrangeArray(nums))
# Expected Output: [1,-1]
# Explanation:
# 1 is the only positive integer and -1 the only negative integer in nums.
# So nums is rearranged to [1,-1].