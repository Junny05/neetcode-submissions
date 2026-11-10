class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROW, COL = len(grid), len(grid[0])
        islands = 0

        def dfs(r,c):
            if r > ROW - 1 or c > COL - 1 or r < 0 or c < 0 or grid[r][c] == "0":
                return 

            grid[r][c] = "0"
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r,c+1)
            dfs(r,c-1)
    

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1":
                    dfs(r,c)
                    islands += 1
        return islands
        