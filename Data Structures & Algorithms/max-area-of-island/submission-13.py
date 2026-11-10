class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        currarea = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        ROW, COL = len(grid), len(grid[0])

        def bfs(r,c):
            q = deque()
            grid[r][c] = 0
            q.append((r,c))
            bfsarea = 1

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    nrow, ncol = row + dr, col + dc

                    if (0 > nrow or 0 > ncol or nrow >= ROW or ncol >= COL or grid[nrow][ncol] == 0):
                        continue

                    q.append((nrow, ncol))
                    grid[nrow][ncol] = 0
                    bfsarea += 1
            return bfsarea

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    currarea = bfs(r,c)
                    area = max(area,currarea)
        return area