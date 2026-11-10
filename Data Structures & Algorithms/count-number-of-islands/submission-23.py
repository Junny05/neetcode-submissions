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
                r, c = q.popleft()

                for dr, dc in directions:
                    nrow, ncol = r + dr , c + dc

                    if (0 > nrow or nrow >= ROW or 0 > ncol or ncol >= COL or grid[nrow][ncol] == '0'):
                        continue
                        
                    q.append((nrow,ncol))
                    grid[nrow][ncol] = "0"
                            
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1":
                    bfs(r,c)
                    islands += 1
        return islands