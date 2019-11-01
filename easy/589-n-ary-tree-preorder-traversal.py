# https://leetcode.com/problems/n-ary-tree-preorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:

        def preorderHelperRecursive(root: Node, result: List[int]) -> None:
            if root is None:
                return

            result.append(root.val)

            if not root.children:
                return

            for c in root.children:
                preorderHelperRecursive(c, result)


        def preorderHelperIterative(root: Node) -> List[int]:
            stack: List[Node] = []
            result: List[int] = []

            if not root:
                return result

            stack.append(root)

            while stack:
                cur = stack.pop()
                result.append(cur.val)
                if cur.children:
                    for c in reversed(cur.children):
                        stack.append(c)

            return result


        #result = []
        #preorderHelperRecursive(root, result)

        result = preorderHelperIterative(root)

        return result
