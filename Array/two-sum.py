#Question: Two Sum
# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.
#Approach: Enumerate the list values and add the value-index pair to a dictionary
#Check for the complement in the dictionary, if found return the indexes, else add the 
#to the dictionary
class Solution():
    def twoSum(self,my_list,target):
        values={}
        for i,num in enumerate(my_list):
            complement=target-num
            if complement in values:
                return [values[complement],i]
            values[num]=i
sol=Solution()
res=sol.twoSum([2,7,5,0,1],9)
print(res)



                                
                        