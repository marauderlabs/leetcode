# https://leetcode.com/problems/n-ary-tree-postorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:

        def postorderRecursive(root: Node) -> List[int]:
            result = []
            if not root:
                return result

            if root.children:
                for c in root.children:
                    result.extend(postorderRecursive(c))

            result.append(root.val)
            return result


        def postorderIterative(root: Node) -> List[int]:
            result = []

            if not root:
                return result

            stack = [root]

            while stack:
                cur = stack.pop()
                if cur.children:
                    stack.extend(cur.children)
                result.append(cur.val)

            return reversed(result)


        #return postorderRecursive(root)
        return postorderIterative(root)

