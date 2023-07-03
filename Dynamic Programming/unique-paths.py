#Question:Unique Paths
#There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

#Approach:Dynamic Programming
#Use dynamic programming to calculate the number of unique paths in a grid of size m by n. Initialize a 2D matrix dp of size (m+1) x (n+1) with all values set to 0, except for dp[1][1] which is set to 1, because if we have a 1 x 1 grid, there is only one path. Then iterate through the matrix, updating each cell with the sum of the values from the adjacent cells. Finally, return the value at dp[m][n], which represents the number of unique paths.

# Time & Space complexity: O(m x n): The 2D matrix dp has dimensions (m+1) x (n+1)

def unique_paths(m,n):
    #create matrix
    dp=[[0]*(n+1) for _ in range(m+1)]

    #base case
    dp[1][1]=1

    for i in range(m+1):
        for j in range(n+1):
            curr=dp[i][j]

            #right
            if j+1<n+1:
                dp[i][j+1]+=curr
            #down
            if i+1<m+1:
                dp[i+1][j]+=curr
    return dp[m][n]    




# Input: m = 3, n = 2
# Expected Output: 3
print(unique_paths(3,2))

# Input: m = 3, n = 7
# Expected Output: 28
print(unique_paths(3,7))