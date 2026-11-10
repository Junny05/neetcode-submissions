class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(heights), len(heights[0])
        pac,alt = set(),set()

        def dfs(r,c,visited,prevHeights):
            # out of boudns
            if r >= ROW or c >= COL or r < 0 or c < 0 or (r,c) in visited or heights[r][c] < prevHeights:
                return
            
            visited.add((r,c))
            dfs(r+1,c,visited,heights[r][c])
            dfs(r-1,c,visited,heights[r][c])
            dfs(r,c-1,visited,heights[r][c])
            dfs(r,c+1,visited,heights[r][c])
        
        for c in range(COL):
            dfs(0,c,pac,heights[0][c])
            dfs(ROW-1,c,alt,heights[ROW-1][c])
        
        for r in range(ROW):
            dfs(r,0,pac,heights[r][0])
            dfs(r,COL-1,alt,heights[r][COL-1])
        
        return [[r,c] for r,c in (pac & alt)]
