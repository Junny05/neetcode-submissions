class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

        res = []

        while top <= bottom and left <= right:
            # all way to the right
            for i in range(left, right+1):
                res.append(matrix[top][i])
            top += 1

            # going down at the last column
            for i in range(top, bottom+1):
                res.append(matrix[i][right])
            right -= 1

            if (left > right or top > bottom):
                break
            
            # bottom right to left
            for i in range(right, left-1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1

            # going bottom left to up
            for i in range(bottom, top-1, -1):
                res.append(matrix[i][left])
            left += 1
        return res


