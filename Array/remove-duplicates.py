#Question:  Remove Duplicates from Sorted Array
#Appraoch:Iterate through the array. Pop repeating elements and adjust the length and index accordingly
#If duplicate element occurs, pop the element at index and reduce the length of the array
#If not increment the index and check for the next element
#space complexity of the updated removeDuplicates method is O(1)
#time complexity of the method is O(n)
class Solution():
    def removeDuplicates(self,my_list):
        n=len(my_list)-1
        i=0
        while i<n:
            if my_list[i]==my_list[i+1]:
                my_list.pop(i+1)
                n-=1
            else:
                i+=1
        return my_list
sol=Solution()
res=sol.removeDuplicates([1,1,1,1,2,2,2,4,4,4,3])
print(res)