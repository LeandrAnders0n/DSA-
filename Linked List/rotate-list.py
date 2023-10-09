#Question:61 Rotate List
#Given the head of a linked list, rotate the list to the right by k places.

#Approach:
# First, calculate the effective rotation amount by taking the modulo of `k` with the length of the linked list. Then, identify the new head and tail of the rotated list using two pointers (`slow` and `fast`). Finally, adjust the next pointers to achieve the rotation and return the new head of the rotated list. The original head is returned if the linked list is empty or has only one node, or if the effective rotation amount is zero.

# Time complexity: O(n)
# Space complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def rotate_list(head,k):
    # Check if the linked list is empty or has only one node
    if not head or not head.next:
        return head
    # Find the length of the linked list
    length = 1
    current = head
    while current.next:
        current = current.next
        length += 1
    # Calculate the effective rotation amount
    k = k % length
    # If k is zero, no rotation is needed
    if k == 0:
        return head
    # Find the new head and tail of the rotated list
    slow = fast = head
    for _ in range(k):
        fast = fast.next
    while fast.next:
        slow = slow.next
        fast = fast.next
    new_head = slow.next
    slow.next = None
    fast.next = head
    return new_head