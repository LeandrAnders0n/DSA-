##Question: Reverse A String
# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.
## Approach:Use 2 pointers, one at the start of the array and one at the end, called left and right respectively.
# Swap the elements using the pointers, increment the left pointer and decrement the right pointer.
#This process continues until the pointers meet at the middle of the array, effectively reversing the array in-place.

class Solution():
    def reverseString(self,my_string):
        left,right=0,len(my_string)-1
        while left<right:
            my_string[left],my_string[right]=my_string[right],my_string[left]
            left+=1
            right-=1
        return my_string
sol=Solution()
res=sol.reverseString(["h","e","l","l","o"])
print(res)