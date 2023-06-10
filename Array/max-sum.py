# Question:Find the maximum subarray sum.
#Approach:Kadane's Algorithm
# Kadane's algorithm is used to find the maximum sum of a subarray within an array by iteratively updating the current subarray sum and the maximum sum found so far. 
# Time complexity: O(n)
# Space complexity:O(1)

def max_subarray_sum(my_list):
    max_value=float('-inf')
    temp=0

    for i in my_list:
        temp=max(i,temp+i)
        max_value=max(temp,max_value)

    return max_value
print(max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]))