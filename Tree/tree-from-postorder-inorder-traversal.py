#Question: Construct Binary Tree from Inorder and Postorder Traversal
# Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.
#Approach:
# Construct a binary tree from its inorder and postorder traversals using recursion. Extract the root value from the end of the postorder list, find its position in the inorder list to divide it into left and right subtrees, and then recursively build these subtrees. 

# Time Complexity & Space Complexity: O(n)


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def construct_tree(inorder, postorder):
    if not inorder or not postorder:
        return None
    root_val = postorder.pop()
    root = TreeNode(root_val)
    root_index = inorder.index(root_val)

    root.right = construct_tree(inorder[root_index + 1:], postorder)
    root.left = construct_tree(inorder[:root_index], postorder)
    
    return root



inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
print(construct_tree(inorder,postorder))
# Output: [3,9,20,null,null,15,7]

inorder = [-1]
postorder = [-1]
# Output: [-1]
print(construct_tree(inorder,postorder))
