#Question: Candy
#There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.
# You are giving candies to these children subjected to the following requirements:
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# Return the minimum number of candies you need to have to distribute the candies to the children.

#Approach: Greedy Algorithm
# Use a greedy algorithm, initialize each child with one candy. Iterate through the ratings twice, first ensuring that children with higher ratings have more candies than their left neighbors, and second, making sure higher-rated children also have more candies than their right neighbors while not decreasing candies for already higher-rated children. Finally, Calculates the total number of candies needed to meet these conditions, by summing the candies.

# Time Complexity & Space Complexity : O(n)

def candies(ratings):
    n = len(ratings)
    if n <= 1:
        return n
    candies = [1] * n
    # Traverse the ratings from left to right
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1
    # Traverse the ratings from right to left and make sure higher-rated children
    # have more candies than their neighbors on the right.
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)
    # Calculate the total number of candies required
    return sum(candies)



ratings = [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
print(candies(ratings))

ratings = [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
# The third child gets 1 candy because it satisfies the above two conditions.
print(candies(ratings))
