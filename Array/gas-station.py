#Question: Gas Station
# There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.
# Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique

#Approach: Greedy Approach
#Iterate through the gas stations, tracking the total gas available and the gas remaining after traveling to the next station. If the remaining gas becomes negative, update the potential starting station and resets the remaining gas. If the total gas available is non-negative at the end, return the potential starting station; otherwise, it return -1 to indicate an impossible solution.

# Time Complexity: O(n)
# Space Complexity: O(1)

def can_circuit(gas,cost):
    total_gas = 0  # Keep track of total gas available.
    current_gas = 0  # Keep track of current gas available from the starting station.
    start_station = 0  # Index of the potential starting station.
    for i in range(len(gas)):
        total_gas += gas[i] - cost[i]
        current_gas += gas[i] - cost[i]
        if current_gas < 0:
            # If we can't reach the next station from the current one, update start_station and reset current_gas.
            start_station = i + 1
            current_gas = 0
    
    # If the total gas available is negative, it means the total cost is greater than the total gas, and a solution is impossible.
    return start_station if total_gas >= 0 else -1

gas = [1,2,3,4,5] 
cost = [3,4,5,1,2]
# Output: 3
print(can_circuit(gas,cost))    

gas = [2,3,4] 
cost = [3,4,3]
# Output: -1
print(can_circuit(gas,cost))    

