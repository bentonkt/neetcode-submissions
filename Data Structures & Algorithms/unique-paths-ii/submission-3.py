class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        if obstacleGrid[0][0] == 1:
            return 0
        dp[m-1][n-1] = 1

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1): 
                if i == m-1 and j == n-1:
                    continue
                if obstacleGrid[i][j] == 1:
                    continue
                base = 0
                if j+1 < n and obstacleGrid[i][j+1] != 1:
                    base += dp[i][j+1]
                if i+1 < m and obstacleGrid[i+1][j] != 1:
                    base += dp[i+1][j]

                dp[i][j] = base

        return dp[0][0]