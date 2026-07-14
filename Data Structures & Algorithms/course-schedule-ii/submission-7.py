class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Map each course to its prerequisites
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visited,cycle = set(),set()  # Used here to detect cycles (in current path)
        res = []

        def dfs(crs):
            if crs in cycle:
                return False  # cycle detected
            if crs in visited:
                return True   # already processed

            cycle.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False  # cycle found below
                    
            cycle.remove(crs) # remove from current path
            visited.add(crs) # mark as processed
            res.append(crs) # add to result
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []  # cycle found

        return res  # topological order