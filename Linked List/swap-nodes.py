#Question:Swapping Nodes in a Linked List
#You are given the head of a linked list, and an integer k.
# Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

#Approach:This code swaps the values of two nodes in a singly-linked list based on their positions, k and (length - k + 1). 
# It first calculates the length of the list, then finds the kth node from the beginning and the kth node from the end using two iterations.
# Finally, it swaps the values of the two nodes. 
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

def traverse(head):
        current=head
        while current:
            yield current.value
            current=current.next

def swap_nodes(head,k):
    first=second=head

    for _ in range(k-1):
        first=first.next

    tail=first

    while tail.next:
        second=second.next
        tail=tail.next
    
    first.value,second.value=second.value,first.value

    return head
    


# Input Linked List: [1,2,3,4,5] and k = 2
#Expected Output: [1,4,3,2,5]
new_list=swap_nodes(a,2)
print(list(traverse(new_list)))





















































