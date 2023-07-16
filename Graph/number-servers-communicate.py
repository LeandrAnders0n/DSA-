#Question: Count Servers that Communicate
#You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.
# Return the number of servers that communicate with any other server.

#Approach:Count the number of servers that communicate with any other server in a grid. 
# Iterate over the grid to count the number of servers in each row and column. 
# Then, check if each row has multiple servers that communicate internally and count them. 
# Finally, check if each server in the grid communicates with at least one other server in its column and count them.

# Time Complexity: O(m * n)
# Space Complexity: O(max(m, n))
 
def servers(grid):
    m,n=len(grid),len(grid[0])

    rows=[0]*m
    cols=[0]*n

    for i in range(m):
        for j in range(n):
            if grid[i][j]:
                cols[j]+=1
                rows[i]+=1
    
    result=0

    for i in range(m):
        if rows[i]>1:
            result+=rows[i]
            continue
    for j in range(n):
        if(grid[i][j] and cols[j]>1):
            result+=1
    
    return result






grid = [[1, 0], [0, 1]]
print(servers(grid))
# Expected Output: 0

grid = [[1, 0], [1, 1]]
print(servers(grid))
# Expected Output: 3
