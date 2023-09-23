#Question: Valid Sudoku
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

#Approach:
# 1) Initialize an empty list called "res," which stores valid elements.
# 2) Iterate through each cell in the board, retrieving the element in that cell.
# 3) If the element is not a dot ('.'), indicating a valid number, add three tuples to "res":
#    - First tuple: (row index, element)
#    - Second tuple: (element, column index)
#    - Third tuple: (3x3 sub-grid index (row and column), element)
# 4) Check if the length of "res" is equal to the length of the set of "res" to ensure there are no repetitions, confirming the validity of the Sudoku board.

def valid_sudoku(board):
    res=[]
    for i in range(9):
        for j in range(9):
            if board[i][j]!='.':
                res+=[(i,board[i][j]),(board[i][j],j),(i//3,j//3,board[i][j])]
    return len(res)==len(set(res))


board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
# Output: true
print(valid_sudoku(board))

board =[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
# Output: false
print(valid_sudoku(board))
