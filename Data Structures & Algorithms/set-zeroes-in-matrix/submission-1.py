class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row_zeros = set()
        col_zeros = set()

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    row_zeros.add(r)
                    col_zeros.add(c)
        
        for row in row_zeros:
            for c in range(len(matrix[0])):
                matrix[row][c] = 0
        
        for r in range(len(matrix)):
            for col in col_zeros:
                matrix[r][col] = 0
        




        
        

                