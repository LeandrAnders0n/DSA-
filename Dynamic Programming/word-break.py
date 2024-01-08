#Question: 139. Word Break
# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.

#Approach: Dynamic Programming
# Use dynamic programming to determine if the string s can be segmented into words from the wordDict. Iterate through each index, and check if a valid segmentation is possible up to that point. 
# Time complexity: O(n * m), where n is the length of the string and m is the size of the dictionary. 
# Space complexity: O(n) for the dynamic programming array.

from typing import List 
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        dp = [False] * (n + 1)
        dp[0] = True  
        
        for i in range(1, n + 1):
            for word in wordDict:
                
                if len(word) <= i and dp[i - len(word)] and s[i - len(word):i] == word:
                    dp[i] = True
                    break
        
        return dp[n]
    
sol=Solution()
# Example 1:
s = "leetcode"
wordDict = ["leet","code"]
print(sol.wordBreak(s,wordDict))
# Expected Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".

# Example 2:
s = "applepenapple"
wordDict = ["apple","pen"]
print(sol.wordBreak(s,wordDict))
# Expected Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.

# Example 3:
s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
print(sol.wordBreak(s,wordDict))
# Expected Output: false
 