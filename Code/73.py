class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col_0 = False
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                col_0 = True
            for j in range(1, len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0
        for i in range(len(matrix) - 1, -1, -1):
            for j in range(len(matrix[i]) - 1, 0, -1):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0
            matrix[i][0] = 0 if col_0 else matrix[i][0]

# Solution().setZeroes([[-4,-2147483648,6,-7,0],[-8,6,-8,-6,0],[2147483647,2,-9,-6,-10]])