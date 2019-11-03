# https://leetcode.com/problems/increasing-order-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:

        def inOrder(root: TreeNode, vals: List[int]):
            if root is None:
                return
            inOrder(root.left, vals)
            vals.append(root.val)
            inOrder(root.right, vals)

        vals = []
        inOrder(root, vals)
        # Now we have it in the inorder order in the list

        cur = newRoot = TreeNode(None)
        for val in vals:
            newNode = TreeNode(val)
            cur.right = newNode
            cur = cur.right

        return newRoot.right

