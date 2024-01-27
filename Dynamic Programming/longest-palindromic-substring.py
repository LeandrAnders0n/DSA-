#Question: 5. Longest Palindromic Substring
# Given a string s, return the longest palindromic substring in s.

#Approach:Dynamic Programming
# Use dynamic programming to fill a 2D table `dp` to store information about whether substrings are palindromes. Iterate through the string, updating the table based on palindrome conditions. Keep track of the maximum length and the corresponding substring found so far. The final result is the longest palindromic substring. 

# Time & Space complexity: O(n^2) 

class SolutionOne:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        max_len=1
        max_str=s[0]
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            for j in range(i):
                if s[j] == s[i] and (i-j <= 2 or dp[j+1][i-1]):
                    dp[j][i] = True
                    if i-j+1 > max_len:
                        max_len = i-j+1
                        max_str = s[j:i+1]
        return max_str
sol1=SolutionOne()

#Approach:Expand Around
# Iterate through each character, treating it as the centre for both odd and even-length palindromes, and expand around it to find the maximum palindrome length. The `start` and `end` pointers are updated to keep track of the longest palindromic substring found so far. The final result is the substring within the range `[start, end]` in the input string.

# Time Complexity: O(n^2) 
# Space complexity: O(1) 
class SolutionTwo:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start, end = 0, 0

        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        for i in range(len(s)):
            len1 = expand_around_center(i, i)
            len2 = expand_around_center(i, i + 1)
            max_len = max(len1, len2)

            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start:end + 1]
sol2=SolutionTwo()
# Example 1:
s = "babad"
print(sol1.longestPalindrome(s))
# Expected Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:
s = "cbbd"
print(sol2.longestPalindrome(s))
# Expected Output: "bb"