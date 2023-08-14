#Question: Split Array Largest Sum
# Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.
# Return the minimized largest sum of the split.
# A subarray is a contiguous part of the array.
#Approach: Binary Search
# We perform binary search to find the minimum possible maximum subarray sum when splitting the given array into k subarrays. Verify if it's possible to split the array with a maximum sum less than or equal to a given mid. 
# Time Complexity: O(n * log(nums))
# Space Complexity: O(1)

def split_array(nums,k):
    def check(mid):
        subarray_count=1
        subarray_sum=0

        for num in nums:
            if subarray_sum+num>mid:
                subarray_count+=1
                subarray_sum=num
            else:
                subarray_sum+=num
        return subarray_count<=k
    
    left=max(nums)
    right=sum(nums)

    while left<right:
        mid=left+(right-left)//2

        if check(mid):
            right=mid
        else:
            left=mid+1

    return left


nums = [7,2,5,10,8]
k = 2
# Output: 18
print(split_array(nums,k))

nums = [1,2,3,4,5]
k = 2
# Output: 9
print(split_array(nums,k))