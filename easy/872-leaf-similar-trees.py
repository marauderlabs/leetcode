# https://leetcode.com/problems/leaf-similar-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        
        def getLeaves(root: TreeNode) -> List[int]:
            leaves = []
            preOrder(root, leaves)
            return leaves
        
        def preOrder(root: TreeNode, leaves: List[int]) -> None:
            if not root:
                return
            
            if root.left is None and root.right is None: #Leaf
                leaves.append(root.val)                
            preOrder(root.left, leaves)
            preOrder(root.right, leaves)
        
        # leafSimilar
        seq1 = getLeaves(root1)
        seq2 = getLeaves(root2)
        
        # list of equalities
        equals = [x == y for x, y in zip(seq1, seq2)]
        return all(equals)
