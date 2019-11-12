# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        parent = {}

# Find each node's parent
        def mapParents(node, par):
            if not node:
                return
            parent[node] = par
            mapParents(node.left, node)
            mapParents(node.right, node)

        mapParents(root, None)


# now for each node, away from target, find neighbors(the children and parent) and 
# print the nodes when we're K edges away. (BFS)
        level = 0
        q = collections.deque([target])
        seen = set([target])

        while q:
            cur_nodes = len(q)
            for _ in range(cur_nodes):
                if level == K:
                    return [node.val for node in q]
                cur = q.popleft()
                for nbr in [cur.left, cur.right, parent[cur]]:
                    if nbr and nbr not in seen:
                        seen.add(nbr)
                        q.append(nbr)
            level += 1
        return []
