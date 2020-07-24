class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_sq = 0
        memo = [[0] * len(matrix[i]) for i in range(len(matrix))]
        print(memo)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):                
                val = matrix[i][j]                
                if val == "1":                                        
                    if i == 0:
                        current = 1
                    elif j == 0:
                        current = 1
                    else:
                        current = min(memo[i - 1][j], memo[i][j - 1], memo[i - 1][j - 1]) + 1
                    max_sq = max(max_sq, current)
                    memo[i][j] = current        
        return max_sq**2

