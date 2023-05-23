# Binary Search
# Binary search is a searching algorithm that locates the target element in a sorted list or array by repeatedly dividing the search space in half.
# Time Complexity: O(log n)
# Space Complexity: O(1)

def binary_search(my_list,target):
    low=0
    high=len(my_list)-1

    while low<=high:
        mid=(low+high)//2

        if my_list[mid]==target:
            return mid
        elif my_list[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1









f = binary_search([1, 2, 4, 5, 7, 8], 7)
if f != -1:
    print("The Element was found at", f)
else:
    print("Element does not exist")

# Time taken to find element
import timeit

def wrapper():
    binary_search([1, 2, 4, 5, 7, 8], 7)

print(timeit.timeit(wrapper, number=1))
