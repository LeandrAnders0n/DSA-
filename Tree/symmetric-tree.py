#Question: Symmetric Tree
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

#Approach:
# Define a recursive function check_symmetry that takes two nodes as arguments (one from the left subtree and one from the right subtree). Recursively compare corresponding nodes for equality and mirror-like symmetry. If both subtrees are symmetric, and the current nodes have equal values, the tree is symmetric.

# Time Complexity: O(n), where n is the number of nodes in the tree
# Space Complexity: O(h), where h is the height of the tree

def isSymmetric(root):
    if not root:
        return True
    
    def check_symmetry(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val == right.val and \
        check_symmetry(left.left, right.right) and \
        check_symmetry(left.right, right.left)
    
    return check_symmetry(root.left, root.right)

# Input: root = [1,2,2,3,4,4,3]
# Output: true

# Input: root = [1,2,2,null,3,null,3]
# Output: false
 