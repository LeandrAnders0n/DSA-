#Question: 257. Binary Tree Paths
# Given the root of a binary tree, return all root-to-leaf paths in any order.
# A leaf is a node with no children.

#Approach: Backtracking
# The approach employs a backtracking strategy to find all possible paths from the root to leaf nodes in a binary tree. The recursive function, backtrack, appends each node's value to the current path and explores both left and right branches. The base case appends the current path to the result when a leaf node is encountered. 
# Time complexity is O(N), where N is the number of nodes in the tree  
# Space complexity is O(H), where H is the height of the tree, representing the maximum depth of the recursive call stack.

from typing import Optional,List
 # Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        result=[]

        def backtrack(node:Optional[TreeNode],path:str)->None:
            path+=str(node.val)

            if not node.left and not node.right:
                result.append(path)
                return 
            
            if node.left:
                backtrack(node.left,path+"->")
            
            if node.right:
                backtrack(node.right,path+"->")
        
        backtrack(root,"")
        return result