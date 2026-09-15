class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        prereqmap = {i: [] for i in range(numCourses)}
        for i in prerequisites:
            for j in range(1,len(i)):
                if i[0] in prereqmap:
                    prereqmap[i[0]].append(i[j])
         
        def dfs(node):
            if node in visited:
                return False
            if node not in prereqmap:
                visited.add(node)
                return True
            
            visited.add(node)
            for i in prereqmap[node]:
                if not dfs(i):
                    return False
            visited.remove(node)
            prereqmap[node] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

        