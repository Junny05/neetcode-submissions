class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])
        visited = set()

        def dfs(r, c, k):
            if k == len(word):
                return True
                
            if r >= ROW or c >= COL or (r,c) in visited or c < 0 or r < 0:
                return False
            
            if board[r][c] != word[k]:
                return False
            
            visited.add((r,c))
            res = dfs(r+1, c, k+1) or dfs(r, c+1, k+1) or dfs(r-1, c, k+1) or dfs(r,c-1, k+1)
            visited.remove((r,c))
            return res
        
        for r in range(ROW):
            for c in range(COL):
                if dfs(r,c,0):
                    return True
        return False