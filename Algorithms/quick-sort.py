# Quick Sort: 
# Quick Sort is also a divide-and-conquer algorithm. 
# It selects a "pivot" element and partitions the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. 
# It then recursively sorts the sub-arrays. 
# It has an average time complexity of O(n log n), but can have a worst-case time complexity of O(n^2) if the pivot selection is not optimized.


def quick_sort(my_list):
    n=len(my_list)

    if n<=1:
        return my_list
    else:
        pivot=my_list[0]

        greater=[x for x in my_list[1:] if x>=pivot]
        lesser=[x for x in my_list[1:] if x<=pivot]

        return quick_sort(lesser)+[pivot]+quick_sort(greater)


print(quick_sort([64, 34, 25, 12, 22, 11, 90]))

#time taken to sort
import timeit
def wrapper():
    quick_sort([64, 34, 25, 12, 22, 11, 90])

execution_time = timeit.timeit(wrapper, number=1)
print(f"Execution time: {execution_time} seconds")