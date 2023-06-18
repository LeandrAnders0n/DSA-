# Question:Four Sum
# Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:
# 0 <= i, j, k, l < n
# nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

# Approach:
# The code calculates the sum of all possible pairs from the first two arrays and stores them in a dictionary. 
# Then, it iterates over the remaining two arrays, finding the complement of the current pair sum and counting the number of tuples that satisfy the sum condition. 
# The final count is returned as the result. 
# This approach optimizes the time complexity to O(n^2) by using a dictionary for efficient lookup.

def four_sum_count(nums1,nums2,nums3,nums4):
    count = 0
    sums = {}
    
    # Calculate the sum of all possible pairs from nums1 and nums2
    for num1 in nums1:
        for num2 in nums2:
            pair_sum = num1 + num2
            sums[pair_sum] = sums.get(pair_sum, 0) + 1
    
    # Count the number of tuples that satisfy the sum condition
    for num3 in nums3:
        for num4 in nums4:
            target = -1 * (num3 + num4)
            if target in sums:
                count += sums[target]
    
    return count










nums1 = [1,2]
nums2 = [-2,-1]
nums3 = [-1,2]
nums4 = [0,2]

print(four_sum_count(nums1,nums2,nums3,nums4))