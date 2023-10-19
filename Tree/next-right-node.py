#Question:117. Populating Next Right Pointers in Each Node II
#Given a binary tree
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
# Initially, all next pointers are set to NULL.

#Approach: BFS Traversal
# Use breadth-first search to connect next right pointers in each node of a binary tree. Use a queue to process nodes level by level, updating the 'next' pointers accordingly. The logic ensures that each node's 'next' pointer points to the subsequent node in the same level

# Time complexity is O(N)
# Space complexity is O(W),W is the maximum width of the tree at any level

# # Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root

        queue = [root]

        while queue:
            size = len(queue)

            for i in range(size):
                current = queue.pop(0)

                if i < size - 1:
                    current.next = queue[0]

                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

        return root