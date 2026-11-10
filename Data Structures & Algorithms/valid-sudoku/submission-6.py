class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashset_row = set()
        hashset_col = set()
        hashset_box = set()

        for row in board:
            for item in row:
                if item in hashset_row:
                    return False
                elif item == '.':
                    continue
                hashset_row.add(item)
            hashset_row.clear()
        
        for c in range(9):
            for r in range(9):
                item = board[r][c]
                if item in hashset_col:
                    return False
                elif item == '.':
                    continue
                hashset_col.add(item)
            hashset_col.clear()
        
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                for r in range(0,3,1):
                    for c in range(0,3,1):
                        if board[r+row][c+col] in hashset_box:
                            return False
                        elif board[r+row][c+col] == '.':
                            continue
                        hashset_box.add(board[row+r][col+c])
                hashset_box.clear()

        return True

