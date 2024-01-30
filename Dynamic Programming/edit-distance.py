#Question:72. Edit Distance
# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
# You have the following three operations permitted on a word:
# Insert a character
# Delete a character
# Replace a character

#Approach: Dynamic Programming
# The dynamic programming matrix dp is of size (m+1) x (n+1), where m and n represents the lengths of word1 and word2 respectively. The matrix is initialized with base cases: the first row represents the cost of converting an empty string to a substring of word2, and the first column represents the cost of converting a substring of word1 to an empty string.
# We then iterate through the matrix, filling in values based on the three allowed operations:
# - If the characters at the current positions in both words are equal, no operation is needed, and the value is inherited from the diagonal element (dp[i-1][j-1]).
# - If the characters are different, the minimum of the three possible operations is considered: deletion (dp[i-1][j]), insertion (dp[i][j-1]), and replacement (dp[i-1][j-1]).
# The final result, representing the minimum edit distance, is stored in the bottom-right cell of the matrix (dp[m][n]). The time complexity is O(m * n), where m and n are the lengths of the input words, and the space complexity is also O(m * n) due to the dynamic programming matrix.

# Time & Space Complexity: O(m*n) 

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        # Create a 2D array to store the minimum edit distances
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Initialize the first row and column
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        # Fill the rest of the matrix
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j],      # Deletion
                                    dp[i][j - 1],      # Insertion
                                    dp[i - 1][j - 1])  # Replacement

        # The bottom-right cell contains the minimum edit distance
        return dp[m][n]

s=Solution()
# Example 1:
word1 = "horse"
word2 = "ros"
# Expected Output: 3
print(s.minDistance(word1,word2))
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')

# # Example 2:
# word1 = "intention"
# word2 = "execution"
# # Expected Output: 5
print(s.minDistance(word1,word2))
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')