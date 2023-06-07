# Question:Given an array of size N-1 such that it only contains distinct integers in the range of 1 to N. 
# Find the missing element.
# Approach:We calculates the missing number in an array by finding the difference between the expected sum of numbers from 1 to n and the actual sum of the given array elements. 
# It returns the missing number.
# Time Complexity: O(n) 
# Space Complexity: O(1)

def missing_number(my_list):
    n=len(my_list)+1

    expected_sum=(n*(n+1))//2

    actual_sum=sum(my_list)

    return expected_sum-actual_sum

print(missing_number([1,2,3,5]))