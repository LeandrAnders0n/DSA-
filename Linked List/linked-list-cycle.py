#Question:Linked List Cycle
##Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.

#Approach: Floyd's Tortoise and Hare algorithm 
# It initializes two pointers, slow and fast, starting from the head and head.next respectively. They move through the list at different speeds until they either meet (indicating a cycle) or reach the end (no cycle). If either pointer reaches the end, the function returns False, otherwise True.

# Time complexity: O(n)
# Space complexity: O(1)

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  
head = node1

def linked_list_cycle(head):
    if head is None or head.next is None:
        return False
    slow=head
    fast=head.next

    while slow!=fast:
        if fast is None or fast.next is None:
            return False
    
        slow=slow.next
        fast=fast.next.next
        
    return True


print(linked_list_cycle(head))
# Expected Output: True







































