class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()

        def dfs(rows,columns,visited,grid):
            if((rows,columns) in visited) or rows<0 or columns<0 or rows>=len(grid) or columns>=len(grid[0]):
                return
            if grid[rows][columns]== '0':
                return

            visited.add((rows,columns))
            dfs(rows+1,columns,visited,grid)
            dfs(rows-1,columns,visited,grid)
            dfs(rows,columns+1,visited,grid)
            dfs(rows,columns-1,visited,grid)
        
        sum1 = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r,c) not in visited and grid[r][c] == '1':
                    dfs(r,c,visited,grid)
                    sum1=sum1+1
        return sum1


        