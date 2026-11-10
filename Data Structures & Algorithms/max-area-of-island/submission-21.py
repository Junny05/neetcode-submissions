class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        ROW, COL = len(grid), len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            grid[r][c] = 0
            curr_area = 1

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    nr, nc = dr + row, dc + col

                    if nc < 0 or nr < 0 or nc >= COL or nr >= ROW or grid[nr][nc] == 0:
                        continue


                    curr_area += 1
                    q.append((nr,nc))
                    grid[nr][nc] = 0
            return curr_area

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    area = max(area, bfs(r,c))
        return area