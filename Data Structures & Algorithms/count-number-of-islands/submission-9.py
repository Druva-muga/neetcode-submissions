class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        def dfs(r,c,visited):
            if r not in range(0,ROWS) or c not in range(0,COLS) or (r,c) in visited or grid[r][c] == "0":
                return
            
            visited.add((r,c))
            dfs(r+1,c,visited)
            dfs(r-1,c,visited)
            dfs(r,c+1,visited)
            dfs(r,c-1,visited)

        sum1=0

        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) not in visited and grid[i][j] == "1":
                    dfs(i,j,visited)
                    sum1=sum1 + 1
        
        return sum1



        