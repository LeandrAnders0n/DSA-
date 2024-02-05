#Question: 387. First Unique Character in a String
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d={}
        for c in s:
            d[c]=d.get(c,0)+1

        for c in s:
            if d[c]==1:
                return s.index(c)

        return -1

sol=Solution()
# Example 1:
s = "leetcode"
print(sol.firstUniqChar(s))
# Expected Output: 0

# Example 2:
s = "loveleetcode"
print(sol.firstUniqChar(s))
# Expected Output: 2

# Example 3:
s = "aabb"
print(sol.firstUniqChar(s))
# Expected Output: -1