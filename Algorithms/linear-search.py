#Linear Search
#Linear search sequentially checks each element in a list or array until the target element is found or the end of the list is reached.
#Time Complexity: O(n)
#Space Complexity: O(1)

def linear_search(my_list,target):
    for i in range(0,len(my_list)):
        if my_list[i]==target:
            return i
    return -1

f=linear_search([2,5,1,4,8,7],7)
if f!=-1:
    print("The Element was found at ",f)
else:
    print("Element does not exist")


#time taken to find element
import timeit
def wrapper():
    linear_search([2,5,1,4,8,7],7)
print(timeit.timeit(wrapper, number=1))