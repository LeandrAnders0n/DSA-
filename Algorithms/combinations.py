#Question: 77. Combinations
# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
# You may return the answer in any order.

#Approach: Backtracking
# The combine method utilizes a backtracking approach to generate combinations of k integers from the range [1, n]. The recursive backtrack function explores possible combinations, appending them to the result list res when their length equals k. The method returns the final list of combinations.

from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        def backtrack(start,comb):
            if len(comb)==k:
                res.append(comb.copy())
                return 
            for i in range(start,n+1):
                comb.append(i)
                backtrack(i+1,comb)
                comb.pop()
        backtrack(1,[])
        return res

s=Solution()   
# Example 1:
n = 4
k = 2
print(s.combine(n,k))
# Expected Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
# Explanation: There are 4 choose 2 = 6 total combinations.
# Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

# Example 2:
n = 1
k = 1
print(s.combine(n,k))
# Excpected Output: [[1]]
# Explanation: There is 1 choose 1 = 1 total combination.