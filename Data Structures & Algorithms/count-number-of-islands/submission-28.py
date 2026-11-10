class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        ROW, COL = len(grid), len(grid[0])
        visited = set()
        count = 0

        def dfs(r,c):
            if r >= ROW or c >= COL or c < 0 or r < 0 or (r,c) in visited or grid[r][c] == "0":
                return
            
            visited.add((r,c))
            for dr, dc in direction:
                dfs(r+dr,c+dc)
        
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == '1' and (r,c) not in visited:
                    dfs(r,c)
                    count += 1
        return count