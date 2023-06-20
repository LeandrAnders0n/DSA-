#Question: Container With Most Water
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.

#Approach:Two Pointer
# The code utilizes a two-pointer approach to find the maximum area of water between two vertical lines represented by the heights in the list. It iterates by moving the pointers inward, calculating the water area based on the minimum height and the distance between the pointers. The maximum water area is updated if a larger area is found. The process continues until the pointers meet. 

# The time complexity is O(n), and the space complexity is O(1).

#Question:https://leetcode.com/problems/container-with-most-water/description/?envType=study-plan-v2&envId=top-interview-150

def container_max_water(height):
    side1 = 0
    side2 = len(height) - 1
    max_water = 0
    while side1 < side2:
        current_height = min(height[side1], height[side2])
        current_width = side2 - side1
        water = current_height * current_width
        if water > max_water:
            max_water = water
        if height[side1] < height[side2]:
            side1 += 1
        else:
            side2 -= 1
    return max_water

    

# Input
height = [1,8,6,2,5,4,8,3,7]
print(container_max_water(height))
# Expected Output: 49