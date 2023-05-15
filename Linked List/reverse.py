#Question: Given the head of a singly linked list, reverse the list, and return the reversed list.
#Approach: Reverse the linked list using three pointers, one to point to 
#current node,the next node and the previous node.
#Keep track of these pointers and switch them while traversing the list
#Time complexity: O(n)
#Space Complexity: O(1) 
class Node():
    def __init__(self,val):
        self.val=val
        self.next=None

class LinkedList():
    def traverse(self,head):
        current=head
        while current:
            print(current.val)
            current=current.next
    def reverse(self,head):
        prev=None
        current=head
        while current:
            current.next,prev,current=prev,current,current.next
        return prev
a=Node('A')
b=Node('B')
c=Node('C')
d=Node('D')

a.next=b
b.next=c
c.next=d

sol=LinkedList()
rev_head=sol.reverse(a)
sol.traverse(rev_head)