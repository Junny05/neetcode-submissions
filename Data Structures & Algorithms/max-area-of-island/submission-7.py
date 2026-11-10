class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        MaxArea = 0
        area = 0
        ROW, COL = len(grid), len(grid[0])

        def bfs(r,c):
            q = deque()
            grid[r][c] = 0
            q.append((r,c))
            area = 1
            while q:
                nr, nc = q.popleft()

                for dr, dc in direction:
                    new_row, new_col = dr + nr, dc + nc

                    if (new_row < 0 or new_col < 0  
                    or new_row >= ROW or new_col >= COL
                    or grid[new_row][new_col] == 0):
                        continue
                    
                    q.append((new_row,new_col))
                    grid[new_row][new_col] = 0
                    area += 1
            return area
            
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    area = bfs(r,c)
                    if area > MaxArea:
                        MaxArea = area

        return MaxArea
            
        
        

        