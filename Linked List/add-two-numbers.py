#Question:Add Two Numbers
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

#Approach:
# Iterate through the lists, calculating the sum and carry for each digit(using divmod) and create a new linked list with the resulting digits.
#  Time Complexity and Space Complexity O(max(N, M)), where N and M are the lengths of the input lists

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

node1 = ListNode(2)
node2 = ListNode(4)
node3 = ListNode(3)

node1.next = node2
node2.next = node3

node4 = ListNode(5)
node5 = ListNode(6)
node6 = ListNode(4)

node4.next = node5
node5.next = node6

head1 = node1
head2 = node4

def add_two_numbers(l1,l2):
    head = ListNode(0)
    tail = head
    carry = 0
    while l1 or l2 or carry:
        digit1 = l1.val if l1 else 0
        digit2 = l2.val if l2 else 0
        carry, digit = divmod(digit1 + digit2 + carry, 10)
        tail.next = ListNode(digit)
        tail = tail.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return head.next
        

print(add_two_numbers(head1,head2))