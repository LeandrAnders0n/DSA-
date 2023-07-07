#Question:Partition Labels
#You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.
# Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.
# Return a list of integers representing the size of these parts.
#Approach: Two Pointers
# Use two pointers to track the start and end positions of the current partition. 
# Iterate through the string, updating the end pointer to the maximum index of the last occurrence of each character. 
# When the current index matches the end pointer, this marks the end of a partition and we add size to the result. 
# Time Complexity: O(n)
# Space Complexity: O(1)

def partitionLabels(s):
    last_occurrence = {}
    for i, c in enumerate(s):
        last_occurrence[c] = i
    partitions = []
    start = 0
    end = 0
    for i, c in enumerate(s):
        end = max(end, last_occurrence[c])
        if i == end:
            partitions.append(end - start + 1)
            start = i + 1
    return partitions
    


s = "ababcbacadefegdehijhklij"
print(partitionLabels(s))
# Expected Output: [9,7,8]
s = "eccbbbbdec"
print(partitionLabels(s))
# Output: [10]