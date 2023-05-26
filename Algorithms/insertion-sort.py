# Insertion Sort: Insertion Sort builds the final sorted array one element at a time by inserting each element into its correct position within the sorted region.
# It has a time complexity of O(n^2) in the worst case, but performs well for small or partially sorted lists.



def insertion_sort(my_list):
    n=len(my_list)

    for i in range(1,n):
        j=i-1
        key=my_list[i]

        while j>=0 and my_list[j]>key:
            my_list[j+1]=my_list[j]
            j-=1
        my_list[j+1]=key

    return my_list



print(insertion_sort([64, 34, 25, 12, 22, 11, 90]))


#time taken to find element
import timeit
def wrapper():
    insertion_sort([64, 34, 25, 12, 22, 11, 90])
print(timeit.timeit(wrapper, number=1))