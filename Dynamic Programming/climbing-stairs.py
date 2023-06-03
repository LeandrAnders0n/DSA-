# Question:Climbing Stairs
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Approach: Dynamic Programming
# The dynamic programming approach calculates the number of distinct ways to reach each step by summing up the number of distinct ways to reach the previous two steps. 
# The result is stored in the climb array.
 
def climbing_stairs(n):
    if n <=2:
        return 2
    climb=[0]*(n+1)

    climb[1]=1
    climb[2]=2

    for i in range(3,n+1):
        climb[i]=climb[i-1]+climb[i-2]
    return climb[n]

print("The number of combinations: ")
print(climbing_stairs(5))