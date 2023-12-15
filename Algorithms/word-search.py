#Question: 79. Word Search
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

#Approach: Backtracking
# The approach employs a recursive backtracking strategy to explore possible paths on the board for the specified word. Each cell is visited, and if it matches the corresponding character in the word, the algorithm proceeds to explore adjacent cells in all four directions. The visited cell is temporarily marked, and if the exploration results in a valid path, the algorithm returns True. In case of a mismatch or reaching the end of the word, the algorithm backtracks by restoring the original value of the cell.
# Time complexity is exponential, O(4^(mn)), where m and n are the dimensions of the board, due to the four possible directions at each step
# Space complexity is determined by the recursive call stack and is O(mn).

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(i, j, k):
            if k == len(word):
                return True
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:
                return False

            temp, board[i][j] = board[i][j], '/'  # Mark the current cell as visited
            found = (backtrack(i + 1, j, k + 1) or
                     backtrack(i - 1, j, k + 1) or
                     backtrack(i, j + 1, k + 1) or
                     backtrack(i, j - 1, k + 1))
            board[i][j] = temp  # Backtrack by restoring the original value
            return found

        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True
        return False

s=Solution()
# Example 1:
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(s.exist(board,word))
# Expected Output: true

# Example 2:
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"
print(s.exist(board,word))
# Expected Output: true

# Example 3:
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
print(s.exist(board,word))
# Expected Output: false