#Question
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

#Approach:The code sorts the intervals based on their start times and merges overlapping intervals by updating the end time of the last merged interval if necessary. It returns a list of non-overlapping intervals that cover all the intervals in the input.

# The time complexity is O(n log n) due to the sorting step, and the space complexity is O(n) to store the merged intervals, where n is the number of intervals.

def mergeIntervals(intervals):
    intervals.sort(key=lambda x:x[0])

    merged=[]

    for interval in intervals:
        if not merged or interval[0]>merged[-1][1]:
            merged.append(interval)
        else:
            merged[-1][1]=max(merged[-1][1],interval[1])
    return merged



intervals = [[1,3],[2,6],[8,10],[15,18]]
#Expected Output: [[1,6],[8,10],[15,18]]
print(mergeIntervals(intervals))