class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        ROW, COL = len(grid), len(grid[0])
        islands = 0

        def bfs(r,c):
            q = deque()
            grid[r][c] = "0"
            q.append((r,c))

            while q:
                new_r, new_c = q.popleft()

                for dr, dc in directions:
                    nr, nc = new_r + dr, new_c + dc
                
                    if (nr < 0 or nc < 0 or nr >= ROW or nc >= COL or grid[nr][nc] == "0"):
                        continue
                    q.append((nr,nc))
                    grid[nr][nc] = "0"
 

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1":
                    bfs(r,c)
                    islands += 1
        return islands