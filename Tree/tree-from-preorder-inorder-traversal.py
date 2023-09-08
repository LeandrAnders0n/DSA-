#Question: Construct Binary Tree from Preorder and Inorder Traversal
#Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

#Approach:
# Construct a binary tree from its preorder and inorder traversals using recursion. Select the root from the preorder list, find its position in the inorder list, and recursively build the left and right subtrees. The process continues until the entire tree is reconstructed. 

# Time Complexity & Space Complexity: O(n)


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def construct_tree(preorder,inorder):
    if not preorder or not inorder:
        return None
        
    root_val=preorder.pop(0)
    root=TreeNode(root_val) 
    root_index=inorder.index(root_val)  
    root.left=construct_tree(preorder,inorder[:root_index])
    root.right=construct_tree(preorder,inorder[root_index+1:])  
    return root



preorder = [3,9,20,15,7] 
inorder = [9,3,15,20,7]
print(construct_tree(preorder,inorder))
# Output: [3,9,20,null,null,15,7]

preorder = [-1] 
inorder = [-1]
# Output: [-1]
print(construct_tree(preorder,inorder))
