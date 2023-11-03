#Question:236. Lowest Common Ancestor of a Binary Tree
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

#Approach:
# Recursively traverse a binary tree, searching for the lowest common ancestor of two nodes, `p` and `q`. If the current node is either `p` or `q`, return the current node. Recursively search for common ancestors in the left and right subtrees, and return the first node where both `p` and `q` are found, or the node where one of them is found if the other is not present in the subtree.
# Time and Space Complexity: O(N)

# class Treenode():
#     def __init__(self,val):
#         self.left=None
#         self.right=None
#         self.val=val

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None

        if root == p or root == q:
            return root

        left_common = self.lowestCommonAncestor(root.left, p, q)
        right_common = self.lowestCommonAncestor(root.right, p, q)

        if left_common and right_common:
            return root
        else:
            return left_common or right_common
