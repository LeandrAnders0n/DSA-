#Question:114. Flatten Binary Tree to Linked List
#Given the root of a binary tree, flatten the tree into a "linked list":
# The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
# The "linked list" should be in the same order as a pre-order traversal of the binary tree.

#Approach:
#Flatten a binary tree to a linked list in a preorder traversal fashion. Use a stack to track the order of nodes, set `left` pointers to `None`, and update `right` pointers to the next node in the traversal. The stack[-1] retrieves the top element of the stack, which is the next node in the preorder traversal.

# Time Complexity: O(N)
# Space Complexity: O(H)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(root):
        if root is None:
            return

        stack = [root]
        while stack:
            current = stack.pop()

            if current.right:
                stack.append(current.right)
            
            if current.left:
                stack.append(current.left)

            # Modify the tree structure to achieve the flattened structure
            current.left = None
            if stack:
                current.right = stack[-1]
