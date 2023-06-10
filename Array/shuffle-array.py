# Question:Shuffle the Array
# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].
#Approach:This code shuffles a list of integers by interleaving elements from two halves. 
# It creates a new list by combining elements from nums[i] and nums[i+n] in each iteration.
#Time Complexity and Space Complexity: O(n)

def shuffle(my_list,n):
    new_list=[]

    for i in range(n):
        new_list+=[my_list[i]]
        new_list+=[my_list[i+n]]

    return new_list

print(shuffle([1,2,3,4,5,6],3))