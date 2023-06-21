# Question:According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
# The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):
# Any live cell with fewer than two live neighbors dies as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

#Approach:
# The game_of_life function implements the rules of Game of Life on a given board of cells represented by a 2D list. 
# It iterates through each cell, counts the number of live neighbors, and updates the cell based on the count and its current state. Live cells with fewer than 2 or more than 3 live neighbors are marked for death, while dead cells with exactly 3 live neighbors are marked for revival. The function then updates the board with the next state by converting marked cells to 1 or 0. 
# Finally, it returns the modified board.


def game_of_life(board):
    m, n = len(board), len(board[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    for i in range(m):
        for j in range(n):
            live_neighbors = 0

            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < m and 0 <= nj < n and (board[ni][nj] == 1 or board[ni][nj] == 2):
                    live_neighbors += 1

            if board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                # Live cell dies
                board[i][j] = 2
            elif board[i][j] == 0 and live_neighbors == 3:
                # Dead cell becomes live
                board[i][j] = 3

    # Update the board with the next state
    for i in range(m):
        for j in range(n):
            board[i][j] %= 2  # Set live cells to 1 and dead cells to 0

    return board
  
    
board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
print(game_of_life(board))
        















