# https://leetcode.com/problems/clone-graph/

"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        nodeDict: Dict[Node, Node] = {} # a 'visited' marker and lookup table
            
        queue = collections.deque()
        
        queue.append(node)
        nodeDict[node] = Node(node.val, [])
        
        while queue:
            cur = queue.popleft()
            
            for n in cur.neighbors:
                if n not in nodeDict:
                    queue.append(n)
                    nodeDict[n] = Node(n.val, [])
                
                nodeDict[cur].neighbors.append(nodeDict[n])
        
        return nodeDict[node]
                
