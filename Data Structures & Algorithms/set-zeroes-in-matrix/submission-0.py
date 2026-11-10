class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_rows = set()
        zero_cols = set()
        
        # checks rows/cols
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)
        
        # updates the matrix
        for r in zero_rows:
            for j in range(len(matrix[0])):
                matrix[r][j] = 0

        for c in zero_cols:
            for j in range(len(matrix)):
                matrix[j][c] = 0
        
        

                