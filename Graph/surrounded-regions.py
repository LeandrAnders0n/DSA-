#Question:130. Surrounded Regions
# Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.
# A region is captured by flipping all 'O's into 'X's in that surrounded region.

#Approach: BFS Traversal
# Utilize a breadth-first search (BFS) strategy to identify and mark 'O' cells on the board's borders as 'Y', indicating that they are not surrounded by 'X'. Enqueue these border cells for BFS traversal. Dequeue cells and explore their neighboring cells, marking valid 'O' cells as 'Y' and enqueuing them for further exploration. Repeat this process until the deque is empty. After completing BFS, iterate through the entire board, changing 'O' cells to 'X' if they are surrounded by 'X' and reverting 'Y' cells back to 'O'. This approach effectively captures and updates regions that are not surrounded by 'X', ultimately solving the problem.

#Time and Space Complexity:O(m * n)

from typing import List
from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m=len(board)
        n=len(board[0])
        q=deque()
        for i in range(m):
            for j in range(n):
                if i==0 or i==m-1 or j==0 or j==n-1:
                    if board[i][j]=='O':
                        board[i][j]='Y'
                        q.append((i,j))   
        while q:
            a,b=q.popleft()
            for r,c in [(a-1,b),(a+1,b),(a,b-1),(a,b+1)]:
                if 0<=r<m and 0<=c<n and board[r][c]=='O':
                    board[r][c]="Y"
                    q.append((r,c))
        for i in range(m):
            for j in range(n):
                if board[i][j]=='O':
                    board[i][j]='X'
                elif board[i][j]=='Y':
                    board[i][j]='O'
        return board
s=Solution()
# Example 1:
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
print(s.solve(board))
# Expected Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# Explanation: Notice that an 'O' should not be flipped if:
# - It is on the border, or
# - It is adjacent to an 'O' that should not be flipped.
# The bottom 'O' is on the border, so it is not flipped.
# The other three 'O' form a surrounded region, so they are flipped.

# Example 2:
board = [["X"]]
print(s.solve(board))
# Expected Output: [["X"]]