#Question:Merge Sorted Array
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
#Approach:The code merges two sorted arrays into a single sorted array by comparing elements and appending them to a new list. 
#Time and Space Complexity: O(n), where n is the total number of elements in both arrays


def merge_sorted_arrays(arr1, arr2):

    n1,n2=len(arr1),len(arr2)
    merged=[]
    i,j=0,0

    while i<n1 and j<n2:
        if arr1[i]<=arr2[j]:
            merged.append(arr2[i])
            i+=1
        else:
            merged.append(arr2[j])
            j+=1
    while i<n1:
        merged.append(arr1[i])
        i+=1
    while j<n2:
        merged.append(arr2[j])
        j+=1
    return merged



















arr1 = [1, 3, 5, 7, 9]
arr2 = [2, 4, 6, 8]
merged_arr = merge_sorted_arrays(arr1, arr2)
print(merged_arr)
