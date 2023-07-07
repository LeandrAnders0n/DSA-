#Question:Difference of Two Arrays
#Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
# answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
# answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
# Note that the integers in the lists may be returned in any order.

#Approach:Find the differences between two lists, nums1 and nums2, using sets and store the results in a 2D list diff. Iterate through the unique elements of nums1 and nums2 and check for elements that are present in one set but not the other, adding them to the respective sublists in diff.

# Time complexity: O(n) 
# Space complexity: O(n)

def difference(nums1,nums2):
        s1 = set(nums1)
        s2 = set(nums2)
        
        diff = [[],[]]

        for n1 in s1:
            if n1 not in s2:
                diff[0].append(n1)
        
        for n2 in s2:
            if n2 not in s1:
                diff[1].append(n2)
        
        return diff

nums1,nums2 = [1,2,3], [2,4,6]
# Expected Output: [[1,3],[4,6]]
print(difference(nums1,nums2))
nums1,nums2 = [1,2,3,3],[1,1,2,2]
print(difference(nums1,nums2))
# Expected Output: [[3],[]]
