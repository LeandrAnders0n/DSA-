# Question:Longest Consecutive Sequence
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

# Approach:
#This code finds the length of the longest consecutive sequence in an unsorted array of integers. It converts the array into a set for quick lookup. 
# It iterates through the array and counts the length of consecutive sequences by incrementing the current number until the next consecutive element is not found. The maximum length encountered is returned. 
# The time complexity is O(n) as it only needs to iterate through the array once.

def longest_consec_seq(nums):
    num_set=set(nums)
    max_length=0

    for num in nums:
        if num-1 not in num_set:
            curr_num=num
            curr_length=1

            while curr_num+1 in num_set:
                curr_num+=1
                curr_length+=1
            max_length=max(max_length,curr_length)

    return max_length
   


nums = [100,4,200,1,3,2]
# Expected Output: 4
print(longest_consec_seq(nums))