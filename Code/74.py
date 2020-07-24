class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        row = len(matrix)
        col = len(matrix[0])
        left, right = 0, row * col
        while left < right:
            mid = (left + right) // 2
            if matrix[mid // col][mid % col] == target:
                return True
            if matrix[mid // col][mid % col] < target:
                left = mid + 1
            else:
                right = mid
        return False
