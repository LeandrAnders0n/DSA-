#Question:Stone Game
# Alice and Bob play a game with piles of stones. There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].
# The objective of the game is to end with the most stones. The total number of stones across all the piles is odd, so there are no ties.
# Alice and Bob take turns, with Alice starting first. Each turn, a player takes the entire pile of stones either from the beginning or from the end of the row. This continues until there are no more piles left, at which point the person with the most stones wins.
# Assuming Alice and Bob play optimally, return true if Alice wins the game, or false if Bob wins.

#Approach: Dynamic Programming
# This code implements the stone game algorithm using dynamic programming. 
# It calculates the maximum score difference between two players playing optimally. 
# It initializes a 2D list dp to store the scores, iterates through different lengths of subarrays, and computes the optimal score difference based on previous calculations. 
# The function returns True if the first player has a higher score than the second player.

# The time complexity of the given code is O(n^2)
# The space complexity is O(n^2)



def stoneGame(piles):
    n=len(piles)
    dp=[[0]*n for _ in range(n)]

    for i in range(n):
        dp[i][i]=piles[i]

    for length in range(2,n+1):
        for i in range(n-length+1):
            j=i+length-1

            dp[i][j]=max(piles[i]-dp[i+1][j],piles[j]-dp[i][j-1])
    return dp[0][n-1]>0




piles = [5,3,4,5]
# Expected Output: True
print(stoneGame(piles))