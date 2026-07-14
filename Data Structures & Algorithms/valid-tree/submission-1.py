class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 0:
            return True
        adj = {i: [] for i in range(n)}
        for crs, pre in edges:
            adj[crs].append(pre)
            adj[pre].append(crs)
        
        visited = set()  
        def dfs(crs,prev):
            if crs in visited:
                return False

            visited.add(crs)  

            for pre in adj[crs]:
                if  pre == prev:
                    continue
                if not dfs(pre,crs):
                    return False 
            return True

        return dfs(0,-1) and len(visited) == n
        
        