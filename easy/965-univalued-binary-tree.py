# https://leetcode.com/problems/univalued-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        def isUniHelper(root: TreeNode, val: int) -> bool:
            if not root:
                return True
            
            if val != root.val:
                return False
            
            return isUniHelper(root.left, root.val) and isUniHelper(root.right, root.val)
        
        if not root:
            return True
        return isUniHelper(root, root.val)
