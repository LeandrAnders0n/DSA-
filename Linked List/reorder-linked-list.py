#Question: 143. Reorder List
# You are given the head of a singly linked-list. The list can be represented as:
# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

#Approach:
# Reorder a singly linked list by first finding its middle point, then reversing the second half, and finally merging the two halves alternatively. Use a slow and fast pointer approach to find the middle, then reverse the second half in-place, and merge the halves by alternating between nodes.
 
# Time Complexity: O(n) 
# Space Complexity: O(1)

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
    
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
    
        p1, p2 = head, prev
        while p2.next:
            p1.next, p1 = p2, p1.next
            p2.next, p2 = p1, p2.next



s=Solution()
# Example 1:
head = [1,2,3,4]
print(s.reorderList(head))
# Expected Output: [1,4,2,3]

# Example 2:
head = [1,2,3,4,5]
print(s.reorderList(head))
# Expected Output: [1,5,2,4,3]