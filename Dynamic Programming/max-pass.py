#Question: Maximum People Passing Exam
# Given a group of N individuals, each with corresponding test Scores and Bounds, determine the maximum number of individuals who can successfully pass the test. To pass, an individual's score must exceed a given threshold score. After passing, the individual's score is replaced by their bound value. Find the optimal strategy to maximize the number of successful passes.
#Approach: Dynamic Programming
# The code uses dynamic programming to find the maximum number of individuals who can pass a test, considering their Scores and Bounds. It iterates through each individual and calculates the maximum passes by comparing the passes without the current individual and passes including the current individual.

# Time Complexity: O(N * max_bound), where N is the number of individuals and max_bound is the maximum bound value in the bounds array.
# Space Complexity: O(N * max_bound), as it uses a 2D DP array to store intermediate results.

def maximumPassedPeople(N, score, bound):
    max_bound=max(bound)

    dp=[[0]*(max_bound+1) for _ in range(N+1)]

    for i in range(1,N+1):
        for j in range(max_bound+1):
            if j>=score[i-1]:
                dp[i][j]=max(dp[i-1][j], dp[i-1][j-bound[i-1]]+1)
            else:
                dp[i][j]=dp[i-1][j]
    return max(dp[N])



N = 5
score = [3, 7, 5, 10, 8]
bound = [4, 2, 2, 7, 3]

result = maximumPassedPeople(N, score, bound)
print(result)  
