#Question:997. Find the Town Judge
# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.
# If the town judge exists, then:
# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.
# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

#Approach:
# Identify the judge in a town with n people based on a trust list. Count the incoming and outgoing trusts for each person using the count array. The judge is the person with n-1 incoming trusts and no outgoing trusts.

# Time complexity: O(t), where t is the number of trusts.
# Space complexity: O(n), where n is the number of people.

from typing import List
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        count=[0]*(n+1)

        for i,j in trust:
            count[i]-=1
            count[j]+=1
        
        for i in range(1,len(count)):
            if count[i]==n-1:
                return i
        return -1

s=Solution()
# Example 1:
n = 2
trust = [[1,2]]
print(s.findJudge(n,trust))
# Output: 2

# Example 2:
n = 3
trust = [[1,3],[2,3]]
print(s.findJudge(n,trust))
# Output: 3

# Example 3:
n = 3
trust = [[1,3],[2,3],[3,1]]
print(s.findJudge(n,trust))
# Output: -1