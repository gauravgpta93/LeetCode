class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        top_line = list(matrix.pop(0))
        anti_clock_matrix = list(zip(*matrix))[::-1]
        return top_line + self.spiralOrder(anti_clock_matrix)