# Heap Sort: Heap Sort uses a binary heap data structure to sort elements. 
# It builds a max-heap from the input array and repeatedly extracts the maximum element from the heap to obtain a sorted array. 
# It has a time complexity of O(n log n) in all cases.


# Simpler Solution with heapq
#import heapq
# def heap_sort(my_list):
#     heapq.heapify(my_list)
#     return my_list


def heapify(arr,n,i):
    largest=i
    left=2*i+1
    right=2*i+2

    if left <n and arr[left]>arr[largest]:
        largest=left

    if right<n and arr[right]>arr[largest]:
        largest=right

    if largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i]

        heapify(arr,n,largest)

def heap_sort(arr):
    n=len(arr)

    for i in range(n//2-1,-1-1):
        heapify(arr,n,i)

    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapify(arr,i,0)
    return arr


























print(heap_sort([64, 34, 25, 12, 22, 11, 90]))


#time taken to find element
import timeit
def wrapper():
    heap_sort([64, 34, 25, 12, 22, 11, 90])
print(timeit.timeit(wrapper, number=1))