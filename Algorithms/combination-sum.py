#Question:39. Combination Sum
# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
# frequency of at least one of the chosen numbers is different.
# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

#Approach:
# The approach uses backtracking to explore all combinations of candidates, starting from each index. It appends candidates to the current combination and recursively reduces the target until it reaches zero, at which point the combination is added to the result. 
# Time complexity: O(2^(N+T)), where N is the number of candidates and T is the target
# Space complexity: O(T) for the recursion stack.

from typing import List 
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, comb, target):
            if target == 0:
                res.append(comb.copy())
                return
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    continue
                comb.append(candidates[i])
                backtrack(i, comb, target - candidates[i])
                comb.pop()

        backtrack(0, [], target)
        return res
    
s=Solution()
# Example 1:
candidates = [2,3,6,7]
target = 7
print(s.combinationSum(candidates,target))
# Expected Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.

# Example 2:
candidates = [2,3,5]
target = 8
print(s.combinationSum(candidates,target))
# Expected Output: [[2,2,2,2],[2,3,3],[3,5]]

# Example 3:
candidates = [2]
target = 1
print(s.combinationSum(candidates,target))
# Expected Output: []
