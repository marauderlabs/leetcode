# https://leetcode.com/problems/range-sum-of-bst/

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def rangeSum(node: TreeNode) -> int:
            val = 0
            if node.val >= L and node.val <= R:
                val = node.val
            if node.left:
                val += rangeSum(node.left)
            if node.right:
                val += rangeSum(node.right)
            return val
        
        return rangeSum(root)
