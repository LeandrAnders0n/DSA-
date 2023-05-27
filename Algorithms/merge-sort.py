# Merge Sort: Merge Sort is a divide-and-conquer algorithm that recursively divides the input list into smaller sublists, sorts them, and then merges them to obtain a sorted output. 
#  The code includes a merge_sort function that recursively divides the list and calls a merge function to merge the sorted sublists. 
# The sorted list is then printed. Additionally, the code measures the execution time of the sorting process using the timeit module and prints the result.
# It has a time complexity of O(n log n) in all cases, making it efficient for large data sets.



def merge_sort(my_list):
    n = len(my_list)

    if n <= 1:
        return my_list
    mid = n // 2

    left = merge_sort(my_list[:mid])
    right = merge_sort(my_list[mid:])

    return merge(left, right)

def merge(left, right):
    i = j = 0
    merged = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged

print(merge_sort([64, 34, 25, 12, 22, 11, 90]))

#time taken to sort
import timeit
def wrapper():
    merge_sort([64, 34, 25, 12, 22, 11, 90])

execution_time = timeit.timeit(wrapper, number=1)
print(f"Execution time: {execution_time} seconds")
