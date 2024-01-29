#Question: 97. Interleaving String
# Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
# An interleaving of two strings s and t is a configuration where s and t are divided into n and m substrings respectively, such that:
# s = s1 + s2 + ... + sn
# t = t1 + t2 + ... + tm
# |n - m| <= 1
# The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
# Note: a + b is the concatenation of strings a and b.

#Approach: Dynamic Programming
# Use dynamic programming with a 1D array (`dp`) to determine whether `s3` can be formed by interleaving `s1` and `s2`. Iterate through the characters of `s1` and `s2`, updating the `dp` array to represent the feasibility of forming each position in `s3`. The final result is based on whether the last position in `s2` can be reached. Check if the lengths of `s1`, `s2`, and `s3` are compatible and return `True` if the interleaving is possible, otherwise `False`.

# Time Complexity: O(len_s1 * len_s2)
# Space Complexity: O(len_s2)

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len_s1, len_s2, len_s3 = len(s1), len(s2), len(s3)

        if len_s1 + len_s2 != len_s3:
            return False

        dp = [False] * (len_s2 + 1)

        # Initialize the first row of dp
        dp[0] = True
        for j in range(1, len_s2 + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

        # Update dp for each character in s1 and s3
        for i in range(1, len_s1 + 1):
            # Update the first element of dp for the current row
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]

            # Update dp for the rest of the row
            for j in range(1, len_s2 + 1):
                dp[j] = (dp[j] and s1[i - 1] == s3[i - 1 + j]) or (dp[j - 1] and s2[j - 1] == s3[i - 1 + j])

        return dp[len_s2]

s=Solution()
# Example 1:
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
print(s.isInterleave(s1,s2,s3))
# Expected Output: true
# Explanation: One way to obtain s3 is:
# Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
# Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
# Since s3 can be obtained by interleaving s1 and s2, we return true.

# Example 2:
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbbaccc"
print(s.isInterleave(s1,s2,s3))
# Expected Output: false
# Explanation: Notice how it is impossible to interleave s2 with any other string to obtain s3.

# Example 3:
s1 = ""
s2 = ""
s3 = ""
print(s.isInterleave(s1,s2,s3))
# Expected Output: true
 
