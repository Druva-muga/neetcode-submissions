class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parenttochild = {i:[] for i in range(n)}
        for i in edges:
            parenttochild[i[0]].append(i[1])
            parenttochild[i[1]].append(i[0])
        
        print(parenttochild)

        visited = set()
        def dfs(node,prev):
            if node in visited:
                return
            visited.add(node)
            for i in parenttochild[node]:
                if prev == i:
                    continue
                dfs(i,node)
            return
        res = 1
        dfs(0,-1)
        print(visited)
        for i in range(n):
            if i not in visited:
                res = res+1
                dfs(i,-1)
                # print(visited)
        return res



        