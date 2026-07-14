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
            return None
        oldtonew = {}
        def dfs(root):
            if root in oldtonew:
                return oldtonew[root]
            new_node = Node(root.val)
            oldtonew[root] = new_node
            for i in root.neighbors:
                new_node.neighbors.append(dfs(i))
            return new_node

        return dfs(node)

        