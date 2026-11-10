class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        max_area = 0
        area = 0
        def dfs(r,c):
            if r > ROW - 1 or c > COL - 1 or r < 0 or c < 0 or grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            return dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1) + 1

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    area = dfs(r,c)
                max_area = max(area, max_area)
        return max_area            
        
        

        