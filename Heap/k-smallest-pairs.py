#Question:373. Find K Pairs with Smallest Sums
# You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.
# Define a pair (u, v) which consists of one element from the first array and one element from the second array.
# Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

#Approach: Min Heap
# This code implements a solution to find the k smallest pairs from two sorted arrays, `nums1` and `nums2`, using a min heap. It maintains a heap (`minHeap`) of pairs' sums along with their indices. It starts with the pair of indices (0, 0) and iteratively pops the smallest sum from the heap, adds the corresponding pair to the result (`ans`), and pushes the next possible pairs with their sums into the heap. The process continues until either k pairs are found or the heap is empty. The use of a set (`visited`) ensures that each pair is considered only once. The result is a list of k smallest pairs.


# Time complexity: O(k log(min(m, n))), where m and n are the lengths of nums1 and nums2.
# Space complexity: O(min(k, m * n)) for the heap and visited set.
    
from typing import List

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        from heapq import heappush, heappop
        m = len(nums1)
        n = len(nums2)

        ans = []
        visited = set()

        minHeap = [(nums1[0] + nums2[0], (0, 0))]
        visited.add((0, 0))
        count = 0

        while k > 0 and minHeap:
            val, (i, j) = heappop(minHeap)
            ans.append([nums1[i], nums2[j]])

            if i + 1 < m and (i + 1, j) not in visited:
                heappush(minHeap, (nums1[i + 1] + nums2[j], (i + 1, j)))
                visited.add((i + 1, j))

            if j + 1 < n and (i, j + 1) not in visited:
                heappush(minHeap, (nums1[i] + nums2[j + 1], (i, j + 1)))
                visited.add((i, j + 1))
            k = k - 1
        
        return ans

s=Solution()
# Example 1:
nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3
print(s.kSmallestPairs(nums1,nums2,k))
# Expected Output: [[1,2],[1,4],[1,6]]
# Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

# Example 2:
nums1 = [1,1,2]
nums2 = [1,2,3]
k = 2
print(s.kSmallestPairs(nums1,nums2,k))
# Expected Output: [[1,1],[1,1]]
# Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

# Example 3:
nums1 = [1,2]
nums2 = [3]
k = 3
print(s.kSmallestPairs(nums1,nums2,k))
# Expected Output: [[1,3],[2,3]]
# Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]