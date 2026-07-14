class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        pacific = set()
        atlantic = set()
        def dfs(r,c,visit,prev):
            if (r in range(ROWS) and c in range(COLS) and (r,c) not in visit and heights[r][c] >= prev):
                visit.add((r,c))
                dfs(r+1,c,visit,heights[r][c])
                dfs(r-1,c,visit,heights[r][c])
                dfs(r,c+1,visit,heights[r][c])
                dfs(r,c-1,visit,heights[r][c])
            return

        for r in range(ROWS):
            dfs(r,0,pacific,heights[r][0])
            dfs(r,COLS-1,atlantic,heights[r][COLS-1])
        
        for c in range(COLS):
            dfs(0,c,pacific,heights[0][c])
            dfs(ROWS-1,c,atlantic,heights[ROWS-1][c])
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in atlantic and (r,c) in pacific:
                    res.append([r,c])
        return res
        