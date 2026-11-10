class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        memo = {}  # or a 2D array memo[r][c]

        def dfs(r, c):
            if (r, c) in memo:
                return memo[(r, c)]        # already solved this one, just hand back the answer
            
            best = 1  # every cell is at least a path of length 1 (itself)
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if nr >= len(matrix) or nc >= len(matrix[0]) or nr < 0 or nc < 0:
                    continue
                if matrix[nr][nc] > matrix[r][c]:  # only move to strictly bigger values
                    best = max(best, 1 + dfs(nr, nc))
            
            memo[(r, c)] = best   # write down the answer before returning
            return best

        result = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                result = max(result, dfs(r, c))
        return result