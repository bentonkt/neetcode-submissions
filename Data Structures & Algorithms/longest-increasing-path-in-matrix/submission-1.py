class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[-1] * n for _ in range(m)]

        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]

        greatest = 0

        def inBounds(i, j):
            if i >= 0 and i < m and j >= 0 and j < n: 
                return True

            return False

        def dfs(i, j):
            nonlocal greatest
            if dp[i][j] != -1: 
                return dp[i][j]

            dp[i][j] = 1

            for y, x in directions: 
                newI, newJ = i+y ,j+x
                if inBounds(newI, newJ) and matrix[i][j] < matrix[newI][newJ]:
                    dp[i][j] = max(dp[i][j], 1+ dfs(newI, newJ))

            greatest = max(greatest, dp[i][j])
            return dp[i][j]

        for i in range(m):
            for j in range(n): 
                dfs(i, j)

        print(dp)

        return greatest