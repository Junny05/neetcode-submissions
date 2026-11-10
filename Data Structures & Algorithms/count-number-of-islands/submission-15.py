class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROW, COL = len(grid), len(grid[0])
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        islands = 0

        def bfs(r,c):
            q = deque()
            grid[r][c] = "0"
            q.append((r,c))

            while q:
                new_row, new_col = q.popleft()
                for dr, dc in direction:
                    nr, nc = new_row + dr, new_col + dc
                
                    if (nr < 0 or nc < 0 or nr >= ROW or nc >= COL or 
                    grid[nr][nc] == "0"):
                        continue
                    
                    grid[nr][nc] = "0"
                    q.append((nr,nc))

                    
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1":
                    bfs(r,c)
                    islands+=1
        return islands

        