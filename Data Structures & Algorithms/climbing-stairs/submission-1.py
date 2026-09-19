class Solution:
    def climbStairs(self, n: int) -> int:
        

        dp = [-1 for _ in range(n+1)]
        dp[n] = 0
        dp[n-1] = 1
        dp[n-2] = 2
        for i in range(n-3, -1, -1):
            res = dp[i+1]
            if i+2 < n:
                res += dp[i+2]

            dp[i] = res

        return dp[0]