#Question:82. Remove Duplicates from Sorted List II
# Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

#Approach:
# Use a dummy node to simplify edge cases and iterate through the list. When encountering duplicate values, skip over them by adjusting pointers.

# Time complexity: O(n)
# Space complexity: O(1)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(head):
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current.next and current.next.next:
            if current.next.val == current.next.next.val:
                val_to_skip = current.next.val
                while current.next and current.next.val == val_to_skip:
                    current.next = current.next.next
            else:
                current = current.next

        return dummy.next

