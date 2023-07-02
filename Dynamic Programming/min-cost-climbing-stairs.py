#Question:Min Cost Climbing Stairs
#You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
# You can either start from the step with index 0, or the step with index 1.
# Return the minimum cost to reach the top of the floor.
#Approach: Dynamic Programming
#Use dynamic programming to find the minimum cost to reach the top of the floor. Initialize a list dp to store the minimum cost for each step, starting from step 0 or step 1. 
# Iteratively calculate the minimum cost for each step by considering the cost of the current step and the minimum cost of the previous two steps. 
# Finally, return the minimum value between the last two steps in the dp list, representing the minimum cost to reach the top.

# Time Complexity:O(n)
# Space Complexity: O(n)

def min_cost(cost):
    n=len(cost)
    dp=[0]*(n+1)
    #base case
    dp[0]=cost[0]
    dp[1]=cost[1]

    for i in range(2,n):
        dp[i]=cost[i]+min(dp[i-1],dp[i-2])
    return min(dp[n-1],dp[n-2])

cost = [10,15,20]
# Expected Output: 15
print(min_cost(cost))

cost = [1,100,1,1,1,100,1,1,100,1]
# Expected Output: 6
print(min_cost(cost))