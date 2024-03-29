#Question: 2962. Count Subarrays Where Max Element Appears at Least K Times
# You are given an integer array nums and a positive integer k.
# Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.
# A subarray is a contiguous sequence of elements within an array.

#Approach: Sliding Window
# Iterate through the list using a sliding window approach, maintaining pointers `left` and `right` to mark the boundaries of the current window. At each step, check if the maximum element of the current window appears at least k times. If it does, calculate the number of subarrays ending at the `right` pointer and add it to the `subarray_count`. The inner while loop shrinks the window from the left side until the condition is no longer met. Finally, return the `subarray_count`, which represents the total number of subarrays meeting the given condition.

# Time Complexity: O(n)
# Space Complexity: O(1)


from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_value, subarray_count, left, right, length = max(nums), 0, 0, 0, len(nums)
        
        while right < length:
            k -= nums[right] == max_value
            right += 1
            
            while k == 0:
                subarray_count += length - right + 1  
                k += nums[left] == max_value
                left += 1
                
        return subarray_count
s=Solution()

# Example 1:
nums = [1,3,2,3,3]
k = 2
print(s.countSubarrays(nums,k))
# Expected Output: 6
# Explanation: The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].

# Example 2:
nums = [1,4,2,1]
k = 3
print(s.countSubarrays(nums,k))
# Expected Output: 0
# Explanation: No subarray contains the element 4 at least 3 times.