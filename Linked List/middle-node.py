#Question:Middle of the Linked List
#Given the head of a singly linked list, return the middle node of the linked list.
#Approach:The code finds the middle node of a singly linked list by using two pointers, one moving twice as fast as the other. 
# It iterates through the list until the fast pointer reaches the end, and returns the position of the slow pointer, which represents the middle node.
# Time complexity: O(n)
# Space complexity: O(1)

class List:
    def __init__(self,value):
        self.next=None
        self.value=value

a=List(1)
b=List(2)
c=List(3)
d=List(4)
e=List(5)

a.next=b
b.next=c
c.next=d
d.next=e

def print_list(head):
    if head is None:
        return
    print(head.value,end='->')
    print_list(head.next)
print("Linked List:")
print_list(a)
print("\n")

def middle_node(head):
    temp=head

    while temp and temp.next:
        head=head.next

        temp=temp.next.next

    return head

print(middle_node(a).value)




































