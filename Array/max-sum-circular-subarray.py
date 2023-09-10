#Question: Maximum Sum Circular Subarray
# Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.
# A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].
# A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.
    
#Approach:Kadane's Algorithm
# Use Kadane's algorithm to find the maximum subarray sum (max_sum) and the minimum subarray sum (min_sum) while keeping track of the total sum of the array. Then checks if max_sum is positive, and if so, return the maximum of max_sum and (total_sum - min_sum) to handle non-circular subarrays. Otherwise, return max_sum as the maximum circular subarray sum.

# Time Complexity: O(n) 
# Space Complexity: O(1)


def max_sum_circular_array(nums):
    max_sum, min_sum, total_sum = float('-inf'), float('inf'), 0
    max_temp, min_temp = 0, 0
    for num in nums:
        max_temp = max(max_temp + num, num)
        min_temp = min(min_temp + num, num)
        max_sum = max(max_sum, max_temp)
        min_sum = min(min_sum, min_temp)
        total_sum += num
    if max_sum > 0:
        # If max_sum is positive, return the maximum of max_sum and (total_sum - min_sum)
        return max(max_sum, total_sum - min_sum)
    else:
        # If max_sum is non-positive, return max_sum as it represents the maximum circular subarray sum
        return max_sum

nums = [1,-2,3,-2]
# Output: 3
# Explanation: Subarray [3] has maximum sum 3.
print(max_sum_circular_array(nums))

nums = [5,-3,5]
# Output: 10
# Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.
print(max_sum_circular_array(nums))

nums = [-3,-2,-3]
# Output: -2
# Explanation: Subarray [-2] has maximum sum -2.
print(max_sum_circular_array(nums))
