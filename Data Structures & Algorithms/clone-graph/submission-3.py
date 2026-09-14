"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        realtodup = {}
        
        def bfs(node):
            if node in realtodup:
                return realtodup[node]
        
            newNode = Node(node.val)
            realtodup[node] = newNode

            for i in node.neighbors:
                newNode.neighbors.append(bfs(i))
            
            return newNode
        return bfs(node) if node else None

        
            
        