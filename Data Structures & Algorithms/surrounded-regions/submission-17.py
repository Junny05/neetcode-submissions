class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROW, COL = len(board), len(board[0])

        def dfs(r,c):
            if (r < 0 or c < 0 or r >= ROW or c >= COL or board[r][c] != 'O'):
                return
            
            board[r][c] = 'T'
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        for r in range(ROW):
            dfs(r, 0)
            dfs(r, COL - 1)
        
        for c in range(COL):
            dfs(0, c)
            dfs(ROW-1, c)
        
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'
        
        