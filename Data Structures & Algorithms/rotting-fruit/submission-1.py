class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # minutes = 0
        # rotfruits = set()
        # visited = set()
        # ROWS = len(grid)
        # COLS = len(grid[0])

        # def bfs(r,c):
        #     q = collections.deque()
        #     q.append((r,c))
        #     visited.add((r,c))
        #     while q:
        #         row , col = q.popleft()
        #         directions = [[1,0],[-1,0],[0,1],[0,-1]]
        #         for dr , dc in directions:
        #             r = dr + row
        #             c = dc + col
        #             if (r in range(ROWS) and c in range(COLS) and (r,c) not in visited and grid[r][c] == 1):
        #                 q.append((r,c))
        #                 visited.add((r,c))
        #                 rotfruits.remove((r,c))

        #         minutes += 1 
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        q = deque()
        fruits = set()
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))
                elif grid[r][c] == 1:
                    fruits.add((r,c))
        if not fruits:
            return 0

        def bfs():
            dist = 0
            while q:
                for _ in range(len(q)):
                    rows, cols = q.popleft()
                    for hr, hc in directions:
                        nr, nc = rows + hr, cols + hc
                        if (0 <= nr < ROWS and 0 <= nc < COLS and
                            (nr, nc) not in visited and grid[nr][nc] == 1):
                            grid[nr][nc] = 2
                            q.append((nr, nc))
                            visited.add((nr, nc))
                            fruits.remove((nr,nc))
                dist += 1
            return dist

        disti = bfs()
        if not fruits:
            return disti-1 
        else:
            return -1
        