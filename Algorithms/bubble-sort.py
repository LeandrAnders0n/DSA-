# Bubble Sort: Bubble Sort compares adjacent elements and swaps them if they are in the wrong order. 
#It repeatedly passes through the list until the entire list is sorted. 
#Time complexity of O(n^2) in the worst case.


def bubble_sort(my_list):
    n=len(my_list)-1

    for i in range(n):
        for j in range(n-i):
            if my_list[j]>my_list[j+1]:
                my_list[j],my_list[j+1]=my_list[j+1],my_list[j]
    return my_list








print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))



#time taken to find element
import timeit
def wrapper():
    bubble_sort([64, 34, 25, 12, 22, 11, 90])
print(timeit.timeit(wrapper, number=1))