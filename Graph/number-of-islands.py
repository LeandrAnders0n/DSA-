#Question:Number of Islands
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

#Approach:
# We traverse the graph in depth-first search (DFS) manner, to count the number of islands in a 2D binary grid. 
# Start from each land cell ('1') and explore all adjacent land cells, marking them as visited.
# Increment the island count when encountering a land cell, and start the traversal from that cell. 
# The final result is the island count.

def num_islands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    island_count = 0
    def traverse(row, col):
        if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] != '1':
            return
        grid[row][col] = '0'  
        traverse(row + 1, col)
        traverse(row - 1, col)
        traverse(row, col + 1)
        traverse(row, col - 1)
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '1':
                island_count += 1
                traverse(row, col)
    return island_count






grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
# Expected Output: 1
print("Grid 1: ",num_islands(grid))

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
# Expected Output: 3
print("Grid 2: ",num_islands(grid))