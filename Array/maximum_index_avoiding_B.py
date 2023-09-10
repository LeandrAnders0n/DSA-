#Question: Maximum index a pointer can reach in N steps by avoiding a given index B
# Given two integers N and B, the task is to print the maximum index a pointer, starting from 0th index can reach in an array of natural numbers(i.e., 0, 1, 2, 3, 4, 5…), say arr[], in N steps without placing itself at index B at any point.
# In each step, the pointer can move from the Current Index to a Jumping Index or can remain at the Current Index. 
# Jumping Index = Current Index + Step Number

#Approach:
# Calculate the maximum reachable index by iterating through values from 0 to N-1, except for the value B. Accumulate the sum of 2^(N-i-1) for each iteration and return the integer value of the result. 

#Explanation:
# Calculate the maximum reachable index by considering the following:
# - For each iteration `i`,check if `i` is equal to `B`. If it is, then skip that iteration.
# - For each non-skipped iteration, calculate 2 raised to the power of `(N-i-1)` and add this value to `max_index`.

# Here's why this calculation is performed:
# - In a binary system, each bit represents a power of 2, starting from 2^0 on the rightmost bit and increasing by one as you move to the left.
# - By iterating through the bits from right to left (from 0 to N-1), the code calculates the maximum possible value that can be represented with N bits.
# - Excluding the bit represented by `B` allows you to calculate the maximum value achievable without considering a specific bit's contribution.

# In summary, the sum of 2^(N-i-1) for each non-excluded iteration calculates the maximum reachable index in a binary system by considering the contributions of each bit, excluding the bit represented by `B`.

# Time Complexity: O(n) 
# Space Complexity: O(1)

import math
def max_index_reached(N, B):
    max_index=0

    for i in range(N):
        if i!=B:
            max_index+=math.pow(2,N-i-1)
    return int(max_index)




N = 3
B = 2
# Output: 6
print(max_index_reached(N,B))

N = 3
B = 1
# Output: 5
print(max_index_reached(N,B))