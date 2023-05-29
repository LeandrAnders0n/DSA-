# Heap:
# A heap is a specialized tree-based data structure that satisfies the heap property. 
# There are two types:
# Min Heap: The minimum value is at the root, and each parent node is smaller than or equal to its child nodes.
# Max Heap: The maximum value is at the root, and each parent node is greater than or equal to its child nodes.

import heapq

my_list=[64, 34, 25, 12, 22, 11, 90]

min_heap=[]
for n in my_list:
    heapq.heappush(min_heap,n)

max_heap=[]
for n in my_list:
    heapq.heappush(max_heap,-n)

print("Min Heap")
while min_heap:
    print(heapq.heappop(min_heap),end=" ")

print("\nMax Heap")
while max_heap:
    print(-heapq.heappop(max_heap),end=" ")
