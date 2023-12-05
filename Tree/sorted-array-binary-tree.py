#Question:108. Convert Sorted Array to Binary Search Tree
# Given an integer array nums where the elements are sorted in ascending order, convert it to a 
# height-balanced binary search tree.

#Approach:
# In this solution, a recursive approach is employed to construct a balanced binary search tree from a sorted array. The `tree` function recursively divides the array range into halves, creating tree nodes with values corresponding to the middle elements. 
# Time complexity is O(n), where n is the length of the array, as each element is processed once. 
# Space complexity is O(log n), representing the maximum depth of the recursion stack.

# Definition for a binary tree node.

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def tree(i,j):

            if i>j:
                return 
                
            mid=(i+j)//2

            root=TreeNode(nums[mid])

            root.left=tree(i,mid-1)
            root.right=tree(mid+1,j)

            return root

        return tree(0,len(nums)-1)