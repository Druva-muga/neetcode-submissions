class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        atl = set()
        ROWS = len(heights)
        COLS = len(heights[0])
        result = []
        def dfs(r,c,visited,prev):
            if r not in range(0,ROWS) or c not in range(0,COLS) or (r,c) in visited or prev>heights[r][c]:
                return
            visited.add((r,c))
            dfs(r+1,c,visited,heights[r][c])
            dfs(r-1,c,visited,heights[r][c])
            dfs(r,c+1,visited,heights[r][c])
            dfs(r,c-1,visited,heights[r][c])

        for c in range(COLS):
            dfs(0,c,pac,heights[0][c])
            dfs(ROWS-1,c,atl,heights[ROWS-1][c])
        
        for r in range(ROWS):
            dfs(r,0,pac,heights[r][0])
            dfs(r,COLS-1,atl,heights[r][COLS-1])

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in atl and (r,c) in pac:
                    result.append([r,c])
        
        return result
        