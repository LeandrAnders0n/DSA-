#Question: Summary Ranges
# You are given a sorted unique integer array nums.
# A range [a,b] is the set of all integers from a to b (inclusive).
# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.
# Each range [a,b] in the list should be output as:
# "a->b" if a != b
# "a" if a == b

#Approach:
# Iterate through `nums`, identify consecutive numbers to form ranges, and construct strings for these ranges. 
# Time & Space Complexity is O(n)

def summary_ranges(nums):
    if not nums:
        return []
    intervals = []
    start = nums[0]
    
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] + 1:
            continue
        elif start == nums[i - 1]:
            intervals.append(str(start))
        else:
            intervals.append(str(start) + "->" + str(nums[i - 1]))
        start = nums[i]
    
    # Handle the last number
    if start == nums[-1]:
        intervals.append(str(start))
    else:
        intervals.append(str(start) + "->" + str(nums[-1]))
    
    return intervals


nums = [0,1,2,4,5,7]
print(summary_ranges(nums))
# Output: ["0->2","4->5","7"]
# Explanation: The ranges are:
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"

nums = [0,2,3,4,6,8,9]
print(summary_ranges(nums))
# Output: ["0","2->4","6","8->9"]
# Explanation: The ranges are:
# [0,0] --> "0"
# [2,4] --> "2->4"
# [6,6] --> "6"
# [8,9] --> "8->9"