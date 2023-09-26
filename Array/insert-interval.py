#Question: Insert Interval
# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
# Return intervals after the insertion.

#Approach:
# The code inserts a new interval into a sorted list of non-overlapping intervals while merging any overlapping intervals. It iterates through the intervals, adjusting the new interval as needed to accommodate overlaps. 
# Time complexity: O(n) where n is the number of intervals, and 
# Space complexity: O(1) because it modifies the input list in-place.

def insert_interval(intervals, newInterval):
        merged = []
        i = 0

        # Add all intervals that come before the newInterval
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i += 1

        # Merge overlapping intervals with the newInterval
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        merged.append(newInterval)

        # Add all intervals that come after the newInterval
        while i < len(intervals):
            merged.append(intervals[i])
            i += 1

        return merged

intervals = [[1,3],[6,9]] 
newInterval = [2,5]
# Output: [[1,5],[6,9]]
print(insert_interval(intervals,newInterval))

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
print(insert_interval(intervals,newInterval))

