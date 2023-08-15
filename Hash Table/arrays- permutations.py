#Question:Check if two arrays are permutations of each other
# Given two unsorted arrays of the same size, write a function that returns true if two arrays are permutations of each other, otherwise false.
#ApproachL Hash Table
# We check if arrays a1 and a2 are permutations of each other by comparing the frequency of their elements. Use dictionaries to count element frequencies and then compare the dictionaries.
# Time Complexity: O(N),
# Space Complexity: O(M), where M is the total number of unique elements in both arrays.
def array_permutations(a1, a2):
    if len(a1)!=len(a2):
        return False
    
    count1={}
    count2={}

    for b1 in a1:
        count1[b1]=count1.get(b1,0)+1
    
    for b2 in a2:
        count2[b2]=count2.get(b2,0)+1

    return count1==count2


arr1 = [2, 1, 3, 5, 4, 3, 2]
arr2 = [3, 2, 2, 4, 5, 3, 1]
# Output: Yes
print(array_permutations(arr1,arr2))

arr1 = [2, 1, 3, 5,]
arr2 = [3, 2, 2, 4]
# Output: No
print(array_permutations(arr1,arr2))

arr1 = [1, 2, 2, 3]
arr2 = [1, 2, 3, 3]
# Output: No
print(array_permutations(arr1,arr2))
