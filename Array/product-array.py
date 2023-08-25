#Question: Product of Array Except Self
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

#Approach:
# Calculate the product of all elements in the nums array except for the element at each index, without using division. Create two arrays left_products and right_products to store the product of elements to the left and right of each index. The final array is created by multiplying the corresponding elements from left_products and right_products
#Time Complexity and Space Complexity: O(n)
 

def product_array(nums):
    n=len(nums)
    left_products=[1]*n
    right_products=[1]*n

    left=1
    for i in range(n):
        left_products[i]=left
        left*=nums[i]

    right=1
    for i in range(n-1,-1,-1):
        right_products[i]=right
        right*=nums[i]

    answer=[ left_products[i]*right_products[i] for i in range(n)]

    return answer








nums = [1,2,3,4]
# Output: [24,12,8,6]
print(product_array(nums))

nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
print(product_array(nums))