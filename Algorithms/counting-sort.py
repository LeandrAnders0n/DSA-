# Counting Sort: Counting sort is a non-comparison-based algorithm that counts the occurrences of each element and uses this information to place the elements in sorted order. 
# It has a time complexity of O(n + k), where n is the number of elements and k is the range of input values.


def counting_sort(my_list):
    max_value=max(my_list)

    count=[0]*(max_value+1)

    for n in my_list:
        count[n]+=1

    sorted_array=[]

    for i in range(len(count)):
        sorted_array.extend([i]*count[i])

    return sorted_array







print(counting_sort([4, 2, 1, 6, 4, 2, 9, 5]))


#time taken to find element
import timeit
def wrapper():
    (counting_sort([4, 2, 1, 6, 4, 2, 9, 5]))
print(timeit.timeit(wrapper, number=1))