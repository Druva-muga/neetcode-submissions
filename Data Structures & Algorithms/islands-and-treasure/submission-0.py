class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        q = deque()
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))

        def bfs():
            dist = 0
            while q:
                for _ in range(len(q)):
                    rows, cols = q.popleft()
                    for hr, hc in directions:
                        nr, nc = rows + hr, cols + hc
                        if (0 <= nr < ROWS and 0 <= nc < COLS and
                            (nr, nc) not in visited and grid[nr][nc] > 0):
                            grid[nr][nc] = dist + 1
                            q.append((nr, nc))
                            visited.add((nr, nc))
                dist += 1

        bfs()
