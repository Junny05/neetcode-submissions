class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        max_area = 0
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        q = deque()
        curr_area = 0

        def bfs(r,c):
            q.append((r,c))
            grid[r][c] = 0
            curr_area = 1

            while q:
                row, col = q.popleft()
                
                for newrow, newcol in directions:
                    nr = newrow + row
                    nc = newcol + col

                    if nr > ROW - 1 or nc > COL - 1 or nr < 0 or nc < 0 or grid[nr][nc] == 0:
                        continue
                    curr_area += 1
                    q.append((nr,nc))
                    grid[nr][nc] = 0
            return curr_area
            
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    curr_area = bfs(r,c)
                max_area = max(curr_area, max_area)
        return max_area
        

        