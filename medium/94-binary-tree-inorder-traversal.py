# https://leetcode.com/problems/binary-tree-inorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result: List[int] = []
        
        def helper_recursive(root: TreeNode):
            if not root:
                return            
            helper_recursive(root.left)
            result.append(root.val)
            helper_recursive(root.right)
        
        def helper_iterative(root: TreeNode):
            if not root:
                return
            
            cur = root
            stack = []
            while cur or stack:
                while cur:
                    stack.append(cur)
                    cur = cur.left
                
                cur = stack.pop()
                result.append(cur.val)
                cur = cur.right            
        
        # inorderTraversal
        # helper_recursive(root)
        helper_iterative(root)
        return result
