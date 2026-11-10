class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        ROW, COL = len(board), len(board[0])

        def dfs(r,c,k):
            if k == len(word):
                print(r,c,k)
                return True
            
            if r >= ROW or c >= COL or c < 0 or r < 0 or (r,c) in visited or board[r][c] != word[k]:
                return

            visited.add((r,c))
            res = dfs(r+1,c,k+1) or dfs(r-1,c,k+1) or dfs(r,c+1,k+1) or dfs(r,c-1,k+1)
            visited.remove((r,c))
            return res
        
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == word[0]:
                    if dfs(r,c,0):
                        return True
        return False