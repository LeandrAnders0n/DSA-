# Selection Sort: Selection Sort divides the input into a sorted and an unsorted region. 
# It repeatedly selects the smallest (or largest) element from the unsorted region and swaps it with the leftmost unsorted element. 
# Time complexity of O(n^2) in all cases.


def selection_sort(my_list):
    n=len(my_list)

    for i in range(n-1):

        min_index=i

        for j in range(i+1,n):

            if my_list[j]<my_list[min_index]:
                min_index=j

        my_list[i],my_list[min_index]=my_list[min_index],my_list[i]
    return my_list



print(selection_sort([64, 34, 25, 12, 22, 11, 90]))


#time taken to find element
import timeit
def wrapper():
    (selection_sort([64, 34, 25, 12, 22, 11, 90]))
print(timeit.timeit(wrapper, number=1))