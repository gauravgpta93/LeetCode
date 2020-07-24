class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[rows - 1][cols - 1] == 1:
            return 0
        for i in range(0, rows):
            for j in range(0, cols):
                if i == 0 and j == 0:
                    obstacleGrid[0][0] = 1
                elif i == 0:
                    obstacleGrid[0][j] = obstacleGrid[0][j - 1] if obstacleGrid[0][j] != 1 else 0
                elif j == 0:
                    obstacleGrid[i][0] = obstacleGrid[i - 1][0] if obstacleGrid[i][0] != 1 else 0
                else:
                    obstacleGrid[i][j] = (obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]) if obstacleGrid[i][j] != 1 else 0
        return obstacleGrid[rows - 1][cols - 1]
