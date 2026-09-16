class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        nodetoedge = {i : [] for i in range(n)}
        
        for i in edges:
            nodetoedge[i[0]].append(i[1])
            nodetoedge[i[1]].append(i[0])

        visited = set()
        def dfs(node,prev):
            if node in visited:
                return False
            visited.add(node)
            for i in nodetoedge[node]:
                if i==prev:
                    continue
                if not dfs(i,node):
                    return False
            
            return True
            
        return dfs(0,-1) and len(visited)==n