#Question:Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

#Approach: We use slicing to extract the last k elements (nums[-k:]) and concatenate them with the elements from the beginning up to k (nums[:-k]). 
#This effectively rotates the list in-place by k positions. 
#The modified list is assigned back to nums[:] to update it in-place.
#time and space complexity of the code is O(n) and O(1) respectively.


def rotate(nums,k):
    k=k%len(nums)
    nums[:]=nums[-k:]+nums[:-k]

k=3
nums=[1,2,3,4,5]
rotate(nums,k)
print(nums)    