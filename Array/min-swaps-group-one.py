#Question: You are given a binary array (with only 1s and 0s), and you are supposed to bring all the 1s to the right and all the 0s to the left, or vice-versa. The operation that can be performed is to swap two adjacent values, find the minimum number of operations needed.
#Approach:
# Iterate through the array from right to left, counting unplaced zeros and adding this count to the total swaps needed when encountering ones. 

# Time Complexity: O(n) 
# Space Complexity: O(1)


def swap(nums):
    count,unplaced_zeroes=0,0

    for i in range(len(nums)-1,-1,-1):
        if nums[i]==0:
            unplaced_zeroes+=1
        else:
            count+=unplaced_zeroes
    return count




nums=[0, 0, 1, 0, 1, 0, 1, 1]
# Output : 3
print(swap(nums))
nums=[0, 1, 0, 1, 0]
# Output : 3
print(swap(nums))
