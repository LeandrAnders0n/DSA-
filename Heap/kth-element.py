#HEAP:A min heap is a specialized data structure that maintains the minimum element at the top (root) of the heap. 
# It is a complete binary tree where the value of each node is less than or equal to the values of its child nodes.

#Question:Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# You must solve it in O(n) time complexity.
#Approach:Create an empty min heap.
# Iterate through the array,if the heap size is less than k, add the element to the heap.
# If the heap size is equal to k, compare the element with the root of the heap (minimum element). 
# If the element is larger, replace the root with the current element. 
# After iterating through all elements,the root of the heap will contain the kth largest element.

import heapq

def kthElement(nums,k):
    heap=[]

    for n in nums:
        if len(heap)<k:
            heapq.heappush(heap,n)
        elif n>heap[0]:
            heapq.heapreplace(heap,n)
    return heap[0]

#Optimized Approached
# def kthElement(nums,k):
#     return heapq.nlargest(k, nums)[-1]

print(kthElement([3,1,4,5,7,2],2))