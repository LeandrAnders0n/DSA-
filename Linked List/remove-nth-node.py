#Question:Remove Nth Node From End of List
# Given the head of a linked list, remove the nth node from the end of the list and return its head.
#Approach: Two pointer
# Use two pointers one fast and and one slow, with the fast initially moving n nodes ahead. Then, both pointers move at the same pace until fast reaches the end. At this point, the slow pointer is pointing to the node just before the target node to be removed, allowing it to modify the pointers and skip the targeted node effectively. 

#Time complexity: O(n)
#Space Complexity: O(1) 

def removeNthFromEnd(head,n):
    fast = head
    slow = head
    for i in range(n):
        fast = fast.next
        
    if not fast:
        return head.next
    while fast.next:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return head