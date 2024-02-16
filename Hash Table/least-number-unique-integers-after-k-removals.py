#Question:1481. Least Number of Unique Integers after K Removals
# Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

#Approach:
# Use the Counter class to count the frequency of each element in the input array, then sort these elements by frequency. Iterate through the sorted list, remove elements with the lowest frequencies until the remaining removals (k) are insufficient. Return the count of unique elements left after removals. 

# Time Complexity: O(n log n) for sorting, where n is the length of the input array.
# Space Complexity: O(n) for the Counter dictionary.
    
from typing import List
from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)

        sorted_counter = sorted(counter.items(), key=lambda item: item[1])

        for i, (num, freq) in enumerate(sorted_counter):
            if k >= freq:
                k -= freq
            else:
                return len(sorted_counter) - i

        return 0


s=Solution()
# Example 1:
arr = [5,5,4]
k = 1
print(s.findLeastNumOfUniqueInts(arr,k))
# Expected Output: 1
# Explanation: Remove the single 4, only 5 is left.

# Example 2:
arr = [4,3,1,1,3,3,2]
k = 3
print(s.findLeastNumOfUniqueInts(arr,k))
# Expected Output: 2
# Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.
 