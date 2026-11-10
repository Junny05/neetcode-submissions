class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        ROW, COL = len(grid), len(grid[0])

        def bfs(r,c):
            q = deque()
            grid[r][c] = 0
            q.append((r, c, 0))

            while q:
                row, col, dist = q.popleft()

                for dr, dc in directions:
                    nr, nc = dr + row, dc + col

                    if (nr < 0 or nc < 0 or nr >= ROW or nc >= COL or grid[nr][nc] == -1):
                        continue

                    if dist + 1 < grid[nr][nc]:
                        q.append((nr,nc,dist+1))
                        grid[nr][nc] = dist + 1
            return dist 

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    distance = bfs(r,c)