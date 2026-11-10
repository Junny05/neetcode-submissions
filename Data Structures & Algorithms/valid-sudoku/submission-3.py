class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            row_set = set()
            for col in range(9):
                curr = board[row][col]
                if curr == ".":
                    continue
                if curr in row_set:
                    return False
                row_set.add(curr)
        
        for col in range(9):
            col_set = set()
            for row in range(9):
                curr = board[row][col]
                if curr == ".":
                    continue 
                if curr in col_set:
                    return False
                col_set.add(curr)
        
        for row in range(0,9,3):
            for col in range(0,9,3):
                box_set = set()
                for i in range(3):
                    for j in range(3):
                        current = board[row+i][col+j]
                        if current == ".":
                            continue 
                        if current in box_set:
                            return False
                        box_set.add(current)
        return True   