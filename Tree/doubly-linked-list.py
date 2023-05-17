#Question:Convert Binary Search Tree to Sorted Doubly Linked List
# Approach: We perform a depth-first traversal of the Tree. Starting from the root, we traverse to the leftmost node while pushing each node onto a stack. Then, we pop nodes from the stack, connect them to the previous node, and update the previous node accordingly. Finally, we set the head of the Doubly Linked List and return it.


class Node:
    def __init__(self,val):
        self.left=None
        self.right=None
        self.data=val

def bstToDll(root):
    if root is None:
        return None
    stack=[]
    curr=root
    prev,head=None,None
    while curr is not None or stack:
        while curr is not None:
            stack.append(curr)
            curr=curr.left
        curr=stack.pop()

        if prev is None:
            head=curr
        else:
            prev.right=curr
            curr.left=prev
        prev=curr
        curr=curr.right

    return head

def display(head):
    while head is not None:
        print(head.data)
        head=head.right



if __name__ == '__main__':
    root = Node(10)
    root.left = Node(6)
    root.right = Node(15)
    root.left.left = Node(3)
    root.left.right = Node(8)
    root.right.left = Node(12)
    root.right.right = Node(20)
    
    head = bstToDll(root)
    
    display(head)