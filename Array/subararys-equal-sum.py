#Question:Find Subarrays With Equal Sum
#Given a 0-indexed integer array nums, determine whether there exist two subarrays of length 2 with equal sum. 
# Note that the two subarrays must begin at different indices.
# Return true if these subarrays exist, and false otherwise.
#Approach:Find the sum of consecutive elements, and add it to a list. Check if the sum alreay exists, and if so return true, else false
# Time complexity: O(n) 
# Space complexity: O(n)

def subarray_sum(my_list):

    sum=[]

    for i in range(len(my_list)-1):

        if my_list[i]+my_list[i+1] in sum:
            return True
        else:
            sum.append(my_list[i]+my_list[i+1])
    return False

print(subarray_sum([4,2,4]))