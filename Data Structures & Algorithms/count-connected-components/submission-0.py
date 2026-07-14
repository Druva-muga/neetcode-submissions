class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n==0:
            return 1
        
        adj = {i:[] for i in range(n)}

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()

        def dfs(i,prev):
            if i in visited:
                return
            visited.add(i)
            for j in adj[i]:
                if j == [prev]:
                    continue
                dfs(j,i)
            return

        res = 0

        for i in range(n):
            if i not in visited:
                res+=1
                dfs(i,-1)
        
        return res
        