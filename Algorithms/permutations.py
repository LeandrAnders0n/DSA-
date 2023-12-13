#Question:46. Permutations
# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

#Approach:Backtracking
# In the provided code, a backtracking approach is employed to generate all permutations of a given list of integers. The algorithm iteratively explores different choices by removing elements, recursively permuting the remaining ones, and backtracking to explore other possibilities until all permutations are generated.

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]

        if len(nums)==1:
            return [nums[:]]

        for i in range(len(nums)):
            n=nums.pop(0)
            perms=self.permute(nums)

            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)
        
        return result

s=Solution()
# Example 1:
nums = [1,2,3]
print(s.permute(nums))
# Expected Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# Example 2:
nums = [0,1]
print(s.permute(nums))
# Expected Output: [[0,1],[1,0]]

# Example 3:
nums = [1]
print(s.permute(nums))
# Expected Output: [[1]]