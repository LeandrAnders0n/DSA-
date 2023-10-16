#Question:86. Partition List
# Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
# You should preserve the original relative order of the nodes in each of the two partitions.
#Approach:
# Use two separate pointers, `before` and `after`, to track elements in each partition. While traversing the original list, rearrange the pointers to create two separate lists for values less than `x` and greater than or equal to `x`. The resulting modified list is returned after the traversal.

#Time complexity: O(n)
#Space Complexity: O(1) 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def partition(self, head, x):
    before, after = ListNode(0), ListNode(0)
    before_curr, after_curr = before, after
    
    while head:
        if head.val < x:
            before_curr.next, before_curr = head, head
        else:
            after_curr.next, after_curr = head, head
        head = head.next
    
    after_curr.next = None
    before_curr.next = after.next
    
    return before.next