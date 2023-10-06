#Question:92. Reverse Linked List II
# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

#Approach:Reverse a portion of a linked list from positions `left` to `right`. Use a dummy node to simplify edge cases, iterate to the node before the reversal portion, and reverse the pointers within the specified range. 

# Time complexity: O(n)
# Space complexity: O(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

def reverse_between_nodes(head, left, right):
    if not head or left == right:
        return head
    
    dummy = ListNode(0, head)
    prev = dummy
    
    for _ in range(left - 1):
        prev = prev.next
    
    current = prev.next
    
    for _ in range(right - left):
        next_node = current.next
        current.next, next_node.next, prev.next = next_node.next, prev.next, next_node
    return dummy.next