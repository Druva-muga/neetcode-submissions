class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            preMap[pre].append(crs)
        
        visited = set()
        res = []
        def dfs(crs):
            if crs in visited:
                return False
            if preMap[crs] == []:
                return True
            
            visited.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            preMap[crs] = []
            visited.remove(crs)
            res.insert(0,crs)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
            if i not in res:
                res.append(i)

        return res
        