# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0

        if not root.children:
            return 1

        m = 0
        for c in root.children:
            m = max(m, self.maxDepth(c))
        return 1+m
