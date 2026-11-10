class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROW, COL = len(matrix), len(matrix[0])

        dp = {}

        def dfs(r,c,preval):
            if r >= ROW or c >= COL or r < 0 or c < 0 or preval >= matrix[r][c]:
                return 0
            
            if (r,c) in dp:
                return dp[(r,c)]

            res = 1
            res = max(res, 1 + dfs(r+1,c,matrix[r][c]))
            res = max(res, 1 + dfs(r-1,c,matrix[r][c]))
            res = max(res, 1 + dfs(r,c+1,matrix[r][c]))
            res = max(res, 1 + dfs(r,c-1,matrix[r][c]))
            dp[(r,c)] = res
            return res

        for r in range(ROW):
            for c in range(COL):
                dfs(r,c,-1)
        return max(dp.values())

